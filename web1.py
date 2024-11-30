import streamlit as st

st.write('Hello Leni!')

st.header('button')

if st.button('say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')