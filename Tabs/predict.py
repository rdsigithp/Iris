import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("Halaman Prediksi")

    col1, col2= st.columns(2)

    with col1:
        SepalLengthCm = st.text_input ('input nilai Panjang kelopak bunga dalam(cm)')
    with col1:
        SepalWidthCm = st.text_input ('input nilai Lebar kelopak bunga dalam(cm)')
    with col2:
        PetalLengthCm = st.text_input ('input nilai Panjang mahkota bunga dalam(cm)')
    with col2:
        PetalWidthCm = st.text_input ('input nilai Lebar mahkota bunga dalam(cm)')
    
    
    features = [SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm]

    #tombol
    if st.button("prediksi"):
        prediction, score =  predict(x,y,features)
        score = score
        st.info("prediksi sukses✔️")

        if (prediction == 1):
            st.warning("Termasuk kedalam spesies Bunga Iris-versicolor")
        elif (prediction == 2):
            st.warning("Termasuk kedalam spesies Bunga Iris-virginica")
        else:
            st.success("Termasuk kedalam spesies Bunga Iris-setosa")
        
        st.write("model akurasi", (score*100), "%")