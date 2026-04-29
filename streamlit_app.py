import streamlit as st
import base64
import os

# 設置網頁標題
#st.set_page_config(page_title="我的靜態封面網頁", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_full_page_background(image_file):
    """
    將圖片設置為全螢幕背景
    """
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{bin_str}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        /* 添加一個深色遮罩 (Scrim)，確保白色文字清晰可見 */
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 70%;
            height: 70%;
            background-color: rgba(0, 0, 0, 0.3); /* 0.3 是透明度，可依需求調整 */
            z-index: -1;
        }}

        /* 調整標題顏色為白色以符合封面感 */
        h1, h2, h3, p {{
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    else:
        st.error(f"找不到圖片檔案: {image_file}，請確認檔案已上傳至 GitHub。")

# 執行背景設置 (請確認檔名完全一致)
set_full_page_background('messageImage_1777436648216.jpg')

# 網頁內容
#st.title("歡迎來到我的 Streamlit 頁面")
#st.subheader("這張背景圖是直接讀取本地檔案生成的")
#st.write("目前不需要透過上傳按鈕，只要專案夾內有圖片即可顯示。")
