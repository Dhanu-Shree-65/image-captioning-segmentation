
import streamlit as st
from PIL import Image
import json
import os

# Set page title
st.title("🖼️ Image Captioning and Segmentation Demo")

# Load sample captions
captions = {}
if os.path.exists("captions.json"):
    with open("captions.json", "r") as f:
        captions = json.load(f)

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    image_name = uploaded_file.name

    # Simulate caption output
    caption = captions.get(image_name, "No caption available.")
    st.markdown(f"**Generated Caption:** {caption}")

    # Display simulated segmentation (static demo)
    st.subheader("Sample Segmentation Result")
    sample_seg_path = "sample_segmented_image.png"
    if os.path.exists(sample_seg_path):
        st.image(sample_seg_path, caption="Segmented Output", use_column_width=True)
    else:
        st.warning("Segmentation image not available.")
else:
    st.info("Please upload an image to begin.")
