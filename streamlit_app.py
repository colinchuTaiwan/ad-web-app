import streamlit as st
import base64
import os

# 1. 網頁設定
st.set_page_config(page_title="AI 跨域人才培訓計畫", layout="wide")

# 2. 定義顏色與資料 (來自你的 React Code)
palette = {
    "rose": {"dark": "#8c5260", "mid": "#e5bcc5", "light": "#f8edf0"},
    "sage": {"dark": "#4e6648", "mid": "#bed0b6", "light": "#eef5ec"},
    "slate": {"dark": "#435d72", "mid": "#b7c9d8", "light": "#edf4f8"},
    "sand": {"dark": "#6e5b34", "mid": "#dbcfae", "light": "#f7f2e7"},
}

# 3. CSS 注入：模擬 React 的精緻感
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Urbanist:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"] {{
        font-family: 'Urbanist', sans-serif;
    }}

    /* 隱藏預設元件 */
    #MainMenu, footer {{visibility: hidden;}}
    .stApp {{ background-color: #f8f9fa; }}

    /* 課程卡片樣式 */
    .course-card {{
        background: white;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 1px solid #ede9f2;
        margin-bottom: 20px;
    }}
    
    .day-header {{
        padding: 10px 20px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        margin-bottom: 15px;
        display: inline-block;
    }}
    </style>
""", unsafe_allow_html=True)

# 4. 頂部宣傳圖 (messageImage_1777436648216.jpg)
# 這裡沿用之前的 Base64 邏輯
def set_banner(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()
        st.markdown(f'''
            <div style="width:100%; overflow:hidden; border-radius:20px; margin-bottom:30px;">
                <img src="data:image/jpg;base64,{bin_str}" style="width:100%; height:auto;">
            </div>
        ''', unsafe_allow_html=True)

set_banner('messageImage_1777436648216.jpg')

# 5. 側邊欄：課程選擇 (對應 React 的 Tabs)
st.sidebar.title("🎯 選擇班別")
course_choice = st.sidebar.radio(
    "培訓班別路徑：",
    ["第一班・AI 辦公室應用班", "第二班・AI 工程開發實務班", "第三班・AI 跨域整合精進班", "第四班・AI 資訊治理整合班"]
)

# 根據選擇設定 theme 與內容 (這裡示範第一班)
if "第一班" in course_choice:
    p = palette["rose"]
    title = "AI 辦公室應用班"
    desc = "以生成式 AI 工具為核心，協助行政、文書人員建立 AI 輔助工作流。"
    outcomes = ["掌握提示詞工程", "熟練 Copilot 工具", "建立 AI SOP"]
elif "第二班" in course_choice:
    p = palette["sage"]
    title = "AI 工程開發實務班"
    desc = "深入 LLM API 串接、地端模型部署與 RAG 系統建構。"
    outcomes = ["LLM API 調教", "地端量化部署", "RAG 系統建構"]
# ... 依此類推 ...

# 6. 主要內容呈現
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown(f"<h1 style='color:{p['dark']}'>{title}</h1>", unsafe_allow_html=True)
    st.write(desc)
    
    # 模擬課表
    st.markdown(f"<div class='day-header' style='background:linear-gradient(135deg, {p['dark']}, {p['mid']})'>第一天：AI 基礎與協作</div>", unsafe_allow_html=True)
    st.info("09:00 - 10:30 | 生成式 AI 基礎素養")
    st.info("10:45 - 12:15 | 提示詞工程入門實作")
    
    st.markdown(f"<div class='day-header' style='background:linear-gradient(135deg, {p['dark']}, {p['mid']})'>第二天：資料分析與整合</div>", unsafe_allow_html=True)
    st.success("09:00 - 10:30 | Excel × AI 資料分析")
    st.success("10:45 - 12:15 | AI 商務溝通與公文撰寫")

with col2:
    st.markdown(f"""
        <div class="course-card">
            <h4 style="color:{p['dark']}">✦ 培訓目標</h4>
            <ul style="font-size:14px; color:#666;">
                {"".join([f"<li>{o}</li>" for o in outcomes])}
            </ul>
            <hr>
            <p style="font-size:12px; color:#999;">證照銜接：iPAS AI 應用規劃師</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("立即報名此班別", use_container_width=True):
        st.balloons()
