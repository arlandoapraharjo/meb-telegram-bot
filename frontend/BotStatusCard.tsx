/// <reference path="./declarations.d.ts" />
import React, { useState, type ElementType, type FC, type MouseEvent } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  ArrowUpRight,
  Bot,
  Sparkles,
  MessageSquare,
  BookOpen,
  PenTool,
  BookMarked,
  Mic,
  Trophy,
  ShieldCheck,
  Server,
  Zap,
  Copy,
  Check,
} from "lucide-react";

export interface LearningTrack {
  id: string;
  emoji: string;
  title: string;
  description: string;
  level: string;
  badgeText?: string;
  icon: ElementType;
}

export interface BotStatusCardProps {
  botName?: string;
  subtitle?: string;
  description?: string;
  telegramHandle?: string;
  telegramUrl?: string;
  uptime?: string;
  status?: "operational" | "degraded" | "maintenance";
  statusText?: string;
  tracks?: LearningTrack[];
  systemSpecs?: string[];
  className?: string;
}

const DEFAULT_TRACKS: LearningTrack[] = [
  {
    id: "conversation",
    emoji: "💬",
    title: "Daily Conversation",
    description: "Sapaan dan perkenalan sekolah sehari-hari yang ramah dan mudah dipahami.",
    level: "A1–A2",
    badgeText: "Sapaan",
    icon: MessageSquare,
  },
  {
    id: "vocabulary",
    emoji: "📚",
    title: "Vocabulary Builder",
    description: "Kosakata anggota tubuh (body parts) & kegiatan sehari-hari (daily activity).",
    level: "Dasar",
    badgeText: "Kosakata",
    icon: BookOpen,
  },
  {
    id: "grammar",
    emoji: "✏️",
    title: "Grammar Lab",
    description: "Aturan to be (am/is/are), kata kerja (verbs), kata sifat, & jenis kata.",
    level: "Dasar",
    badgeText: "Tata Bahasa",
    icon: PenTool,
  },
  {
    id: "reading",
    emoji: "📖",
    title: "Reading Corner",
    description: "Teks deskripsi sederhana, fabel pendek (narrative), & pengalaman lampau (recount).",
    level: "Cerita",
    badgeText: "Membaca",
    icon: BookMarked,
  },
  {
    id: "speaking",
    emoji: "🗣️",
    title: "Speaking Practice",
    description: "Pelafalan kata dasar dan kalimat sapaan dengan panduan cara baca.",
    level: "Pengucapan",
    badgeText: "Bicara",
    icon: Mic,
  },
  {
    id: "challenge",
    emoji: "🎮",
    title: "English Challenge",
    description: "Susun kata mudah (seperti 'I am a girl') dan kuis to be seru tanpa bikin pusing.",
    level: "Santai",
    badgeText: "Tantangan",
    icon: Trophy,
  },
];

const DEFAULT_SPECS = [
  "Vercel Serverless",
  "Python Async Core",
  "Zero Data Retention",
  "Gemini Flash Hybrid",
];

export const BotStatusCard: FC<BotStatusCardProps> = ({
  botName = "English Buddy",
  subtitle = "Interactive Telegram Language Companion",
  description = "A craft-engineered Telegram bot delivering CEFR-calibrated daily conversation, vocabulary drills, grammar coaching, and gamified challenges directly in your chat.",
  telegramHandle = "EnglishBuddyBot",
  telegramUrl = "https://t.me/EnglishBuddyBot",
  uptime = "99.9%",
  status = "operational",
  statusText = "Webhook Active",
  tracks = DEFAULT_TRACKS,
  systemSpecs = DEFAULT_SPECS,
  className = "",
}) => {
  const [copied, setCopied] = useState(false);
  const [hoveredTrack, setHoveredTrack] = useState<string | null>(null);

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
        className="pointer-events-none absolute -top-24 left-1/2 -translate-x-1/2 w-96 h-96 bg-emerald-500/[0.07] rounded-full blur-3xl"
      />
      <div
        aria-hidden="true"
        className="pointer-events-none absolute -bottom-16 right-10 w-72 h-72 bg-zinc-700/[0.08] rounded-full blur-3xl"
      />

      {/* Main Bento Card */}
      <motion.div
        variants={containerVariants}
        initial="hidden"
        animate="visible"
        className="relative overflow-hidden rounded-3xl border border-zinc-800/80 bg-zinc-950/70 p-6 sm:p-8 backdrop-blur-2xl shadow-[0_0_0_1px_rgba(255,255,255,0.03),0_20px_50px_-12px_rgba(0,0,0,0.7)] ring-1 ring-white/[0.04]"
      >
        {/* Subtle Top Accent Line */}
        <div
          aria-hidden="true"
          className="absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-emerald-500/30 to-transparent"
        />

        {/* 1. HEADER SECTION */}
        <header className="flex flex-col gap-5 sm:gap-6">
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
              <div className="flex h-12 w-12 sm:h-14 sm:w-14 items-center justify-center rounded-2xl border border-zinc-700/60 bg-gradient-to-br from-zinc-800 to-zinc-900 shadow-inner">
                <Bot className="h-6 w-6 sm:h-7 sm:w-7 text-zinc-100" />
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

        {/* 2. LEARNING TRACKS (BENTO / PILL GRID) */}
        <motion.section
          variants={itemVariants}
          className="mt-6 sm:mt-7"
          aria-label="Interactive Learning Tracks"
        >
          <div className="mb-3 flex items-center justify-between">
            <h2 className="text-xs font-mono font-medium uppercase tracking-wider text-zinc-400">
              Core Learning Tracks
            </h2>
            <span className="text-[11px] font-mono text-zinc-500">
              CEFR Aligned • 6 Modes
            </span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
            {tracks.map((track) => {
              const Icon = track.icon;
              const isHovered = hoveredTrack === track.id;

              return (
                <motion.div
                  key={track.id}
                  variants={itemVariants}
                  onMouseEnter={() => setHoveredTrack(track.id)}
                  onMouseLeave={() => setHoveredTrack(null)}
                  tabIndex={0}
                  role="article"
                  aria-label={`${track.title}: ${track.description}`}
                  className="group relative flex flex-col justify-between overflow-hidden rounded-2xl border border-zinc-800/80 bg-zinc-900/30 p-3.5 transition-all duration-200 hover:border-zinc-700/80 hover:bg-zinc-900/70 hover:shadow-lg hover:shadow-black/40 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-400"
                >
                  {/* Subtle hover gradient */}
                  <div
                    aria-hidden="true"
                    className={`pointer-events-none absolute inset-0 bg-gradient-to-br from-emerald-500/[0.04] to-transparent opacity-0 transition-opacity duration-200 ${
                      isHovered ? "opacity-100" : ""
                    }`}
                  />

                  <div>
                    <div className="flex items-center justify-between gap-2">
                      <div className="flex items-center gap-2">
                        <span className="text-base" role="img" aria-hidden="true">
                          {track.emoji}
                        </span>
                        <h3 className="text-xs sm:text-sm font-semibold tracking-tight text-zinc-200 transition-colors group-hover:text-zinc-100">
                          {track.title}
                        </h3>
                      </div>

                      <span className="inline-flex items-center rounded-md border border-zinc-800/80 bg-zinc-900/80 px-1.5 py-0.5 text-[10px] font-mono font-medium text-zinc-400 group-hover:border-zinc-700 group-hover:text-zinc-300">
                        {track.level}
                      </span>
                    </div>

                    <p className="mt-1.5 text-xs leading-relaxed text-zinc-400 transition-colors group-hover:text-zinc-300">
                      {track.description}
                    </p>
                  </div>

                  <div className="mt-3 flex items-center justify-between border-t border-zinc-800/40 pt-2 text-[11px] font-mono text-zinc-500">
                    <span className="flex items-center gap-1">
                      <Icon className="h-3 w-3 text-zinc-400 group-hover:text-emerald-400 transition-colors" />
                      <span>{track.badgeText || "Active"}</span>
                    </span>
                    <span className="text-zinc-600 transition-colors group-hover:text-zinc-400">
                      Instant Feedback
                    </span>
                  </div>
                </motion.div>
              );
            })}
          </div>
        </motion.section>

        {/* 3. PRIMARY ACTION & COMMAND SHORTCUTS */}
        <motion.section
          variants={itemVariants}
          className="mt-7 sm:mt-8 flex flex-col sm:flex-row items-stretch sm:items-center justify-between gap-3 pt-5 border-t border-zinc-800/80"
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

          {/* Prominent Understated Action Button */}
          <motion.a
            href={telegramUrl}
            target="_blank"
            rel="noopener noreferrer"
            whileHover={{ scale: 1.01 }}
            whileTap={{ scale: 0.98 }}
            className="group relative inline-flex items-center justify-center gap-2 rounded-xl bg-zinc-100 px-5 py-2.5 text-sm font-medium tracking-tight text-zinc-950 shadow-[0_1px_2px_rgba(0,0,0,0.1),0_0_12px_rgba(255,255,255,0.12)] transition-all duration-200 hover:bg-white hover:shadow-[0_0_20px_rgba(255,255,255,0.22)] focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-zinc-200"
          >
            <span>Launch on Telegram</span>
            <ArrowUpRight className="h-4 w-4 transition-transform duration-200 group-hover:-translate-y-0.5 group-hover:translate-x-0.5" />
          </motion.a>
        </motion.section>

        {/* 4. FOOTER SYSTEM METADATA */}
        <motion.footer
          variants={itemVariants}
          className="mt-6 pt-4 border-t border-zinc-900 flex flex-wrap items-center justify-between gap-2 text-[11px] font-mono text-zinc-500"
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
