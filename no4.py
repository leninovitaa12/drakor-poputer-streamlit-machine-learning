import streamlit as st

st.checkbox('yes')
st.button('klik')
st.radio('Pilih gender anda', ('Pria', 'Wanita'))
st.selectbox('choose a planet', ('Choose an option', 'Mars', 'Earth'))

st.slider('Pick a mark', 0, 100, 50)

st.slider('Pick a number', 0, 50, 9)