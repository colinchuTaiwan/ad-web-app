import streamlit as st
import base64
import os

st.set_page_config(page_title="大氣封面網頁", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_professional_hero(image_file):
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        
        hero_html = f'''
        <style>
        /* 封面容器：使用 60vh 代表佔據螢幕高度的 60% */
        .hero-section {{
            width: 100%;
            height: 60vh; 
            min-height: 400px;
            background: linear-gradient(rgba(0,0,0,0.2), rgba(0,0,0,0.2)), 
                        url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            flex-direction: column;
            border-radius: 20px;
            margin-bottom: 50px;
        }}

        /* 隱藏 Streamlit 預設的多餘間距 */
        .block-container {{
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }}

        /* 封面文字特效 */
        .hero-text {{
            font-size: 3.5rem;
            font-weight: 800;
            text-shadow: 0px 4px 10px rgba(0,0,0,0.5);
            letter-spacing: 2px;
        }}
        </style>
        
        <div class="hero-section">
            <h1 class="hero-text">WELCOME</h1>
            <p style="font-size: 1.2rem; opacity: 0.9;">探索資料的視覺之美</p>
        </div>
        '''
        st.markdown(hero_html, unsafe_allow_html=True)
    else:
        st.error(f"檔案 {image_file} 不存在")

# 執行封面
set_professional_hero('messageImage_1777436648216.jpg')

# 下方內容
st.header("📊 數據概覽")
col1, col2, col3 = st.columns(3)
col1.metric("造訪人數", "1,200", "+5%")
col2.metric("活躍用戶", "450", "-2%")
col3.metric("完成率", "88%", "+10%")
