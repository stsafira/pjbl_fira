import streamlit as st

st.set_page_config(
    page_title = "Website Fira",
    page_icon = ":fire:"
)

with st.sidebar:
    col1, col2, col3 = st.columns((1,2,1))
    with col2:
        st.image("fira.jpeg")
    st.title("Belajar Berhitung Bersama Fira")
    pilihan = st.selectbox("Pilihan Fitur", ["Persegi","Persegi Panjang","Lingkaran"])
    st.caption("Dibuat dengan :fire: oleh Siti Safira")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi 
            st.success(f"Luas Persegi Adalah {luas} dan Kelilingnya Adalah {keliling}")

    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung 'luas' dan 'keliling' persegi panjang")
        lebar = st.number_input("Masukkan Lebar")
        panjang = st.number_input("Masukkan Panjang")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2*(panjang + lebar)
            st.success(f"Luas Persegi Panjang Adalah {luas} dan Kelilingnya Adalah {keliling}")

    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung 'luas' dan 'keliling' lingkaran")
        jarijari = st.number_input("Masukkan Jari-Jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * (jarijari**2)
            keliling = 2 * 3.14 * jarijari
            st.success(f"Luas Lingkaran Adalah {luas} dan Kelilingnya Adalah {keliling}")