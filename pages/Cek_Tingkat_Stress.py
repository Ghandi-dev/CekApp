import streamlit as st
import pandas as pd

with st.sidebar:
    str = "Ingatlah bahwa hasil dari tes ini hanyalah sebagian gambaran dari seseorang dan tidak selalu benar 100%, sebaiknya jangan mengambil keputusan yang signifikan hanya dengan hasil tes ini saja.Jika anda ingin tes yang lebih valid dan akurat, anda harus mengambil tes yang dikembangkan dan divalidasi oleh profesional psikologi."
    st.info(str)
st.title("Test tingkat stres")
st.write("Kuisioner ini terdiri dari berbagai yang mungkin sesuai dengan pengalaman kamu dalam menghadapi situasi hidup sehari-hari.")
st.write("Terdapat empat pilihan jawaban yang disediakan untuk setiap pertanyaan")
st.write("Keterangan :<br>0 : Tidak ada atau tidak pernah<br>1 : Sesuai dengan yang dialami sampai tingkat tertentu, atau kadang-kadang<br>2 : Sering<br>3 : Sangat sesuai dengan yang dialami, atau hampir setiap saat.",unsafe_allow_html=True)

df = pd.read_excel('Book1.xlsx')
data = df.to_numpy()
stres = []


def hitung(stres):
    return sum(stres)

def cek(cekStres):
     #Stress
    if cekStres <= 7:
        tingkatStres ="Normal"
    elif cekStres > 7 and cekStres <= 9:
        tingkatStres ="Ringan"
    elif cekStres > 9 and cekStres <=14:
        tingkatStres ="Sedang"
    elif cekStres > 14 and cekStres <=19:
        tingkatStres ="Parah"
    elif cekStres >= 20:
        tingkatStres = "Sangat Parah"
    return tingkatStres

p = 1
i =0
no = 1
while i != p :
    if data[i][1] == "Stress":
        st.info(f"{no}. {data[i][0]}")
        pilih = st.radio("Hai",[0,1,2,3],horizontal=True,key=i,label_visibility="collapsed")
        stres.append(pilih)
        no+=1
    if p < data.size/2:
        p+=1
    i+=1

if st.button("Submit"):
    cekStres= hitung(stres)
    st.success(f"{cek(cekStres)}")