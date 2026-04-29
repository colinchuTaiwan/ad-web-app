import streamlit as st
import base64
import os

st.set_page_config(layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def display_ad_only(image_file):
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        st.markdown(
            f"""
            <style>
            /* 隱藏所有 Streamlit 預設元件 */
            header, footer, #MainMenu {{visibility: hidden;}}
            .block-container {{padding: 0 !important; max-width: 100%;}}
            
            .ad-wrapper {{
                width: 100%;
                display: flex;
                justify-content: center;
                background-color: white;
            }}
            .ad-img {{
                width: 100%;
                height: auto;
                display: block;
            }}
            </style>
            <div class="ad-wrapper">
                <img class="ad-img" src="data:image/jpg;base64,{bin_str}">
            </div>
            """,
            unsafe_allow_html=True
        )

display_ad_only('messageImage_1777436648216.jpg')
