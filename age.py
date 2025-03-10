import streamlit as st
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

def age_reduction(image: Image.Image):
    """
    Dummy function to simulate age reduction.
    Ideally, this would be replaced by a pre-trained AI model like GFPGAN, StyleGAN, etc.
    """
    image_np = np.array(image)
    image_np = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    # Apply a simple smoothing filter to mimic skin softening
    processed_image = cv2.GaussianBlur(image_np, (15, 15), 5)
    processed_image = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
    
    return Image.fromarray(processed_image)

def main():
    st.title("Age Reduction App")
    st.write("Upload an image, and we'll try to make the person look younger!")
    
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Original Image", use_column_width=True)
        
        if st.button("Reduce Age"):
            result_image = age_reduction(image)
            st.image(result_image, caption="Age Reduced Image", use_column_width=True)
            
            # Convert image to bytes for download
            buf = BytesIO()
            result_image.save(buf, format="PNG")
            byte_im = buf.getvalue()
            
            st.download_button(
                label="Download Image",
                data=byte_im,
                file_name="age_reduced.png",
                mime="image/png"
            )

if __name__ == "__main__":
    main()
