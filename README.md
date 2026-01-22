# Prediksi Risiko Stres Mahasiswa - Random Forest

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_logo.svg)](https://resiko-stress-random-forest-a2dcgt3xhzuhgj4nx5umxw.streamlit.app/)

Aplikasi berbasis web untuk memprediksi tingkat risiko stres pada mahasiswa menggunakan algoritma Random Forest. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Penambangan Data (Data Mining).

## 🚀 Fitur Utama

- **Prediksi Risiko Stres**: Input data psikologis dan gaya hidup untuk mendapatkan prediksi tingkat stres (Rendah, Sedang, Tinggi).
- **Visualisasi Data**: Menampilkan grafik performa model dan distribusi fitur.
- **Rekomendasi Personal**: Memberikan saran kesehatan mental berdasarkan hasil prediksi.
- **Antarmuka Interaktif**: Dibangun menggunakan Streamlit untuk pengalaman pengguna yang intuitif.

## 🛠️ Tech Stack

- **Bahasa Pemrograman**: Python
- **Framework Web**: Streamlit
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Data Manipulation**: Pandas, Numpy
- **Visualisasi**: Plotly, Matplotlib
- **Laporan**: PDF (Laporan Akhir & PPT)

## 📁 Struktur Proyek

```text
├── app/                # Source code aplikasi Streamlit
│   ├── pages/          # Halaman tambahan (Home, Dashboard, dll)
│   ├── styles/         # File CSS custom
│   └── app.py          # Main entry point aplikasi
├── data/               # Dataset (csv/xlsx)
├── models/             # Model machine learning yang sudah dilatih (pkl)
├── notebooks/          # Jupyter Notebooks untuk EDA dan eksperimen
├── reports/            # Dokumentasi proyek (Laporan & PPT)
├── src/                # Script utilitas (preprocessing, training)
├── requirements.txt    # Daftar dependensi Python
└── README.md           # Dokumentasi utama
```

## ⚙️ Instalasi & Penggunaan

### 1. Clone Repositori
```bash
git clone <repository-url>
cd resiko-stress-random-forest
```

### 2. Install Dependensi
Pastikan Anda sudah menginstal Python 3.9+.
```bash
pip install -r requirements.txt
```

### 3. Jalankan Aplikasi
```bash
streamlit run app/app.py
```

## 📊 Dataset
Dataset yang digunakan mencakup berbagai variabel mahasiswa seperti IPK, jam tidur, aktivitas fisik, dan faktor stres lainnya yang diproses menggunakan teknik Penambangan Data.

## 👥 Kontributor
**Kelompok 1 - Penambangan Data**
- Nabil Hibban Hardian
- Muhammad Aldo Toni Saputra
- Muhammad Abid
- Naia Syafina Hikmayanti
- Ridlo Fanata Wicaksana

---
*Dikembangkan untuk memenuhi Tugas Kuliah Semester 3 - Penambangan Data.*
