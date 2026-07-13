import streamlit as st
from datetime import datetime

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="RK SafeSpace - Safe Relationship Check",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap");

*, *::before, *::after { box-sizing: border-box; }

html, body, [class*="css"] {
    font-family: "Plus Jakarta Sans", sans-serif !important;
    background-color: #2a2a2a !important;
}

.stApp { background-color: #2a2a2a !important; }

/* ── MOBILE FRAME ── */
.block-container {
    background: #FAFAFA !important;
    max-width: 460px !important;
    margin: 20px auto !important;
    padding: 20px 18px 120px 18px !important;
    border-radius: 28px !important;
    border: 6px solid #c8c8c8 !important;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5) !important;
    min-height: calc(100vh - 40px) !important;
    position: relative !important;
    /* PENTING: jangan overflow:hidden agar bisa scroll */
    overflow-x: hidden !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, [data-testid="stToolbar"] { visibility: hidden !important; }
header { visibility: hidden !important; }

/* ── HEADER ── */
.app-header {
    display: flex; align-items: center;
    justify-content: space-between;
    margin-bottom: 16px; padding: 4px 0;
}
.app-logo {
    display: flex; align-items: center;
    gap: 6px; font-size: 1rem;
    font-weight: 700; color: #6B0F3A;
}
.app-alert-btn {
    width: 34px; height: 34px; border-radius: 50%;
    background: #FFF0F5; display: flex;
    align-items: center; justify-content: center;
    border: 1px solid #F5D0DF;
}

/* ── TYPOGRAPHY ── */
.greeting-text { font-size: 0.8rem; font-weight: 500; color: #888; margin-bottom: 4px; }
.heading-text { font-size: 1.3rem; font-weight: 700; color: #1a1a1a; line-height: 1.3; margin-bottom: 16px; }

/* ── HERO CARD ── */
.card-hero {
    background: #6B0F3A; border-radius: 20px;
    padding: 22px 20px 20px 20px;
    margin-bottom: 12px; position: relative; overflow: hidden;
}
.card-hero h3 { font-size: 1.15rem; font-weight: 700; color: #fff; margin-bottom: 8px; margin-top: 0; }
.card-hero p { font-size: 0.78rem; color: rgba(255,255,255,0.82); line-height: 1.45; max-width: 72%; margin: 0; }
.card-hero-icon { position: absolute; top: 18px; right: 18px; opacity: 0.85; }

/* ── "MULAI SEKARANG" - primary button after hero card ── */
/* Target: stButton that immediately follows the hero-card markdown */
div:has(.hero-btn-marker) + div[data-testid="stButton"] > button,
div:has(.hero-btn-marker) + [data-testid="stButton"] > button {
    background: #E91E8C !important;
    color: white !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 10px 24px !important;
    font-size: 0.85rem !important;
    font-weight: 600 !important;
    height: auto !important;
    min-height: 0 !important;
    margin-bottom: 16px !important;
    box-shadow: 0 4px 12px rgba(233,30,140,0.3) !important;
}

/* ── GRID 2x2 CARD BUTTONS ── */
/* Common card style for all buttons in grid row columns */
div:has(.grid-row-1) + [data-testid="stHorizontalBlock"] .stButton > button,
div:has(.grid-row-2) + [data-testid="stHorizontalBlock"] .stButton > button {
    min-height: 110px !important;
    background: #FFFFFF !important;
    border: 1.5px solid #F0E8ED !important;
    border-radius: 18px !important;
    color: #333 !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    white-space: pre-line !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1.6 !important;
    padding: 14px 8px !important;
    box-shadow: 0 2px 8px rgba(107,15,58,0.04) !important;
    gap: 0 !important;
    transition: box-shadow 0.2s, transform 0.2s !important;
}
div:has(.grid-row-1) + [data-testid="stHorizontalBlock"] .stButton > button:hover,
div:has(.grid-row-2) + [data-testid="stHorizontalBlock"] .stButton > button:hover {
    box-shadow: 0 6px 18px rgba(107,15,58,0.1) !important;
    transform: translateY(-2px) !important;
    border-color: #E8D0DC !important;
}

/* Icon circles via ::before */
div:has(.grid-row-1) + [data-testid="stHorizontalBlock"] .stButton > button::before,
div:has(.grid-row-2) + [data-testid="stHorizontalBlock"] .stButton > button::before {
    content: "";
    display: block;
    width: 46px; height: 46px;
    border-radius: 50%;
    margin-bottom: 10px;
    background-size: 24px;
    background-repeat: no-repeat;
    background-position: center;
    flex-shrink: 0;
}

/* Row 1, Col 1 - Hubungan Sehat */
div:has(.grid-row-1) + [data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button::before {
    background-color: #FFF0F5;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23E91E8C'%3E%3Cpath d='M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z'/%3E%3C/svg%3E");
}
/* Row 1, Col 2 - Riwayat Skrining */
div:has(.grid-row-1) + [data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button::before {
    background-color: #F3E8FF;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%238E24AA'%3E%3Cpath d='M19 3h-4.18C14.4 1.84 13.3 1 12 1s-2.4.84-2.82 2H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-7 0c.55 0 1 .45 1 1s-.45 1-1 1-1-.45-1-1 .45-1 1-1zm2 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z'/%3E%3C/svg%3E");
}
/* Row 2, Col 1 - Bantuan & Konseling */
div:has(.grid-row-2) + [data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button::before {
    background-color: #FFF3E0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23EF6C00'%3E%3Cpath d='M12 1C5.925 1 1 5.925 1 12s4.925 11 11 11 11-4.925 11-11S18.075 1 12 1zm-1 6h2v6h-2V7zm0 8h2v2h-2v-2z'/%3E%3C/svg%3E");
}
/* Row 2, Col 2 - Tentang Aplikasi */
div:has(.grid-row-2) + [data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button::before {
    background-color: #ECEFF1;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23546E7A'%3E%3Cpath d='M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'/%3E%3C/svg%3E");
}

/* ── QUOTE BOX ── */
.quote-box {
    background: #FFF6F9; border: 1px solid #F5E0EA;
    border-radius: 16px; padding: 14px 16px;
    display: flex; align-items: flex-start;
    gap: 10px; margin: 14px 0;
}
.quote-mark {
    font-family: Georgia, serif; font-size: 2.8rem;
    font-weight: 700; color: #E91E8C;
    line-height: 0.7; margin-top: 8px; flex-shrink: 0;
}
.quote-text { font-size: 0.78rem; font-style: italic; color: #555; line-height: 1.5; }

/* ── FAB BUTTON (reset) ── */
div:has(.fab-marker) + [data-testid="stButton"] > button {
    position: fixed !important;
    bottom: 90px !important;
    right: max(16px, calc(50% - 215px)) !important;
    width: 46px !important; height: 46px !important;
    min-height: 0 !important; border-radius: 50% !important;
    background: #D32F2F !important; color: #fff !important;
    font-size: 1.2rem !important; border: none !important;
    box-shadow: 0 4px 16px rgba(211,47,47,0.4) !important;
    padding: 0 !important; z-index: 999 !important;
    line-height: 1 !important;
}

/* ── BOTTOM NAV CONTAINER ── */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] {
    position: fixed !important;
    bottom: 0 !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 460px !important;
    background: #ffffff !important;
    border-top: 1px solid #EDE8EC !important;
    box-shadow: 0 -4px 20px rgba(107,15,58,0.06) !important;
    padding: 8px 8px 18px !important;
    z-index: 998 !important;
}
@media (max-width: 520px) {
    div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] { width: 100% !important; }
}

/* ── BOTTOM NAV BUTTONS ── */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] .stButton > button {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    color: #999 !important;
    font-size: 0.65rem !important;
    font-weight: 500 !important;
    height: 52px !important;
    min-height: 0 !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    justify-content: center !important;
    white-space: pre-line !important;
    padding: 2px 4px !important;
    line-height: 1.4 !important;
    gap: 0 !important;
}
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] .stButton > button:hover {
    background: transparent !important;
    color: #E91E8C !important;
}

/* Nav icons via ::before */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] .stButton > button::before {
    content: "";
    display: block;
    width: 44px; height: 28px;
    border-radius: 50px;
    background-size: 20px;
    background-repeat: no-repeat;
    background-position: center;
    margin-bottom: 2px;
    flex-shrink: 0;
    transition: background-color 0.2s;
}

/* Nav Home icon */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23999'%3E%3Cpath d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z'/%3E%3C/svg%3E");
}
/* Nav Screening icon */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23999'%3E%3Cpath d='M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 14l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'/%3E%3C/svg%3E");
}
/* Nav Resources icon */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] > div:nth-child(3) .stButton > button::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23999'%3E%3Cpath d='M12 6v14c1.35-3.1 4.96-3 7-3V3c-2.04 0-5.65-.1-7 3zm-2 0C8.65 3 5.04 3 3 3v14c2.04 0 5.65-.1 7 3V6z'/%3E%3C/svg%3E");
}
/* Nav AI icon */
div:has(.nav-section-marker) + [data-testid="stHorizontalBlock"] > div:nth-child(4) .stButton > button::before {
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23999'%3E%3Cpath d='M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z'/%3E%3C/svg%3E");
}

/* ── ACTIVE NAV - Home ── */
div:has(.nav-active-home) ~ [data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button::before {
    background-color: #E91E8C !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fff'%3E%3Cpath d='M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z'/%3E%3C/svg%3E") !important;
}
div:has(.nav-active-home) ~ [data-testid="stHorizontalBlock"] > div:nth-child(1) .stButton > button {
    color: #E91E8C !important; font-weight: 700 !important;
}

/* ── ACTIVE NAV - Screening ── */
div:has(.nav-active-screening) ~ [data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button::before {
    background-color: #E91E8C !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fff'%3E%3Cpath d='M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-9 14l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z'/%3E%3C/svg%3E") !important;
}
div:has(.nav-active-screening) ~ [data-testid="stHorizontalBlock"] > div:nth-child(2) .stButton > button {
    color: #E91E8C !important; font-weight: 700 !important;
}

/* ── ACTIVE NAV - Resources ── */
div:has(.nav-active-resources) ~ [data-testid="stHorizontalBlock"] > div:nth-child(3) .stButton > button::before {
    background-color: #E91E8C !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fff'%3E%3Cpath d='M12 6v14c1.35-3.1 4.96-3 7-3V3c-2.04 0-5.65-.1-7 3zm-2 0C8.65 3 5.04 3 3 3v14c2.04 0 5.65-.1 7 3V6z'/%3E%3C/svg%3E") !important;
}
div:has(.nav-active-resources) ~ [data-testid="stHorizontalBlock"] > div:nth-child(3) .stButton > button {
    color: #E91E8C !important; font-weight: 700 !important;
}

/* ── ACTIVE NAV - Chat ── */
div:has(.nav-active-chat) ~ [data-testid="stHorizontalBlock"] > div:nth-child(4) .stButton > button::before {
    background-color: #E91E8C !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23fff'%3E%3Cpath d='M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z'/%3E%3C/svg%3E") !important;
}
div:has(.nav-active-chat) ~ [data-testid="stHorizontalBlock"] > div:nth-child(4) .stButton > button {
    color: #E91E8C !important; font-weight: 700 !important;
}

/* ── GENERIC CARDS ── */
.card { background: #fff; border: 1px solid #F0E8ED; border-radius: 18px; padding: 16px; margin-bottom: 10px; }
.progress-wrap { background: #F0DDE6; border-radius: 10px; height: 7px; overflow: hidden; margin: 8px 0 18px; }
.progress-fill { background: linear-gradient(90deg, #E91E8C, #6B0F3A); height: 100%; border-radius: 10px; transition: width 0.3s; }
.score-circle { width: 170px; height: 170px; border-radius: 50%; background: #fff; border: 8px solid #FCE4EC; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0 auto 16px; box-shadow: 0 4px 20px rgba(107,15,58,0.1); }
.score-number { font-size: 3rem; font-weight: 700; color: #6B0F3A; }
.score-label { font-size: 0.82rem; color: #888; }
.badge { display: inline-block; padding: 5px 18px; border-radius: 50px; font-size: 0.82rem; font-weight: 600; margin-bottom: 10px; }
.badge-low { background: #E8F5E9; color: #2E7D32; }
.badge-medium { background: #FFF3E0; color: #EF6C00; }
.badge-high { background: #FFEBEE; color: #C62828; }
.rec-item { display: flex; gap: 12px; background: #fff; border: 1px solid #F0E8ED; border-radius: 16px; padding: 14px; margin-bottom: 8px; align-items: flex-start; }
.rec-icon { font-size: 1.4rem; flex-shrink: 0; }
.rec-content h4 { font-size: 0.95rem; color: #1a1a1a; margin-bottom: 3px; }
.rec-content p { font-size: 0.8rem; color: #666; line-height: 1.5; }
.disclaimer-banner { background: linear-gradient(90deg,#FFF3E0,#FFE0B2); border-left: 4px solid #FF9800; padding: 10px 14px; border-radius: 0 12px 12px 0; margin-bottom: 12px; font-size: 0.82rem; color: #6B4C1E; }
.chat-ai { background: #fff; border: 1px solid #F0E8ED; border-radius: 18px 18px 18px 4px; padding: 12px 14px; margin-bottom: 8px; max-width: 88%; font-size: 0.88rem; line-height: 1.6; }
.chat-user { background: linear-gradient(135deg,#E91E8C,#6B0F3A); color: #fff; border-radius: 18px 18px 4px 18px; padding: 12px 14px; margin-bottom: 8px; margin-left: auto; max-width: 88%; font-size: 0.88rem; line-height: 1.6; color: #1a1a1a !important; }
.chat-meta { font-size: 0.68rem; color: #999; margin-top: 4px; }
.chat-meta-white { font-size: 0.68rem; color: rgba(255,255,255,0.65); margin-top: 4px; }

/* ── GENERAL BUTTON OVERRIDES ── */
.stButton > button {
    font-family: "Plus Jakarta Sans", sans-serif !important;
    font-weight: 600 !important;
    border-radius: 50px !important;
    transition: all 0.2s !important;
}
.stButton > button[kind="primary"] {
    background: #E91E8C !important;
    border: none !important;
    color: white !important;
}
.stButton > button[kind="primary"]:hover {
    background: #C7157A !important;
}
.stButton > button[kind="secondary"] {
    border: 1.5px solid #E0D0D8 !important;
    color: #6B0F3A !important;
    background: white !important;
}

/* Column horizontal block gap */
[data-testid="stHorizontalBlock"] { gap: 10px !important; }

/* Text input styling */
.stTextInput > div > div > input {
    border-radius: 50px !important;
    border: 1.5px solid #F0E8ED !important;
    font-family: "Plus Jakarta Sans", sans-serif !important;
    padding: 10px 16px !important;
}
.stTextInput > div > div > input:focus {
    border-color: #E91E8C !important;
    box-shadow: 0 0 0 2px rgba(233,30,140,0.1) !important;
}
</style>
""", unsafe_allow_html=True)

# ============================================
# DATA PERTANYAAN (24 Item)
# ============================================
QUESTIONS = [
    "Pasangan saya sering memeriksa pesan di ponsel saya tanpa izin.",
    "Pasangan saya melarang saya bertemu dengan teman atau keluarga.",
    "Pasangan saya sering mengejek atau mempermalukan saya di depan orang lain.",
    "Pasangan saya pernah mengancam akan menyakiti diri sendiri jika saya meninggalkannya.",
    "Pasangan saya sering mengontrol apa yang saya pakai atau bagaimana penampilan saya.",
    "Saya merasa takut untuk mengungkapkan pendapat yang berbeda dengan pasangan.",
    "Pasangan saya sering menyalahkan saya atas masalah yang terjadi dalam hubungan.",
    "Pasangan saya pernah mendorong, menjambak, atau memukul saya.",
    "Pasangan saya menuntut saya untuk selalu melaporkan keberadaan saya.",
    "Pasangan saya tidak menghargai batasan pribadi saya.",
    "Saya merasa terisolasi dari lingkungan sosial saya sejak berhubungan dengan pasangan.",
    "Pasangan saya sering memaksa saya untuk melakukan hal yang tidak saya inginkan.",
    "Pasangan saya mengancam akan menyebarkan rahasia atau foto saya.",
    "Pasangan saya tidak pernah meminta maaf meski sudah menyakiti saya.",
    "Saya merasa hubungan ini lebih membebani daripada membahagiakan.",
    "Pasangan saya sering membandingkan saya dengan orang lain secara negatif.",
    "Pasangan saya tidak mendukung pencapaian atau impian saya.",
    "Saya sering merasa cemas atau takut ketika berinteraksi dengan pasangan.",
    "Pasangan saya pernah memaksa saya untuk melakukan kontak fisik yang tidak saya inginkan.",
    "Pasangan saya mengontrol pengeluaran atau uang saya.",
    "Saya merasa kehilangan identitas diri sejak berhubungan dengan pasangan.",
    "Pasangan saya sering memata-matai aktivitas saya di media sosial.",
    "Pasangan saya mengancam akan menyakiti orang yang saya sayangi.",
    "Saya merasa tidak punya tempat untuk melarikan diri jika hubungan ini memburuk."
]

OPTIONS = [("Sangat Tidak Setuju", 0), ("Tidak Setuju", 1), ("Setuju", 2), ("Sangat Setuju", 3)]

RECOMMENDATIONS = {
    "low": [
        ("🛡️", "Tetap saling percaya", "Kepercayaan adalah fondasi utama hubungan yang damai. Pertahankan komunikasi yang terbuka dan jujur."),
        ("💬", "Komunikasi terbuka", "Jangan ragu ungkapkan perasaanmu dengan cara yang baik. Diskusikan ekspektasi dan batasan bersama."),
        ("🔒", "Menghargai privasi", "Setiap individu butuh ruang pribadi untuk bertumbuh. Hormati batasan satu sama lain."),
        ("🌱", "Terus berkembang", "Dukung satu sama lain dalam mencapai impian dan pencapaian pribadi."),
    ],
    "medium": [
        ("⚠️", "Waspadai tanda-tanda", "Beberapa pola dalam hubunganmu mulai menunjukkan ketidakseimbangan. Perhatikan perubahan perilaku pasangan."),
        ("🗣️", "Bicarakan batasan", "Cobalah berdiskusi dengan pasangan tentang apa yang membuatmu tidak nyaman. Gunakan 'I-statement'."),
        ("👥", "Jaga koneksi sosial", "Jangan isolasi diri dari teman dan keluarga. Mereka adalah support system penting."),
        ("📚", "Pelajari hubungan sehat", "Memahami ciri-ciri hubungan yang sehat dan tidak sehat bisa membantumu mengevaluasi kembali."),
    ],
    "high": [
        ("🚨", "Prioritaskan keselamatan", "Keselamatanmu adalah yang utama. Jika ada kekerasan fisik, segera cari bantuan profesional."),
        ("📞", "Hubungi layanan bantuan", "Jangan menghadapi ini sendirian. Hubungi hotline atau konselor yang bisa membantu rencana keselamatan."),
        ("🏠", "Rencana pelarian", "Siapkan tempat aman dan orang yang bisa kamu hubungi jika situasi memburuk. Simpan dokumen penting."),
        ("💚", "Kamu tidak sendirian", "Ingat, tidak ada alasan yang membenarkan kekerasan. Kamu berhak mendapatkan hubungan yang aman dan menghargai."),
    ]
}

# ============================================
# SESSION STATE
# ============================================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "screening_done" not in st.session_state:
    st.session_state.screening_done = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "name" not in st.session_state:
    st.session_state.name = ""
if "history" not in st.session_state:
    st.session_state.history = []

# ============================================
# NAVIGASI
# ============================================
def set_page(page_name):
    st.session_state.page = page_name
    st.rerun()

def next_question():
    if st.session_state.current_question < len(QUESTIONS) - 1:
        st.session_state.current_question += 1
        st.rerun()
    else:
        st.session_state.screening_done = True
        st.session_state.page = "result"
        st.rerun()

def prev_question():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1
        st.rerun()

def reset_screening():
    st.session_state.answers = {}
    st.session_state.current_question = 0
    st.session_state.screening_done = False
    st.session_state.page = "screening"
    st.rerun()

# ============================================
# FUNGSI AI
# ============================================
def calculate_score(answers):
    return sum(answers.values())

def get_category(score):
    max_score = len(QUESTIONS) * 3
    if score <= max_score * 0.33:
        return "low", "Risiko Rendah", "badge-low"
    elif score <= max_score * 0.66:
        return "medium", "Risiko Sedang", "badge-medium"
    else:
        return "high", "Risiko Tinggi", "badge-high"

def get_result_message(category):
    if category == "low":
        return "Hubunganmu Cukup Sehat!", "Berdasarkan jawabanmu, hubunganmu menunjukkan tanda-tanda yang sehat. Tetap jaga komunikasi dan batasan ya!"
    elif category == "medium":
        return "Perlu Diperhatikan", "Ada beberapa pola dalam hubunganmu yang perlu diwaspadai. Komunikasikan perasaanmu dan pertimbangkan untuk berbicara dengan orang terpercaya."
    else:
        return "Segera Dapatkan Bantuan", "Hubunganmu menunjukkan beberapa tanda kekerasan. Keselamatanmu adalah prioritas utama. Jangan ragu untuk mencari bantuan profesional."

def generate_ai_response(user_msg, history):
    try:
        import google.generativeai as genai
        api_key = st.secrets.get("GEMINI_API_KEY", None)
        if not api_key:
            return get_fallback_response(user_msg)
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")
        context = ""
        if st.session_state.screening_done:
            score = calculate_score(st.session_state.answers)
            _, cat_label, _ = get_category(score)
            context = f"\nKonteks: Pengguna baru saja menyelesaikan skrining dengan kategori {cat_label} (skor {score})."
        system_prompt = f"""Kamu adalah Safe Support AI. Aturan: empati, singkat (3-4 paragraf), nada hangat seperti kakak.
Jika ada kekerasan/ancaman, sertakan: hubungi 112 atau 119 (KemenPPPA).
{context}\nRiwayat:\n"""
        recent = history[-6:] if len(history) > 6 else history
        for msg in recent:
            role = "Pengguna" if msg["role"] == "user" else "AI"
            system_prompt += f"{role}: {msg['content']}\n"
        system_prompt += f"Pengguna: {user_msg}\nAI:"
        response = model.generate_content(system_prompt)
        return response.text.strip()
    except Exception:
        return get_fallback_response(user_msg)

def get_fallback_response(user_msg):
    msg_lower = user_msg.lower()
    if any(w in msg_lower for w in ["takut", "ancam", "pukul", "sakit", "darurat", "bunuh", "keras"]):
        return ("Saya sangat menyesal mendengar bahwa kamu merasa tidak aman.\n\n"
                "🚨 **Layanan Darurat:**\n• **112** - Call Center Darurat\n• **119** - Hotline KemenPPPA\n\n"
                "Kamu tidak sendiri. Ada orang yang peduli dan siap membantu.")
    if any(w in msg_lower for w in ["sedih", "kecewa", "putus", "bingung", "sendirian", "galau"]):
        return ("Terima kasih sudah berbagi. Merasa sedih itu wajar.\n\n"
                "Ceritakan lebih banyak agar saya bisa membantu. Ingat, mencari bantuan adalah tanda kekuatan.")
    return ("Terima kasih sudah mempercayai Safe Support AI. Saya di sini untuk mendengarkan.\n\n"
            "💡 *Catatan: Saya bukan pengganti konselor profesional.*")

# ============================================
# HEADER APLIKASI
# ============================================
st.markdown("""
<div class="app-header">
    <div class="app-logo">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L4 5V11C4 16.52 7.42 21.74 12 23C16.58 21.74 20 16.52 20 11V5L12 2Z" fill="#6B0F3A"/>
            <path d="M12 7C10.3 7 9 8.3 9 10C9 11.9 10.5 13 12 14.5C13.5 13 15 11.9 15 10C15 8.3 13.7 7 12 7Z" fill="#fff"/>
        </svg>
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="margin-left:-2px">
            <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z" fill="#E91E8C"/>
        </svg>
        <span>RK SafeSpace</span>
    </div>
    <div class="app-alert-btn">
        <svg width="15" height="15" viewBox="0 0 24 24" fill="none">
            <path d="M12 2L2 12L12 22L22 12L12 2Z" fill="#FFF0F5" stroke="#6B0F3A" stroke-width="2"/>
            <path d="M12 8V13" stroke="#6B0F3A" stroke-width="2" stroke-linecap="round"/>
            <circle cx="12" cy="16.5" r="1.2" fill="#6B0F3A"/>
        </svg>
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================
# HALAMAN: HOME
# ============================================
if st.session_state.page == "home":
    st.markdown("""
    <p class="greeting-text">Halo, Selamat Datang</p>
    <h2 class="heading-text">Mari pastikan hubunganmu aman &amp; nyaman.</h2>
    <div class="card-hero">
        <div class="card-hero-icon">
            <svg width="36" height="36" viewBox="0 0 24 24" fill="none">
                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z" fill="rgba(255,255,255,0.2)" stroke="rgba(255,255,255,0.6)" stroke-width="1.5"/>
            </svg>
        </div>
        <h3>Mulai Skrining</h3>
        <p>Ambil tes singkat untuk mengevaluasi kesehatan hubunganmu saat ini.</p>
    </div>
    """, unsafe_allow_html=True)

    # Marker untuk tombol Mulai Sekarang
    st.markdown('<span class="hero-btn-marker"></span>', unsafe_allow_html=True)
    if st.button("Mulai Sekarang →", key="btn_mulai_skrining", type="primary"):
        set_page("screening")

    # Grid Row 1
    st.markdown('<span class="grid-row-1"></span>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Hubungan Sehat", key="btn_healthy", use_container_width=True):
            set_page("healthy")
    with col2:
        if st.button("Riwayat Skrining", key="btn_history", use_container_width=True):
            set_page("history")

    # Grid Row 2
    st.markdown('<span class="grid-row-2"></span>', unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        if st.button("Bantuan & Konseling", key="btn_help", use_container_width=True):
            set_page("help")
    with col4:
        if st.button("Tentang Aplikasi", key="btn_about", use_container_width=True):
            set_page("about")

    st.markdown("""
    <div class="quote-box">
        <div class="quote-mark">&#8220;</div>
        <div class="quote-text">"Kamu berhak merasa aman, dihargai, dan dicintai tanpa rasa takut atau tekanan."</div>
    </div>
    """, unsafe_allow_html=True)

    # FAB button (reset)
    st.markdown('<span class="fab-marker"></span>', unsafe_allow_html=True)
    if st.button("✕", key="fab_reset_btn"):
        st.session_state.name = ""
        reset_screening()

# ============================================
# HALAMAN: SCREENING
# ============================================
elif st.session_state.page == "screening":
    q_idx = st.session_state.current_question
    total = len(QUESTIONS)
    progress = ((q_idx + 1) / total) * 100

    st.markdown(f"<p style='color:#E91E8C;font-weight:600;font-size:0.82rem;margin-bottom:4px;'>Safe Relationship Check</p>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
        <span style="font-weight:700;font-size:1rem;color:#1a1a1a;">Pertanyaan {q_idx+1} dari {total}</span>
        <span style="font-weight:600;font-size:0.85rem;color:#E91E8C;">{int(progress)}%</span>
    </div>
    <div class="progress-wrap"><div class="progress-fill" style="width:{progress}%"></div></div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <p style="font-size:1rem;font-weight:600;color:#1a1a1a;line-height:1.55;">"{QUESTIONS[q_idx]}"</p>
        <p style="font-size:0.75rem;color:#888;margin-top:10px;margin-bottom:0;">ⓘ Jawablah berdasarkan pengalaman Anda selama 6 bulan terakhir.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    for label, score in OPTIONS:
        is_selected = st.session_state.answers.get(q_idx) == score
        btn_type = "primary" if is_selected else "secondary"
        if st.button(label, key=f"opt_{q_idx}_{score}", use_container_width=True, type=btn_type):
            st.session_state.answers[q_idx] = score
            st.rerun()

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)
    col_prev, col_next = st.columns(2)
    with col_prev:
        if q_idx > 0:
            if st.button("← Sebelumnya", type="secondary", use_container_width=True):
                prev_question()
    with col_next:
        if q_idx in st.session_state.answers:
            if st.button("Selanjutnya →", type="primary", use_container_width=True):
                next_question()
        else:
            st.button("Selanjutnya →", type="primary", use_container_width=True, disabled=True)

# ============================================
# HALAMAN: RESULT
# ============================================
elif st.session_state.page == "result":
    score = calculate_score(st.session_state.answers)
    category, cat_label, badge_class = get_category(score)
    title, desc = get_result_message(category)

    st.markdown(f"""
    <div style="text-align:center;margin:24px 0 16px;">
        <div class="score-circle">
            <span class="score-label">SKOR KAMU</span>
            <span class="score-number">{score}</span>
        </div>
        <div class="badge {badge_class}">{cat_label}</div>
    </div>
    <h2 style="text-align:center;font-size:1.2rem;color:#1a1a1a;margin-bottom:6px;">{title}</h2>
    <p style="text-align:center;color:#666;font-size:0.85rem;margin-bottom:20px;line-height:1.5;">{desc}</p>
    <p style="color:#E91E8C;font-weight:700;font-size:0.78rem;letter-spacing:1px;margin-bottom:10px;">REKOMENDASI UNTUKMU</p>
    """, unsafe_allow_html=True)

    for icon, rec_title, rec_desc in RECOMMENDATIONS[category]:
        st.markdown(f"""
        <div class="rec-item">
            <div class="rec-icon">{icon}</div>
            <div class="rec-content"><h4>{rec_title}</h4><p>{rec_desc}</p></div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="disclaimer-banner">⚠️ <strong>Disclaimer:</strong> Aplikasi ini bukan alat diagnosis medis. Jika Anda dalam bahaya, hubungi layanan darurat.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Ulangi Skrining", type="secondary", use_container_width=True):
            reset_screening()
    with col2:
        if st.button("🤖 Safe Support AI", type="primary", use_container_width=True):
            set_page("chat")

    st.session_state.history.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "score": score,
        "category": cat_label
    })

# ============================================
# HALAMAN: CHAT AI
# ============================================
elif st.session_state.page == "chat":
    st.markdown("""
    <div style="background:#FFF3E0;border-left:3px solid #FF9800;border-radius:0 10px 10px 0;padding:8px 12px;margin-bottom:12px;font-size:0.8rem;color:#6B4C1E;">
        ⚠️ Safe Support AI bukan pengganti tenaga profesional kesehatan.
    </div>
    """, unsafe_allow_html=True)

    if not st.session_state.chat_history:
        st.markdown("""
        <div class="chat-ai">
            Halo! Aku Safe Support AI 💗 Ada yang ingin kamu ceritakan atau tanyakan hari ini?
            <div class="chat-meta">Safe Support AI • sekarang</div>
        </div>
        """, unsafe_allow_html=True)

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f'<div class="chat-user">{msg["content"]}<div class="chat-meta-white">Kamu • {msg.get("time","")}</div></div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-ai">{msg["content"]}<div class="chat-meta">Safe Support AI • {msg.get("time","")}</div></div>', unsafe_allow_html=True)

    col_input, col_send = st.columns([6, 1])
    with col_input:
        user_input = st.text_input("Tulis ceritamu di sini...", key="chat_input", label_visibility="collapsed")
    with col_send:
        send_clicked = st.button("➤", key="send_btn", use_container_width=True)

    if send_clicked and user_input.strip():
        st.session_state.chat_history.append({"role": "user", "content": user_input.strip(), "time": datetime.now().strftime("%H:%M")})
        ai_response = generate_ai_response(user_input.strip(), st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": ai_response, "time": datetime.now().strftime("%H:%M")})
        st.rerun()

# ============================================
# HALAMAN: HUBUNGAN SEHAT
# ============================================
elif st.session_state.page == "healthy":
    st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:6px;'>🌸 Ciri Hubungan yang Sehat</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666;font-size:0.85rem;margin-bottom:16px;'>Hubungan yang sehat dibangun atas fondasi saling menghargai dan mendukung.</p>", unsafe_allow_html=True)
    traits = [
        ("🗣️", "Komunikasi Terbuka", "Masing-masing pihak merasa aman untuk mengungkapkan perasaan, pikiran, dan kebutuhan tanpa takut dihakimi."),
        ("🤝", "Saling Percaya", "Tidak ada kebutuhan untuk memeriksa ponsel pasangan secara diam-diam atau melarang pasangan bertemu siapa pun."),
        ("🎯", "Respek terhadap Batasan", "Memahami bahwa setiap orang membutuhkan ruang pribadi, waktu sendiri, dan hak untuk menolak."),
        ("💪", "Dukungan Timbal Balik", "Mendukung impian dan pencapaian pasangan, bukan merasa terancam oleh kesuksesannya."),
        ("⚖️", "Kesetaraan", "Keputusan diambil bersama, tidak ada yang mendominasi atau merasa lebih berkuasa."),
        ("😊", "Kebahagiaan Bersama", "Hubungan seharusnya menambah kebahagiaan, bukan menjadi sumber stres atau ketakutan terus-menerus."),
    ]
    for icon, title, desc in traits:
        st.markdown(f'<div class="rec-item"><div class="rec-icon">{icon}</div><div class="rec-content"><h4>{title}</h4><p>{desc}</p></div></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="quote-box" style="margin-top:16px;">
        <div class="quote-mark">&#8220;</div>
        <div class="quote-text">"Cinta sejati tidak memiliki keinginan untuk menguasai, melainkan keinginan untuk membebaskan." — Bell Hooks</div>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# HALAMAN: BANTUAN & KONSELING
# ============================================
elif st.session_state.page == "help":
    st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:6px;'>🆘 Bantuan &amp; Konseling</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#666;font-size:0.85rem;margin-bottom:16px;'>Jangan ragu untuk menghubungi layanan berikut jika membutuhkan bantuan.</p>", unsafe_allow_html=True)
    contacts = [
        ("🚨", "Call Center Darurat", "112", "Layanan darurat nasional untuk keadaan genting."),
        ("👩", "Hotline KemenPPPA", "119", "Layanan perlindungan perempuan dan anak (24 jam)."),
        ("💬", "Layanan Konseling Psikolog", "1500-567", "Konseling gratis dari Kemenkes (sehat jiwa)."),
        ("🏥", "RS Jiwa / IGD Terdekat", "Cari di Google Maps", "Kunjungi IGD terdekat jika ada krisis mental."),
        ("📱", "Aplikasi Sehat Jiwa", "Download di Play/App Store", "Aplikasi resmi Kemenkes untuk kesehatan mental."),
    ]
    for icon, name, contact, desc in contacts:
        st.markdown(f"""
        <div class="card" style="margin-bottom:8px;">
            <div style="display:flex;align-items:center;gap:12px;margin-bottom:6px;">
                <span style="font-size:1.4rem;">{icon}</span>
                <div>
                    <p style="margin:0;font-weight:600;color:#1a1a1a;font-size:0.9rem;">{name}</p>
                    <p style="margin:0;font-size:1rem;font-weight:700;color:#E91E8C;">{contact}</p>
                </div>
            </div>
            <p style="margin:0;color:#666;font-size:0.82rem;">{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('<div class="disclaimer-banner">💚 Ingat: Mencari bantuan adalah tanda keberanian. Kamu berhak untuk merasa aman.</div>', unsafe_allow_html=True)

# ============================================
# HALAMAN: RIWAYAT
# ============================================
elif st.session_state.page == "history":
    st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:12px;'>📋 Riwayat Skrining</h2>", unsafe_allow_html=True)
    if not st.session_state.history:
        st.markdown("""
        <div class="card" style="text-align:center;padding:40px 16px;">
            <span style="font-size:3rem;">📭</span>
            <p style="color:#666;margin-top:12px;font-size:0.9rem;">Belum ada riwayat skrining.</p>
            <p style="color:#E91E8C;font-size:0.85rem;">Mulai skrining pertamamu dari menu Home!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        for item in reversed(st.session_state.history):
            badge = "badge-low" if "Rendah" in item["category"] else "badge-medium" if "Sedang" in item["category"] else "badge-high"
            st.markdown(f"""
            <div class="card" style="display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <p style="margin:0;font-size:0.75rem;color:#888;">{item["timestamp"]}</p>
                    <p style="margin:4px 0 0;font-weight:600;color:#1a1a1a;">Skor: {item["score"]}</p>
                </div>
                <div class="badge {badge}">{item["category"]}</div>
            </div>
            """, unsafe_allow_html=True)

# ============================================
# HALAMAN: TENTANG APLIKASI
# ============================================
elif st.session_state.page == "about":
    st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:12px;'>ℹ️ Tentang SafeSpace</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="line-height:1.7;color:#1a1a1a;font-size:0.88rem;"><strong>SafeSpace</strong> adalah aplikasi skrining mandiri berbasis web yang dirancang untuk membantu remaja mengenali pola hubungan pacaran yang sehat versus berisiko kekerasan.</p>
        <p style="line-height:1.7;color:#666;font-size:0.85rem;margin-top:8px;">Aplikasi ini <strong>bukan alat diagnosis</strong>, melainkan media edukasi, deteksi dini, dan pintu masuk ke bantuan lanjutan dari profesional atau layanan hotline.</p>
    </div>
    <h3 style="margin:16px 0 8px;font-size:1rem;color:#1a1a1a;">🔒 Privasi &amp; Keamanan</h3>
    <div class="card">
        <ul style="color:#666;line-height:1.9;padding-left:18px;font-size:0.85rem;">
            <li>Data skrining disimpan hanya di perangkat ini (local session).</li>
            <li>Tidak ada data pribadi yang dikirim ke server kami.</li>
            <li>Chat dengan AI bersifat anonim dan tidak disimpan secara permanen.</li>
            <li>Kamu bisa menggunakan nama samaran atau tanpa nama sama sekali.</li>
        </ul>
    </div>
    <div class="disclaimer-banner" style="margin-top:16px;">
        SafeSpace dan Safe Support AI <strong>bukan pengganti konseling profesional</strong>. Jika mengalami krisis, segera hubungi 112 atau 119.
    </div>
    <div class="card" style="text-align:center;margin-top:16px;">
        <p style="color:#666;font-size:0.85rem;">Dibuat dengan 💗 untuk keselamatan remaja Indonesia</p>
        <p style="color:#E91E8C;font-weight:600;margin-top:6px;font-size:0.9rem;">SafeSpace v1.0</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# BOTTOM NAVIGATION - Selalu tampil di semua halaman
# ============================================
st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

current = st.session_state.page
active_tab = "home"
if current in ["home"]:
    active_tab = "home"
elif current in ["screening", "result"]:
    active_tab = "screening"
elif current in ["healthy", "help", "about", "history"]:
    active_tab = "resources"
elif current == "chat":
    active_tab = "chat"

# Render active state markers SEBELUM nav section
st.markdown(f'<span class="nav-active-{active_tab}"></span>', unsafe_allow_html=True)

# Nav section marker - CSS akan posisikan container ini sebagai fixed bottom
st.markdown('<span class="nav-section-marker"></span>', unsafe_allow_html=True)

nav_cols = st.columns(4)
with nav_cols[0]:
    if st.button("Home", key="nav_home_btn", use_container_width=True):
        set_page("home")
with nav_cols[1]:
    if st.button("Screening", key="nav_screening_btn", use_container_width=True):
        set_page("screening")
with nav_cols[2]:
    if st.button("Resources", key="nav_resources_btn", use_container_width=True):
        set_page("healthy")
with nav_cols[3]:
    if st.button("Support AI", key="nav_chat_btn", use_container_width=True):
        set_page("chat")