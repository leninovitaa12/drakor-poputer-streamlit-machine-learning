import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer  

st.set_page_config(
    page_title="Analisis Data Korean Drama",
    page_icon=":heart:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Load data from CSV file 
drama_data = pd.read_csv("kdrama.csv", sep=",", header=None)  

# nama kolom dari file csv
drama_data.columns = ["ID", "Title", "Genre", "Tags", "Synopsis", "Rank", "Popularity", "Score", "Episodes", "Duration", "Watchers", "Start_date", "End_date", "Day_aired", "Main Role"]

# kolom dibuat numeric
drama_data['Score'] = pd.to_numeric(drama_data['Score'], errors='coerce')
drama_data['Rank'] = pd.to_numeric(drama_data['Rank'], errors='coerce')
drama_data['Popularity'] = pd.to_numeric(drama_data['Popularity'], errors='coerce')
drama_data['Episodes'] = pd.to_numeric(drama_data['Episodes'], errors='coerce')
drama_data['Duration'] = pd.to_numeric(drama_data['Duration'], errors='coerce')
drama_data['Watchers'] = pd.to_numeric(drama_data['Watchers'], errors='coerce')

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Select Page", ["Home", "Data", "Visualization", "Machine Learning", "Contact"])

# Home Page
if page == "Home":
    st.title("Analisis Data Korean Drama :heart:")
    st.image("rumah.jpg", caption="Korean Drama", use_container_width=True)  
    st.markdown("Selamat datang di Aplikasi Web Korean Drama Data Analysis! Explore and discover insights about popular Korean dramas.")

    # poster gambar
    st.header("Popular Korean Dramas")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("drama1.jpeg", caption="Drama 1") 
    with col2:
        st.image("drama2.jpeg", caption="Drama 2") 
    with col3:
        st.image("drama3.jpeg", caption="Drama 3") 

# Data Page
elif page == "Data":
    st.title("Korean Drama Data")
    st.header("Drama List")
    st.dataframe(drama_data)

    st.header("Descriptive Statistics")
    st.write(drama_data.describe())

# Drama Data Page
elif page == "Drama Data":
    st.title("Drama Data")
    st.header("Drama List")
    st.dataframe(drama_data)

# Visualization Page
elif page == "Visualization":
    st.title("Data Visualization")

    # Define highest_rated_drama before the if statement
    highest_rated_drama = drama_data[drama_data['Rank'] == 1]

    # Select chart type
    chart_type = st.selectbox("Select Chart Type", ["Scatter Plot", "Duration vs Rating", "Episode vs Rating"])

    if chart_type == "Scatter Plot":
        st.header("Scatter Plot")
        x_axis = st.selectbox("Select X-axis", drama_data.columns)
        y_axis = st.selectbox("Select Y-axis", drama_data.columns)

        fig, ax = plt.subplots()
        ax.scatter(drama_data[x_axis], drama_data[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title("Data Visualization")
        st.pyplot(fig)

    elif chart_type == "Duration vs Rating":
        st.header("Duration vs Rating (Highest Rated Drama)")
        fig, ax = plt.subplots()
        ax.scatter(highest_rated_drama["Duration"], highest_rated_drama["Score"])
        ax.set_xlabel("Duration")
        ax.set_ylabel("Rating")
        ax.set_title("Duration vs Rating")
        st.pyplot(fig)

    elif chart_type == "Episode vs Rating":
        st.header("Episode vs Rating (Highest Rated Drama)")
        fig, ax = plt.subplots()
        ax.scatter(highest_rated_drama["Episodes"], highest_rated_drama["Score"])
        ax.set_xlabel("Episode")
        ax.set_ylabel("Rating")
        ax.set_title("Episode vs Rating")
        st.pyplot(fig)

# Machine Learning Page
elif page == "Machine Learning":
    st.title("Prediksi dengan Machine Learning")

    # Select features (X) dan target variable (y)
    features = st.multiselect("Pilih Fitur", drama_data.columns, default=["Score"])
    target = st.selectbox("Pilih Target", drama_data.columns, index=drama_data.columns.get_loc('Rank'))

    # Method 2: Impute Missing Values 
    imputer = SimpleImputer(strategy='mean')
    drama_data[features] = imputer.fit_transform(drama_data[features])

    # Split data into dan tarining set
    X = drama_data[features]
    y = drama_data[target]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Handle NaN values in y_test and y_pred
    y_test_valid = y_test[~np.isnan(y_test)]  
    y_pred_valid = y_pred[~np.isnan(y_test)]  

    mse = mean_squared_error(y_test_valid, y_pred_valid)  
    r2 = r2_score(y_test_valid, y_pred_valid)  

    # Display model evaluation 
    st.write(f"Mean Squared Error: {mse}")
    st.write(f"R-squared: {r2}")

    # Display prediksi
    st.header("Prediksi vs Nilai Sebenarnya")
    st.write(f"Prediksi: {y_pred.tolist()}")
    st.write(f"Nilai Sebenarnya: {y_test.tolist()}")

# Contact Page
elif page == "Contact":
    st.title("Contact and About")
    st.header("About Me")
    st.write("Aplikasi web ini dibuat oleh Leni Novitasari")
    st.write("Aplikasi ini dibuat untuk mem-visualisasi dan menganalisis data dari Korean Drama.")

    st.header("Contact Information")
    st.write("Email: leninovitaa12@gmail.com")
    st.write("GitHub: https://github.com/leninovitaa12")
    st.write("Instagram: https://www.instagram.com/lenissii/")

    st.write("Seberapa suka anda dengan aplikasi saya?")
    st.slider('Geser untuk suka/tidak suka', 0, 100, 50)