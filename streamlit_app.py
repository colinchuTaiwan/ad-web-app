import streamlit as st
import base64
import os

# 1. 網頁基本設定
st.set_page_config(page_title="課程宣傳網頁", layout="wide")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_course_banner(image_file):
    if os.path.exists(image_file):
        bin_str = get_base64_of_bin_file(image_file)
        
        # CSS 讓廣告圖完整顯示並呈現專業質感
        banner_html = f'''
        <style>
        /* 移除 Streamlit 預設邊距，讓廣告圖頂天立地 */
        .block-container {{
            padding-top: 0rem !important;
            padding-bottom: 0rem !important;
            max-width: 100% !important; /* 讓內容可以延伸到最邊緣 */
        }}

        .ad-container {{
            width: 100%;
            background-color: #f0f2f6; /* 圖片加載前的底色 */
            display: flex;
            justify-content: center;
            margin-bottom: 40px;
        }}

        .ad-img {{
            width: 100%;       /* 寬度百分之百 */
            max-width: 1200px; /* 限制最大寬度，避免在大螢幕上圖片糊掉 */
            height: auto;      /* 高度自動，保證宣傳圖文字不變形、不被切 */
            box-shadow: 0 10px 30px rgba(0,0,0,0.2); /* 幫廣告加點陰影，更有質感 */
        }}
        
        /* 手機版適應 */
        @media (max-width: 768px) {{
            .ad-img {{
                max-width: 100%;
            }}
        }}
        </style>
        
        <div class="ad-container">
            <img class="ad-img" src="data:image/jpg;base64,{bin_str}" alt="Course Advertisement">
        </div>
        '''
        st.markdown(banner_html, unsafe_allow_html=True)
    else:
        st.error(f"找不到宣傳圖片：{image_file}")

# --- 網頁開始 ---

# 2. 顯示課程宣傳廣告圖 (保證完整顯示)
set_course_banner('messageImage_1777436648216.jpg')

# 3. 課程詳細資訊區塊
# 使用 Container 讓下方的文字內容集中，不要太分散
container = st.container()
with container:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.title("🚀 2026 年度旗艦課程：從零到一掌握 AI")
        st.write("""
        這是一門專為初學者設計的實戰課程，我們將帶領你深入淺出地了解最新技術。
        不僅有理論教學，更有豐富的專案實作，讓你學完後能直接應用在工作上！
        """)
        st.markdown("### 🗓️ 課程大綱")
        st.write("- 第一週：基礎概念與環境架構")
        st.write("- 第二週：核心技術深挖")
        st.write("- 第三週：實戰專案演練")

    with col2:
        # 側邊資訊卡片
        st.info("🕒 **開課時間**：2026/05/20")
        st.warning("🔥 **剩餘名額**：最後 5 位")
        if st.button("👉 立即報名課程", use_container_width=True):
            st.balloons()
            st.success("跳轉至報名表單...")

st.divider()
st.center = st.write("© 2026 課程學苑 版權所有")
