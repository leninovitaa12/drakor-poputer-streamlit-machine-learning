import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(layout="wide")

st.sidebar.title("Select Page")
page = st.sidebar.selectbox("", ["Home", "Dataset", "Chart"])

if page == "Home":
    st.title("Selamat datang di Web Leni dengan Streamlit python!")
    st.image("tesspeed.png", width=500)

elif page == "Dataset":
    st.title("Dataset")
    df = pd.read_csv("data_mhs.csv", sep=";", header=0)
    st.dataframe(df)

elif page == "Chart":
    st.title("Chart pada data anda akan tampil disini")
    df = pd.read_csv("data_mhs.csv", sep=";", header=0)
    df["Income $"] = df["Income $"].astype(str).str.replace(",", "").astype(int)
    chart = alt.Chart(df).mark_bar().encode(
        alt.X("ID", title="ID"),
        alt.Y("Income $", title="Income $"),
        alt.Color("Jurusan", title="Jurusan"),
    )
    st.altair_chart(chart, use_container_width=True)