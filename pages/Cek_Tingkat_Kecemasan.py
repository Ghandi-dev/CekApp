import streamlit as st
import pandas as pd

with st.sidebar:
    str = "Ingatlah bahwa hasil dari tes ini hanyalah sebagian gambaran dari seseorang dan tidak selalu benar 100%, sebaiknya jangan mengambil keputusan yang signifikan hanya dengan hasil tes ini saja.Jika anda ingin tes yang lebih valid dan akurat, anda harus mengambil tes yang dikembangkan dan divalidasi oleh profesional psikologi."
    st.info(str)
st.title("Test tingkat kecemasan")
st.write("Kuisioner ini terdiri dari berbagai yang mungkin sesuai dengan pengalaman kamu dalam menghadapi situasi hidup sehari-hari.")
st.write("Terdapat empat pilihan jawaban yang disediakan untuk setiap pertanyaan")
st.write("Keterangan :<br>0 : Tidak ada atau tidak pernah<br>1 : Sesuai dengan yang dialami sampai tingkat tertentu, atau kadang-kadang<br>2 : Sering<br>3 : Sangat sesuai dengan yang dialami, atau hampir setiap saat.",unsafe_allow_html=True)

df = pd.read_excel('Book1.xlsx')
data = df.to_numpy()
kecemasan = []


def hitung(kecemasan):
    return sum(kecemasan)

def cek(cekKecemasan):
    #kecemasan
    if cekKecemasan <= 7:
        tingkatKecemasan ="Normal"
    elif cekKecemasan > 7 and cekKecemasan <= 9:
        tingkatKecemasan ="Ringan"
    elif cekKecemasan > 9 and cekKecemasan <=14:
        tingkatKecemasan ="Sedang"
    elif cekKecemasan > 14 and cekKecemasan <=19:
        tingkatKecemasan ="Parah"
    elif cekKecemasan >= 20:
        tingkatKecemasan = "Sangat Parah"
    return tingkatKecemasan

p = 1
i =0
no = 1
while i != p :
    if data[i][1] == "kecemasan":
        st.info(f"{no}. {data[i][0]}")
        pilih = st.radio("Hai",[0,1,2,3],horizontal=True,key=i,label_visibility="collapsed")
        kecemasan.append(pilih)
        no+=1
    if p < data.size/2:
        p+=1
    i+=1

if st.button("Submit"):
    cekKecemasan= hitung(kecemasan)
    st.success(f"{cek(cekKecemasan)}")