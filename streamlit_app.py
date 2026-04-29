import streamlit as st

# 1. 網頁設定與樣式
st.set_page_config(page_title="中科院 AI 培訓計畫", layout="wide")

# 2. 定義顏色與資料 (翻譯自 React Palette)
palette = {
    "rose": {"dark": "#8c5260", "mid": "#e5bcc5", "light": "#f8edf0", "grad": "linear-gradient(135deg, #e4b6c0, #ecc9d0, #dfc2d6)", "btn": "linear-gradient(135deg, #a86878, #b878a0)", "icon": "✦"},
    "sage": {"dark": "#4e6648", "mid": "#bed0b6", "light": "#eef5ec", "grad": "linear-gradient(135deg, #b4c8ac, #c7d7bf, #b8d0ce)", "btn": "linear-gradient(135deg, #5a7855, #4a7070)", "icon": "</>"},
    "slate": {"dark": "#435d72", "mid": "#b7c9d8", "light": "#edf4f8", "grad": "linear-gradient(135deg, #aac0d4, #c1d1df, #b5c8d8)", "btn": "linear-gradient(135deg, #446080, #5a7090)", "icon": "✓"},
    "sand": {"dark": "#6e5b34", "mid": "#dbcfae", "light": "#f7f2e7", "grad": "linear-gradient(135deg, #d4c0a8, #e2d6b8, #c8d2dc)", "btn": "linear-gradient(135deg, #7a6050, #6a5870, #506070)", "icon": "◇"},
}

# 3. 課程資料 (完整翻譯)
tracks = [
    {
        "id": "a",
        "tabTitle": "第一班・AI 辦公室應用班",
        "title": "AI 辦公室應用班",
        "level": "第一班・初階・無需程式背景",
        "theme": "rose",
        "audience": "行政人員・文書幕僚・非技術背景同仁",
        "requirement": "一般電腦・網路環境",
        "cta": "核心工具：ChatGPT・Microsoft 365 Copilot",
        "desc": "以生成式 AI 工具為核心，協助行政人員建立完整的 AI 輔助工作流，全程無需程式設計背景。",
        "days": [
            {"label": "第一天", "name": "AI 基礎素養與 Office 智能協作", "rows": [["09:00", "90分", "概念", "生成式 AI 基礎素養", "LLM 原理、資安規範、應用倫理"], ["10:45", "90分", "實作", "提示詞工程入門", "提示詞四要素設計、公文自動化"]]},
            {"label": "第二天", "name": "資料分析與 AI 工作流整合", "rows": [["09:00", "90分", "實作", "Excel x AI 分析", "自然語言生成公式與樞紐分析"], ["10:45", "90分", "實作", "成果展示工作坊", "分組選題、完整產出發表"]]}
        ],
        "outcomes": ["掌握結構化提示詞設計", "熟練操作 Copilot 工具", "建立 AI 辦公標準流程"],
        "cert": "iPAS AI 應用規劃師・初級認證"
    },
    {
        "id": "b",
        "tabTitle": "第二班・AI 工程開發實務班",
        "title": "AI 工程開發實務班",
        "level": "第二班・進階・需 Python 基礎",
        "theme": "sage",
        "audience": "系統工程師・研發人員",
        "requirement": "Python 開發環境・GPU 選配",
        "cta": "核心技術：LLM API・RAG・Llama.cpp",
        "desc": "深入大型語言模型 API 串接、地端模型部署與 RAG 檢索增強生成系統建構。",
        "days": [
            {"label": "第一天", "name": "LLM 核心技術與 API 整合", "rows": [["09:00", "90分", "講授", "API 串接與參數調優", "環境變數管理、防幻覺策略"], ["13:30", "105分", "專案", "地端模型量化部署", "Llama.cpp 部署實務"]]}
        ],
        "outcomes": ["具備 LLM API 調校能力", "完成地端模型部署", "建構 RAG 系統架構"],
        "cert": "生成式 AI 應用工程・進階認證銜接"
    }
    # ... 其餘班別依此類推
]

# 4. 注入 CSS (模擬 React 樣式)
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@400;700&display=swap');
    body, html {{ font-family: 'Noto Sans TC', sans-serif; }}
    .main-header {{
        background: linear-gradient(150deg, #4a344f 0%, #594466 45%, #42546a 100%);
        padding: 50px 30px;
        border-radius: 0 0 30px 30px;
        color: white;
        margin-bottom: 30px;
    }}
    .course-card {{
        background: white;
        border-radius: 20px;
        border: 1px solid #ede9f2;
        padding: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }}
    .pill {{
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        margin-right: 8px;
        margin-bottom: 8px;
    }}
    .day-header {{
        padding: 10px 15px;
        border-radius: 12px 12px 0 0;
        color: white;
        font-weight: bold;
        font-size: 14px;
    }}
    .schedule-row {{
        border-bottom: 1px solid #eee;
        padding: 12px 15px;
        display: flex;
        gap: 15px;
    }}
    </style>
""", unsafe_allow_html=True)

# 5. 頂部 Banner
st.markdown("""
    <div class="main-header">
        <p style="letter-spacing: 0.2em; font-size: 12px; opacity: 0.8;">✦ 國家中山科學研究院・AI 應用訓練課程</p>
        <h1 style="font-size: 42px; margin: 10px 0;">人工智慧應用能力培訓計畫</h1>
        <h2 style="font-size: 24px; opacity: 0.9; font-weight: 400;">兩天密集課程・專業班別切換</h2>
    </div>
""", unsafe_allow_html=True)

# 6. 側邊欄切換 (模擬 React Tabs)
selected_tab = st.sidebar.radio(
    "🎯 選擇培訓路徑",
    [t["tabTitle"] for t in tracks]
)

# 獲取當前選中資料
active = next(t for t in tracks if t["tabTitle"] == selected_tab)
p = palette[active["theme"]]

# 7. 渲染主內容
# 標題與簡介卡
st.markdown(f"""
    <div style="background: {p['grad']}; padding: 40px; border-radius: 30px; position: relative; overflow: hidden; margin-bottom: 30px;">
        <div style="position: relative; z-index: 10;">
            <div class="pill" style="background: rgba(255,255,255,0.2); border: 1px solid white; color: white;">
                {p['icon']} {active['level']}
            </div>
            <h2 style="color: #181018; font-size: 32px; margin: 15px 0;">{active['title']}</h2>
            <p style="color: rgba(24,16,24,0.8); line-height: 1.8;">{active['desc']}</p>
        </div>
    </div>
""", unsafe_allow_html=True)

# 標籤列
col_info1, col_info2 = st.columns(2)
with col_info1:
    st.markdown(f'<div class="pill" style="background:{p["light"]}; color:{p["dark"]}; border:1px solid {p["mid"]}">適訓對象：{active["audience"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="pill" style="background:{p["light"]}; color:{p["dark"]}; border:1px solid {p["mid"]}">設備需求：{active["requirement"]}</div>', unsafe_allow_html=True)
with col_info2:
    st.markdown(f'<div class="pill" style="background:{p["btn"]}; color:white;">{active["cta"]}</div>', unsafe_allow_html=True)

# 課表呈現 (使用兩欄佈局)
st.write("### 📅 課程大綱")
col1, col2 = st.columns(2)
cols = [col1, col2]

for i, day in enumerate(active["days"]):
    with cols[i % 2]:
        st.markdown(f'<div class="day-header" style="background:{p["btn"]}">{day["label"]}：{day["name"]}</div>', unsafe_allow_html=True)
        for row in day["rows"]:
            st.markdown(f"""
                <div class="schedule-row" style="background: white;">
                    <div style="min-width: 60px; font-family: monospace; color: #888;">{row[0]}<br><small>{row[1]}</small></div>
                    <div>
                        <div style="font-size: 14px; font-weight: bold; color: #333;">{row[3]}</div>
                        <div style="font-size: 12px; color: #666;">{row[4]}</div>
                    </div>
                </div>
            """, unsafe_allow_html=True)

# 底部目標與認證
st.markdown("---")
c1, c2 = st.columns(2)
with c1:
    st.write("#### 🎯 訓練目標")
    for outcome in active["outcomes"]:
        st.write(f"◆ {outcome}")
with c2:
    st.write("#### 🏅 銜接認證")
    st.info(active["cert"])

# 立即報名按鈕
if st.button(f"🚀 查看 {active['title']} 詳細簡章", use_container_width=True):
    st.balloons()
