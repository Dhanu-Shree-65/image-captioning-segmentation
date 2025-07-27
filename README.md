# 🖼️Image Captioning and Segmentation

This project combines two major tasks in computer vision — **Image Captioning** and **Image Segmentation** — into one integrated system. Image captioning automatically generates descriptive text for a given image using deep learning models like CNN+LSTM, while segmentation detects and labels objects within the image using models like U-Net.

We used datasets such as MS COCO for captioning and Pascal VOC for segmentation. The models were trained, evaluated, and then integrated into a Streamlit app to provide a simple user interface. Users can upload an image and receive a caption along with a segmented output.

This project provides hands-on experience with deep learning, natural language processing, and computer vision. Evaluation metrics include BLEU scores for captioning and IoU scores for segmentation.

##  Features
- Automatic image caption generation
- Semantic segmentation of image regions
- Web-based interactive app using Streamlit
- Sample results and model code included

## Files Included
- `app.py`: Web app code
- `captions.json`: Sample caption outputs
- `sample_segmented_image.png`: Segmentation example
- `Image_Captioning_Segmentation_Report.pdf`: Project report
