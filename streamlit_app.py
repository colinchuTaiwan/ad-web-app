import streamlit as st
import base64
import os

# =========================
# 1. 基本設定
# =========================
st.set_page_config(
    page_title="AI 跨域人才培訓計畫",
    layout="wide"
)

# =========================
# 2. 顏色系統
# =========================
palette = {
    "rose": {"dark": "#8c5260", "mid": "#e5bcc5", "light": "#f8edf0"},
    "sage": {"dark": "#4e6648", "mid": "#bed0b6", "light": "#eef5ec"},
    "slate": {"dark": "#435d72", "mid": "#b7c9d8", "light": "#edf4f8"},
    "sand": {"dark": "#6e5b34", "mid": "#dbcfae", "light": "#f7f2e7"},
}

# =========================
# 3. CSS（穩定版）
# =========================
st.markdown("""
<style>
html, body {
    font-family: 'Arial', sans-serif;
}

#MainMenu, footer {visibility: hidden;}

.course-card {
    background: white;
    border-radius: 20px;
    padding: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05);
    border: 1px solid #eee;
}

.day-header {
    padding: 8px 16px;
    border-radius: 10px;
    color: white;
    font-weight: bold;
    margin-top: 15px;
    margin-bottom: 10px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

# =========================
# 4. Banner（安全版）
# =========================
def set_banner(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            data = f.read()
        bin_str = base64.b64encode(data).decode()

        st.markdown(f"""
        <div style="border-radius:20px; overflow:hidden; margin-bottom:20px;">
            <img src="data:image/jpg;base64,{bin_str}" style="width:100%;">
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("⚠️ Banner 圖片未找到，請確認已上傳至 repo")

set_banner("messageImage_1777436648216.jpg")

# =========================
# 5. 課程資料（完整四班）
# =========================
courses = {
    "第一班・AI 辦公室應用班": {
        "color": "rose",
        "desc": "以生成式 AI 工具為核心，協助行政與文書人員建立 AI 工作流。",
        "outcomes": [
            "掌握提示詞工程",
            "熟練 Copilot / ChatGPT",
            "建立 AI SOP 流程"
        ],
        "days": [
            ("第一天：AI 基礎", [
                "09:00 - 10:30 | 生成式 AI 基礎素養",
                "10:45 - 12:15 | 提示詞工程入門"
            ]),
            ("第二天：辦公應用", [
                "09:00 - 10:30 | Excel × AI 自動化",
                "10:45 - 12:15 | AI 公文與報告生成"
            ])
        ]
    },

    "第二班・AI 工程開發實務班": {
        "color": "sage",
        "desc": "深入 LLM API、RAG 系統與地端模型部署。",
        "outcomes": [
            "LLM API 串接",
            "地端模型部署",
            "RAG 系統建構"
        ],
        "days": [
            ("第一天：模型基礎", [
                "09:00 - 10:30 | LLM 架構解析",
                "10:45 - 12:15 | API 串接實作"
            ]),
            ("第二天：RAG 系統", [
                "09:00 - 10:30 | 向量資料庫",
                "10:45 - 12:15 | RAG 應用實作"
            ])
        ]
    },

    "第三班・AI 跨域整合精進班": {
        "color": "slate",
        "desc": "AI + 業務 + 資料整合跨域應用。",
        "outcomes": [
            "跨系統整合能力",
            "AI 流程自動化",
            "企業應用設計"
        ],
        "days": [
            ("第一天：整合架構", [
                "09:00 - 10:30 | API 整合設計",
                "10:45 - 12:15 | AI 工作流設計"
            ]),
            ("第二天：應用實作", [
                "09:00 - 10:30 | 系統整合案例",
                "10:45 - 12:15 | 實戰專案"
            ])
        ]
    },

    "第四班・AI 資訊治理整合班": {
        "color": "sand",
        "desc": "AI + 資安 + 政府資訊治理應用。",
        "outcomes": [
            "AI 資安治理",
            "合規與法規理解",
            "企業級 AI 管理"
        ],
        "days": [
            ("第一天：治理基礎", [
                "09:00 - 10:30 | AI 法規與合規",
                "10:45 - 12:15 | 資安風險分析"
            ]),
            ("第二天：治理實務", [
                "09:00 - 10:30 | 資料治理架構",
                "10:45 - 12:15 | 政府案例分析"
            ])
        ]
    }
}

# =========================
# 6. Sidebar
# =========================
st.sidebar.title("🎯 AI 跨域培訓")
course_choice = st.sidebar.radio(
    "選擇班別",
    list(courses.keys())
)

course = courses[course_choice]
p = palette[course["color"]]

# =========================
# 7. 主標題
# =========================
st.markdown(f"""
<div style="
    padding:20px;
    border-radius:20px;
    background:linear-gradient(135deg, {p['light']}, white);
    margin-bottom:20px;
">
    <h1 style="color:{p['dark']}">{course_choice}</h1>
    <p>{course['desc']}</p>
</div>
""", unsafe_allow_html=True)

# =========================
# 8. Layout
# =========================
col1, col2 = st.columns([2, 1])

# =========================
# 左側：課程內容
# =========================
with col1:
    for day_title, items in course["days"]:
        st.markdown(f"""
        <div class="day-header"
             style="background:linear-gradient(135deg,{p['dark']},{p['mid']})">
            {day_title}
        </div>
        """, unsafe_allow_html=True)

        for item in items:
            st.info(item)

# =========================
# 右側：培訓目標卡片
# =========================
with col2:
    st.markdown(f"""
    <div class="course-card">
        <h4>✦ 培訓目標</h4>
        <ul>
            {"".join([f"<li>{o}</li>" for o in course["outcomes"]])}
        </ul>

        <hr>
        <small>證照銜接：iPAS AI 應用規劃師</small>
    </div>
    """, unsafe_allow_html=True)

    # 按鈕
    if st.button("立即報名", use_container_width=True):
        st.success("報名成功（示範功能）")
        st.balloons()
