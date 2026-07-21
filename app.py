import streamlit as st
import os

# 1. Page Settings
st.set_page_config(
    page_title="🍒 SignBridge Suite - Bold Pinterest Edition",
    page_icon="🤟",
    layout="wide"
)

# 2. Bold Pinterest Custom CSS (High Contrast Cherry & Warm Cream)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap');
    
    /* Core layout background - Warm Pinterest Cream */
    .stApp {
        background-color: #F9F6F0;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }
    
    /* Bold Typography */
    h1, h2, h3 {
        font-family: 'Comfortaa', cursive !important;
        color: #1A1A1A !important;
        font-weight: 700;
    }
    
    /* Bold Cherry Red Badges */
    .cute-badge {
        background-color: #BD162C;
        color: #FFFFFF;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 700;
        padding: 6px 16px;
        border-radius: 8px;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 1px;
        display: inline-block;
        margin-bottom: 15px;
    }

    /* High Contrast Info Cards */
    .info-card {
        background-color: #FFFFFF;
        border: 2px solid #1A1A1A;
        border-radius: 16px;
        padding: 26px;
        margin-bottom: 25px;
        box-shadow: 6px 6px 0px #1A1A1A; /* Trendy brutalist/pinterest pop shadow */
    }
    
    /* Grid Flashcards Styling */
    .pinterest-card {
        background-color: #FFFFFF;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        border: 2px solid #EAE6DF;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
        transition: all 0.2s ease;
        margin-bottom: 20px;
        min-height: 190px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    
    .pinterest-card:hover {
        border-color: #BD162C;
        transform: translateY(-2px);
    }

    .card-title {
        font-family: 'Comfortaa', cursive;
        font-size: 26px;
        color: #BD162C;
        margin-bottom: 10px;
        font-weight: 700;
    }
    
    .card-desc {
        font-size: 14px;
        color: #333333;
        line-height: 1.5;
        font-weight: 500;
    }
    
    /* Custom style for main action buttons */
    .stButton>button {
        background-color: #BD162C !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 24px !important;
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. App Header Banner
st.markdown('<span class="cute-badge">❤️ SignBridge Premium</span>', unsafe_allow_html=True)
st.title("🤟 SignBridge: AI Sign Language Suite")
st.write("A bold, high-contrast visual workspace designed to make learning sign language intuitive, accessible, and elegant.")
st.markdown("---")

# 4. Content Navigation Tabs
tab1, tab2, tab3 = st.tabs(["📚 Flashcard Dictionary", "📷 Live Recognition", "ℹ️ Project Overview"])

# =========================================================
# TAB 1: ALL FLASHCARDS DICTIONARY
# =========================================================
with tab1:
    st.header("🔴 Visual Reference Library")
    
    category = st.radio(
        "Select Category to Browse:", 
        ["Alphabets (A-Z)", "Numerals (0-9)", "Essential Gestures"], 
        horizontal=True
    )
    st.markdown("<br>", unsafe_allow_html=True)
    
    alphabets_data = {
        "A": "Fist closed, thumb resting upright along the side of the index finger.",
        "B": "Open flat palm, fingers straight up together, thumb folded neatly over the palm.",
        "C": "Fingers and thumb curved deeply to trace a visible, clear crescent 'C' shape.",
        "D": "Index finger extended straight up; middle, ring, pinky touch the thumb tip to form a loop.",
        "E": "Fingers curled tightly down, tips resting lightly on top of a folded thumb.",
        "F": "Index finger and thumb tips touch to make a circle; middle, ring, pinky extend up.",
        "G": "Thumb and index finger pointing out horizontally, like measuring a tiny distance.",
        "H": "Index and middle fingers extended straight out sideways together, thumb tucked down.",
        "I": "Fist tightly closed with only the pinky finger extended straight upward.",
        "J": "Pinky finger extended up, tracing a small 'J' hook shape down through the air.",
        "K": "Index and middle fingers upright in a 'V'; thumb rests gently against the inside middle.",
        "L": "Index finger straight up, thumb straight out at a right angle creating an 'L'.",
        "M": "Fist closed with the thumb tucked deeply underneath the first three fingers.",
        "N": "Fist closed with the thumb tucked underneath the index and middle fingers.",
        "O": "All fingers curved downward, meeting the thumb tip to make a perfect circle.",
        "P": "An inverted 'K' sign pointing down; index straight down, middle outward, thumb resting on it.",
        "Q": "An inverted 'G' sign; thumb and index finger pointing straight down toward the ground.",
        "R": "Index and middle fingers crossed tightly over one another, remaining fingers down.",
        "S": "A tight, classic fist with the thumb wrapped firmly across the front of the fingers.",
        "T": "Fist closed with the thumb tucked vertically up between the index and middle fingers.",
        "U": "Index and middle fingers extended straight upward, pressed tightly together.",
        "V": "Index and middle fingers extended straight upward, spread apart in a clear 'V' shape.",
        "W": "Index, middle, and ring fingers spread apart and extended up; thumb holds the pinky.",
        "X": "Fist closed with the index finger curved into a rigid hook or question mark shape.",
        "Y": "Thumb and pinky finger extended completely outward; middle three fingers folded flat.",
        "Z": "Index finger extended, tracing a quick 'Z' pattern smoothly through the air."
    }

    numerals_data = {
        "0": "Fingers circled cleanly to meet the thumb, forming a round zero shape.",
        "1": "Index finger pointing straight up, palm facing inward toward your body.",
        "2": "Index and middle fingers extended upward in a spread 'V' position.",
        "3": "Thumb, index, and middle fingers all extended fully; ring and pinky flat.",
        "4": "Four fingers extended straight up and spread apart; thumb folded across the palm.",
        "5": "All five fingers completely extended and spread wide facing the camera.",
        "6": "Pinky finger tip touches the thumb tip; index, middle, ring fingers stay up.",
        "7": "Ring finger tip touches the thumb tip; index, middle, pinky fingers stay up.",
        "8": "Middle finger tip touches the thumb tip; index, ring, pinky fingers stay up.",
        "9": "Index finger tip touches the thumb tip; middle, ring, pinky fingers stay up."
    }

    gestures_data = {
        "🤟 I Love You (ILY)": "The iconic sign! Extend your pinky, index, and thumb completely, while folding your middle and ring fingers flat against your palm.",
        "👋 Hello": "Open flat hand facing forward, starting at your forehead and executing a gentle, elegant wave outward.",
        "🙏 Thank You": "Touch the fingertips of your flat, open hand to your lips, then move your hand down and outward towards the person gracefully.",
        "🤫 Please": "Place your right palm flat against the center of your chest and move it in a smooth, circular motion clockwise a few times."
    }

    if category == "Alphabets (A-Z)":
        cols = st.columns(4)
        idx = 0
        for letter, desc in alphabets_data.items():
            with cols[idx % 4]:
                st.markdown(f"""
                <div class="pinterest-card">
                    <div class="card-title">{letter}</div>
                    <div class="card-desc">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
            idx += 1

    elif category == "Numerals (0-9)":
        cols = st.columns(3)
        idx = 0
        for num, desc in numerals_data.items():
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="pinterest-card">
                    <div class="card-title">{num}</div>
                    <div class="card-desc">{desc}</div>
                </div>
                """, unsafe_allow_html=True)
            idx += 1

    elif category == "Essential Gestures":
        for title, desc in gestures_data.items():
            st.markdown(f"""
            <div class="info-card">
                <span class="cute-badge" style="background-color: #1A1A1A;">Interactive Sign</span>
                <h3 style="color: #BD162C !important;">{title}</h3>
                <p style="font-size: 15px; color: #1A1A1A; line-height: 1.6; font-weight: 500;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# TAB 2: LIVE WEBCAM TRANSLATOR INTERACTION
# =========================================================
with tab2:
    st.header("📹 Real-Time Webcam Translation")
    
    st.markdown("""
    <div class="info-card">
        <h3>How to Interact with Live Prediction:</h3>
        <ul style="color: #1A1A1A; font-size: 15px; line-height: 1.8; font-weight: 500;">
            <li>Position yourself in a well-lit area without blinding background glares.</li>
            <li>Present a <strong>single hand</strong> clearly in front of the lens.</li>
            <li>The system maps landmarks and outputs continuous translations immediately in a dynamic overlay window.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🚀 Launch Live SignBridge Camera"):
        with st.spinner("Initializing system models... Please prepare your gestures."):
            os.system("python inference.py")

# =========================================================
# TAB 3: PROJECT OVERVIEW & METRICS
# =========================================================
with tab3:
    st.header("📖 Project Summary & System Parameters")
    
    st.markdown("""
    <div class="info-card">
        <h3>Architecture Details</h3>
        <p style="font-size: 15px; color: #1A1A1A; line-height: 1.6; font-weight: 500;">
            <strong>SignBridge</strong> bridges communication gaps by leveraging optimized computer vision frameworks 
            and geometric coordinate vectors to interpret manual communication channels into explicit natural languages.
        </p>
        <hr style="border-top: 2px solid #1A1A1A;">
        <p style="font-size: 13px; color: #666666; font-weight: 600;">Developed as an educational engineering module under advanced machine learning parameters.</p>
    </div>
    """, unsafe_allow_html=True)