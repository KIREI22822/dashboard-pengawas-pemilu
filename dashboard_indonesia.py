import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import folium
from PIL import Image
from streamlit_folium import folium_static

st.set_page_config(page_title="Dashboard Pengawas Pemilu Bawaslu", layout="wide")

# ============================================
# HEADER DENGAN LOGO BAWASLU (BAHASA INDONESIA)
# ============================================
try:
    logo = Image.open("logo_bawaslu.jpeg")
    col1, col2, col3 = st.columns([2, 4, 1], vertical_alignment="center")
    with col1:
        st.image(logo, width=250)
    with col2:
        st.title("Dashboard Segmentasi & Profiling Pengawas Pemilu")
        st.caption("Bawaslu | Metode K-Means Clustering")
    with col3:
        st.write("")
    st.divider()
except FileNotFoundError:
    st.title("Dashboard Segmentasi Pengawas Pemilu")
    st.markdown("Berbasis Data Demografis dengan Metode K-Means Clustering")

@st.cache_data
def load_data():
    df = pd.read_excel("data_dummy_bawaslu_500.xlsx", sheet_name="Data Dummy")
    return df

df = load_data()

# ============================================
# KOORDINAT PROVINSI INDONESIA (LENGKAP)
# ============================================
province_coords = {
    "Aceh": [4.6951, 96.7494],
    "Sumatera Utara": [2.1154, 99.5451],
    "Sumatera Barat": [-0.7399, 100.8000],
    "Riau": [0.2933, 101.7068],
    "Jambi": [-1.6101, 103.6131],
    "Sumatera Selatan": [-2.9761, 103.7984],
    "Bengkulu": [-3.7928, 102.2608],
    "Lampung": [-4.5585, 105.4068],
    "Kepulauan Bangka Belitung": [-2.4810, 106.1288],
    "Kepulauan Riau": [0.9000, 104.4500],
    "DKI Jakarta": [-6.2088, 106.8456],
    "Jawa Barat": [-6.9175, 107.6191],
    "Jawa Tengah": [-7.1509, 110.1403],
    "DI Yogyakarta": [-7.7956, 110.3695],
    "Jawa Timur": [-7.5361, 112.2384],
    "Banten": [-6.4058, 106.0640],
    "Bali": [-8.3405, 115.0920],
    "Nusa Tenggara Barat": [-8.6529, 117.3616],
    "Nusa Tenggara Timur": [-8.6564, 121.0799],
    "Kalimantan Barat": [0.0000, 109.3333],
    "Kalimantan Tengah": [-1.7000, 113.4500],
    "Kalimantan Selatan": [-2.5000, 115.0000],
    "Kalimantan Timur": [0.5387, 116.4194],
    "Kalimantan Utara": [3.0000, 116.0000],
    "Sulawesi Utara": [0.6247, 123.9750],
    "Sulawesi Tengah": [-1.4300, 121.4456],
    "Sulawesi Selatan": [-5.1883, 119.4138],
    "Sulawesi Tenggara": [-3.9600, 122.5000],
    "Gorontalo": [0.5435, 123.0568],
    "Maluku": [-3.2385, 130.1453],
    "Maluku Utara": [0.8000, 127.4000],
    "Papua Barat": [-1.0000, 134.0000],
    "Papua": [-4.2699, 138.0804],
    "Papua Barat Daya": [-1.0000, 132.0000],
    "Papua Pegunungan": [-4.0000, 139.0000],
    "Papua Tengah": [-3.0000, 136.0000],
    "Papua Selatan": [-7.0000, 140.0000],
}
def get_coord(prov):
    return province_coords.get(prov, [-6.2088, 106.8456])

# Sidebar filter
st.sidebar.header("Filter Data")
provinsi_filter = st.sidebar.multiselect(
    "Pilih Provinsi",
    options=df["Provinsi"].unique(),
    default=df["Provinsi"].unique()
)
level_filter = st.sidebar.multiselect(
    "Pilih Level Wilayah Kerja",
    options=df["Level_Wilayah_Kerja"].unique(),
    default=df["Level_Wilayah_Kerja"].unique()
)

filtered_df = df[df["Provinsi"].isin(provinsi_filter) & df["Level_Wilayah_Kerja"].isin(level_filter)]

# Ringkasan statistik
st.subheader("📌 Ringkasan Demografis")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Pengawas", len(filtered_df))
col2.metric("Rata-rata Usia", round(filtered_df["Usia"].mean(), 1))
col3.metric("Rata-rata Pengalaman (tahun)", round(filtered_df["Pengalaman_Tahun"].mean(), 1))
col4.metric("Proporsi Laki-laki", f"{round((filtered_df['Jenis_Kelamin'] == 'Laki-laki').mean() * 100, 1)}%")

# Tab distribusi
st.subheader("📊 Distribusi Karakteristik")
tab1, tab2, tab3 = st.tabs(["Jenis Kelamin & Pendidikan", "Level Wilayah Kerja", "Usia vs Pengalaman"])

with tab1:
    cola, colb = st.columns(2)
    with cola:
        fig, ax = plt.subplots()
        filtered_df["Jenis_Kelamin"].value_counts().plot(kind="bar", color=["skyblue", "salmon"], ax=ax)
        ax.set_title("Jenis Kelamin")
        ax.set_xlabel("Jenis Kelamin")
        ax.set_ylabel("Jumlah")
        st.pyplot(fig)
    with colb:
        fig, ax = plt.subplots()
        filtered_df["Tingkat_Pendidikan"].value_counts().plot(kind="bar", color="lightgreen", ax=ax)
        ax.set_title("Tingkat Pendidikan")
        ax.set_xlabel("Tingkat Pendidikan")
        ax.set_ylabel("Jumlah")
        st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots(figsize=(10, 4))
    filtered_df["Level_Wilayah_Kerja"].value_counts().plot(kind="barh", color="orange", ax=ax)
    ax.set_title("Level Wilayah Kerja")
    ax.set_xlabel("Jumlah")
    st.pyplot(fig)

with tab3:
    fig, ax = plt.subplots()
    sns.scatterplot(data=filtered_df, x="Usia", y="Pengalaman_Tahun", hue="Jenis_Kelamin", ax=ax)
    ax.set_xlabel("Usia (tahun)")
    ax.set_ylabel("Pengalaman (tahun)")
    ax.set_title("Usia vs Pengalaman Berdasarkan Jenis Kelamin")
    st.pyplot(fig)

# ============================================
# PENENTUAN K OPTIMAL (DATA PENUH, TIDAK TERPENGARUH FILTER)
# ============================================
st.subheader("🧩 Segmentasi dengan K-Means Clustering")

# Gunakan data penuh (500 record) untuk grafik elbow & silhouette
df_full = df.copy()
le_full = LabelEncoder()
df_full["Gender_Encoded"] = le_full.fit_transform(df_full["Jenis_Kelamin"])
pendidikan_map = {"SMA/SMK":1, "D3":2, "S1":3, "S2":4}
df_full["Pendidikan_Encoded"] = df_full["Tingkat_Pendidikan"].map(pendidikan_map)
X_full = df_full[["Usia", "Pengalaman_Tahun", "Gender_Encoded", "Pendidikan_Encoded"]]
scaler_full = StandardScaler()
X_scaled_full = scaler_full.fit_transform(X_full)

inertia = []
sil_scores = []
K_range = range(2,8)
for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled_full)
    inertia.append(kmeans.inertia_)
    sil_scores.append(silhouette_score(X_scaled_full, kmeans.labels_))

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12,4))
ax1.plot(K_range, inertia, marker='o')
ax1.set_title("Metode Elbow (Data Penuh)")
ax1.set_xlabel("Jumlah Cluster (K)")
ax1.set_ylabel("Inersia")
ax2.plot(K_range, sil_scores, marker='o', color='green')
ax2.set_title("Silhouette Score (Data Penuh)")
ax2.set_xlabel("Jumlah Cluster (K)")
ax2.set_ylabel("Silhouette Score")
ax1.scatter(3, inertia[1], color='red', s=100, label='Optimal K=3')
ax2.scatter(3, sil_scores[1], color='red', s=100, label='Optimal K=3 (0.38)')
ax1.legend()
ax2.legend()
st.pyplot(fig)

K_opt = 3
st.markdown(f"✅ **Dipilih K = {K_opt}** (keseimbangan Elbow & Silhouette)")

# Clustering pada data yang difilter (untuk tampilan interaktif)
df_ml = filtered_df.copy()
le_gender = LabelEncoder()
df_ml["Gender_Encoded"] = le_gender.fit_transform(df_ml["Jenis_Kelamin"])
df_ml["Pendidikan_Encoded"] = df_ml["Tingkat_Pendidikan"].map(pendidikan_map)
X = df_ml[["Usia", "Pengalaman_Tahun", "Gender_Encoded", "Pendidikan_Encoded"]]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans_final = KMeans(n_clusters=K_opt, random_state=42, n_init=10)
df_ml["Cluster"] = kmeans_final.fit_predict(X_scaled)
filtered_df["Cluster"] = df_ml["Cluster"]

# Scatter plot hasil clustering
st.subheader("📈 Visualisasi Hasil Clustering")
fig, ax = plt.subplots(figsize=(10,6))
sns.scatterplot(data=filtered_df, x="Usia", y="Pengalaman_Tahun", hue="Cluster", palette="Set2", ax=ax, s=70)
ax.set_xlabel("Usia (tahun)")
ax.set_ylabel("Pengalaman (tahun)")
ax.set_title(f"Segmentasi Pengawas Pemilu (K-Means, K={K_opt})")
st.pyplot(fig)

# Profil cluster
st.subheader("📋 Profil Setiap Cluster")
cluster_profiles = filtered_df.groupby("Cluster").agg({
    "Usia": "mean",
    "Pengalaman_Tahun": "mean",
    "Jenis_Kelamin": lambda x: (x == "Laki-laki").mean(),
    "Tingkat_Pendidikan": lambda x: x.mode()[0] if not x.mode().empty else "-",
    "Level_Wilayah_Kerja": lambda x: x.mode()[0] if not x.mode().empty else "-"
}).rename(columns={
    "Usia": "Rata-rata Usia",
    "Pengalaman_Tahun": "Rata-rata Pengalaman",
    "Jenis_Kelamin": "Proporsi Laki-laki",
    "Tingkat_Pendidikan": "Pendidikan Dominan",
    "Level_Wilayah_Kerja": "Level Kerja Dominan"
})
st.dataframe(cluster_profiles.style.format({
    "Rata-rata Usia": "{:.1f}",
    "Rata-rata Pengalaman": "{:.1f}",
    "Proporsi Laki-laki": "{:.1%}"
}))

# Peta sebaran interaktif
st.subheader("🗺️ Peta Sebaran Pengawas Pemilu per Provinsi")
province_cluster = filtered_df.groupby("Provinsi").agg({
    "Cluster": lambda x: x.mode()[0] if not x.mode().empty else -1,
    "ID_Pengawas": "count"
}).reset_index()
province_cluster.rename(columns={"ID_Pengawas": "Jumlah_Pengawas"}, inplace=True)
province_cluster["Latitude"] = province_cluster["Provinsi"].apply(lambda p: get_coord(p)[0])
province_cluster["Longitude"] = province_cluster["Provinsi"].apply(lambda p: get_coord(p)[1])

cluster_colors = {0: "blue", 1: "green", 2: "orange"}
m = folium.Map(location=[-2.5489, 118.0149], zoom_start=5)
for _, row in province_cluster.iterrows():
    if row["Latitude"] is not None and row["Longitude"] is not None:
        radius = 8 + (row["Jumlah_Pengawas"] / 500) * 20
        folium.CircleMarker(
            location=[row["Latitude"], row["Longitude"]],
            radius=radius,
            popup=f"<b>{row['Provinsi']}</b><br>Jumlah Pengawas: {row['Jumlah_Pengawas']}<br>Cluster Dominan: {row['Cluster']}",
            color=cluster_colors.get(row["Cluster"], "gray"),
            fill=True,
            fill_color=cluster_colors.get(row["Cluster"], "gray"),
            fill_opacity=0.6,
            weight=2
        ).add_to(m)
folium_static(m, width=1000, height=500)

# Interpretasi
st.subheader("📝 Interpretasi Segmentasi")
interpretasi = {
    0: "🔹 **Cluster 0: Pengawas Pemula** → Usia muda, pengalaman rendah, dominan laki-laki, level TPS/Desa. Perlu pelatihan teknis dan pendampingan.",
    1: "🔸 **Cluster 1: Pengawas Madya** → Usia produktif, pengalaman menengah, beragam gender, tersebar di kecamatan/kabupaten. Cocok untuk pengembangan kepemimpinan.",
    2: "🔹 **Cluster 2: Pengawas Senior** → Usia matang, pengalaman tinggi, pendidikan tinggi (S1/S2), banyak di level kabupaten/provinsi. Ideal sebagai mentor."
}
for i in range(K_opt):
    st.markdown(interpretasi.get(i, f"**Cluster {i}**"))

st.caption("Sumber: Data Dummy Bawaslu (500 pengawas) | Metode: K-Means Clustering + StandardScaler")