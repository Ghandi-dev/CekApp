import streamlit as st
import pandas as pd

df = pd.read_excel('Book1.xlsx')
data = df.to_numpy()
pilihan = []
p = 1
i =0
stress = []
kecemasan = []
depresi = []
with st.sidebar:
    str = "Ingatlah bahwa hasil dari tes ini hanyalah sebagian gambaran dari seseorang dan tidak selalu benar 100%, sebaiknya jangan mengambil keputusan yang signifikan hanya dengan hasil tes kepribadian saja.Jika anda ingin tes yang lebih valid dan akurat, anda harus mengambil tes yang dikembangkan dan divalidasi oleh profesional psikologi."
    st.info(str)
st.title("Test tingkat depresi")
st.write("Kuisioner ini terdiri dari berbagai yang mungkin sesuai dengan pengalaman kamu dalam menghadapi situasi hidup sehari-hari.")
st.write("Terdapat empat pilihan jawaban yang disediakan untuk setiap pertanyaan")
st.write("Keterangan :<br>0 : Tidak ada atau tidak pernah<br>1 : Sesuai dengan yang dialami sampai tingkat tertentu, atau kadang-kadang<br>2 : Sering<br>3 : Sangat sesuai dengan yang dialami, atau hampir setiap saat.",unsafe_allow_html=True)
print(data)
print(data.size)
def hitung(depresi):
    return sum(depresi)

def cek(cekDepresi):
    #Depresi
    if cekDepresi <= 9:
        tingkatDepresi ="Normal"
    elif cekDepresi > 9 and cekDepresi <= 13:
        tingkatDepresi ="Ringan"
    elif cekDepresi > 13 and cekDepresi <=20:
        tingkatDepresi ="Sedang"
    elif cekDepresi > 20 and cekDepresi <=27:
        tingkatDepresi ="Parah"
    elif cekDepresi >= 27:
        tingkatDepresi = "Sangat Parah"
    return tingkatDepresi

no =1
while i != p :
    if data[i][1] == "depresi":
        st.info(f"{no}. {data[i][0]}")
        pilih = st.radio("Hai",[0,1,2,3],horizontal=True,key=i,label_visibility="collapsed")
        depresi.append(pilih)
        no+=1
    if p < data.size/2:
        p+=1
    i+=1

if st.button("Submit"):
    cekDepresi = hitung(depresi)
    st.success(f"{cek(cekDepresi)}")
