import React, { useMemo, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

const palette = {
  rose: {
    dark: "#8c5260",
    mid: "#e5bcc5",
    light: "#f8edf0",
    grad: "from-[#e4b6c0] via-[#ecc9d0] to-[#dfc2d6]",
    btn: "from-[#a86878] to-[#b878a0]",
    icon: "✦",
  },
  sage: {
    dark: "#4e6648",
    mid: "#bed0b6",
    light: "#eef5ec",
    grad: "from-[#b4c8ac] via-[#c7d7bf] to-[#b8d0ce]",
    btn: "from-[#5a7855] to-[#4a7070]",
    icon: "</>",
  },
  slate: {
    dark: "#435d72",
    mid: "#b7c9d8",
    light: "#edf4f8",
    grad: "from-[#aac0d4] via-[#c1d1df] to-[#b5c8d8]",
    btn: "from-[#446080] to-[#5a7090]",
    icon: "✓",
  },
  lavender: {
    dark: "#594a70",
    mid: "#c9c0de",
    light: "#f4f0fb",
    grad: "from-[#bfb6dc] via-[#d2c9e8] to-[#c7bee2]",
    btn: "from-[#604880] to-[#7868a8]",
    icon: "▣",
  },
  sand: {
    dark: "#6e5b34",
    mid: "#dbcfae",
    light: "#f7f2e7",
    grad: "from-[#d4c0a8] via-[#e2d6b8] to-[#c8d2dc]",
    btn: "from-[#7a6050] via-[#6a5870] to-[#506070]",
    icon: "◇",
  },
};

const tracks = [
  {
    id: "a",
    tabCode: "第一班・初階",
    tabTitle: "AI 辦公室應用班",
    title: "AI 辦公室應用班",
    level: "第一班・初階・無需程式背景",
    theme: "rose",
    audience: "行政人員・文書幕僚・非技術背景同仁",
    requirement: "一般電腦・網路環境",
    cta: "核心工具：ChatGPT・Microsoft 365 Copilot・Google Gemini",
    desc: "以生成式 AI 工具為核心，協助行政、文書及幕僚人員建立完整的 AI 輔助辦公室工作流，涵蓋文件撰寫、簡報製作、資料分析及商務溝通等職場核心技能，全程無需程式設計背景。",
    days: [
      {
        label: "第一天",
        name: "AI 基礎素養與 Office 智能協作",
        rows: [
          ["$1\n$2", "90 分", "概念講授", "生成式 AI 基礎素養", "大型語言模型運作原理直覺解說・AI 工具生態全覽・院所資訊安全使用規範・應用倫理與常見迷思破解"],
          ["$1\n$2", "90 分", "實作演練", "提示詞工程入門實作", "提示詞四要素設計（角色／任務／格式／限制）・技術摘要撰寫・公文草稿生成・會議記錄自動化"],
          ["$1\n$2", "", "", "— 午 休 —", ""],
          ["$1\n$2", "90 分", "上機實作", "Word × AI 文件協作", "Copilot for Word 操作實務・技術報告大綱自動生成・段落改寫潤稿・多語言摘要輸出・範本建立"],
          ["$1\n$2", "105 分", "上機實作", "PowerPoint × AI 簡報製作", "從文字大綱一鍵生成投影片・視覺配置優化・完成業務簡報一份"],
        ],
      },
      {
        label: "第二天",
        name: "資料分析與 AI 工作流整合",
        rows: [
          ["$1\n$2", "90 分", "上機實作", "Excel × AI 資料分析", "自然語言生成公式與樞紐分析表・資料視覺化・採購與人力數據分析實作"],
          ["$1\n$2", "90 分", "上機實作", "AI 商務溝通與公文撰寫", "商務信函撰寫・往來信件快速回覆生成・多語言翻譯校稿・涉密內容處理原則"],
          ["$1\n$2", "", "", "— 午 休 —", ""],
          ["$1\n$2", "90 分", "概念講授", "AI 辦公室工作流程設計", "多工具協作流程規劃・重複性業務自動化思維導入・文件管理 AI 化情境設計"],
          ["$1\n$2", "105 分", "分組成果", "綜合實作工作坊暨成果展示", "分組選題・完整產出・成果發表・Q&A・資源包發放"],
        ],
      },
    ],
    outcomes: ["掌握提示詞工程結構化設計能力", "熟練操作 Microsoft 365 Copilot 全套辦公室工具", "建立 AI 輔助文件與簡報產出標準作業流程", "具備日常業務商務溝通 AI 化應用能力"],
    cert: "iPAS AI 應用規劃師・初級認證",
    note: "全程無需程式設計背景，具備電腦基本操作能力即可參訓。",
  },
  {
    id: "b",
    tabCode: "第二班・進階",
    tabTitle: "AI 工程開發實務班",
    title: "AI 工程開發實務班",
    level: "第二班・進階・需具備 Python 程式基礎",
    theme: "sage",
    audience: "系統工程師・軟硬體研發人員・技術骨幹",
    requirement: "Python 開發環境・GPU 選配",
    cta: "核心技術：LLM API・RAG・Llama.cpp・向量資料庫",
    desc: "面向具備 Python 程式基礎之研發工程師，深入大型語言模型 API 串接、地端模型部署、檢索增強生成系統建構與多模態整合技術。",
    days: [
      { label: "第一天", name: "大型語言模型核心技術與 API 整合", rows: [["$1\n$2", "90 分", "概念講授", "大型語言模型原理與雲端模型調用", "Transformer 架構直覺理解・API 串接・環境變數安全管理"], ["$1\n$2", "90 分", "實驗室", "提示詞工程進階技術", "少樣本學習・思維鏈提示・結構化 JSON 輸出・防幻覺策略"], ["$1\n$2", "", "", "— 午 休 —", ""], ["$1\n$2", "90 分", "實驗室", "地端模型量化部署實作", "Hugging Face 模型評選・INT4/INT8/FP16・Llama.cpp 部署"], ["$1\n$2", "105 分", "專案建構", "私有化 AI 問答服務雛形", "API + Streamlit 建立展示介面・本地端完整部署展示"]] },
      { label: "第二天", name: "檢索增強生成架構與多模態整合", rows: [["$1\n$2", "90 分", "實驗室", "向量嵌入與向量資料庫", "文字向量化・ChromaDB / FAISS 比較・語料分塊策略"], ["$1\n$2", "90 分", "實驗室", "RAG 完整流程實作", "查詢→檢索→語言模型→回答完整鏈路・幻覺評估"], ["$1\n$2", "", "", "— 午 休 —", ""], ["$1\n$2", "90 分", "實驗室", "多模態應用整合", "視覺語言模型・OCR 文件理解・技術圖紙自動解讀"], ["$1\n$2", "105 分", "專題成果", "院所技術知識庫問答系統", "分組建立 RAG 問答系統・離線部署環境驗證・成果展示"]] },
    ],
    outcomes: ["具備 LLM API 串接與參數調校能力", "完成地端模型量化部署", "建構 RAG 系統完整架構", "具備多模態文件理解系統開發能力"],
    cert: "生成式 AI 應用工程・進階課程銜接",
    note: "學員需具備 Python 基礎能力；系統可於內部隔離網路環境中執行。",
  },
  {
    id: "e",
    tabCode: "第三班・精英",
    tabTitle: "AI 跨域整合精進班",
    title: "AI 跨域整合精進班",
    level: "第三班・跨域精英・最高強度密集訓練",
    theme: "sand",
    audience: "跨域骨幹（工程師＋資訊人員＋專案管理混合編組）",
    requirement: "Python＋Git 開發環境・GPU 選配",
    cta: "銜接 AIELC・AI 工程師養成認證",
    desc: "為院所跨領域核心骨幹設計之高強度兩日密集課程，以分組專題開發為核心，結業時每組完成可展示之 AI 原型系統。",
    days: [
      { label: "第一天", name: "AI 全技術棧快速建構", rows: [["$1\n$2", "60 分", "快速上手", "LLM 與 API 快速建構", "OpenAI / Gemini / Ollama API・提示詞精要・地端模型部署"], ["$1\n$2", "120 分", "實驗室", "RAG 系統完整流程全實作", "文件載入→向量嵌入→語意檢索→語言模型生成"], ["$1\n$2", "", "", "— 午 休 —", ""], ["$1\n$2", "90 分", "實驗室", "多模態應用整合實作", "VLM・OCR＋LLM 文件理解・語音辨識整合"], ["$1\n$2", "105 分", "原型建構", "Streamlit 快速原型開發", "介面元件・檔案上傳下載・即時 API 串接展示"]] },
      { label: "第二天", name: "分組專題衝刺與成果展示評審", rows: [["$1\n$2", "45 分", "資安專題", "AI 系統資訊安全架構設計", "氣隙隔離部署・涉密文件處理・資料去識別化"], ["$1\n$2", "135 分", "分組衝刺", "專題開發衝刺（上）", "三組選題：知識問答、規格摘要、多模態分析平台"], ["$1\n$2", "", "", "— 午 休 —", ""], ["$1\n$2", "120 分", "分組衝刺", "專題開發衝刺（下）", "功能整合・UI 優化・資安合規自檢・版本控制"], ["$1\n$2", "75 分", "成果展示", "Demo Day 與評審回饋", "系統展示・技術架構說明・後續落地建議"]] },
    ],
    outcomes: ["完成可展示 AI 原型系統", "具備跨域協作與技術整合能力", "熟悉 RAG、多模態與資安部署核心流程", "形成可複製的院所 AI 專案衝刺模式"],
    cert: "AIELC・AI 工程師養成認證銜接",
    note: "建議採混合編組，讓工程、資訊治理與專案管理角色共同完成原型。",
  },
  {
    id: "c",
    tabCode: "第四班・中階",
    tabTitle: "AI 資訊治理整合班",
    title: "AI 資訊治理整合班",
    level: "第四班・中階・建議具備基礎資訊背景",
    theme: "slate",
    audience: "資訊維運人員・資安管理人員・數位轉型推動者",
    requirement: "Python 基礎佳・雲端服務帳號",
    cta: "核心主題：資安治理・導入評估・架構規劃・系統整合",
    desc: "面向資訊維運、資安管理及數位轉型推動人員，建立 AI 技術導入評估能力、資訊安全治理框架及系統整合規劃能力。",
    days: [
      { label: "第一天", name: "AI 技術評估與資訊安全治理框架", rows: [["$1\n$2", "90 分", "概念講授", "AI 技術全景與部署模式選型", "雲端 vs 地端 vs 氣隙隔離部署比較・模型成本效益評估"], ["$1\n$2", "90 分", "資安專題", "AI 資訊安全風險分析", "提示詞注入・資料外洩・模型竄改・敏感資料保護策略"], ["$1\n$2", "", "", "— 午 休 —", ""], ["$1\n$2", "90 分", "實驗室", "API 安全管理與部署環境工程", "API 金鑰管理・網路隔離架構・模型離線下載與驗證"], ["$1\n$2", "105 分", "實驗室", "AI 服務監控與維運管理", "穩定性監控・Token 成本控管・模型版本管理・故障排除 SOP"]] },
      { label: "第二天", name: "自動化整合與 AI 導入規劃實作", rows: [["$1\n$2", "90 分", "實驗室", "Python 自動化與 AI 系統整合", "腳本串接 LLM API・定時自動化・文件管理整合"], ["$1\n$2", "90 分", "概念講授", "企業私有知識庫架構設計", "RAG 系統架構・向量資料庫選型・權限設計・資料治理"], ["$1\n$2", "", "", "— 午 休 —", ""], ["$1\n$2", "90 分", "實驗室", "快速部署與內部 Web 應用", "Streamlit 部署・GitHub 版控・內部 UI 設計"], ["$1\n$2", "105 分", "規劃書產出", "AI 導入規劃工作坊", "技術選型・資安評估・效益預估・時程規劃"]] },
    ],
    outcomes: ["具備 AI 部署模式選型與資安評估能力", "建立符合保密需求之 AI 治理框架", "完成 Python 自動化系統整合實作", "產出 AI 導入規劃書"],
    cert: "iPAS AI 應用規劃師・中級認證",
    note: "建議與工程開發實務班同期辦理，形成架構規劃與系統實作分工。",
  },
];

function Pill({ children, color, filled = false }) {
  return (
    <span
      className={`inline-flex items-center rounded-full px-4 py-1.5 text-xs font-medium ${filled ? "text-white" : ""}`}
      style={
        filled
          ? { background: `linear-gradient(135deg, ${color.dark}, ${color.mid})` }
          : { background: color.light, border: `1.5px solid ${color.mid}`, color: color.dark }
      }
    >
      {children}
    </span>
  );
}

function ScheduleCard({ day, color }) {
  return (
    <Card className="overflow-hidden rounded-2xl border-[#ede9f2] bg-white shadow-[0_2px_16px_rgba(60,40,80,.07),0_8px_40px_rgba(60,40,80,.05)]">
      <div className="flex items-center gap-3 bg-gradient-to-r from-white to-[#f7f5f9] px-5 py-4">
        <span className="rounded-full px-4 py-1 text-xs font-bold text-white" style={{ background: `linear-gradient(135deg, ${color.dark}, ${color.mid})` }}>
          {day.label}
        </span>
        <span className="text-sm font-bold text-[#2c2830]">{day.name}</span>
      </div>
      <CardContent className="p-0">
        {day.rows.map(([time, dur, tag, title, desc], index) => {
          const isBreak = title.includes("午 休");
          return (
            <div key={`${time}-${title}`} className={`grid grid-cols-[72px_1fr] gap-3 border-t border-[#ede9f2] px-5 py-4 transition hover:bg-[#f7f5f9] ${isBreak ? "bg-[#f7f5f9]" : ""}`}>
              <div className="whitespace-pre-line pt-0.5 font-mono text-[10px] leading-relaxed text-[#b8aec8]">
                {time}
                {dur && <div className="mt-1 text-[9px] text-[#dcd6e6]">{dur}</div>}
              </div>
              <div>
                {tag && (
                  <span className="mb-2 inline-flex rounded-full px-2.5 py-1 font-mono text-[9px] uppercase tracking-widest" style={{ background: color.light, color: color.dark, border: `1px solid ${color.mid}` }}>
                    {tag}
                  </span>
                )}
                <div className={`text-sm font-bold leading-snug ${isBreak ? "text-[#b8aec8]" : "text-[#2c2830]"}`}>{title}</div>
                {desc && <p className="mt-1 text-xs leading-6 text-[#7a6e84]">{desc}</p>}
              </div>
            </div>
          );
        })}
      </CardContent>
    </Card>
  );
}

export default function CSISTAITrainingReact() {
  const [activeId, setActiveId] = useState("a");
  const active = useMemo(() => tracks.find((track) => track.id === activeId) ?? tracks[0], [activeId]);
  const color = palette[active.theme];
  const Icon = color.icon;

  return (
    <main className="min-h-screen bg-[linear-gradient(150deg,#f5f2f8_0%,#f0f4f0_50%,#f2f0f5_100%)] font-sans text-[#2c2830]">
      <section className="relative overflow-hidden bg-[linear-gradient(150deg,#4a344f_0%,#594466_45%,#42546a_100%)] px-5 pt-10 md:px-10 md:pt-12">
        <div className="absolute -right-16 -top-28 h-80 w-80 rounded-full bg-[#d4a8b0]/30 blur-3xl" />
        <div className="absolute bottom-0 left-[8%] h-56 w-56 rounded-full bg-[#a8b8a0]/20 blur-3xl" />
        <div className="absolute left-[38%] top-4 h-52 w-52 rounded-full bg-[#9eb0c0]/20 blur-3xl" />

        <div className="relative z-10 mx-auto max-w-7xl">
          <div className="mb-6 inline-flex items-center gap-2 rounded-full border border-[#d4a8b0]/30 bg-[#d4a8b0]/10 px-4 py-1.5 font-mono text-[10px] uppercase tracking-[.18em] text-[#d4a8b0]">
            <span className="text-xs">✦</span> 國家中山科學研究院・AI 應用訓練課程
          </div>
          <h1 className="max-w-4xl font-serif text-3xl font-bold leading-tight tracking-wide text-[#f5f0f8] md:text-5xl">
            人工智慧應用能力培訓計畫
            <span className="mt-2 block bg-gradient-to-r from-[#d4a8b0] via-[#b0a8c8] to-[#a8b8a0] bg-clip-text text-2xl text-transparent md:text-4xl">
              兩天密集課程・五大專業班別
            </span>
          </h1>
          <p className="mt-5 max-w-3xl text-sm font-light leading-8 text-white/70">
            本計畫以三階段學習框架設計，涵蓋辦公室 AI 應用、系統整合開發、資訊安全治理、策略決策與跨域精英培訓，全面強化院所各層級人員之人工智慧應用能力。
          </p>
          <div className="mt-6 flex flex-wrap gap-2 pb-8">
            {["五 大班別", "每天 六 小時", "理論與實作並重", "銜接 iPAS 認證", "銜接 AIELC 認證"].map((tag) => (
              <span key={tag} className="rounded-full border border-white/10 bg-white/10 px-4 py-1.5 text-xs text-white/60">
                {tag}
              </span>
            ))}
          </div>

          <div className="flex overflow-x-auto scrollbar-hide">
            {tracks.map((track) => (
              <button
                key={track.id}
                onClick={() => setActiveId(track.id)}
                className={`shrink-0 rounded-t-2xl px-5 py-4 text-left text-sm font-medium transition ${activeId === track.id ? "bg-white text-[#2c2830]" : "text-white/60 hover:text-white/90"}`}
              >
                <span className="mb-1 block font-mono text-[9px] uppercase tracking-[.16em] opacity-60">{track.tabCode}</span>
                {track.tabTitle}
              </button>
            ))}
          </div>
        </div>
      </section>

      <section className="mx-auto max-w-7xl bg-white px-5 py-7 md:px-10 md:py-9">
        <AnimatePresence mode="wait">
          <motion.div
            key={active.id}
            initial={{ opacity: 0, y: 16 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -10 }}
            transition={{ duration: 0.22 }}
          >
            <div className={`relative overflow-hidden rounded-[28px] bg-gradient-to-br ${color.grad} p-7 md:p-9`}>
              <div className="absolute -right-16 -top-24 h-72 w-72 rounded-full bg-white/30 blur-3xl" />
              <div className="absolute bottom-0 left-1/4 h-44 w-44 rounded-full bg-white/20 blur-3xl" />
              <div className="relative z-10">
                <div className="mb-5 flex gap-1.5">
                  {[color.dark, color.mid, "#f0ece2", "#e2ebf0"].map((dot) => (
                    <span key={dot} className="h-2.5 w-2.5 rounded-full" style={{ background: dot }} />
                  ))}
                </div>
                <div className="mb-4 inline-flex items-center gap-2 rounded-full border border-white/40 bg-white/20 px-4 py-1.5 font-mono text-[10px] uppercase tracking-[.18em] text-white">
                  <span className="text-sm leading-none">{Icon}</span> {active.level}
                </div>
                <h2 className="font-serif text-3xl font-bold tracking-wide text-[#181018] md:text-4xl">{active.title}</h2>
                <p className="mt-4 max-w-3xl text-sm leading-8 text-[#181018]/75">{active.desc}</p>
              </div>
            </div>

            <div className="mt-6 flex flex-wrap gap-2">
              <Pill color={color}>適訓對象：{active.audience}</Pill>
              <Pill color={color}>設備需求：{active.requirement}</Pill>
              <Pill color={color} filled>{active.cta}</Pill>
            </div>

            <div className="mt-7 grid gap-5 lg:grid-cols-2">
              {active.days.map((day) => (
                <ScheduleCard key={day.label} day={day} color={color} />
              ))}
            </div>

            <div className="mt-7 grid gap-5 lg:grid-cols-2">
              <Card className="rounded-2xl border-[#ede9f2] shadow-[0_2px_16px_rgba(60,40,80,.07),0_8px_40px_rgba(60,40,80,.05)]">
                <CardContent className="p-6">
                  <div className="mb-4 flex items-center gap-3 font-mono text-[10px] uppercase tracking-[.16em] text-[#7a6e84]">
                    <span className="h-1 w-7 rounded-full" style={{ background: `linear-gradient(90deg, ${color.dark}, ${color.mid})` }} />
                    訓練目標與能力產出
                  </div>
                  <div className="space-y-3">
                    {active.outcomes.map((item) => (
                      <div key={item} className="flex gap-3 text-sm leading-7 text-[#3d3545]">
                        <span style={{ color: color.dark }}>◆</span>
                        <span>{item}</span>
                      </div>
                    ))}
                  </div>
                </CardContent>
              </Card>

              <Card className="rounded-2xl border-[#ede9f2] shadow-[0_2px_16px_rgba(60,40,80,.07),0_8px_40px_rgba(60,40,80,.05)]" style={{ background: `linear-gradient(150deg, ${color.light}, #ffffff)` }}>
                <CardContent className="p-6">
                  <div className="mb-4 flex items-center gap-3 font-mono text-[10px] uppercase tracking-[.16em] text-[#7a6e84]">
                    <span className="h-1 w-7 rounded-full" style={{ background: `linear-gradient(90deg, ${color.dark}, ${color.mid})` }} />
                    銜接認證與後續學習
                  </div>
                  <div className="inline-flex items-center gap-2 rounded-full border bg-white px-4 py-2 text-sm font-medium" style={{ borderColor: color.mid, color: color.dark }}>
                    <span className="text-base leading-none">🏅</span> {active.cert}
                  </div>
                  <p className="mt-4 text-sm leading-7 text-[#7a6e84]">{active.note}</p>
                </CardContent>
              </Card>
            </div>

            <div className="mt-7 flex flex-col gap-3 border-t border-dashed border-[#ede9f2] pt-5 font-mono text-[10px] leading-6 tracking-wide text-[#b8aec8] md:flex-row md:items-center md:justify-between">
              <span>TRAINING NOTE · 兩天密集課程・理論與實作並重・可依院所資安規範調整部署情境</span>
              <Button className={`rounded-full bg-gradient-to-r ${color.btn} px-5 text-white hover:opacity-90`}>查看課程細節</Button>
            </div>
          </motion.div>
        </AnimatePresence>
      </section>
    </main>
  );
}
