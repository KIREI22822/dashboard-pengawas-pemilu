# 🗳️ Dashboard Segmentasi Pengawas Pemilu

Dashboard interaktif untuk memvisualisasikan hasil segmentasi dan profiling pengawas pemilu berbasis data demografis menggunakan algoritma **K-Means Clustering**.

---

## 📌 Tentang Proyek

Proyek ini merupakan implementasi dari skripsi yang berjudul:

> **"Segmentasi dan Profiling Pengawas Pemilu Berbasis Data Demografis Menggunakan Algoritma K-Means Clustering"**

Dashboard ini dirancang untuk membantu Badan Pengawas Pemilihan Umum (Bawaslu) dalam:
- Memetakan karakteristik pengawas pemilu secara objektif
- Melihat distribusi pengawas berdasarkan cluster
- Menganalisis kebutuhan pelatihan dan pembinaan per wilayah

---

## ✨ Fitur Utama

| Fitur | Deskripsi |
|-------|-----------|
| 📊 **Ringkasan Statistik** | Total pengawas, rata-rata usia, pengalaman, dan proporsi gender |
| 📈 **Distribusi Data** | Grafik jenis kelamin, tingkat pendidikan, dan level wilayah kerja |
| 🗺️ **Peta Interaktif** | Sebaran pengawas per provinsi dengan warna berdasarkan cluster dominan |
| 📉 **Scatter Plot** | Hubungan antara usia dan pengalaman kerja |
| 📋 **Tabel Profil Cluster** | Karakteristik setiap cluster (usia, pengalaman, pendidikan, level kerja) |
| 🎯 **Rekomendasi** | Saran praktis untuk pelatihan dan penugasan berbasis cluster |

---

## 🛠️ Teknologi yang Digunakan

| Teknologi | Fungsi |
|-----------|--------|
| ![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python) | Bahasa pemrograman |
| ![Streamlit](https://img.shields.io/badge/Streamlit-1.36.0-FF4B4B?logo=streamlit) | Framework dashboard interaktif |
| ![Pandas](https://img.shields.io/badge/Pandas-2.2.0-150458?logo=pandas) | Manipulasi dan analisis data |
| ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.5.0-F7931E?logo=scikit-learn) | Implementasi K-Means Clustering |
| ![Folium](https://img.shields.io/badge/Folium-0.16.0-77B829?logo=leaflet) | Peta interaktif |

---

## 🚀 Cara Menjalankan Aplikasi
## 📁 Struktur Folder

---

## 📊 Hasil Penelitian

Berdasarkan analisis 500 data pengawas pemilu, ditemukan **3 cluster optimal**:

| Cluster | Nama | Jumlah | Rata-rata Usia | Rata-rata Pengalaman | Pendidikan Dominan | Level Kerja Dominan |
|---------|------|--------|----------------|----------------------|---------------------|---------------------|
| 0 | Pengawas Pemula | 37% | 26,5 tahun | 1,0 tahun | SMA/SMK | PTPS/TPS |
| 1 | Pengawas Madya | 39% | 33,2 tahun | 2,5 tahun | S1 | Kecamatan |
| 2 | Pengawas Senior | 24% | 44,8 tahun | 6,8 tahun | S1/S2 | Kabupaten/Kota |

### Rekomendasi Praktis:
- **Cluster 0 (Pemula)** → Pelatihan teknis dasar, pendampingan mentor
- **Cluster 1 (Madya)** → Pelatihan kepemimpinan, penanganan sengketa
- **Cluster 2 (Senior)** → Peran sebagai mentor dan advokasi kebijakan

---

## 👩‍💻 Penulis

**Kirei Debora Tasya Palar**  
Mahasiswa Program Studi Teknik Informatika  
Fakultas Teknik, Universitas Negeri Manado  
NIM: 22 210 054

### Dosen Pembimbing:
- **Dr. Irene R.H.T. Tangkawarouw, S.T., MISD**
- **Sondy C. Kumajas ST, MT**

---

## 📝 Lisensi

Proyek ini dibuat untuk tujuan akademik sebagai bagian dari skripsi di Program Studi Teknik Informatika, Universitas Negeri Manado.

---

## 📞 Kontak

- **Email:** [kireipalar@gmail.com]
- **GitHub:** [KIREI22822](https://github.com/KIREI22822)

### Prasyarat

Pastikan Anda telah menginstal:
- Python 3.8 atau lebih tinggi
- Pip (package manager Python)

### Langkah-langkah
cd dashboard-pengawas-pemilu
pip install -r requirements.txt
streamlit run dashboard_indonesia.py

1. **Clone repositori ini**
   ```bash
   git clone https://github.com/KIREI22822/dashboard-pengawas-pemilu.git
