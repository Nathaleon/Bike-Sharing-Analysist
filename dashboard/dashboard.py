import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Bike Sharing Analysis Dashboard")

day_data = pd.read_csv('dashboard/day_clean.csv')
hour_data = pd.read_csv('dashboard/hour_clean.csv')

dataset_option = st.sidebar.selectbox("Pilih Dataset:", ("Harian", "Per Jam"))

if dataset_option == "Harian":
    data = day_data
    st.header("Analisis Data Harian")
else:
    data = hour_data
    st.header("Analisis Data Per Jam")

st.subheader("Pengaruh Cuaca terhadap Penyewaan Sepeda")
avg_rentals_weather = data.groupby('weathersit')['cnt'].mean().reset_index()

weather_fig = px.bar(
    avg_rentals_weather,
    x='weathersit',
    y='cnt',
    title='Rata-rata Penyewaan Sepeda Berdasarkan Cuaca',
    labels={
        'weathersit': 'Kondisi Cuaca',
        'cnt': 'Rata-rata Penyewaan Sepeda'
    },
    color='cnt',
    color_continuous_scale='viridis'
)

weather_fig.update_layout(
    xaxis=dict(
        ticktext=['Cerah', 'Berawan', 'Hujan', 'Badai'],
        tickvals=[1, 2, 3, 4]
    )
)
st.plotly_chart(weather_fig)

if dataset_option == "Harian":
    st.subheader("Pola Musiman dalam Penyewaan Sepeda")
    avg_rentals_season = data.groupby('season')['cnt'].mean().reset_index()
    
    season_fig = px.bar(
        avg_rentals_season,
        x='season',
        y='cnt',
        title='Rata-rata Penyewaan Sepeda Berdasarkan Musim',
        labels={
            'season': 'Musim',
            'cnt': 'Rata-rata Penyewaan Sepeda'
        },
        color='cnt',
        color_continuous_scale='RdBu'  # Changed from 'coolwarm' to 'RdBu'
    )
    
    season_fig.update_layout(
        xaxis=dict(
            ticktext=['Dingin', 'Semi', 'Panas', 'Gugur'],
            tickvals=[1, 2, 3, 4]
        )
    )
    st.plotly_chart(season_fig)

if dataset_option == "Per Jam":
    st.subheader("Distribusi Penyewaan Sepeda Berdasarkan Jam")
    avg_rentals_hour = data.groupby('hr')['cnt'].mean().reset_index()
    
    hour_fig = px.bar(
        avg_rentals_hour,
        x='hr',
        y='cnt',
        title='Distribusi Penyewaan Sepeda Berdasarkan Jam',
        labels={
            'hr': 'Jam dalam Sehari',
            'cnt': 'Rata-rata Penyewaan Sepeda'
        },
        color='cnt',
        color_continuous_scale='spectral'
    )
    st.plotly_chart(hour_fig)

st.subheader("Hubungan antara Suhu dan Jumlah Penyewaan Sepeda")
temp_fig = px.scatter(
    data,
    x='temp',
    y='cnt',
    title='Hubungan antara Suhu dan Jumlah Penyewaan Sepeda',
    labels={
        'temp': 'Suhu (normalisasi)',
        'cnt': 'Jumlah Penyewaan Sepeda'
    },
    color_discrete_sequence=['purple']
)
st.plotly_chart(temp_fig)

st.subheader("Hubungan antara Kelembapan dan Jumlah Penyewaan Sepeda")
hum_fig = px.scatter(
    data,
    x='hum',
    y='cnt',
    title='Hubungan antara Kelembapan dan Jumlah Penyewaan Sepeda',
    labels={
        'hum': 'Kelembapan (normalisasi)',
        'cnt': 'Jumlah Penyewaan Sepeda'
    },
    color_discrete_sequence=['green']
)
st.plotly_chart(hum_fig)

if dataset_option == "Per Jam":
    st.subheader("Kombinasi Suhu dan Kelembapan terhadap Jumlah Penyewaan Sepeda")
    heatmap_fig = px.density_heatmap(
        data,
        x='temp',
        y='hum',
        z='cnt',
        title='Kombinasi Suhu dan Kelembapan terhadap Jumlah Penyewaan Sepeda',
        labels={
            'temp': 'Suhu (normalisasi)',
            'hum': 'Kelembapan (normalisasi)',
            'cnt': 'Jumlah Penyewaan'
        }
    )
    st.plotly_chart(heatmap_fig)

if st.checkbox("Show Raw Data"):
    st.subheader("Data yang Ditampilkan")
    st.write(data)
