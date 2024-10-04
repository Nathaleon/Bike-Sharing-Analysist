# Bike-Sharing-Analysist

Proyek ini adalah analisis penyewaan sepeda menggunakan dataset Bike Sharing. Analisis ini mencakup pengaruh cuaca terhadap penyewaan sepeda, pola musiman, dan faktor-faktor lain yang memengaruhi penggunaan sepeda.

## Fitur

- Analisis penyewaan sepeda berdasarkan cuaca
- Identifikasi pola musiman dalam penyewaan sepeda
- Visualisasi interaktif menggunakan Streamlit
- Dataset yang sudah dibersihkan dan siap untuk analisis

## Prasyarat

Sebelum menjalankan proyek ini, pastikan Anda telah menginstal Python (versi 3.7 atau yang lebih baru) dan pip.

## Langkah-langkah untuk Meng-clone dan Menjalankan Proyek

1. **Clone repositori ini**

   Gunakan perintah git berikut untuk meng-clone repositori:

   ```bash
   git clone https://github.com/username/bike-sharing-analysis.git
Ganti username dengan nama pengguna GitHub Anda.

Navigasi ke direktori proyek

bash
Copy code
cd bike-sharing-analysis
Buat lingkungan virtual (opsional)

Sangat disarankan untuk menggunakan lingkungan virtual untuk menghindari konflik dengan paket lain:

bash
Copy code
python -m venv venv
source venv/bin/activate  # Untuk Linux/Mac
venv\Scripts\activate     # Untuk Windows
Instal dependensi

Pastikan untuk menginstal semua pustaka yang diperlukan dengan menjalankan:

bash
Copy code
pip install -r requirements.txt
Jalankan aplikasi Streamlit

Setelah semua dependensi terinstal, jalankan aplikasi dengan perintah:

bash
Copy code
streamlit run dashboard/dashboard.py
Akses aplikasi

Setelah menjalankan perintah di atas, Streamlit akan memberikan tautan di terminal (biasanya http://localhost:8501) di mana Anda dapat melihat aplikasi di browser Anda.

Dataset
Dataset yang digunakan dalam proyek ini:

day_clean.csv: Data penyewaan sepeda per hari
hour_clean.csv: Data penyewaan sepeda per jam
Kedua file ini harus diletakkan di dalam folder dashboard.
