import streamlit as st
from PIL import Image

# 1. 設置網頁標題
st.set_page_config(page_title="自定義封面網頁", layout="wide")

st.title("🖼️ 網頁封面設置工具")

# 2. 側邊欄上傳圖片
st.sidebar.header("上傳區域")
uploaded_file = st.sidebar.file_uploader("選擇一張圖片作為封面", type=["jpg", "jpeg", "png"])

# 3. 封面邏輯
if uploaded_file is not None:
    # 讀取圖片
    image = Image.open(uploaded_file)
    
    # 顯示封面 (use_container_width 會讓圖片填滿容器寬度)
    st.image(image, caption="目前網頁封面", use_container_width=True)
    
    st.success("封面更換成功！")
else:
    # 若未上傳，顯示預設提示或預設圖片
    st.info("請從左側上傳圖片來生成封面。")
    # 你也可以放一張預設圖
    # st.image("https://via.placeholder.com/1200x400", use_container_width=True)

# 4. 網頁其餘內容
st.divider()
st.header("歡迎來到我的網站")
st.write("這是一個展示如何動態更換封面的簡單範例。")
