import pickle
import streamlit as st
import pandas as pd 
import os
import numpy as np
import altair as alt

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))

st.title('Prediksi Harga Mobil')

st.header("Dataset")

#open file csv
df1 = pd.read_csv('HargaMobil.csv')
st.dataframe(df1)

st.write("Grafik Highway-mpg")
chart_highwaympg = df1[['highwaympg', 'price']]
st.line_chart(chart_highwaympg)

st.write("Grafik curbweight")
chart_curbweight = df1[['curbweight', 'price']]
st.line_chart(chart_curbweight)

st.write("Grafik horsepower")
chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
st.line_chart(chart_horsepower)

#input nilai dari variable independent
highwaympg = st.number_input("Highway MPG", min_value=0.0, max_value=50.0, step=0.1)
curbweight = st.number_input("Curb Weight", min_value=0.0, max_value=5000.0, step=1.0)
horsepower = st.number_input("Horsepower", min_value=0.0, max_value=500.0, step=1.0)


if st.button('Prediksi'):
    #prediksi variable yang telah diinputkan
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

    #convert ke string
    harga_mobil_float = car_prediction[0] 
    
    #tampilkan hasil prediksi
    harga_mobil_formatted = f"${harga_mobil_float:,.2f}"
    st.success(f"Harga Mobil yang diprediksi: {harga_mobil_formatted}")