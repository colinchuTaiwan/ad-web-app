import streamlit as st
import base64
import os

st.set_page_config(page_title="精簡封面網頁", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_hero_banner(image_file):
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        
        # 這裡調整高度 (height) 和邊距 (margin)
        banner_html = f'''
        <style>
        .hero-container {{
            width: 100%;
            height: 350px; /* 控制封面高度，你可以改為 250px 或 400px */
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 15px; /* 圓角看起來更現代 */
            margin-bottom: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }}
        
        .hero-img {{
            width: 100%;
            height: 100%;
            object-fit: cover; /* 關鍵：裁切圖片以填滿區域，不拉伸變形 */
            object-position: center; /* 圖片對齊中心 */
        }}
        
        /* 移除 Streamlit 預設的上邊距，讓封面更靠上 */
        .block-container {{
            padding-top: 2rem !important;
        }}
        </style>
        
        <div class="hero-container">
            <img class="hero-img" src="data:image/jpg;base64,{bin_str}">
        </div>
        '''
        st.markdown(banner_html, unsafe_allow_html=True)
    else:
        st.error("找不到圖片檔案")

# 1. 放置封面 (高度較小，不會塞滿整個螢幕)
set_hero_banner('messageImage_1777436648216.jpg')

# 2. 放置標題與內容
st.title("專案標題")
st.write("現在封面高度被限制在 350px，看起來會精緻許多，不會有壓迫感。")

# 3. 測試一些內容讓頁面可以捲動
st.divider()
for i in range(5):
    st.write(f"這是內容區塊 {i+1}，你可以在這裡放置你的數據或圖表。")
