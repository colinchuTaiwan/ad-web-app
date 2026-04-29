import React, { useMemo, useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";

// --- 配置資料保持不變 ---
const palette = {
  rose: {
    dark: "#8c5260", mid: "#e5bcc5", light: "#f8edf0",
    grad: "from-[#e4b6c0] via-[#ecc9d0] to-[#dfc2d6]",
    btn: "from-[#a86878] to-[#b878a0]", icon: "✦",
  },
  sage: {
    dark: "#4e6648", mid: "#bed0b6", light: "#eef5ec",
    grad: "from-[#b4c8ac] via-[#c7d7bf] to-[#b8d0ce]",
    btn: "from-[#5a7855] to-[#4a7070]", icon: "</>",
  },
  slate: {
    dark: "#435d72", mid: "#b7c9d8", light: "#edf4f8",
    grad: "from-[#aac0d4] via-[#c1d1df] to-[#b5c8d8]",
    btn: "from-[#446080] to-[#5a7090]", icon: "✓",
  },
  sand: {
    dark: "#6e5b34", mid: "#dbcfae", light: "#f7f2e7",
    grad: "from-[#d4c0a8] via-[#e2d6b8] to-[#c8d2dc]",
    btn: "from-[#7a6050] via-[#6a5870] to-[#506070]",
    icon: "◇",
  },
};

const tracks = [
  // ... 此處延用您提供的 tracks 資料數組 ...
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
        label: "Day 1",
        name: "AI 基礎素養與 Office 智能協作",
        rows: [
          ["09:00\n10:30", "90 Min", "概念講授", "生成式 AI 基礎素養", "大型語言模型運作原理直覺解說・AI 工具生態全覽・資安規範解析"],
          ["10:45\n12:15", "90 Min", "實作演練", "提示詞工程入門實作", "提示詞四要素設計・技術摘要撰寫・公文草稿生成"],
          ["12:15\n13:30", "", "", "— 午 休 —", ""],
          ["13:30\n15:00", "90 Min", "上機實作", "Word × AI 文件協作", "Copilot for Word 操作實務・技術報告大綱自動生成"],
          ["15:15\n17:00", "105 Min", "上機實作", "PowerPoint × AI 簡報製作", "從文字大綱一鍵生成投影片・視覺配置優化"],
        ],
      },
      {
        label: "Day 2",
        name: "資料分析與 AI 工作流整合",
        rows: [
          ["09:00\n10:30", "90 Min", "上機實作", "Excel × AI 資料分析", "自然語言生成公式與樞紐分析表・資料視覺化"],
          ["10:45\n12:15", "90 Min", "上機實作", "AI 商務溝通與公文撰寫", "商務信函撰寫・多語言翻譯校稿・涉密內容處理"],
          ["12:15\n13:30", "", "", "— 午 休 —", ""],
          ["13:30\n15:00", "90 Min", "概念講授", "AI 辦公室工作流程設計", "多工具協作流程規劃・重複性業務自動化思維導入"],
          ["15:15\n17:00", "105 Min", "分組成果", "綜合實作工作坊暨成果展示", "分組選題・成果發表・Q&A・資源包發放"],
        ],
      },
    ],
    outcomes: ["掌握提示詞工程結構化設計能力", "熟練操作 Microsoft 365 Copilot", "建立 AI 輔助標準作業流程"],
    cert: "iPAS AI 應用規劃師・初級認證",
    note: "全程無需程式設計背景。",
  },
  // 這裡建議補齊 b, c, e 三個 tracks...
];

// --- 組件部分 ---

function Pill({ children, color, filled = false }) {
  return (
    <span
      className={`inline-flex items-center rounded-full px-4 py-1.5 text-xs font-medium transition-all ${filled ? "text-white" : ""}`}
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
    <Card className="overflow-hidden rounded-2xl border-[#ede9f2] bg-white shadow-xl">
      <div className="flex items-center gap-3 bg-gradient-to-r from-white to-[#f7f5f9] px-5 py-4">
        <span 
          className="rounded-full px-4 py-1 text-xs font-bold text-white" 
          style={{ background: `linear-gradient(135deg, ${color.dark}, ${color.mid})` }}
        >
          {day.label}
        </span>
        <span className="text-sm font-bold text-[#2c2830]">{day.name}</span>
      </div>
      <CardContent className="p-0">
        {day.rows.map(([time, dur, tag, title, desc], index) => {
          const isBreak = title.includes("午 休");
          return (
            <div key={index} className={`grid grid-cols-[72px_1fr] gap-3 border-t border-[#ede9f2] px-5 py-4 transition hover:bg-[#f7f5f9] ${isBreak ? "bg-[#f7f5f9]" : ""}`}>
              <div className="whitespace-pre-line pt-0.5 font-mono text-[10px] leading-relaxed text-[#b8aec8]">
                {time}
                {dur && <div className="mt-1 text-[9px] text-[#dcd6e6]">{dur}</div>}
              </div>
              <div>
                {tag && (
                  <span className="mb-2 inline-flex rounded-full px-2.5 py-1 font-mono text-[9px] uppercase tracking-widest" 
                    style={{ background: color.light, color: color.dark, border: `1px solid ${color.mid}` }}>
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
  const active = useMemo(() => tracks.find((t) => t.id === activeId) || tracks[0], [activeId]);
  const color = palette[active.theme];

  return (
    <main className="min-h-screen bg-[#f8f9fa] font-sans text-[#2c2830] pb-20">
      {/* Header */}
      <section className="relative overflow-hidden bg-[#2c2830] px-6 py-16 text-center text-white">
        <div className="relative z-10 mx-auto max-w-4xl">
          <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
            <h1 className="text-4xl font-bold tracking-tight md:text-5xl">AI 跨域人才培訓計畫</h1>
            <p className="mt-4 text-lg text-gray-400">專為院所同仁設計的全方位 AI 賦能課程，從辦公室應用到工程開發。</p>
          </motion.div>
        </div>
      </section>

      {/* Tabs */}
      <div className="sticky top-0 z-50 bg-white/80 backdrop-blur-md shadow-sm">
        <div className="mx-auto max-w-6xl px-4 py-4 overflow-x-auto flex gap-2">
          {tracks.map((track) => (
            <button
              key={track.id}
              onClick={() => setActiveId(track.id)}
              className={`whitespace-nowrap rounded-lg px-4 py-2 text-sm font-medium transition-all ${
                activeId === track.id 
                ? "bg-[#2c2830] text-white shadow-md" 
                : "bg-gray-100 text-gray-600 hover:bg-gray-200"
              }`}
            >
              {track.tabTitle}
            </button>
          ))}
        </div>
      </div>

      {/* Content */}
      <div className="mx-auto max-w-6xl px-4 mt-10">
        <AnimatePresence mode="wait">
          <motion.div
            key={activeId}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            className="grid grid-cols-1 lg:grid-cols-[1fr_350px] gap-8"
          >
            {/* Left: Schedule */}
            <div className="space-y-8">
              <div className="flex flex-wrap gap-3">
                <Pill color={color}>{active.level}</Pill>
                <Pill color={color} filled>{active.cert}</Pill>
              </div>
              <h2 className="text-3xl font-bold">{active.title}</h2>
              <p className="text-gray-600 leading-relaxed">{active.desc}</p>
              
              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {active.days.map((day, i) => (
                  <ScheduleCard key={i} day={day} color={color} />
                ))}
              </div>
            </div>

            {/* Right: Sidebar */}
            <aside className="space-y-6">
              <Card className="p-6 border-none bg-white shadow-lg rounded-2xl">
                <h3 className="font-bold mb-4 flex items-center gap-2">
                  <span style={{ color: color.dark }}>{color.icon}</span> 培訓目標
                </h3>
                <ul className="space-y-3 text-sm text-gray-600">
                  {active.outcomes.map((item, i) => (
                    <li key={i} className="flex gap-2">
                      <span style={{ color: color.dark }}>•</span> {item}
                    </li>
                  ))}
                </ul>
              </Card>

              <Card className="p-6 border-none bg-[#2c2830] text-white shadow-lg rounded-2xl">
                <h3 className="font-bold mb-4 opacity-80 text-sm tracking-widest uppercase">參訓對象</h3>
                <p className="text-sm leading-relaxed mb-4">{active.audience}</p>
                <h3 className="font-bold mb-4 opacity-80 text-sm tracking-widest uppercase">硬體需求</h3>
                <p className="text-sm leading-relaxed">{active.requirement}</p>
              </Card>
              
              <p className="text-[10px] text-gray-400 italic px-2">註：{active.note}</p>
            </aside>
          </motion.div>
        </AnimatePresence>
      </div>
    </main>
  );
}
