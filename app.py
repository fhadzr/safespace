import streamlit as st
from datetime import datetime

# ============================================
# KONFIGURASI HALAMAN
# ============================================
st.set_page_config(
    page_title="SafeSpace - Safe Relationship Check",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>
    @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap");
    html, body, [class*="css"] { font-family: "Inter", sans-serif; }
    .main { background-color: #FFF8F9; }
    .app-header { display: flex; align-items: center; justify-content: space-between; padding: 1rem 0; margin-bottom: 1.5rem; }
    .app-logo { font-size: 1.5rem; font-weight: 700; color: #9D2B5E; display: flex; align-items: center; gap: 0.5rem; }
    .card { background: #FFFFFF; border-radius: 20px; padding: 1.5rem; margin-bottom: 1rem; border: 1px solid #F0E0E5; box-shadow: 0 2px 12px rgba(157, 43, 94, 0.06); }
    .card-hero { background: linear-gradient(135deg, #9D2B5E 0%, #7A1F48 100%); color: white; border-radius: 24px; padding: 2rem; margin-bottom: 1.5rem; }
    .progress-container { background: #F0E0E5; border-radius: 10px; height: 8px; margin: 1rem 0; overflow: hidden; }
    .progress-fill { background: linear-gradient(90deg, #FF6B9D, #9D2B5E); height: 100%; border-radius: 10px; transition: width 0.3s ease; }
    .score-circle { width: 180px; height: 180px; border-radius: 50%; background: white; border: 8px solid #FCE4EC; display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 0 auto 1rem; box-shadow: 0 4px 20px rgba(157, 43, 94, 0.1); }
    .score-number { font-size: 3rem; font-weight: 700; color: #9D2B5E; }
    .score-label { font-size: 0.9rem; color: #6B6B6B; }
    .badge { display: inline-block; padding: 0.4rem 1.2rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600; margin-bottom: 1rem; }
    .badge-low { background: #E8F5E9; color: #2E7D32; }
    .badge-medium { background: #FFF3E0; color: #EF6C00; }
    .badge-high { background: #FFEBEE; color: #C62828; }
    .recommendation-item { display: flex; gap: 1rem; padding: 1rem; background: white; border-radius: 16px; margin-bottom: 0.8rem; border: 1px solid #F0E0E5; align-items: flex-start; }
    .rec-icon { font-size: 1.5rem; flex-shrink: 0; }
    .rec-content h4 { margin: 0 0 0.3rem 0; font-size: 1rem; color: #2D2D2D; }
    .rec-content p { margin: 0; font-size: 0.85rem; color: #6B6B6B; line-height: 1.5; }
    .chat-message-ai { background: white; border-radius: 18px 18px 18px 4px; padding: 1rem; margin-bottom: 0.8rem; max-width: 85%; border: 1px solid #F0E0E5; font-size: 0.9rem; line-height: 1.6; }
    .chat-message-user { background: linear-gradient(135deg, #FF6B9D, #9D2B5E); color: white; border-radius: 18px 18px 4px 18px; padding: 1rem; margin-bottom: 0.8rem; margin-left: auto; max-width: 85%; font-size: 0.9rem; line-height: 1.6; }
    .chat-meta { font-size: 0.7rem; color: #6B6B6B; margin-top: 0.3rem; }
    .disclaimer-banner { background: linear-gradient(90deg, #FFF3E0, #FFE0B2); border-left: 4px solid #FF9800; padding: 0.8rem 1rem; border-radius: 0 12px 12px 0; margin-bottom: 1rem; font-size: 0.85rem; color: #6B4C1E; }
    .quote-box { background: white; border-radius: 16px; padding: 1.2rem; text-align: center; font-style: italic; color: #6B6B6B; border: 1px solid #F0E0E5; margin-top: 1rem; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container { padding-bottom: 100px !important; padding-top: 1rem !important; max-width: 480px; }
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

# ============================================
# REKOMENDASI PER KATEGORI
# ============================================
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
# FUNGSI SKORING
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

# ============================================
# INISIALISASI SESSION STATE
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

# ============================================
# FUNGSI NAVIGASI
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
        system_prompt = f"""Kamu adalah Safe Support AI, pendengar awal dan edukator untuk remaja tentang hubungan yang sehat. Kamu BUKAN psikolog atau pengganti profesional medis.\n
Aturan:
1. Berikan respons empatik, tidak menghakimi, dan singkat (maksimal 3-4 paragraf).
2. Jangan melabeli kondisi psikologis pengguna.
3. Jika ada indikasi kekerasan fisik/seksual/ancaman, SELALU sertakan info bantuan: Hubungi 112 (darurat) atau 119 (KemenPPPA).
4. Berikan informasi edukatif dan arahan, bukan nasihat klinis.
5. Nada: hangat, mendukung, seperti kakak yang peduli.
{context}
Riwayat percakapan terbaru:
"""
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
    if any(w in msg_lower for w in ["takut", "ancam", "pukul", "sakit", "darurat", "bunuh", "keras", "hajar"]):
        return ("Saya sangat menyesal mendengar bahwa kamu merasa tidak aman. Keselamatanmu adalah yang paling penting.\n\n"
                "🚨 **Layanan Darurat:**\n"
                "• **112** - Call Center Darurat\n"
                "• **119** - Hotline KemenPPPA (Perlindungan Perempuan & Anak)\n\n"
                "Kamu tidak sendiri dan tidak perlu menghadapi ini sendirian. Ada orang yang peduli dan siap membantu.")
    if any(w in msg_lower for w in ["sedih", "kecewa", "putus", "bingung", "sendirian", "galau", "stress"]):
        return ("Terima kasih sudah berbagi perasaanmu. Merasa sedih atau bingung itu wajar, terutama dalam hubungan.\n\n"
                "Apa yang kamu rasakan valid. Jika ingin, ceritakan lebih banyak agar saya bisa membantu memilah pikiranmu. "
                "Ingat, mencari bantuan adalah tanda kekuatan, bukan kelemahan.")
    return ("Terima kasih sudah mempercayai Safe Support AI. Saya di sini untuk mendengarkan.\n\n"
            "Jika kamu ingin berbagi lebih lanjut tentang hubunganmu atau butuh arahan, saya siap membantu. "
            "Kamu juga bisa membaca bagain 'Hubungan Sehat' untuk referensi.\n\n"
            "💡 *Catatan: Saya bukan pengganti konselor profesional. Jika butuh bantuan intensif, silakan hubungi layanan konseling di menu Bantuan & Konseling.*")

# ============================================
# HEADER APLIKASI
# ============================================
st.markdown("""
<div class="app-header">
    <div class="app-logo"><span>🛡️</span><span>SafeSpace</span></div>
    <div style="font-size: 1.2rem;">💎</div>
</div>
""", unsafe_allow_html=True)

# ============================================
# HALAMAN: HOME
# ============================================
if st.session_state.page == "home":
    if not st.session_state.name:
        st.session_state.name = st.text_input("Nama panggilan (opsional):", placeholder="Contoh: Ani", key="input_name")
    else:
        st.markdown("<p style='color: #6B6B6B; margin-bottom: 0;'>Halo, Selamat Datang</p>", unsafe_allow_html=True)
        st.markdown("<h2 style='margin-top: 0; color: #2D2D2D;'>Mari pastikan hubunganmu aman & nyaman.</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card-hero">
        <h3 style="margin: 0 0 0.5rem 0; font-size: 1.3rem;">Mulai Skrining</h3>
        <p style="margin: 0 0 1.2rem 0; opacity: 0.9; font-size: 0.95rem;">Ambil tes singkat untuk mengevaluasi kesehatan hubunganmu saat ini.</p>
        <div style="display: flex; align-items: center; gap: 0.5rem; font-weight: 600;"><span>💕</span></div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Mulai Sekarang →", type="primary", use_container_width=True):
        set_page("screening")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("💗\n\nHubungan Sehat", use_container_width=True):
            set_page("healthy")
    with col2:
        if st.button("📋\n\nRiwayat Skrining", use_container_width=True):
            set_page("history")
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🎧\n\nBantuan & Konseling", use_container_width=True):
            set_page("help")
    with col4:
        if st.button("ℹ️\n\nTentang Aplikasi", use_container_width=True):
            set_page("about")
    st.markdown("""
    <div class="quote-box">
        💬 "Kamu berhak merasa aman, dihargai, dan dicintai tanpa rasa takut atau tekanan."
    </div>
    """, unsafe_allow_html=True)

# ============================================
# HALAMAN: SCREENING
# ============================================
elif st.session_state.page == "screening":
    st.markdown("<p style='color: #9D2B5E; font-weight: 600; font-size: 0.9rem;'>Safe Relationship Check</p>", unsafe_allow_html=True)
    q_idx = st.session_state.current_question
    total = len(QUESTIONS)
    progress = ((q_idx + 1) / total) * 100
    st.markdown(f"<h3 style='margin: 0;'>Pertanyaan {q_idx + 1} dari {total}</h3>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: right; color: #9D2B5E; font-weight: 600; margin-top: -1.5rem;'>{int(progress)}%</p>", unsafe_allow_html=True)
    st.markdown(f'''<div class="progress-container"><div class="progress-fill" style="width: {progress}%"></div></div>''', unsafe_allow_html=True)
    st.markdown(f'''
    <div class="card">
        <h3 style="font-size: 1.2rem; line-height: 1.5; margin: 0; color: #2D2D2D;">"{QUESTIONS[q_idx]}"</h3>
        <p style="font-size: 0.8rem; color: #6B6B6B; margin-top: 0.8rem; margin-bottom: 0;">ⓘ Jawablah berdasarkan pengalaman Anda selama 6 bulan terakhir.</p>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown("<div style='margin-top: 1.5rem;'></div>", unsafe_allow_html=True)
    for label, score in OPTIONS:
        is_selected = st.session_state.answers.get(q_idx) == score
        if st.button(f"{label} — {score}", key=f"opt_{q_idx}_{score}", use_container_width=True, type="secondary" if not is_selected else "primary"):
            st.session_state.answers[q_idx] = score
            st.rerun()
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
    st.markdown(f'''
    <div style="text-align: center; margin: 2rem 0;">
        <div class="score-circle"><div class="score-label">SKOR KAMU</div><div class="score-number">{score}</div></div>
        <div class="badge {badge_class}">{cat_label}</div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown(f"<h2 style='text-align: center; margin-bottom: 0.5rem;'>{title}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; color: #6B6B6B; margin-bottom: 2rem;'>{desc}</p>", unsafe_allow_html=True)
    st.markdown("<p style='color: #9D2B5E; font-weight: 700; font-size: 0.9rem; letter-spacing: 1px; margin-bottom: 1rem;'>REKOMENDASI UNTUKMU</p>", unsafe_allow_html=True)
    for icon, rec_title, rec_desc in RECOMMENDATIONS[category]:
        st.markdown(f'''
        <div class="recommendation-item">
            <div class="rec-icon">{icon}</div>
            <div class="rec-content"><h4>{rec_title}</h4><p>{rec_desc}</p></div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown("""
    <div class="disclaimer-banner">
        ⚠️ <strong>Disclaimer:</strong> Aplikasi ini bukan alat diagnosis medis. Jika Anda dalam bahaya segera, hubungi layanan darurat setempat.
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Ulangi Skrining", type="secondary", use_container_width=True):
            reset_screening()
    with col2:
        if st.button("🤖 Safe Support AI", type="primary", use_container_width=True):
            set_page("chat")
    if "history" not in st.session_state:
        st.session_state.history = []
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
    <div style="background: #F3E5F5; border-radius: 12px; padding: 0.8rem 1rem; margin-bottom: 1rem; font-size: 0.85rem; color: #6B4C1E;">
        ⚠️ AI bukan pengganti tenaga profesional.
    </div>
    """, unsafe_allow_html=True)
    if not st.session_state.chat_history:
        st.markdown("""
        <div class="chat-message-ai">
            Halo! Aku Safe Support AI. Ada yang ingin kamu ceritakan atau tanyakan hari ini?
            <div class="chat-meta">Safe Support AI • just now</div>
        </div>
        """, unsafe_allow_html=True)
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f'''<div class="chat-message-user">{msg["content"]}<div class="chat-meta" style="color: rgba(255,255,255,0.7);">Kamu • {msg.get("time", "")}</div></div>''', unsafe_allow_html=True)
        else:
            st.markdown(f'''<div class="chat-message-ai">{msg["content"]}<div class="chat-meta">Safe Support AI • {msg.get("time", "")}</div></div>''', unsafe_allow_html=True)
    with st.container():
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
    st.markdown("<h2>🌸 Ciri Hubungan yang Sehat</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B6B6B; margin-bottom: 1.5rem;'>Hubungan yang sehat dibangun atas fondasi saling menghargai dan mendukung.</p>", unsafe_allow_html=True)
    traits = [
        ("🗣️", "Komunikasi Terbuka", "Masing-masing pihak merasa aman untuk mengungkapkan perasaan, pikiran, dan kebutuhan tanpa takut dihakimi."),
        ("🤝", "Saling Percaya", "Tidak ada kebutuhan untuk memeriksa ponsel pasangan secara diam-diam atau melarang pasangan bertemu siapa pun."),
        ("🎯", "Respek terhadap Batasan", "Memahami bahwa setiap orang membutuhkan ruang pribadi, waktu sendiri, dan hak untuk menolak."),
        ("💪", "Dukungan Timbal Balik", "Mendukung impian dan pencapaian pasangan, bukan merasa terancam oleh kesuksesannya."),
        ("⚖️", "Kesetaraan", "Keputusan diambil bersama, tidak ada yang mendominasi atau merasa lebih berkuasa."),
        ("😊", "Kebahagiaan Bersama", "Hubungan seharusnya menambah kebahagiaan, bukan menjadi sumber stres atau ketakutan terus-menerus."),
    ]
    for icon, title, desc in traits:
        st.markdown(f'''<div class="recommendation-item"><div class="rec-icon">{icon}</div><div class="rec-content"><h4>{title}</h4><p>{desc}</p></div></div>''', unsafe_allow_html=True)
    st.markdown("""<div class="quote-box" style="margin-top: 1.5rem;">💬 "Cinta sejati tidak memiliki keinginan untuk menguasai, melainkan keinginan untuk membebaskan." — Bell Hooks</div>""", unsafe_allow_html=True)

# ============================================
# HALAMAN: BANTUAN & KONSELING
# ============================================
elif st.session_state.page == "help":
    st.markdown("<h2>🆘 Bantuan & Konseling</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color: #6B6B6B; margin-bottom: 1.5rem;'>Jangan ragu untuk menghubungi layanan berikut jika membutuhkan bantuan.</p>", unsafe_allow_html=True)
    contacts = [
        ("🚨", "Call Center Darurat", "112", "Layanan darurat nasional untuk keadaan genting."),
        ("👩", "Hotline KemenPPPA", "119", "Layanan perlindungan perempuan dan anak (24 jam)."),
        ("💬", "Layanan Konseling Psikolog", "1500-567", "Konseling gratis dari Kemenkes (sehat jiwa)."),
        ("🏥", "RS Jiwa / IGD Terdekat", "Cari di Google Maps", "Kunjungi IGD terdekat jika ada krisis mental."),
        ("📱", "Aplikasi Sehat Jiwa", "Download di Play/App Store", "Aplikasi resmi Kemenkes untuk kesehatan mental."),
    ]
    for icon, name, contact, desc in contacts:
        st.markdown(f'''<div class="card" style="margin-bottom: 0.8rem;"><div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 0.5rem;"><span style="font-size: 1.5rem;">{icon}</span><div><h4 style="margin: 0; color: #2D2D2D;">{name}</h4><p style="margin: 0; font-size: 1.1rem; font-weight: 700; color: #9D2B5E;">{contact}</p></div></div><p style="margin: 0; color: #6B6B6B; font-size: 0.9rem;">{desc}</p></div>''', unsafe_allow_html=True)
    st.markdown("""<div class="disclaimer-banner">💚 Ingat: Mencari bantuan adalah tanda keberanian, bukan kelemahan. Kamu berhak untuk merasa aman.</div>""", unsafe_allow_html=True)

# ============================================
# HALAMAN: RIWAYAT
# ============================================
elif st.session_state.page == "history":
    st.markdown("<h2>📋 Riwayat Skrining</h2>", unsafe_allow_html=True)
    if "history" not in st.session_state or not st.session_state.history:
        st.markdown("""<div class="card" style="text-align: center; padding: 3rem 1rem;"><span style="font-size: 3rem;">📭</span><p style="color: #6B6B6B; margin-top: 1rem;">Belum ada riwayat skrining.</p><p style="color: #9D2B5E; font-size: 0.9rem;">Mulai skrining pertamamu dari menu Home!</p></div>""", unsafe_allow_html=True)
    else:
        for item in reversed(st.session_state.history):
            badge = "badge-low" if "Rendah" in item["category"] else "badge-medium" if "Sedang" in item["category"] else "badge-high"
            st.markdown(f'''<div class="card" style="display: flex; justify-content: space-between; align-items: center;"><div><p style="margin: 0; font-size: 0.8rem; color: #6B6B6B;">{item["timestamp"]}</p><p style="margin: 0.3rem 0 0 0; font-weight: 600; color: #2D2D2D;">Skor: {item["score"]}</p></div><div class="badge {badge}">{item["category"]}</div></div>''', unsafe_allow_html=True)

# ============================================
# HALAMAN: TENTANG APLIKASI
# ============================================
elif st.session_state.page == "about":
    st.markdown("<h2>ℹ️ Tentang SafeSpace</h2>", unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="line-height: 1.7; color: #2D2D2D;"><strong>SafeSpace</strong> adalah aplikasi skrining mandiri berbasis web yang dirancang untuk membantu remaja mengenali pola hubungan pacaran yang sehat versus berisiko kekerasan.</p>
        <p style="line-height: 1.7; color: #6B6B6B;">Aplikasi ini <strong>bukan alat diagnosis</strong>, melainkan media edukasi, deteksi dini, dan pintu masuk ke bantuan lanjutan dari profesional atau layanan hotline.</p>
    </div>
    <h3 style="margin-top: 1.5rem; color: #2D2D2D;">🔒 Privasi & Keamanan</h3>
    <div class="card">
        <ul style="color: #6B6B6B; line-height: 1.8; padding-left: 1.2rem;">
            <li>Data skrining disimpan hanya di perangkat ini (local session).</li>
            <li>Tidak ada data pribadi yang dikirim ke server kami.</li>
            <li>Chat dengan AI bersifat anonim dan tidak disimpan secara permanen.</li>
            <li>Kamu bisa menggunakan nama samaran atau tanpa nama sama sekali.</li>
        </ul>
    </div>
    <h3 style="margin-top: 1.5rem; color: #2D2D2D;">⚠️ Disclaimer</h3>
    <div class="disclaimer-banner">
        SafeSpace dan Safe Support AI <strong>bukan pengganti konseling profesional</strong> atau terapi. Jika Anda mengalami krisis atau kekerasan, segera hubungi layanan darurat (112) atau hotline KemenPPPA (119).
    </div>
    <div class="card" style="text-align: center; margin-top: 2rem;">
        <p style="color: #6B6B6B; font-size: 0.9rem;">Dibuat dengan 💗 untuk keselamatan remaja Indonesia</p>
        <p style="color: #9D2B5E; font-weight: 600; margin-top: 0.5rem;">SafeSpace v1.0</p>
    </div>
    """)

# ============================================
# BOTTOM NAVIGATION
# ============================================
st.markdown("<div style='height: 80px;'></div>", unsafe_allow_html=True)
current = st.session_state.page
nav_items = [("home", "🏠", "Home"), ("screening", "📝", "Screening"), ("healthy", "📚", "Resources"), ("chat", "🤖", "Support AI")]
cols = st.columns(4)
for i, (page, icon, label) in enumerate(nav_items):
    with cols[i]:
        if st.button(f"{icon}\n{label}", key=f"nav_{page}", use_container_width=True):
            set_page(page)