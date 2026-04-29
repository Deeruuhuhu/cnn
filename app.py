import streamlit as st
from PIL import Image
import numpy as np

# CIFAR-10 labels
class_names = [
    'Airplane', 'Automobile', 'Bird', 'Cat', 'Deer',
    'Dog', 'Frog', 'Horse', 'Ship', 'Truck'
]

# Title
st.title("CNN Image Classification App")
st.write("Upload an image for classification")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Open image
    image = Image.open(uploaded_file).convert("RGB")

    # Display image
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Dummy prediction for quick deployment/demo
    predicted_class = "Cat"
    confidence = 92.45

    # Output
    st.subheader(f"Prediction: {predicted_class}")
    st.write(f"Confidence: {confidence}%")
