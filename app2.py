import streamlit as st
import pandas as pd
import keras
import numpy as np

# Inisialisasi default session_state
if "page" not in st.session_state:
    st.session_state.page = "Beranda"

# Load model dan data
model = keras.models.load_model('model.obesity.keras')
df = pd.read_excel('obesity_data.xlsx')

# Rekomendasi makanan berdasarkan hasil prediksi
food_recommendations = {
    0: """🍽️ **Normal:** Pertahankan pola makan seimbang!
- Konsumsi karbohidrat kompleks seperti nasi merah, quinoa, dan roti gandum.
- Perbanyak sayur berwarna-warni dan buah segar.
- Protein: ikan, ayam tanpa kulit, tahu, tempe, atau telur.
- Hindari makanan cepat saji & batasi konsumsi gula tambahan.
- Minum air putih minimal 2 liter per hari.""",

    1: """🍽️ **Underweight:** Tambah kalori sehat secara bertahap!
- Konsumsi makanan tinggi energi: alpukat, kacang-kacangan, selai kacang, granola.
- Susu full cream, keju, dan yogurt juga sangat disarankan.
- Tambahkan minyak zaitun/kelapa dalam masakan untuk menambah kalori sehat.
- Makan lebih sering (5–6 kali sehari) dalam porsi kecil.
- Tetap olahraga ringan untuk membentuk massa otot.""",

    2: """🍽️ **Overweight:** Fokus pada kontrol porsi & makanan padat gizi!
- Ganti nasi putih dengan nasi merah, jagung, atau ubi rebus.
- Hindari minuman manis dan snack tinggi gula.
- Konsumsi dada ayam, ikan panggang, dan sayuran rebus atau kukus.
- Kurangi gorengan, fast food, dan camilan tinggi lemak jenuh.
- Minum air putih sebelum makan untuk mengurangi nafsu makan.""",

    3: """🍽️ **Obese:** Prioritaskan makanan rendah kalori dan kaya serat!
- Hindari gorengan, makanan cepat saji, dan minuman berpemanis.
- Konsumsi banyak sayuran hijau, buah rendah gula (pepaya, apel, pir).
- Pilih karbohidrat kompleks: oats, nasi merah, kentang rebus.
- Utamakan protein tanpa lemak: tahu, tempe, ikan kukus.
- Gunakan teknik memasak sehat: rebus, kukus, panggang.
- Tetapkan jadwal makan teratur dan perbanyak aktivitas fisik ringan setiap hari."""
}


# ======================== HEADER UTAMA ========================
with st.container():
    image_col, title_col = st.columns([0.5, 2])
    with image_col:
        st.image("logo.png", width=150)
    with title_col:
        st.markdown("## **Smart Obesity Analyzer** 🔍")

# Styling agar judul sidebar rapi
st.markdown("""
    <style>
    .stMarkdown h3 {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)
# ======================== SIDEBAR NAVIGASI ========================
with st.sidebar:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("logo.png", width=150)

    st.markdown(
        "<div style='color: black; font-size: 18px; font-weight: bold; margin-bottom: 0px;'>📑 Navigasi Halaman</div>",
        unsafe_allow_html=True
    )

    # List opsi
    options = ["Beranda", "Tentang Aplikasi", "Cara Menggunakan", "Prediksi Obesitas"]

    # Simpan page di session_state agar bisa digunakan antar-halaman
    if "page" not in st.session_state:
        st.session_state.page = "Beranda"

    # Selectbox untuk navigasi
    page = st.selectbox(
        label="",
        options=options,
        index=options.index(st.session_state.page),
        label_visibility="collapsed"
    )
    
    # Simpan pilihan saat ini ke session_state
    st.session_state.page = page

    st.markdown("---")
    st.caption("© 2025 ObeSync by JasmineAbelVica")



# ======================== KONTEN ========================
if st.session_state.page == "Beranda":
    st.markdown("## 👋 Selamat Datang!")
    st.write("Prediksi cerdas hidup sehat mulai hari ini.")

    st.markdown("### 📌 Navigasi Cepat")
    st.markdown("""
- Pilih menu di **sidebar kiri** untuk mengakses fitur aplikasi.  
- Klik tombol di bawah ini untuk langsung menuju halaman prediksi obesitas.
""")

    if st.button("🔍 Mulai Prediksi Sekarang", key="btn_prediksi"):
        st.session_state.page = "Prediksi Obesitas"
        st.rerun()

   

elif page == "Tentang Aplikasi":
    st.markdown("### Apa Itu ObeSync?")
    st.markdown("""
**ObeSync** adalah alat pintar berbasis AI untuk mendeteksi tingkat obesitas secara cepat dan akurat.  
Tujuannya adalah membantu Anda mengenali status kesehatan tubuh sejak dini, sehingga Anda dapat mengambil langkah tepat untuk memulai gaya hidup yang lebih sehat dan seimbang.
Obesitas bukan sekadar masalah penampilan—ini adalah kondisi medis serius yang dapat meningkatkan risiko berbagai penyakit kronis, seperti:

❤️ Penyakit jantung.  
🧬 Diabetes tipe 2.  
🧠 Hipertensi atau tekanan darah tinggi.  

Sayangnya, banyak orang tidak menyadari kondisi tubuhnya hingga gejala muncul. Padahal, deteksi dini dapat menyelamatkan hidup.  
Dengan ObeSync, Anda memiliki alat bantu yang praktis untuk:

1. Mengetahui status kesehatan tubuh secara objektif  
2. Mengambil tindakan pencegahan sebelum terlambat  
3. Memulai perubahan kecil menuju gaya hidup yang lebih sehat dan berkelanjutan  

Jadikan ObeSync sebagai langkah awal menuju tubuh yang lebih sehat dan masa depan yang lebih baik.  
Karena kesehatan Anda, adalah investasi paling berharga.
""")

elif page == "Cara Menggunakan":
    st.markdown("### Bagaimana Cara Kerjanya?")
    st.markdown("""
Masukkan data berikut:
- 👤 Umur  
- ⚧️ Jenis Kelamin  
- 📏 Tinggi Badan  
- ⚖️ Berat Badan  

Sistem akan:
- ✅ Menghitung BMI otomatis  
- 🤖 Memprediksi tingkat obesitas menggunakan model AI  

Hasilnya akan membantu Anda memahami kondisi tubuh saat ini dan mengambil langkah yang tepat untuk meningkatkan kesehatan.
        """, unsafe_allow_html=True)


if page == "Prediksi Obesitas":
    output = None  # untuk menyimpan hasil prediksi

    with st.container():
        st.markdown("---")

        # Membuat dua kolom: input (2 bagian) dan output (1 bagian)
        input_col, output_col = st.columns([2, 1], vertical_alignment='top')

        # ===================== INPUT =====================
        with input_col:
            st.markdown("<h3 style='text-align: center; color: green;'>MASUKKAN DATA DIRI ANDA</h3>", unsafe_allow_html=True)

            age_col, gender_col, height_col = st.columns(3)
            weight_col, bmi_col, pal_col = st.columns(3)

            with age_col:
                age = st.text_input('**Umur**', placeholder=f"{df['Age'].min()} to {df['Age'].max()}")
                age = int(age) if age else None

            with gender_col:
                gender = st.selectbox('**Jenis Kelamin**', options=['Male', 'Female'])

            with height_col:
                height_input = st.text_input('**Tinggi Badan (cm)**', placeholder="e.g. 160")
                height = float(height_input) if height_input else None

            with weight_col:
                weight_input = st.text_input('**Berat Badan (kg)**', placeholder="e.g. 60")
                weight = float(weight_input) if weight_input else None

            with bmi_col:
                if height and weight:
                    bmi = round(weight / ((height / 100) ** 2), 2)
                    st.text_input('**BMI (auto-calculated)**', value=str(bmi), disabled=True)
                else:
                    bmi = None
                    st.text_input('**BMI (auto-calculated)**', value="Waiting input...", disabled=True)

            with pal_col:
                activity_mapping = {
                    'Tidak aktif': 1,
                    'Sedikit aktif': 2,
                    'Cukup aktif': 3,
                    'Sangat aktif': 4
                }
                pal_label = st.selectbox('**Aktivitas Fisik**', options=list(activity_mapping.keys()))
                pal = activity_mapping[pal_label]

        # ===================== OUTPUT =====================
        with output_col:
            st.markdown("<h3 style='text-align: center; color: green;'>HASIL PREDIKSI</h3>", unsafe_allow_html=True)
            result = st.empty()

            if st.button("🔍 Predict Obesity Level", key="btn_prediksi_obesitas"):
                if all([age, height, weight, pal, gender, bmi]):
                    try:
                        sample = {
                            'Age': age,
                            ' BMI ': bmi,
                            'Gender': gender,
                            ' Height ': height,
                            ' Weight ': weight,
                            'PhysicalActivityLevel': pal
                        }

                        raw_input = {
                            key: keras.ops.convert_to_tensor([value]) for key, value in sample.items()
                        }

                        prediction = model.predict(raw_input)
                        output = prediction[0].argmax()

                        with result.container():
                            if output == 0:
                                st.write('# 🙆🏻🤗✅')
                                st.info('**NORMAL WEIGHT ✅**')
                            elif output == 1:
                                st.write('# 🤦🏻😔👎🏻')
                                st.info('**UNDER WEIGHT 👎🏻**')
                            elif output == 2:
                                st.write('# 🙅🏻😲❌')
                                st.info('**OVER WEIGHT ❌**')
                            else:
                                st.write('# 🫄🏻🙄❎')
                                st.info('**OBESED ❎**')

                    except:
                        st.error("❌ Terjadi kesalahan saat menghitung atau memprediksi.")
                else:
                    st.warning("⚠️ Mohon isi semua input terlebih dahulu sebelum memprediksi.")

    # ===================== REKOMENDASI =====================
    if output is not None:
        st.markdown("<h3 style='text-align: center;'>🍽️ Rekomendasi Makanan</h3>", unsafe_allow_html=True)
        st.success(food_recommendations[output])


