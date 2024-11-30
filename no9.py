import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import streamlit as st


#database
df_mobil = pd.read_csv("HargaMobil.csv")

#pilih fitur (x), variable target (y)
x = df_mobil[['highwaympg', 'curbweight', 'horsepower']]
y = df_mobil['price']

#bagi data menjadi set pelatihan  dan pengujian
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#buat dan latih model regresi linear
model_regresi = LinearRegression()
model_regresi.fit(x_train, y_train)

#simpan model yang telah dilatih ke file pickle
filename = 'model_prediksi_harga_mobil.sav'
pickle.dump(model_regresi, open(filename, 'wb'))

st.header('Anda sudah berhasil')