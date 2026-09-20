/// <reference path="./declarations.d.ts" />
import React, { useState, type FC, type MouseEvent } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowUpRight,
  Bot,
  GitBranch,
  Sparkles,
  Copy,
  Check,
  Database,
  Cpu,
  CheckCircle2,
  Clock,
  Layers,
} from "lucide-react";
import { ShaderBackground } from "./components/ui/dotted-veil";

// 21st.dev / Lucide Animated Icons (Micro-Interactions powered by Framer Motion)
const AnimatedChatIcon: FC<{ className?: string }> = ({ className = "w-3 h-3" }) => (
  <motion.svg
    fill="none"
    height={14}
    width={14}
    stroke="currentColor"
    strokeLinecap="round"
    strokeLinejoin="round"
    strokeWidth="2"
    viewBox="0 0 24 24"
    className={className}
    variants={{
      normal: { scale: 1, rotate: 0 },
      hover: {
        scale: [1, 1.2, 1.05],
        rotate: [0, -9, 9, -4, 0],
        transition: { duration: 0.5, ease: "easeInOut" },
      },
    }}
  >
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
    <motion.circle
      cx="9"
      cy="10"
      r="1"
      fill="currentColor"
      variants={{
        normal: { opacity: 0.7, scale: 1 },
        hover: { opacity: [0.3, 1, 0.7], scale: [0.8, 1.3, 1], transition: { duration: 0.4, repeat: 1 } },
      }}
    />
    <motion.circle
      cx="12"
      cy="10"
      r="1"
      fill="currentColor"
      variants={{
        normal: { opacity: 0.7, scale: 1 },
        hover: { opacity: [0.3, 1, 0.7], scale: [0.8, 1.3, 1], transition: { duration: 0.4, delay: 0.1, repeat: 1 } },
      }}
    />
    <motion.circle
      cx="15"
      cy="10"
      r="1"
      fill="currentColor"
      variants={{
        normal: { opacity: 0.7, scale: 1 },
        hover: { opacity: [0.3, 1, 0.7], scale: [0.8, 1.3, 1], transition: { duration: 0.4, delay: 0.2, repeat: 1 } },
      }}
    />
  </motion.svg>
);

const AnimatedVocabIcon: FC<{ className?: string }> = ({ className = "w-3 h-3" }) => (
  <motion.svg
    fill="none"
    height={14}
    width={14}
    stroke="currentColor"
    strokeLinecap="round"
    strokeLinejoin="round"
    strokeWidth="2"
    viewBox="0 0 24 24"
    className={className}
    variants={{
      normal: { scale: 1, rotate: 0, y: 0 },
      hover: {
        scale: [1, 1.15, 1],
        rotate: [0, -8, 8, -5, 0],
        y: [0, -2, 0],
        transition: { duration: 0.55, ease: "easeInOut" },
      },
    }}
  >
    <path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1-2.5-2.5Z" />
    <motion.path
      d="m8 13 4-7 4 7"
      variants={{
        normal: { pathLength: 1 },
        hover: { pathLength: [0, 1], transition: { duration: 0.45, ease: "easeOut" } },
      }}
    />
    <motion.path
      d="M9.1 11h5.7"
      variants={{
        normal: { opacity: 1 },
        hover: { opacity: [0, 1], transition: { duration: 0.3, delay: 0.2 } },
      }}
    />
  </motion.svg>
);

const AnimatedGrammarIcon: FC<{ className?: string }> = ({ className = "w-3 h-3" }) => (
  <motion.svg
    fill="none"
    height={14}
    width={14}
    stroke="currentColor"
    strokeLinecap="round"
    strokeLinejoin="round"
    strokeWidth="2"
    viewBox="0 0 24 24"
    className={className}
    variants={{
      normal: { rotate: 0, x: 0, y: 0 },
      hover: {
        rotate: [0, -16, 6, -10, 0],
        x: [0, -1, 1, 0],
        y: [0, -2, 0, 0],
        transition: { duration: 0.6, ease: "easeInOut" },
      },
    }}
  >
    <path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z" />
    <path d="m15 5 3 3" />
    <motion.path
      d="M12 20h9"
      variants={{
        normal: { pathLength: 1, opacity: 1 },
        hover: { pathLength: [0, 1], opacity: [0, 1], transition: { duration: 0.5, ease: "easeOut" } },
      }}
    />
  </motion.svg>
);

const AnimatedReadingIcon: FC<{ className?: string }> = ({ className = "w-3 h-3" }) => (
  <motion.svg
    fill="none"
    height={14}
    width={14}
    stroke="currentColor"
    strokeLinecap="round"
    strokeLinejoin="round"
    strokeWidth="2"
    viewBox="0 0 24 24"
    className={className}
    variants={{
      normal: { scale: 1 },
      hover: {
        scale: [1, 1.2, 1],
        transition: { duration: 0.5, ease: "easeInOut" },
      },
    }}
  >
    <motion.path
      d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"
      variants={{
        normal: { x: 0 },
        hover: { x: [0, -1.5, 0], transition: { duration: 0.5 } },
      }}
    />
    <motion.path
      d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"
      variants={{
        normal: { x: 0 },
        hover: { x: [0, 1.5, 0], transition: { duration: 0.5 } },
      }}
    />
  </motion.svg>
);

const AnimatedZapIcon: FC<{ className?: string }> = ({ className = "w-3 h-3" }) => (
  <motion.svg
    fill="none"
    height={14}
    width={14}
    stroke="currentColor"
    strokeLinecap="round"
    strokeLinejoin="round"
    strokeWidth="2"
    viewBox="0 0 24 24"
    className={className}
    variants={{
      normal: { scale: 1, rotate: 0 },
      hover: {
        scale: [1, 1.25, 1],
        rotate: [0, -12, 10, 0],
        transition: { duration: 0.55, ease: "easeInOut" },
      },
    }}
  >
    <motion.path
      d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"
      variants={{
        normal: { pathLength: 1, opacity: 1 },
        hover: {
          pathLength: [0, 1],
          opacity: [0.3, 1],
          transition: { duration: 0.5, ease: "easeOut" },
        },
      }}
    />
  </motion.svg>
);

export interface BotStatusCardProps {
  botName?: string;
  subtitle?: string;
  description?: string;
  telegramHandle?: string;
  telegramUrl?: string;
  uptime?: string;
  status?: "operational" | "degraded" | "maintenance";
  statusText?: string;
  systemSpecs?: string[];
  className?: string;
  contentBankActive?: boolean;
  geminiActive?: boolean;
}

export const BotStatusCard: FC<BotStatusCardProps> = ({
  botName = "Mebby",
  subtitle = "My English Buddy • AI & Offline English Tutor Bot",
  description = "Interactive English learning bot powered by a 1,000-exercise offline content bank & Gemini Flash AI.",
  telegramHandle = "EnglishBuddy_Practice_Bot",
  telegramUrl = "https://t.me/EnglishBuddy_Practice_Bot",
  uptime = "99.9%",
  status = "operational",
  statusText = "Online",
  systemSpecs = ["FastAPI Webhook", "< 1ms Offline Fallback", "1,000 Exercises • Free"],
  className = "",
  contentBankActive = true,
  geminiActive = false,
}) => {
  const [copied, setCopied] = useState(false);

  const handleCopyHandle = (e: MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    navigator.clipboard.writeText(`@${telegramHandle.replace(/^@/, "")}`);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  const containerVariants = {
    hidden: { opacity: 0, y: 16, scale: 0.98 },
    visible: {
      opacity: 1,
      y: 0,
      scale: 1,
      transition: {
        duration: 0.45,
        ease: [0.16, 1, 0.3, 1],
        staggerChildren: 0.06,
        delayChildren: 0.08,
      },
    },
  };

  const itemVariants = {
    hidden: { opacity: 0, y: 12 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.35, ease: [0.16, 1, 0.3, 1] },
    },
  };

  return (
    <div className={`relative w-full max-w-2xl mx-auto ${className}`}>
      {/* Subtle Ambient Sunset Radial Glow */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -top-24 left-1/2 -translate-x-1/2 w-96 h-96 bg-amber-500/[0.08] rounded-full blur-3xl"
      />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -bottom-16 right-10 w-72 h-72 bg-rose-500/[0.06] rounded-full blur-3xl"
      />

      {/* Main Solid Dark Obsidian Bento Card */}
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        className="relative overflow-hidden rounded-2xl sm:rounded-3xl border border-[#231e2b] bg-[#0d0a13] p-5 sm:p-8 shadow-[inset_0_1px_0_0_rgba(255,255,255,0.06),0_25px_50px_-12px_rgba(0,0,0,0.95)]"
      >
        {/* WebGL Shader Background embedded */}
        <div className="absolute inset-0 pointer-events-none opacity-30 -z-10 overflow-hidden rounded-2xl sm:rounded-3xl">
          <ShaderBackground className="w-full h-full" />
        </div>

        {/* Top Precision Edge Highlight in Rose Gold */}
        <div
          aria-hidden="true"
          className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-rose-400/50 to-transparent"
        />

        {/* 1. HEADER SECTION */}
        <header className="flex flex-col gap-5 sm:gap-6 relative z-10">
          <div className="flex flex-wrap items-center justify-between gap-2.5 sm:gap-3">
            {/* Live Status Indicator (Borderless, Emerald Pulse, Monospace) */}
            <motion.div
              variants={itemVariants}
              role="status"
              aria-label={`System status: ${statusText} with ${uptime} uptime`}
              className="inline-flex shrink-0 items-center gap-2 text-xs font-mono text-zinc-400 select-none"
            >
              <span className="relative flex h-2 w-2 shrink-0" aria-hidden="true">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-500 opacity-75" />
                <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-500" />
              </span>
              <span className="whitespace-nowrap">
                {statusText}
              </span>
            </motion.div>

            {/* Micro Quick-Action: Copy Handle */}
            <motion.button
              variants={itemVariants}
              onClick={handleCopyHandle}
              type="button"
              aria-label={`Copy Telegram bot handle @${telegramHandle}`}
              className="inline-flex shrink-0 max-w-full items-center gap-1.5 rounded-full border border-[#262031] bg-[#14101c] px-2.5 py-1 text-xs font-mono text-zinc-400 transition-colors hover:border-[#382f47] hover:bg-[#1b1526] hover:text-zinc-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-rose-400"
            >
              <AnimatePresence mode="wait" initial={false}>
                {copied ? (
                  <motion.span
                    key="check"
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.8 }}
                    className="flex items-center gap-1 text-rose-400"
                  >
                    <Check className="h-3 w-3" />
                    <span>Copied!</span>
                  </motion.span>
                ) : (
                  <motion.span
                    key="copy"
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.8 }}
                    className="flex items-center gap-1"
                  >
                    <Copy className="h-3 w-3 shrink-0 opacity-70" />
                    <span className="truncate max-w-[200px] xs:max-w-none">@{telegramHandle.replace(/^@/, "")}</span>
                  </motion.span>
                )}
              </AnimatePresence>
            </motion.button>
          </div>

          {/* Bot Identity */}
          <motion.div variants={itemVariants} className="flex items-start gap-4 sm:gap-5">
            <div className="relative flex-shrink-0">
              <div className="flex h-12 w-12 sm:h-14 sm:w-14 items-center justify-center rounded-2xl border border-[#2e243b] bg-[#14101b] p-1 shadow-inner ring-1 ring-white/[0.06] overflow-hidden group-hover:border-rose-400/50">
                <img
                  src="/icon.png"
                  alt={botName}
                  className="h-full w-full object-contain drop-shadow select-none"
                  onError={(e) => {
                    const target = e.currentTarget as HTMLElement;
                    target.style.display = "none";
                  }}
                />
                <Bot className="h-6 w-6 sm:h-7 sm:w-7 text-zinc-100 hidden" />
              </div>
              <div
                aria-hidden="true"
                className="absolute -bottom-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full border border-[#0d0a13] bg-gradient-to-r from-amber-500 to-rose-500 text-zinc-950 shadow-sm"
              >
                <Sparkles className="h-3 w-3 text-zinc-950" />
              </div>
            </div>

            <div className="min-w-0 flex-1">
              <h1 className="text-xl sm:text-2xl font-semibold tracking-tight text-zinc-100 flex items-center gap-2">
                {botName}
                <span className="inline-flex items-center rounded-md border border-[#262031] bg-[#14101c] px-1.5 py-0.5 text-[10px] font-mono font-medium tracking-normal text-zinc-400">
                  v2.0
                </span>
              </h1>
              <p className="mt-1 text-sm font-medium tracking-tight bg-gradient-to-r from-amber-300 via-rose-300 to-amber-200 bg-clip-text text-transparent">
                {subtitle}
              </p>
              <p className="mt-2 text-xs sm:text-sm leading-relaxed text-zinc-400 line-clamp-2 sm:line-clamp-none">
                {description}
              </p>
            </div>
          </motion.div>
        </header>

        {/* 2. DUAL ENGINE STATUS (SOLID MATTE) */}
        <motion.section
          variants={itemVariants}
          className="mt-6 sm:mt-7 relative z-10"
          aria-label="Engine Operational Status"
        >
          <div className="mb-3.5 flex items-center justify-between">
            <h2 className="text-[11px] font-mono tracking-wider text-zinc-400 uppercase flex items-center gap-1.5">
              <Layers className="h-3.5 w-3.5 text-rose-400" />
              <span>System Status</span>
            </h2>
          </div>

          {/* Solid Matte Engine Cards Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {/* Engine 1: Content Bank (Always Active) */}
            <div className="relative overflow-hidden rounded-xl border border-amber-500/30 bg-[#15111a] p-3.5 transition-all duration-200 hover:border-amber-500/40">
              <div className="flex items-center justify-between gap-2">
                <div className="flex items-center gap-2.5 min-w-0">
                  <div className="flex h-9 w-9 shrink-0 items-center justify-center rounded-xl border border-amber-500/30 bg-[#241712] text-amber-400 shadow-sm">
                    <Database className="h-4.5 w-4.5" />
                  </div>
                  <div className="min-w-0">
                    <h3 className="text-xs font-semibold text-zinc-100 truncate">Content Bank</h3>
                    <p className="text-[10px] text-zinc-400 truncate">1,000 Exercises • 5 Tracks</p>
                  </div>
                </div>

                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 font-medium">
                  ACTIVE
                </span>
              </div>
            </div>

            {/* Engine 2: Gemini Flash AI (Dynamic) */}
            <div
              className={`relative overflow-hidden rounded-xl border p-3.5 transition-all duration-300 ${
                geminiActive
                  ? "border-rose-500/30 bg-[#16101c] hover:border-rose-500/40"
                  : "border-[#251f2e] bg-[#141019]"
              }`}
            >
              <div className="flex items-center justify-between gap-2">
                <div className="flex items-center gap-2.5 min-w-0">
                  <div
                    className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-xl border transition-colors ${
                      geminiActive
                        ? "border-rose-500/30 bg-[#25121b] text-rose-400"
                        : "border-[#2c2436] bg-[#1a1422] text-zinc-400"
                    }`}
                  >
                    <Cpu className="h-4.5 w-4.5" />
                  </div>
                  <div className="min-w-0">
                    <h3 className={`text-xs font-semibold truncate ${geminiActive ? "text-zinc-100" : "text-zinc-300"}`}>
                      Gemini Flash AI
                    </h3>
                    <p className="text-[10px] text-zinc-500 truncate">Smart Generator &amp; Evaluator</p>
                  </div>
                </div>

                <span
                  className={`text-[10px] font-mono px-2 py-0.5 rounded font-medium transition-colors ${
                    geminiActive
                      ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20"
                      : "bg-zinc-800/60 text-zinc-500 border border-zinc-700/40"
                  }`}
                >
                  {geminiActive ? "ACTIVE" : "STANDBY"}
                </span>
              </div>
            </div>
          </div>

          {/* Dynamic Status Note (Solid Matte) */}
          <div
            className={`mt-3 flex items-start sm:items-center gap-2.5 rounded-xl border p-3 text-xs transition-all duration-300 ${
              geminiActive
                ? "border-rose-500/30 bg-[#18101a] text-zinc-300"
                : "border-amber-500/30 bg-[#181316] text-zinc-300"
            }`}
          >
            <div className={`flex h-4 w-4 shrink-0 items-center justify-center mt-0.5 sm:mt-0 ${geminiActive ? "text-rose-400" : "text-amber-400"}`}>
              {geminiActive ? <CheckCircle2 className="h-3.5 w-3.5" /> : <Clock className="h-3.5 w-3.5" />}
            </div>
            <p className="text-[11px] leading-relaxed text-zinc-300">
              {geminiActive ? (
                <>
                  <b>Hybrid Mode Active</b>: AI dynamically generates fresh exercises &amp; intelligent evaluations, backed by{" "}
                  <b>1,000 curated exercises</b> as instant fallback.
                </>
              ) : (
                <>
                  <b>Content Bank Operating</b>: 1,000 curated exercises ready for learners without requiring an API key.
                </>
              )}
            </p>
          </div>

          {/* 5 Learning Tracks Chips (Solid Matte with Rose Gold & Amber Animated Icons) */}
          <div className="mt-3.5 flex flex-wrap items-center gap-1.5 text-[11px] font-mono text-zinc-400">
            <span className="text-zinc-500 text-[10px] uppercase tracking-wider mr-0.5 select-none">Tracks:</span>

            <motion.span
              initial="normal"
              whileHover="hover"
              className="inline-flex cursor-pointer select-none items-center gap-1.5 rounded-md border border-[#292033] bg-[#14101c] px-2 py-0.5 text-zinc-300 hover:border-amber-400/50 hover:bg-[#1b1425] hover:text-amber-200 hover:shadow-[0_0_12px_rgba(245,158,11,0.12)] transition-all duration-200"
            >
              <AnimatedChatIcon className="w-3 h-3 text-amber-400 shrink-0" />
              <span>Conversation</span>
            </motion.span>

            <motion.span
              initial="normal"
              whileHover="hover"
              className="inline-flex cursor-pointer select-none items-center gap-1.5 rounded-md border border-[#292033] bg-[#14101c] px-2 py-0.5 text-zinc-300 hover:border-rose-400/50 hover:bg-[#1b1425] hover:text-rose-200 hover:shadow-[0_0_12px_rgba(251,113,133,0.12)] transition-all duration-200"
            >
              <AnimatedVocabIcon className="w-3 h-3 text-rose-400 shrink-0" />
              <span>Vocabulary</span>
            </motion.span>

            <motion.span
              initial="normal"
              whileHover="hover"
              className="inline-flex cursor-pointer select-none items-center gap-1.5 rounded-md border border-[#292033] bg-[#14101c] px-2 py-0.5 text-zinc-300 hover:border-amber-400/50 hover:bg-[#1b1425] hover:text-amber-200 hover:shadow-[0_0_12px_rgba(245,158,11,0.12)] transition-all duration-200"
            >
              <AnimatedGrammarIcon className="w-3 h-3 text-amber-400 shrink-0" />
              <span>Grammar</span>
            </motion.span>

            <motion.span
              initial="normal"
              whileHover="hover"
              className="inline-flex cursor-pointer select-none items-center gap-1.5 rounded-md border border-[#292033] bg-[#14101c] px-2 py-0.5 text-zinc-300 hover:border-rose-400/50 hover:bg-[#1b1425] hover:text-rose-200 hover:shadow-[0_0_12px_rgba(251,113,133,0.12)] transition-all duration-200"
            >
              <AnimatedReadingIcon className="w-3 h-3 text-rose-400 shrink-0" />
              <span>Reading</span>
            </motion.span>

            <motion.span
              initial="normal"
              whileHover="hover"
              className="inline-flex cursor-pointer select-none items-center gap-1.5 rounded-md border border-[#292033] bg-[#14101c] px-2 py-0.5 text-zinc-300 hover:border-amber-400/50 hover:bg-[#1b1425] hover:text-amber-200 hover:shadow-[0_0_12px_rgba(245,158,11,0.12)] transition-all duration-200"
            >
              <AnimatedZapIcon className="w-3 h-3 text-amber-400 shrink-0" />
              <span>Challenge</span>
            </motion.span>
          </div>
        </motion.section>

        {/* 3. PRIMARY ACTION & COMMAND SHORTCUTS */}
        <motion.section
          variants={itemVariants}
          className="mt-7 sm:mt-8 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 pt-5 border-t border-[#231e2b] relative z-10"
        >
          {/* Quick command hints */}
          <div className="flex items-center gap-1.5 overflow-x-auto py-1 text-xs text-zinc-400 scrollbar-none">
            <span className="text-zinc-500 font-mono text-[11px]">Quick:</span>
            <code className="rounded bg-[#14101c] px-1.5 py-0.5 font-mono text-[11px] text-zinc-300 border border-[#271f32]">
              /start
            </code>
            <code className="rounded bg-[#14101c] px-1.5 py-0.5 font-mono text-[11px] text-zinc-300 border border-[#271f32]">
              /help
            </code>
          </div>

          {/* Prominent Action Button in Sunset Amber & Rose Gold Gradient */}
          <motion.a
            href={telegramUrl}
            target="_blank"
            rel="noopener noreferrer"
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
            className="group relative inline-flex items-center justify-center gap-2 rounded-xl bg-gradient-to-r from-amber-500 via-rose-500 to-amber-500 bg-[length:200%_auto] px-5 py-2.5 text-sm font-semibold tracking-tight text-white shadow-[0_4px_20px_rgba(245,158,11,0.35)] transition-all duration-300 hover:bg-right hover:shadow-[0_6px_25px_rgba(244,63,94,0.45)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-rose-300"
          >
            <span>Open in Telegram</span>
            <ArrowUpRight className="h-4 w-4 transition-transform duration-200 group-hover:-translate-y-0.5 group-hover:translate-x-0.5" />
          </motion.a>
        </motion.section>

        {/* 4. DEVELOPER SIGNATURE FOOTER */}
        <motion.footer
          variants={itemVariants}
          className="mt-6 pt-4 border-t border-zinc-800/60 flex flex-wrap items-center justify-center gap-y-1.5 text-[11px] text-zinc-500 font-normal tracking-wide relative z-10"
        >
          {/* Author with GitHub Octocat Icon */}
          <span className="inline-flex items-center gap-1">
            <span>by</span>
            <a
              href="https://github.com/arlandoapraharjo"
              target="_blank"
              rel="noopener noreferrer"
              className="group inline-flex items-center gap-1 text-zinc-400 hover:text-zinc-200 underline decoration-zinc-700 underline-offset-4 transition-colors duration-150"
            >
              <svg
                className="w-3.5 h-3.5 fill-current shrink-0 transition-transform duration-200 group-hover:scale-110"
                viewBox="0 0 24 24"
              >
                <path
                  fillRule="evenodd"
                  clipRule="evenodd"
                  d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z"
                />
              </svg>
              <span>@arlandoapraharjo</span>
            </a>
          </span>

          <span className="mx-2 text-zinc-700 select-none">•</span>

          {/* Repo with GitBranch and Arrow Icons */}
          <a
            href="https://github.com/arlandoapraharjo/mebby-telegram-bot"
            target="_blank"
            rel="noopener noreferrer"
            className="group inline-flex items-center gap-1 text-zinc-400 hover:text-zinc-200 underline decoration-zinc-700 underline-offset-4 transition-colors duration-150"
          >
            <GitBranch className="h-3.5 w-3.5 shrink-0 transition-transform duration-200 group-hover:rotate-12" />
            <span>View Repo</span>
            <ArrowUpRight className="h-3 w-3 text-zinc-500 transition-transform duration-200 group-hover:text-zinc-300 group-hover:-translate-y-0.5 group-hover:translate-x-0.5" />
          </a>
        </motion.footer>
      </motion.div>
    </div>
  );
};

export default BotStatusCard;
