import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Load Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Train model
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

# Streamlit app
st.title("🌸 Iris Flower Prediction App")
st.write("Enter the flower measurements and get the species prediction!")

# Input fields
sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.1)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 1.4)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 0.2)

# Make prediction
if st.button("Predict"):
    features = [[sepal_length, sepal_width, petal_length, petal_width]]
    prediction = model.predict(features)
    species = iris.target_names[prediction][0]
    st.success(f"Predicted Species: {species}")
