import time
import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="RK SafeSpace",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# CSS GLOBAL — FIXED & CLEAN
# ============================================================
st.markdown("""
<style>
@import url("https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap");

html, body, [class*="css"] { font-family: "Plus Jakarta Sans", sans-serif !important; }
.stApp { background: #F3EEF1 !important; }

/* MAIN CONTAINER — Fixed width, proper padding for bottom nav */
.block-container {
    background: #FAFAFA !important;
    max-width: 520px !important;
    margin: 0 auto !important;
    padding: 20px 24px 120px 24px !important;
    border-radius: 0 !important;
    box-shadow: none !important;
    min-height: 100vh !important;
}
#MainMenu, footer, [data-testid="stToolbar"], header { visibility: hidden !important; }

/* ===================== SPLASH SCREEN ===================== */
.splash-wrap {
    position: fixed; inset: 0; z-index: 9999;
    background: radial-gradient(circle at 50% 35%, #FBDCE9 0%, #FCE9F1 40%, #FDF3F7 75%, #FFFFFF 100%);
    display: flex; align-items: center; justify-content: center;
}
.splash-inner { text-align: center; max-width: 420px; padding: 20px; }
.splash-icon-box {
    width: 100px; height: 100px; border-radius: 24px; background: #fff;
    display: flex; align-items: center; justify-content: center; margin: 0 auto 20px;
    box-shadow: 0 12px 34px rgba(107,15,58,0.16);
}
.splash-title { font-size: 1.5rem; font-weight: 800; color: #6B0F3A; margin-bottom: 8px; }
.splash-sub { font-size: .9rem; color: #555; margin-bottom: 18px; }
.splash-badge {
    display: inline-flex; align-items: center; gap: 6px; background: #fff;
    border: 1px solid #F5D0DF; border-radius: 50px; padding: 6px 14px;
    font-size: .75rem; font-weight: 600; color: #6B0F3A; margin-bottom: 12px;
}
.splash-progress { width: 180px; height: 4px; border-radius: 10px; background: #F5D6E4; margin: 0 auto 14px; overflow: hidden; }
.splash-progress-fill {
    height: 100%; width: 40%; border-radius: 10px;
    background: linear-gradient(90deg,#E91E8C,#6B0F3A);
    animation: splashLoad 2.1s ease-in-out infinite;
}
@keyframes splashLoad { 0% { margin-left: -40%; } 100% { margin-left: 100%; } }
.splash-caption { font-size: .7rem; letter-spacing: 1.5px; font-weight: 700; color: #C7157A; text-transform: uppercase; }

/* HEADER */
.app-header { display:flex; align-items:center; justify-content:space-between; margin-bottom:16px; padding-bottom:12px; border-bottom:1px solid #F0E8ED; }
.app-logo { display:flex; align-items:center; gap:6px; font-size:1.1rem; font-weight:700; color:#6B0F3A; }
.app-alert { width:32px; height:32px; border-radius:50%; background:#FFF0F5; border:1px solid #F5D0DF; display:flex; align-items:center; justify-content:center; font-size: 1rem; }
.app-greeting { font-size:.78rem; color:#888; }

/* BOTTOM NAV via JS classes */
.fixed-bottom-nav {
    position: fixed !important;
    bottom: 0 !important;
    left: 50% !important;
    transform: translateX(-50%) !important;
    width: 100% !important;
    max-width: 520px !important;
    background: #FAFAFA !important;
    padding: 10px 16px 16px 16px !important;
    box-shadow: 0 -4px 20px rgba(107,15,58,0.08) !important;
    border-top: 1px solid #F0E8ED !important;
    z-index: 9999 !important;
    margin: 0 !important;
}
.fixed-bottom-nav div[data-testid="column"] { padding: 0 4px !important; }

button.nav-bottom-btn {
    height: 60px !important; min-height: 60px !important;
    flex-direction: column !important;
    gap: 4px !important;
    border-radius: 12px !important;
    background: transparent !important;
    border: none !important;
    color: #888 !important;
    font-size: .7rem !important;
    padding: 6px 4px !important;
    box-shadow: none !important;
}
button.nav-bottom-btn-active {
    background: #FFF0F5 !important;
    color: #E91E8C !important;
    font-weight: 700 !important;
}

/* HERO CARD */
.card-hero { background:#6B0F3A; border-radius:16px; padding:16px 18px; margin-bottom:12px; position:relative; overflow:hidden; }
.card-hero h3 { font-size:1.1rem; font-weight:700; color:#fff; margin:0 0 4px 0; }
.card-hero p { font-size:0.78rem; color:rgba(255,255,255,0.85); line-height:1.4; max-width:320px; margin:0 0 10px 0; }
.card-hero-icon { position:absolute; top:14px; right:16px; opacity:0.6; font-size: 2rem; }

.section-label { color:#E91E8C; font-weight:700; font-size:.72rem; letter-spacing:1px; margin: 14px 0 8px; text-transform:uppercase; }

/* GRID BUTTONS via JS classes */
button.jelajahi-btn {
    height: auto !important; min-height: 80px !important;
    background:#fff !important; border:1.5px solid #F0E8ED !important; border-radius:16px !important;
    box-shadow:0 4px 12px rgba(107,15,58,.04) !important;
    font-size: .85rem !important; font-weight:600 !important; color:#333 !important;
    display:flex !important; flex-direction:column !important; white-space: pre-wrap !important;
    line-height:1.4 !important; padding:12px 10px !important; text-align:center !important;
    justify-content: center !important;
}
button.jelajahi-btn:hover {
    box-shadow:0 6px 16px rgba(107,15,58,.08) !important; transform:translateY(-2px); border-color:#E91E8C !important;
}

/* QUOTE */
.quote-box { background:#FFF6F9; border:1px solid #F5E0EA; border-radius:14px; padding:12px 14px; display:flex; align-items:flex-start; gap:10px; margin:10px 0 0; }
.quote-mark { font-family:Georgia,serif; font-size:2rem; font-weight:700; color:#E91E8C; line-height:.7; margin-top:2px; flex-shrink:0; }
.quote-text { font-size:.78rem; font-style:italic; color:#555; line-height:1.45; }

/* GENERIC ELEMENTS */
.card { background:#fff; border:1px solid #F0E8ED; border-radius:16px; padding:16px; margin-bottom:12px; }
.progress-wrap { background:#F0DDE6; border-radius:10px; height:6px; overflow:hidden; margin:6px 0 16px; }
.progress-fill { background:linear-gradient(90deg,#E91E8C,#6B0F3A); height:100%; border-radius:10px; }

/* SCORE DISPLAY — Fixed circular layout */
.score-box { text-align: center; padding: 16px 0 12px; }
.score-circle {
    width: 140px; height: 140px; border-radius: 50%; background: #fff;
    border: 5px solid #FCE4EC; display: flex; flex-direction: column;
    align-items: center; justify-content: center; margin: 0 auto 14px;
    box-shadow: 0 4px 16px rgba(107,15,58,.08);
}
.score-number { font-size: 2.6rem; font-weight: 700; color: #6B0F3A; line-height: 1; }
.score-label { font-size: .72rem; color: #888; letter-spacing: 1px; }

.badge { display:inline-block; padding:5px 16px; border-radius:50px; font-size:.82rem; font-weight:600; margin-bottom:10px; }
.badge-low { background:#E8F5E9; color:#2E7D32; }
.badge-medium { background:#FFF3E0; color:#EF6C00; }
.badge-high { background:#FFEBEE; color:#C62828; }

/* RECOMMENDATION LIST — Grid layout */
.rec-list { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-bottom: 24px; }
.rec-row { background:#fff; border:1px solid #F0E8ED; border-radius:16px; padding:14px 12px; display:flex; flex-direction:column; gap:8px; align-items:flex-start; text-align:left; box-shadow:0 2px 8px rgba(107,15,58,.02); transition: all 0.2s; }
.rec-row:hover { transform: translateY(-2px); box-shadow:0 4px 12px rgba(107,15,58,.06); border-color:#E91E8C; }
.rec-icon { font-size: 1.8rem; line-height: 1; flex-shrink: 0; }
.rec-content h4 { font-size:.85rem; font-weight:700; color:#1a1a1a; margin:0 0 4px 0; line-height:1.2; }
.rec-content p { font-size:.75rem; color:#666; line-height:1.4; margin:0; }

/* HELP LIST — Fixed for Resources page */
.help-list { background:#fff; border:1px solid #F0E8ED; border-radius:16px; overflow:hidden; margin-bottom:12px; }
.help-row { display:flex; gap:12px; padding:14px 16px; align-items:flex-start; border-bottom:1px solid #F5EFF2; }
.help-row:last-child { border-bottom:none; }
.help-icon { font-size: 1.5rem; flex-shrink: 0; line-height: 1; }
.help-name { margin:0; font-weight:600; color:#1a1a1a; font-size:.9rem; }
.help-contact { margin:2px 0 4px; font-size:1rem; font-weight:700; color:#E91E8C; }
.help-desc { margin:0; color:#666; font-size:.82rem; line-height:1.4; }

.disclaimer-banner { background:linear-gradient(90deg,#FFF3E0,#FFE0B2); border-left:4px solid #FF9800; padding:10px 14px; border-radius:0 12px 12px 0; margin-bottom:14px; font-size:.82rem; color:#6B4C1E; }

/* CHAT — Fixed gap issues */
.chat-window { max-height: 420px; overflow-y: auto; padding-right: 4px; margin-bottom: 12px; }
.chat-ai { background:#fff; border:1px solid #F0E8ED; border-radius:18px 18px 18px 4px; padding:12px 14px; margin-bottom:8px; max-width:85%; font-size:.88rem; line-height:1.5; color:#1a1a1a; }
.chat-user { background:linear-gradient(135deg,#E91E8C,#6B0F3A); color:#fff; border-radius:18px 18px 4px 18px; padding:12px 14px; margin-bottom:8px; margin-left:auto; max-width:85%; font-size:.88rem; line-height:1.5; }
.chat-meta { font-size:.7rem; color:#999; margin-top:4px; }
.chat-meta-w { font-size:.7rem; color:rgba(255,255,255,.65); margin-top:4px; }

/* NAME GATE */
.namegate-icon { width:80px; height:80px; border-radius:20px; background:#FFF0F5; display:flex; align-items:center; justify-content:center; margin:10px auto 16px; font-size: 2rem; }

/* GLOBAL BUTTON */
.stButton > button { font-family:"Plus Jakarta Sans",sans-serif !important; font-weight:600 !important; border-radius:50px !important; transition:all .2s !important; }
.stButton > button[kind="primary"] { background:#E91E8C !important; border:none !important; color:#fff !important; }
.stButton > button[kind="primary"]:hover { background:#C7157A !important; }
.stButton > button[kind="secondary"] { border:1.5px solid #E0D0D8 !important; color:#6B0F3A !important; background:#fff !important; }

.stTextInput > div > div { background:#fff !important; border-radius:50px !important; }
.stTextInput > div > div > input { background:#fff !important; border-radius:50px !important; border:1.5px solid #F0E8ED !important; font-family:"Plus Jakarta Sans",sans-serif !important; padding:10px 16px !important; color:#1a1a1a !important; }
.stTextInput > div > div > input::placeholder { color:#999 !important; }

/* Active nav button */
.nav-active button { background:#E91E8C !important; color:#fff !important; border:none !important; }

/* Bottom spacer to prevent nav overlap */
.bottom-spacer { height: 80px; }
</style>
""", unsafe_allow_html=True)

# ============================================================
# DATA
# ============================================================
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
    "Saya merasa tidak punya tempat untuk melarikan diri jika hubungan ini memburuk.",
]
OPTIONS = [("Sangat Tidak Setuju", 0), ("Tidak Setuju", 1), ("Setuju", 2), ("Sangat Setuju", 3)]
RECS = {
    "low": [
        ("🛡️","Tetap saling percaya","Kepercayaan adalah fondasi utama hubungan yang damai. Pertahankan komunikasi yang terbuka dan jujur."),
        ("💬","Komunikasi terbuka","Jangan ragu ungkapkan perasaanmu dengan cara yang baik. Diskusikan ekspektasi dan batasan bersama."),
        ("🔒","Menghargai privasi","Setiap individu butuh ruang pribadi untuk bertumbuh. Hormati batasan satu sama lain."),
        ("🌱","Terus berkembang","Dukung satu sama lain dalam mencapai impian dan pencapaian pribadi."),
    ],
    "medium": [
        ("⚠️","Waspadai tanda-tanda","Beberapa pola dalam hubunganmu mulai menunjukkan ketidakseimbangan. Perhatikan perubahan perilaku pasangan."),
        ("🗣️","Bicarakan batasan","Cobalah berdiskusi dengan pasangan tentang apa yang membuatmu tidak nyaman. Gunakan 'I-statement'."),
        ("👥","Jaga koneksi sosial","Jangan isolasi diri dari teman dan keluarga. Mereka adalah support system penting."),
        ("📚","Pelajari hubungan sehat","Memahami ciri-ciri hubungan yang sehat dan tidak sehat bisa membantumu mengevaluasi kembali."),
    ],
    "high": [
        ("🚨","Prioritaskan keselamatan","Keselamatanmu adalah yang utama. Jika ada kekerasan fisik, segera cari bantuan profesional."),
        ("📞","Hubungi layanan bantuan","Jangan menghadapi ini sendirian. Hubungi hotline atau konselor yang bisa membantu rencana keselamatan."),
        ("🏠","Rencana pelarian","Siapkan tempat aman dan orang yang bisa dihubungi jika situasi memburuk. Simpan dokumen penting."),
        ("💚","Kamu tidak sendirian","Ingat, tidak ada alasan yang membenarkan kekerasan. Kamu berhak mendapatkan hubungan yang aman."),
    ],
}

# ============================================================
# SESSION STATE
# ============================================================
for k, v in [("page","loading"),("answers",{}),("current_question",0),
             ("screening_done",False),("chat_history",[]),("history",[]),
             ("user_name",""),("next_after_name","screening")]:
    if k not in st.session_state:
        st.session_state[k] = v

# ============================================================
# HELPERS
# ============================================================
def set_page(p): st.session_state.page = p; st.rerun()

def go_to_screening():
    if st.session_state.user_name.strip():
        st.session_state.answers = {}
        st.session_state.current_question = 0
        st.session_state.screening_done = False
        set_page("screening")
    else:
        st.session_state.next_after_name = "screening"
        set_page("name_gate")

def next_q():
    if st.session_state.current_question < len(QUESTIONS)-1:
        st.session_state.current_question += 1; st.rerun()
    else:
        st.session_state.screening_done = True; set_page("result")

def prev_q():
    if st.session_state.current_question > 0:
        st.session_state.current_question -= 1; st.rerun()

def reset():
    st.session_state.answers = {}; st.session_state.current_question = 0
    st.session_state.screening_done = False; set_page("screening")

def calc_score(a): return sum(a.values())

def get_cat(s):
    m = len(QUESTIONS)*3
    if s <= m*0.33: return "low","Risiko Rendah","badge-low"
    elif s <= m*0.66: return "medium","Risiko Sedang","badge-medium"
    else: return "high","Risiko Tinggi","badge-high"

def get_msg(cat):
    msgs = {
        "low": ("Hubunganmu Cukup Sehat!","Berdasarkan jawabanmu, hubunganmu menunjukkan tanda-tanda yang sehat. Tetap jaga komunikasi dan batasan ya!"),
        "medium": ("Perlu Diperhatikan","Ada beberapa pola yang perlu diwaspadai. Komunikasikan perasaanmu dan pertimbangkan untuk berbicara dengan orang terpercaya."),
        "high": ("Segera Dapatkan Bantuan","Hubunganmu menunjukkan tanda kekerasan. Keselamatanmu adalah prioritas utama. Jangan ragu untuk mencari bantuan profesional."),
    }
    return msgs[cat]

import requests

def ai_response(msg, hist):
    try:
        key = st.secrets.get("GROQ_API_KEY", "")
        if not key: 
            print("[Safe Support AI] GROQ_API_KEY not found in secrets.")
            return fallback(msg)
        
        ctx = ""
        if st.session_state.screening_done:
            s = calc_score(st.session_state.answers)
            _, cl, _ = get_cat(s)
            ctx = f" Konteks skrining: {cl} (skor {s})."
        name_ctx = f" Nama pengguna: {st.session_state.user_name}." if st.session_state.user_name else ""
        
        sys_prompt = f"Kamu adalah Safe Support AI. Nada hangat, penuh empati, dan berikan jawaban yang singkat (maksimal 2-3 paragraf pendek). Jika mendeteksi tanda kekerasan atau ancaman, wajib sertakan 112 atau 119 (KemenPPPA).{ctx}{name_ctx}"
        
        messages = [{"role": "system", "content": sys_prompt}]
        for m in hist[-6:]:
            role = "user" if m["role"] == "user" else "assistant"
            messages.append({"role": role, "content": m["content"]})
        messages.append({"role": "user", "content": msg})

        headers = {
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama3-8b-8192", 
            "messages": messages,
            "temperature": 0.5,
            "max_tokens": 512
        }
        res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=10)
        
        if res.status_code == 200:
            return res.json()["choices"][0]["message"]["content"].strip()
        else:
            print(f"[Safe Support AI] Groq API Error: {res.status_code} - {res.text}")
            return fallback(msg)
            
    except Exception as e:
        print(f"[Safe Support AI] API call failed, using fallback: {e}")
        return fallback(msg)

def fallback(msg):
    ml = msg.lower()
    if any(w in ml for w in ["takut","ancam","pukul","sakit","darurat","bunuh"]):
        return "Saya sangat menyesal mendengar itu. Keselamatanmu yang utama.\n\n🚨 **Layanan Darurat:**\n• **112** - Call Center Darurat\n• **119** - Hotline KemenPPPA\n\nKamu tidak sendirian."
    if any(w in ml for w in ["sedih","kecewa","putus","bingung","sendirian","galau"]):
        return "Terima kasih sudah berbagi. Perasaanmu valid.\n\nCeritakan lebih banyak agar saya bisa membantu. Mencari bantuan adalah tanda kekuatan."
    return "Terima kasih sudah mempercayai Safe Support AI. Saya di sini untuk mendengarkan.\n\n💡 *Catatan: Saya bukan pengganti konselor profesional.*"

def centered(ratio=(1,4,1)):
    return st.columns(ratio)[1]

# ============================================================
# BOTTOM NAV COMPONENT
# ============================================================
def render_bottom_nav():
    page = st.session_state.page
    at = "home" if page == "home" else "screening" if page in ["screening","result"] else "chat" if page == "chat" else "resources"
    
    st.markdown('<span id="nav-container-marker"></span>', unsafe_allow_html=True)
    n1, n2, n3, n4 = st.columns(4)
    nav_defs = [
        (n1, "🏠", "Home", "home", "home"),
        (n2, "📝", "Screening", "screening", "screening"),
        (n3, "📚", "Resources", "healthy", "resources"),
        (n4, "🤖", "Support AI", "chat", "chat"),
    ]
    for col, icon, label, target, group in nav_defs:
        with col:
            active = at == group
            if active:
                st.markdown('<span class="nav-active-marker"></span>', unsafe_allow_html=True)
            else:
                st.markdown('<span class="nav-btn-marker"></span>', unsafe_allow_html=True)
            if st.button(f"{icon}\n{label}", key=f"nav_{target}", use_container_width=True):
                if target == "screening":
                    go_to_screening()
                else:
                    set_page(target)
                    
    # Inject JS to apply CSS classes (fallback for webviews/browsers without :has() support)
    components.html('''
    <script>
        const doc = window.parent.document;
        setTimeout(() => {
            const navMarker = doc.getElementById('nav-container-marker');
            if (navMarker) {
                const elContainer = navMarker.closest('div[data-testid="stElementContainer"]');
                if (elContainer && elContainer.nextElementSibling) {
                    elContainer.nextElementSibling.classList.add('fixed-bottom-nav');
                }
            }
            
            doc.querySelectorAll('.nav-btn-marker, .nav-active-marker').forEach(marker => {
                const elContainer = marker.closest('div[data-testid="stElementContainer"]');
                if (elContainer && elContainer.nextElementSibling) {
                    const btn = elContainer.nextElementSibling.querySelector('button');
                    if (btn) {
                        btn.classList.add('nav-bottom-btn');
                        if (marker.classList.contains('nav-active-marker')) {
                            btn.classList.add('nav-bottom-btn-active');
                        }
                    }
                }
            });
            
            doc.querySelectorAll('.card-btn-marker').forEach(marker => {
                const elContainer = marker.closest('div[data-testid="stElementContainer"]');
                if (elContainer && elContainer.nextElementSibling) {
                    const btn = elContainer.nextElementSibling.querySelector('button');
                    if (btn) btn.classList.add('jelajahi-btn');
                }
            });
        }, 100);
    </script>
    ''', height=0)

# ============================================================
# LOADING / SPLASH PAGE
# ============================================================
if st.session_state.page == "loading":
    st.markdown("""
    <div class="splash-wrap">
      <div class="splash-inner">
        <div class="splash-icon-box">🛡️</div>
        <div class="splash-title">Safe Relationship Check</div>
        <div class="splash-sub">Kenali hubunganmu, lindungi dirimu.</div>
        <div class="splash-badge">🔒 Data Anda terenkripsi & anonim</div>
        <div class="splash-progress"><div class="splash-progress-fill"></div></div>
        <div class="splash-caption">Menciptakan ruang aman...</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    time.sleep(2.4)
    st.session_state.page = "home"
    st.rerun()

# ============================================================
# NAME GATE
# ============================================================
elif st.session_state.page == "name_gate":
    st.markdown("""
    <div class="app-header">
      <div class="app-logo">
        <span style="font-size: 1.2rem;">🛡️</span>
        <span>RK SafeSpace</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    with centered((1,4,1)):
        st.markdown("""
        <div style="text-align:center;">
          <div class="namegate-icon">👤</div>
          <h2 style="font-size:1.15rem;color:#1a1a1a;margin-bottom:6px;">Siapa nama kamu?</h2>
          <p style="color:#666;font-size:.85rem;margin-bottom:18px;">Ini membantu kami menyapamu secara personal. Namamu hanya disimpan di sesi ini.</p>
        </div>
        """, unsafe_allow_html=True)

        name_input = st.text_input("Nama kamu", placeholder="Tulis namamu di sini...", label_visibility="collapsed", key="name_gate_input")

        cbtn = st.columns([1,1])
        with cbtn[0]:
            if st.button("← Kembali", type="secondary", use_container_width=True):
                set_page("home")
        with cbtn[1]:
            if st.button("Lanjutkan →", type="primary", use_container_width=True, disabled=not name_input.strip()):
                st.session_state.user_name = name_input.strip()
                st.session_state.answers = {}
                st.session_state.current_question = 0
                st.session_state.screening_done = False
                set_page(st.session_state.next_after_name)

    render_bottom_nav()

# ============================================================
# ALL OTHER PAGES
# ============================================================
else:
    # HEADER
    greeting = f'<span class="app-greeting">Halo, {st.session_state.user_name}!</span>' if st.session_state.user_name else '<span class="app-greeting">&nbsp;</span>'
    st.markdown(f"""
    <div class="app-header">
      <div class="app-logo">
        <span style="font-size: 1.2rem;">🛡️</span>
        <span>RK SafeSpace</span>
      </div>
      {greeting}
      <div class="app-alert">🔔</div>
    </div>
    """, unsafe_allow_html=True)

    # ============================================================
    # HOME
    # ============================================================
    if st.session_state.page == "home":
        st.markdown('<p style="font-size:.78rem;font-weight:500;color:#888;margin-bottom:2px;">Halo, Selamat Datang</p>', unsafe_allow_html=True)
        st.markdown('<h2 style="font-size:1.15rem;font-weight:700;color:#1a1a1a;line-height:1.25;margin-bottom:10px;">Mari pastikan hubunganmu aman & nyaman.</h2>', unsafe_allow_html=True)

        st.markdown("""
        <div class="card-hero">
          <div class="card-hero-icon">💗</div>
          <h3>Mulai Skrining</h3>
          <p>Ambil tes singkat untuk mengevaluasi kesehatan hubunganmu saat ini.</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Mulai Sekarang →", key="btn_start", type="primary", use_container_width=True):
            go_to_screening()

        st.markdown('<div class="section-label">JELAJAHI</div>', unsafe_allow_html=True)

        g1, g2 = st.columns(2)
        g3, g4 = st.columns(2)
        grid_items = [
            (g1, "btn_healthy", "🌸\nHubungan Sehat", "healthy"),
            (g2, "btn_history", "📋\nRiwayat Skrining", "history"),
            (g3, "btn_help", "🆘\nBantuan & Konseling", "help"),
            (g4, "btn_about", "ℹ️\nTentang Aplikasi", "about"),
        ]
        for col, key, label, target in grid_items:
            with col:
                st.markdown('<span class="card-btn-marker"></span>', unsafe_allow_html=True)
                if st.button(label, key=key, use_container_width=True):
                    set_page(target)

        st.markdown("""
        <div class="quote-box">
          <div class="quote-mark">"</div>
          <div class="quote-text">Kamu berhak merasa aman, dihargai, dan dicintai tanpa rasa takut atau tekanan.</div>
        </div>
        """, unsafe_allow_html=True)

        # Bottom spacer
        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # SCREENING
    # ============================================================
    elif st.session_state.page == "screening":
        with centered((1,4,1)):
            qi = st.session_state.current_question
            total = len(QUESTIONS)
            pct = (qi+1)/total*100

            st.markdown(f'<p style="color:#E91E8C;font-weight:600;font-size:.82rem;margin-bottom:4px;">Safe Relationship Check</p>', unsafe_allow_html=True)
            st.markdown(f"""
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px;">
              <span style="font-weight:700;font-size:1rem;color:#1a1a1a;">Pertanyaan {qi+1} dari {total}</span>
              <span style="font-weight:600;font-size:.85rem;color:#E91E8C;">{int(pct)}%</span>
            </div>
            <div class="progress-wrap"><div class="progress-fill" style="width:{pct}%"></div></div>
            """, unsafe_allow_html=True)
            st.markdown(f"""
            <div class="card">
              <p style="font-size:1rem;font-weight:600;color:#1a1a1a;line-height:1.5;margin:0;">{QUESTIONS[qi]}</p>
              <p style="font-size:.75rem;color:#888;margin-top:8px;margin-bottom:0;">ⓘ Jawablah berdasarkan pengalaman 6 bulan terakhir.</p>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)

            oc = st.columns(2)
            for i, (lbl, sc) in enumerate(OPTIONS):
                with oc[i % 2]:
                    t = "primary" if st.session_state.answers.get(qi) == sc else "secondary"
                    if st.button(lbl, key=f"o{qi}_{sc}", use_container_width=True, type=t):
                        st.session_state.answers[qi] = sc; st.rerun()

            st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
            cp, cn = st.columns(2)
            with cp:
                if qi > 0:
                    if st.button("← Sebelumnya", type="secondary", use_container_width=True): prev_q()
            with cn:
                if qi in st.session_state.answers:
                    if st.button("Selanjutnya →", type="primary", use_container_width=True): next_q()
                else:
                    st.button("Selanjutnya →", type="primary", use_container_width=True, disabled=True)

        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # RESULT — FIXED LAYOUT
    # ============================================================
    elif st.session_state.page == "result":
        with centered((1,4,1)):
            sc = calc_score(st.session_state.answers)
            cat, cl, bc = get_cat(sc)
            title, desc = get_msg(cat)

            # Score display
            st.markdown(f"""
            <div class="score-box">
              <div class="score-circle">
                <span class="score-label">SKOR KAMU</span>
                <span class="score-number">{sc}</span>
              </div>
              <div class="badge {bc}">{cl}</div>
            </div>
            <h2 style="text-align:center;font-size:1.15rem;color:#1a1a1a;margin-bottom:6px;">{title}</h2>
            <p style="text-align:center;color:#666;font-size:.85rem;margin-bottom:18px;line-height:1.5;">{desc}</p>
            <p style="color:#E91E8C;font-weight:700;font-size:.75rem;letter-spacing:1px;margin-bottom:10px;">REKOMENDASI UNTUKMU</p>
            """, unsafe_allow_html=True)

            # Recommendation list
            rec_rows = "".join(
                f'<div class="rec-row"><div class="rec-icon">{icon}</div><div class="rec-content"><h4>{rt}</h4><p>{rd}</p></div></div>'
                for icon, rt, rd in RECS[cat]
            )
            st.markdown(f'<div class="rec-list">{rec_rows}</div>', unsafe_allow_html=True)

            st.markdown('<div class="disclaimer-banner" style="margin-bottom: 24px;">⚠️ <strong>Disclaimer:</strong> Bukan alat diagnosis medis. Jika dalam bahaya, hubungi layanan darurat.</div>', unsafe_allow_html=True)

            cr, ca = st.columns(2)
            with cr:
                if st.button("🔄 Ulangi", type="secondary", use_container_width=True): reset()
            with ca:
                if st.button("🤖 Support AI", type="primary", use_container_width=True): set_page("chat")
                
            st.markdown('<div style="height: 16px;"></div>', unsafe_allow_html=True)

            # Save history
            if not st.session_state.history or st.session_state.history[-1].get("score") != sc or st.session_state.history[-1].get("timestamp","")[:16] != datetime.now().strftime("%Y-%m-%d %H:%M"):
                st.session_state.history.append({
                    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
                    "score": sc,
                    "category": cl,
                    "name": st.session_state.user_name,
                })

        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # CHAT AI — FIXED GAP
    # ============================================================
    elif st.session_state.page == "chat":
        with centered((1,4,1)):
            st.markdown('<div class="disclaimer-banner" style="font-size:.78rem;padding:8px 12px;">⚠️ Safe Support AI bukan pengganti tenaga profesional kesehatan.</div>', unsafe_allow_html=True)

            if not st.session_state.chat_history:
                bubbles = '<div class="chat-ai">Halo! Aku Safe Support AI 💗 Ada yang ingin kamu ceritakan atau tanyakan?<div class="chat-meta">Safe Support AI • sekarang</div></div>'
            else:
                parts = []
                for m in st.session_state.chat_history:
                    if m["role"] == "user":
                        parts.append(f'<div class="chat-user">{m["content"]}<div class="chat-meta-w">{st.session_state.user_name or "Kamu"} • {m.get("time","")}</div></div>')
                    else:
                        parts.append(f'<div class="chat-ai">{m["content"]}<div class="chat-meta">AI • {m.get("time","")}</div></div>')
                bubbles = "".join(parts)
            st.markdown(f'<div class="chat-window">{bubbles}</div>', unsafe_allow_html=True)

            user_msg_count = sum(1 for m in st.session_state.chat_history if m.get("role") == "user")
            
            if user_msg_count >= 2:
                st.markdown('<div class="disclaimer-banner" style="background:linear-gradient(90deg,#FFEBEE,#FFCDD2); border-left:4px solid #C62828; color:#B71C1C; margin-top: 12px;"><strong>Sesi cerita mencapai batas maksimal.</strong><br>Untuk perlindungan dan penanganan terbaik, kami sarankan Anda bertemu dengan tenaga profesional.<br>Silakan buka tab <b>Resources</b> atau segera hubungi:<br>🚨 <b>112</b> (Darurat)<br>🚨 <b>119</b> (KemenPPPA)</div>', unsafe_allow_html=True)
            else:
                with st.form(key="chat_form", clear_on_submit=True):
                    ci, cs = st.columns([6,1])
                    with ci:
                        ui = st.text_input("Tulis pesan...", key="chat_in", label_visibility="collapsed", placeholder="Tulis ceritamu di sini...")
                    with cs:
                        sent = st.form_submit_button("➤", use_container_width=True, type="primary")

                if sent and ui.strip():
                    st.session_state.chat_history.append({"role":"user","content":ui.strip(),"time":datetime.now().strftime("%H:%M")})
                    
                    user_msg_count += 1
                    if user_msg_count == 2:
                        resp = ai_response(ui.strip(), st.session_state.chat_history[:-1])
                        resp += "\n\n---\n⚠️ *Sesi ini mencapai batas. Jika kamu merasa terancam atau butuh dukungan segera, silakan hubungi **112 / 119** atau buka tab **Resources** untuk menemui tenaga profesional.*"
                    else:
                        resp = ai_response(ui.strip(), st.session_state.chat_history[:-1])
                        
                    st.session_state.chat_history.append({"role":"assistant","content":resp,"time":datetime.now().strftime("%H:%M")})
                    st.rerun()

        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # HUBUNGAN SEHAT
    # ============================================================
    elif st.session_state.page == "healthy":
        st.markdown("<h2 style='font-size:1.15rem;color:#1a1a1a;margin-bottom:4px;'>🌸 Ciri Hubungan yang Sehat</h2>", unsafe_allow_html=True)
        st.markdown("<p style='color:#666;font-size:.8rem;margin-bottom:12px;'>Hubungan yang sehat dibangun atas fondasi saling menghargai dan mendukung.</p>", unsafe_allow_html=True)
        
        items_html = "".join(
            f'<div class="rec-row"><div class="rec-icon">{icon}</div><div class="rec-content"><h4>{title}</h4><p>{desc}</p></div></div>'
            for icon, title, desc in [
                ("🗣️","Komunikasi Terbuka","Merasa aman mengungkapkan perasaan tanpa takut dihakimi."),
                ("🤝","Saling Percaya","Tidak ada kebutuhan memeriksa ponsel pasangan diam-diam."),
                ("🎯","Respek Batasan","Setiap orang berhak atas ruang pribadi dan hak menolak."),
                ("💪","Dukungan Timbal Balik","Mendukung impian pasangan, bukan merasa terancam."),
                ("⚖️","Kesetaraan","Keputusan diambil bersama, tidak ada yang mendominasi."),
                ("😊","Kebahagiaan Bersama","Menambah kebahagiaan, bukan menjadi sumber stres."),
            ]
        )
        st.markdown(f'<div class="rec-list">{items_html}</div>', unsafe_allow_html=True)
        st.markdown("""
        <div class="quote-box" style="margin-top:10px;padding:12px 14px;">
          <div class="quote-mark">"</div>
          <div class="quote-text">Cinta sejati tidak memiliki keinginan untuk menguasai, melainkan keinginan untuk membebaskan. — Bell Hooks</div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # BANTUAN & KONSELING — FIXED
    # ============================================================
    elif st.session_state.page == "help":
        st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:4px;'>🆘 Bantuan & Konseling</h2>", unsafe_allow_html=True)
        
        help_rows = "".join(
            f'<div class="help-row"><div class="help-icon">{icon}</div><div><p class="help-name">{name}</p><p class="help-contact">{contact}</p><p class="help-desc">{desc}</p></div></div>'
            for icon, name, contact, desc in [
                ("🚨","Call Center Darurat","112","Layanan darurat nasional untuk keadaan genting."),
                ("👩","Hotline KemenPPPA","119","Perlindungan perempuan & anak 24 jam."),
                ("💬","Konseling Kemenkes","1500-567","Konseling gratis (sehat jiwa)."),
                ("🏥","RS Jiwa / IGD","Cari di Google Maps","Kunjungi IGD terdekat jika ada krisis mental."),
                ("📱","Aplikasi Sehat Jiwa","Play/App Store","Aplikasi resmi Kemenkes untuk kesehatan mental."),
            ]
        )
        st.markdown(f'<div class="help-list">{help_rows}</div>', unsafe_allow_html=True)
        st.markdown('<div class="disclaimer-banner">💚 Ingat: Mencari bantuan adalah tanda keberanian. Kamu berhak untuk merasa aman.</div>', unsafe_allow_html=True)
        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # RIWAYAT
    # ============================================================
    elif st.session_state.page == "history":
        st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:12px;'>📋 Riwayat Skrining</h2>", unsafe_allow_html=True)
        if not st.session_state.history:
            st.markdown('<div class="card" style="text-align:center;padding:40px 16px;"><span style="font-size:2.5rem;">📭</span><p style="color:#666;margin-top:10px;font-size:.9rem;">Belum ada riwayat skrining.</p><p style="color:#E91E8C;font-size:.82rem;">Mulai skrining dari Home!</p></div>', unsafe_allow_html=True)
        else:
            for item in reversed(st.session_state.history):
                b = "badge-low" if "Rendah" in item["category"] else "badge-medium" if "Sedang" in item["category"] else "badge-high"
                who = f' — {item["name"]}' if item.get("name") else ""
                st.markdown(f'<div class="card" style="display:flex;justify-content:space-between;align-items:center;padding:12px 16px;"><div><p style="margin:0;font-size:.75rem;color:#888;">{item["timestamp"]}{who}</p><p style="margin:4px 0 0;font-weight:600;color:#1a1a1a;font-size:.9rem;">Skor: {item["score"]}</p></div><div class="badge {b}" style="margin:0;">{item["category"]}</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # ============================================================
    # TENTANG
    # ============================================================
    elif st.session_state.page == "about":
        st.markdown("<h2 style='font-size:1.2rem;color:#1a1a1a;margin-bottom:12px;'>ℹ️ Tentang SafeSpace</h2>", unsafe_allow_html=True)
        st.markdown("""
        <div class="card">
          <p style="line-height:1.6;color:#1a1a1a;font-size:.88rem;"><strong>SafeSpace</strong> adalah aplikasi skrining mandiri untuk membantu remaja mengenali pola hubungan pacaran yang sehat versus berisiko kekerasan.</p>
          <p style="line-height:1.6;color:#666;font-size:.82rem;margin-top:8px;">Aplikasi ini <strong>bukan alat diagnosis</strong>, melainkan media edukasi dan deteksi dini.</p>
        </div>
        <h3 style="margin:14px 0 8px;font-size:1rem;color:#1a1a1a;">🔒 Privasi</h3>
        <div class="card">
          <ul style="color:#666;line-height:1.8;padding-left:18px;font-size:.82rem;margin:0;">
            <li>Data skrining disimpan hanya di sesi ini (tidak permanen).</li>
            <li>Tidak ada data pribadi yang dikirim ke server kami.</li>
            <li>Chat dengan AI bersifat anonim.</li>
          </ul>
        </div>
        <div class="disclaimer-banner" style="margin-top:14px;">SafeSpace <strong>bukan pengganti konseling profesional</strong>. Jika dalam krisis, hubungi 112 atau 119.</div>
        <div class="card" style="text-align:center;margin-top:14px;padding:16px;">
          <p style="color:#666;font-size:.82rem;">Dibuat dengan 💗 untuk keselamatan remaja Indonesia</p>
          <p style="color:#E91E8C;font-weight:600;margin-top:6px;font-size:.9rem;">SafeSpace v1.0</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('<div class="bottom-spacer"></div>', unsafe_allow_html=True)

    # Render bottom nav for all pages
    render_bottom_nav()