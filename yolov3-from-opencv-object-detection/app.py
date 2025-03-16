import streamlit as st
from PIL import Image
import os

import main

st.title('An Optical Character Recognition service specialized in plate number recognition')
st.write('Upload the image, please:')
language = st.radio('Choose number plate region:', ('English', 'Farsi'), index=0)
uploaded_file = st.file_uploader("Choose the image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    file_path = os.path.join(main.input_dir, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.image(image, caption='uploaded image', use_container_width=True)

    results = main.logic(file_path, language)
    if results:
        st.write(f'plate number: {results[0]}')
        st.image(results[2], caption='black and white plate pic', use_container_width=True)
        st.image(results[3], caption='thresh plate pic', use_container_width=True)

    else:
        st.write('plate number was not recognized in the image')