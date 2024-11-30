import streamlit as st
import datetime

st.number_input('Pick a number', value=1, step=1)
st.text_input('Email Address')

st.date_input('Travelling date', value=datetime.datetime.strptime('2024/07/23', '%Y/%m/%d').date())

st.time_input('School time', value=datetime.datetime.strptime('08:00', '%H:%M').time())
st.text_area('Description')

st.file_uploader('Upload a photo', type=['jpg', 'jpeg', 'png'])
st.color_picker('Pilih warna favorit anda', value='#1E3E62')