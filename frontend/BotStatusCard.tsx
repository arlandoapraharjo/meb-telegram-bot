/// <reference path="./declarations.d.ts" />
import React, { useState, type ElementType, type FC, type MouseEvent } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowUpRight,
  Bot,
  Sparkles,
  ShieldCheck,
  Server,
  Zap,
  Copy,
  Check,
  Database,
  Cpu,
  CheckCircle2,
  Clock,
  Layers,
} from "lucide-react";
import { ShaderBackground } from "./components/ui/dotted-veil";

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
  botName = "Mandiri English Buddy",
  subtitle = "AI & Offline English Tutor Bot",
  description = "Bot Telegram edukasi bahasa Inggris adaptif untuk siswa Indonesia dengan sistem Dual Engine: Bank Soal Kurasi Offline dan AI Flash Engine.",
  telegramHandle = "EnglishBuddy_Practice_Bot",
  telegramUrl = "https://t.me/EnglishBuddy_Practice_Bot",
  uptime = "99.98%",
  status = "operational",
  statusText = "Online",
  systemSpecs = ["FastAPI Webhook", "< 1ms Offline Fallback", "100% Free / No Key Req"],
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
      {/* Subtle Ambient Radial Glow */}
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -top-24 left-1/2 -translate-x-1/2 w-96 h-96 bg-emerald-500/[0.08] rounded-full blur-3xl"
      />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -bottom-16 right-10 w-72 h-72 bg-emerald-700/[0.06] rounded-full blur-3xl"
      />

      {/* Main Bento Card with WebGL ShaderBackground embedded */}
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        className="relative overflow-hidden rounded-3xl border border-zinc-800/80 bg-zinc-950/80 p-6 sm:p-8 backdrop-blur-2xl shadow-[0_0_0_1px_rgba(255,255,255,0.03),0_20px_50px_-12px_rgba(0,0,0,0.7)] ring-1 ring-white/[0.04]"
      >
        {/* WebGL Shader Background behind card content */}
        <div className="absolute inset-0 pointer-events-none opacity-30 -z-10 overflow-hidden rounded-3xl">
          <ShaderBackground className="w-full h-full" />
        </div>

        {/* Subtle Top Accent Line */}
        <div
          aria-hidden="true"
          className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-emerald-500/40 to-transparent"
        />

        {/* 1. HEADER SECTION */}
        <header className="flex flex-col gap-5 sm:gap-6 relative z-10">
          <div className="flex items-center justify-between gap-3">
            {/* Live Status Pill Badge */}
            <motion.div
              variants={itemVariants}
              role="status"
              aria-label={`System status: ${statusText} with ${uptime} uptime`}
              className="inline-flex items-center gap-2 rounded-full border border-emerald-500/20 bg-emerald-500/[0.08] px-3 py-1 text-xs font-medium text-emerald-400 shadow-[0_0_12px_rgba(16,185,129,0.12)] transition-colors hover:border-emerald-500/30 hover:bg-emerald-500/[0.12]"
            >
              <span className="relative flex h-2 w-2" aria-hidden="true">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-emerald-400 opacity-75" />
                <span className="relative inline-flex h-2 w-2 rounded-full bg-emerald-500" />
              </span>
              <span className="tracking-tight font-medium">
                {statusText} • {uptime} Uptime
              </span>
            </motion.div>

            {/* Micro Quick-Action: Copy Handle */}
            <motion.button
              variants={itemVariants}
              onClick={handleCopyHandle}
              type="button"
              aria-label={`Copy Telegram bot handle @${telegramHandle}`}
              className="inline-flex items-center gap-1.5 rounded-full border border-zinc-800 bg-zinc-900/60 px-2.5 py-1 text-xs font-mono text-zinc-400 transition-colors hover:border-zinc-700 hover:bg-zinc-800/80 hover:text-zinc-200 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
            >
              <AnimatePresence mode="wait" initial={false}>
                {copied ? (
                  <motion.span
                    key="check"
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.8 }}
                    className="flex items-center gap-1 text-emerald-400"
                  >
                    <Check className="h-3 w-3" />
                    <span>Copied</span>
                  </motion.span>
                ) : (
                  <motion.span
                    key="copy"
                    initial={{ opacity: 0, scale: 0.8 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.8 }}
                    className="flex items-center gap-1"
                  >
                    <Copy className="h-3 w-3 opacity-70" />
                    <span>@{telegramHandle.replace(/^@/, "")}</span>
                  </motion.span>
                )}
              </AnimatePresence>
            </motion.button>
          </div>

          {/* Bot Identity */}
          <motion.div variants={itemVariants} className="flex items-start gap-4 sm:gap-5">
            <div className="relative flex-shrink-0">
              <div className="flex h-12 w-12 sm:h-14 sm:w-14 items-center justify-center rounded-2xl border border-amber-500/25 bg-gradient-to-br from-amber-500/[0.08] via-zinc-900 to-zinc-950 p-1 shadow-inner shadow-amber-500/10 ring-1 ring-white/[0.06] overflow-hidden">
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
                className="absolute -bottom-1 -right-1 flex h-5 w-5 items-center justify-center rounded-full border border-zinc-900 bg-emerald-500 text-zinc-950"
              >
                <Sparkles className="h-3 w-3" />
              </div>
            </div>

            <div className="min-w-0 flex-1">
              <h1 className="text-xl sm:text-2xl font-semibold tracking-tight text-zinc-100 flex items-center gap-2">
                {botName}
                <span className="inline-flex items-center rounded-md border border-zinc-800 bg-zinc-900 px-1.5 py-0.5 text-[10px] font-mono font-medium tracking-normal text-zinc-400">
                  v2.0
                </span>
              </h1>
              <p className="mt-1 text-sm font-medium tracking-tight text-zinc-400">
                {subtitle}
              </p>
              <p className="mt-2 text-xs sm:text-sm leading-relaxed text-zinc-500 line-clamp-2 sm:line-clamp-none">
                {description}
              </p>
            </div>
          </motion.div>
        </header>

        {/* 2. DUAL ENGINE STATUS: CONTENT BANK VS GEMINI MODE */}
        <motion.section
          variants={itemVariants}
          className="mt-6 sm:mt-7 relative z-10"
          aria-label="Engine Operational Status"
        >
          <div className="mb-3 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <h2 className="text-xs font-mono font-medium uppercase tracking-wider text-zinc-300 flex items-center gap-1.5">
                <Layers className="h-3.5 w-3.5 text-emerald-400" />
                <span>Dual Engine Status</span>
              </h2>
              <span className="inline-flex items-center rounded-md border border-zinc-800 bg-zinc-900/80 px-1.5 py-0.5 text-[10px] font-mono text-zinc-400">
                2 Modes
              </span>
            </div>

            {/* Overarching Summary Pill: Only 1 Mode Active */}
            <div className="inline-flex items-center gap-1.5 rounded-full border border-amber-500/30 bg-amber-500/[0.08] px-2.5 py-1 text-[11px] font-mono text-amber-300 shadow-[0_0_10px_rgba(245,158,11,0.1)]">
              <span className="relative flex h-2 w-2">
                <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-amber-400 opacity-75" />
                <span className="relative inline-flex h-2 w-2 rounded-full bg-amber-400" />
              </span>
              <span className="font-medium">1 Mode Aktif (Content Bank)</span>
            </div>
          </div>

          {/* Mode Comparison Grid */}
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {/* Mode 1: Content Bank (ACTIVE) */}
            <div className="relative overflow-hidden rounded-2xl border border-emerald-500/40 bg-gradient-to-b from-emerald-500/[0.08] to-zinc-900/80 p-4 shadow-[0_0_20px_rgba(16,185,129,0.08)] backdrop-blur-md">
              <div className="flex items-start justify-between gap-2">
                <div className="flex items-center gap-2.5">
                  <div className="flex h-9 w-9 items-center justify-center rounded-xl border border-emerald-500/30 bg-emerald-500/10 text-emerald-400 shadow-sm">
                    <Database className="h-4.5 w-4.5" />
                  </div>
                  <div>
                    <h3 className="text-xs font-semibold text-zinc-100 flex items-center gap-1.5">
                      Content Bank Mode
                      <span className="rounded bg-emerald-500/20 px-1.5 py-0.5 text-[9px] font-mono font-medium text-emerald-300">
                        Offline
                      </span>
                    </h3>
                    <p className="text-[10px] text-zinc-400">Materi Terkurasi & Mandiri</p>
                  </div>
                </div>

                <span className="inline-flex items-center gap-1.5 rounded-full border border-emerald-500/40 bg-emerald-500/15 px-2 py-0.5 text-[10px] font-mono font-semibold text-emerald-300">
                  <span className="h-1.5 w-1.5 rounded-full bg-emerald-400 animate-pulse" />
                  AKTIF
                </span>
              </div>

              <div className="mt-3.5 space-y-1.5 text-[11px] border-t border-zinc-800/80 pt-2.5 font-sans">
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Status Mesin:</span>
                  <span className="font-medium text-emerald-400 flex items-center gap-1">
                    <CheckCircle2 className="h-3 w-3" /> Siap Melayani
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Kapasitas:</span>
                  <span className="font-mono text-zinc-200">108 Soal (6 Kategori)</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Kecepatan:</span>
                  <span className="font-mono text-emerald-400">&lt; 1 ms (Instan)</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Kebutuhan Kuota:</span>
                  <span className="font-mono text-zinc-300">100% Gratis / No API Key</span>
                </div>
              </div>
            </div>

            {/* Mode 2: Gemini Flash AI (STANDBY / INACTIVE) */}
            <div className="relative overflow-hidden rounded-2xl border border-zinc-800/80 bg-zinc-900/40 p-4 backdrop-blur-md">
              <div className="flex items-start justify-between gap-2">
                <div className="flex items-center gap-2.5">
                  <div className="flex h-9 w-9 items-center justify-center rounded-xl border border-zinc-800 bg-zinc-800/40 text-zinc-400">
                    <Cpu className="h-4.5 w-4.5" />
                  </div>
                  <div>
                    <h3 className="text-xs font-semibold text-zinc-300 flex items-center gap-1.5">
                      Gemini Flash Mode
                      <span className="rounded bg-zinc-800 px-1.5 py-0.5 text-[9px] font-mono font-medium text-zinc-400">
                        Online AI
                      </span>
                    </h3>
                    <p className="text-[10px] text-zinc-500">Dynamic AI Question & Feedback</p>
                  </div>
                </div>

                <span className="inline-flex items-center gap-1.5 rounded-full border border-zinc-700/60 bg-zinc-800/60 px-2 py-0.5 text-[10px] font-mono font-medium text-zinc-400">
                  <span className="h-1.5 w-1.5 rounded-full bg-zinc-500" />
                  STANDBY
                </span>
              </div>

              <div className="mt-3.5 space-y-1.5 text-[11px] border-t border-zinc-800/80 pt-2.5 font-sans">
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Status Mesin:</span>
                  <span className="font-medium text-zinc-400 flex items-center gap-1">
                    <Clock className="h-3 w-3 text-zinc-500" /> Menunggu API Key
                  </span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Kondisi .env:</span>
                  <span className="font-mono text-amber-400/90">GEMINI_API_KEY kosong</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Kecepatan:</span>
                  <span className="font-mono text-zinc-500">-- ms (Standby)</span>
                </div>
                <div className="flex items-center justify-between">
                  <span className="text-zinc-400">Aktivasi:</span>
                  <span className="text-zinc-400">Isi API key di .env</span>
                </div>
              </div>
            </div>
          </div>

          {/* Operational Clarity Callout Banner */}
          <div className="mt-3 rounded-2xl border border-emerald-500/20 bg-emerald-500/[0.04] p-3.5 text-xs leading-relaxed text-zinc-300 flex items-start gap-3">
            <div className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-emerald-500/20 text-emerald-400 mt-0.5">
              <Check className="h-3 w-3" />
            </div>
            <div>
              <p className="font-semibold text-zinc-100 mb-0.5">
                Status Operasional Saat Ini: Hanya 1 Mode yang Aktif
              </p>
              <p className="text-zinc-400 text-[11px]">
                Bot saat ini beroperasi penuh menggunakan <b>Mode Content Bank (Offline Engine)</b>. Semua 108 materi dan latihan aktif 100% tanpa risiko downtime atau kuota habis. Jika Anda memasukkan <code>GEMINI_API_KEY</code> di file <code>.env</code>, bot akan otomatis beralih menjadi <b>Hybrid Mode</b> (AI dinamis + fallback bank soal).
              </p>
            </div>
          </div>
        </motion.section>

        {/* 3. PRIMARY ACTION & COMMAND SHORTCUTS */}
        <motion.section
          variants={itemVariants}
          className="mt-7 sm:mt-8 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 pt-5 border-t border-zinc-800/80 relative z-10"
        >
          {/* Quick command hints */}
          <div className="flex items-center gap-1.5 overflow-x-auto py-1 text-xs text-zinc-400 scrollbar-none">
            <span className="text-zinc-500 font-mono text-[11px]">Quick:</span>
            <code className="rounded bg-zinc-900 px-1.5 py-0.5 font-mono text-[11px] text-zinc-300 border border-zinc-800">
              /start
            </code>
            <code className="rounded bg-zinc-900 px-1.5 py-0.5 font-mono text-[11px] text-zinc-300 border border-zinc-800">
              /level
            </code>
            <code className="rounded bg-zinc-900 px-1.5 py-0.5 font-mono text-[11px] text-zinc-300 border border-zinc-800">
              /help
            </code>
          </div>

          {/* Prominent Action Button */}
          <motion.a
            href={telegramUrl}
            target="_blank"
            rel="noopener noreferrer"
            whileHover={{ scale: 1.01 }}
            whileTap={{ scale: 0.98 }}
            className="group relative inline-flex items-center justify-center gap-2 rounded-xl bg-zinc-100 px-5 py-2.5 text-sm font-medium tracking-tight text-zinc-950 shadow-[0_1px_2px_rgba(0,0,0,0.1),0_0_12px_rgba(255,255,255,0.12)] transition-all duration-200 hover:bg-white hover:shadow-[0_0_20px_rgba(255,255,255,0.22)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-200"
          >
            <span>Buka di Telegram</span>
            <ArrowUpRight className="h-4 w-4 transition-transform duration-200 group-hover:-translate-y-0.5 group-hover:translate-x-0.5" />
          </motion.a>
        </motion.section>

        {/* 4. FOOTER SYSTEM METADATA */}
        <motion.footer
          variants={itemVariants}
          className="mt-6 pt-4 border-t border-zinc-900 flex flex-wrap items-center justify-between gap-2 text-[11px] font-mono text-zinc-500 relative z-10"
        >
          <div className="flex flex-wrap items-center gap-2">
            <span className="inline-flex items-center gap-1">
              <Server className="h-3 w-3 text-zinc-400" />
              {systemSpecs[0]}
            </span>
            <span className="text-zinc-700">•</span>
            <span className="inline-flex items-center gap-1">
              <Zap className="h-3 w-3 text-zinc-400" />
              {systemSpecs[1]}
            </span>
            <span className="text-zinc-700">•</span>
            <span className="inline-flex items-center gap-1">
              <ShieldCheck className="h-3 w-3 text-emerald-500" />
              {systemSpecs[2]}
            </span>
          </div>

          <div className="text-zinc-600">
            HTTPS Encrypted • RFC 7231
          </div>
        </motion.footer>
      </motion.div>
    </div>
  );
};

export default BotStatusCard;
