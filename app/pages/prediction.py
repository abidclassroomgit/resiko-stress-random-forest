import streamlit as st
import pandas as pd

def show_prediction_page(df, model, stats):
    st.markdown("## 🔮 Prediksi Risiko Stres")

    st.warning("""
    ⚠️ **DISCLAIMER**
    
    Aplikasi ini diperuntukkan **Mahasiswa S1**
    dengan rentang umur **maksimal 25 tahun**.
    
    Hasil prediksi **bukan diagnosis medis**.
    """)

    if "show_result" not in st.session_state:
        st.session_state.show_result = False

    jurusan_list = df['Jurusan/Program Studi'].unique().tolist()

    jumlah_data = st.selectbox(
        "Jumlah data yang ingin diprediksi (maksimal 5)",
        [1, 2, 3, 4, 5]
    )

    data_batch = []

    for i in range(jumlah_data):
        st.markdown(f"### 👤 Data ke-{i+1}")
        col1, col2 = st.columns(2)

        with col1:
            gender = st.selectbox("Gender", ["Laki-laki", "Perempuan"], key=f"g{i}")
            umur = st.slider("Umur", 18, 25, 20, key=f"u{i}")
            jurusan = st.selectbox("Jurusan", jurusan_list, key=f"j{i}")
            status = st.selectbox("Status Hubungan", ["Jomblo", "Dalam hubungan"], key=f"s{i}")
            pemasukan = st.selectbox("Pemasukan Keluarga", ["Rendah", "Sedang", "Tinggi"], key=f"p{i}")

        with col2:
            ipk = st.slider("IPK", 0.0, 4.0, 3.0, 0.01, key=f"ipk{i}")
            belajar = st.slider("Jam Belajar per Hari", 1, 7, 4, key=f"b{i}")
            tidur = st.slider("Jam Tidur per Hari", 3, 9, 6, key=f"t{i}")
            tugas = st.slider("Jumlah Tugas Besar per Minggu", 0, 5, 2, key=f"tb{i}")
            olahraga = st.selectbox("Frekuensi Olahraga", ["Jarang", "Kadang", "Sering"], key=f"o{i}")

        data_batch.append({
            "Gender": gender,
            "Umur": umur,
            "Jurusan/Program Studi": jurusan,
            "Status Hubungan": status,
            "Pemasukan Keluarga": pemasukan,
            "IPK": ipk,
            "Jam Belajar": belajar,
            "Jam Tidur": tidur,
            "Jumlah Tugas": tugas,
            "Olahraga": olahraga
        })

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Prediksi Sekarang"):
            st.session_state.show_result = True

    with col2:
        # CUMA UBAH INI DOANG
        if st.button("➕ Input Data Baru"):
            # Clear ALL session state
            st.session_state.clear()
            st.rerun()

    if st.session_state.show_result:
        for idx, data in enumerate(data_batch):
            st.markdown("---")
            st.markdown(f"## 📊 Hasil Prediksi Data ke-{idx+1}")

            input_df = pd.DataFrame({
                "Gender": [data["Gender"]],
                "Umur": [data["Umur"]],
                "Jurusan/Program Studi": [data["Jurusan/Program Studi"]],
                "Jam Belajar per Hari": [(data["Jam Belajar"] - stats['mean']['Jam Belajar per Hari']) / stats['std']['Jam Belajar per Hari']],
                "Jam Tidur per Hari": [(data["Jam Tidur"] - stats['mean']['Jam Tidur per Hari']) / stats['std']['Jam Tidur per Hari']],
                "IPK": [(data["IPK"] - stats['mean']['IPK']) / stats['std']['IPK']],
                "Jumlah Tugas Besar per Minggu": [(data["Jumlah Tugas"] - stats['mean']['Jumlah Tugas Besar per Minggu']) / stats['std']['Jumlah Tugas Besar per Minggu']],
                "Frekuensi Olahraga": [data["Olahraga"]],
                "Pemasukan Keluarga": [data["Pemasukan Keluarga"]],
                "Status Hubungan": [data["Status Hubungan"]]
            })

            pred = model.predict(input_df)[0]
            proba = model.predict_proba(input_df)[0]

            sehat_idx = list(model.classes_).index("Sehat")
            stres_idx = list(model.classes_).index("Risiko Stres")

            if pred == "Sehat":
                st.markdown("""
                <div class="result-box result-sehat">
                    <h2>✅ SEHAT</h2>
                    <p>Risiko stres rendah</p>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="result-box result-stres">
                    <h2>⚠️ RISIKO STRES</h2>
                    <p>Berpotensi mengalami stres</p>
                </div>
                """, unsafe_allow_html=True)

            col1, col2 = st.columns(2)
            col1.metric("Probabilitas Sehat", f"{proba[sehat_idx]*100:.1f}%")
            col2.metric("Probabilitas Risiko Stres", f"{proba[stres_idx]*100:.1f}%")

            if pred == "Risiko Stres":
                st.warning("""
                💡 **Rekomendasi**
                - Tidur cukup 7–9 jam
                - Atur waktu belajar
                - Lakukan olahraga rutin
                - Konsultasi bila perlu
                """)
            else:
                st.success("""
                💡 **Pertahankan Pola Sehat**
                - Jaga manajemen waktu
                - Tetap aktif bergerak
                - Pertahankan kualitas tidur
                """)