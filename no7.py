import streamlit as st
import pandas as pd
import numpy as np

df= pd.DataFrame(
    np.random.randn(10, 2),
    columns=['x', 'y'])
st.line_chart(df)

st.bar_chart(df)
st.area_chart(df)