import streamlit as st
import random

# --- 1. PAGE CONFIG & FUN STYLING ---
st.set_page_config(
    page_title="AzeoSpark: FUN MODE",
    page_icon="🤪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS for BIG, COLORFUL, GAME-SHOW VIBES
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        height: 3.5em;
        font-size: 24px !important;
        font-weight: 900;
        border-radius: 15px;
        border: 4px solid #FF5722;
        background-color: #FFCCBC;
        color: #BF360C;
        transition: transform 0.1s;
    }
    .stButton>button:active {
        transform: scale(0.95);
    }
    .big-header {
        font-size: 50px;
        font-weight: 900;
        text-align: center;
        color: #1565C0;
        text-shadow: 3px 3px 0px #90CAF9;
        margin-bottom: 20px;
    }
    .fun-card {
        padding: 30px;
        background: #FFF9C4;
        border: 5px dashed #FBC02D;
        border-radius: 20px;
        text-align: center;
        font-size: 35px;
        font-weight: bold;
        color: #3E2723;
        margin: 20px 0;
    }
    .answer-box {
        padding: 20px;
        background-color: #C8E6C9;
        border: 4px solid #2E7D32;
        border-radius: 15px;
        color: #1B5E20;
        font-size: 28px;
        font-weight: bold;
        text-align: center;
        animation: pop 0.5s ease-out;
    }
    @keyframes pop {
        0% { transform: scale(0.8); opacity: 0; }
        100% { transform: scale(1); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)

# --- 2. TEAMS & SCOREBOARD ---
if 'teams' not in st.session_state:
    st.session_state.teams = {
        "Team Alpha 🦁": 0,
        "Team Beta 🐯": 0,
        "Team Gamma 🐻": 0,
        "Team Delta 🦅": 0
    }

if 'charades_word' not in st.session_state:
    st.session_state.charades_word = "???"

def add_points(team, points):
    st.session_state.teams[team] += points
    st.toast(f"🎉 +{points} to {team}!", icon="🎈")

# --- 3. SIDEBAR CONTROLS ---
with st.sidebar:
    st.title("🎮 CONTROLS")
    
    st.markdown("### 🏆 SCOREBOARD")
    for t, s in st.session_state.teams.items():
        st.markdown(f"**{t}** : `{s}`")
    
    with st.expander("👮 Manual Score Adjust"):
        t_sel = st.selectbox("Team", list(st.session_state.teams.keys()))
        p_val = st.number_input("Points", step=10, value=10)
        if st.button("➕ Add Points"):
            add_points(t_sel, p_val)
            st.rerun()

    if st.button("🗑️ RESET GAME"):
        for t in st.session_state.teams: st.session_state.teams[t] = 0
        st.rerun()

    st.divider()
    menu = st.radio("🚀 JUMP TO ROUND:", [
        "🏠 START",
        "🎭 R1: Dumb Charades (Physical)", 
        "🧠 R2: Guess the Scale", 
        "💣 R3: The 'Faaltu' Buzzer", 
        "💰 R4: Quick Auction", 
        "🏆 WINNER"
    ])

# --- 4. GAME CONTENT ---

# === HOME ===
if menu == "🏠 START":
    st.markdown("<div class='big-header'>🎉 AZEO SPARK: FUN MODE 🎉</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; font-size: 22px;'>
    <b>Welcome to the Craziest Engineering Game!</b><br><br>
    <b>The Rules:</b><br>
    1. 🔊 <b>LOUD</b> answers only.<br>
    2. 🏃 <b>FAST</b> pace.<br>
    3. 😂 <b>FUN</b> is mandatory.<br>
    </div>
    """, unsafe_allow_html=True)

# === ROUND 1: CHARADES (PHYSICAL) ===
elif menu == "🎭 R1: Dumb Charades (Physical)":
    st.markdown("<div class='big-header'>🎭 R1: ChemE Charades</div>", unsafe_allow_html=True)
    st.info("📢 **INSTRUCTION:** Call 1 student to the front. Show them the word on screen (Hide from audience!). They must ACT it out. (+20 Pts)")
    
    # List of fun words to act out
    words = [
        "Centrifugal Pump 🌀", 
        "Explosion 💥", 
        "Safety Helmet ⛑️", 
        "Leaky Pipe 💧", 
        "Lazy Engineer 😴", 
        "Bunsen Burner 🔥", 
        "Stuck Valve 🔧", 
        "Exam Stress 📚",
        "Distillation Column 🏗️",
        "Toxic Gas ☠️"
    ]
    
    col1, col2 = st.columns([1, 2])
    with col1:
        if st.button("🎲 NEW WORD"):
            st.session_state.charades_word = random.choice(words)
    
    with col2:
        if st.session_state.charades_word != "???":
            st.markdown(f"<div class='fun-card'>🤫 SHHH! ACT THIS:<br><br><span style='color:#D84315'>{st.session_state.charades_word}</span></div>", unsafe_allow_html=True)
            st.caption("(Only the actor should see this!)")
    
    st.markdown("---")
    st.write("**Who guessed it right?**")
    w_team = st.selectbox("Select Winner:", list(st.session_state.teams.keys()))
    if st.button("🏆 Award +20 Points"):
        add_points(w_team, 20)

# === ROUND 2: GUESS SCALE ===
elif menu == "🧠 R2: Guess the Scale":
    st.markdown("<div class='big-header'>🧠 R2: Big or Small?</div>", unsafe_allow_html=True)
    st.info("📢 **INSTRUCTION:** Teams write answer. Closest one wins! (+10 Pts)")
    
    q = st.selectbox("Select Question:", [
        "Q1: Water in a Refinery?", 
        "Q2: Furnace Temperature?", 
        "Q3: Tallest Tower?"
    ])
    
    st.markdown("---")
    
    if "Q1" in q:
        st.markdown("<div class='fun-card'>How much WATER to process 1 Barrel of Oil? 🛢️</div>", unsafe_allow_html=True)
        if st.button("👀 REVEAL ANSWER"):
            st.markdown("<div class='answer-box'>🛁 ~300 Liters<br>(About 2 Bathtubs!)</div>", unsafe_allow_html=True)

    elif "Q2" in q:
        st.markdown("<div class='fun-card'>Temperature inside a Steam Cracker Furnace? 🔥</div>", unsafe_allow_html=True)
        if st.button("👀 REVEAL ANSWER"):
            st.markdown("<div class='answer-box'>🌡️ ~850°C<br>(Pizza oven is only 250°C!)</div>", unsafe_allow_html=True)

    elif "Q3" in q:
        st.markdown("<div class='fun-card'>Height of the World's Tallest Distillation Column? 🏗️</div>", unsafe_allow_html=True)
        if st.button("👀 REVEAL ANSWER"):
            st.markdown("<div class='answer-box'>📏 ~110 Meters<br>(Tall as a 35-story building!)</div>", unsafe_allow_html=True)

# === ROUND 3: FAALTU BUZZER ===
elif menu == "💣 R3: The 'Faaltu' Buzzer":
    st.markdown("<div class='big-header'>💣 R3: The 'Faaltu' Buzzer</div>", unsafe_allow_html=True)
    st.info("📢 **INSTRUCTION:** First team to SHOUT the answer wins! (+5 Pts)")
    
    # List of Silly/Easy Questions
    qs = [
        ("Chemical Formula of Water?", "H2O (Duh!) 💧"),
        ("Can you drink Sulphuric Acid?", "NO! (You will die 💀)"),
        ("What is the 'King' of Chemicals?", "H2SO4 👑"),
        ("Is a Tomato a fruit or veg?", "Fruit! 🍅"),
        ("Full form of LPG?", "Liquefied Petroleum Gas ⛽"),
        ("Do Engineers sleep?", "No (It's a Myth) 😴"),
        ("Smell of Rotten Eggs?", "H2S (Hydrogen Sulfide) 🥚"),
        ("Symbol for Gold?", "Au (Aurum) 🥇"),
        ("Is Air a pure element?", "No! It's a mixture 🌬️")
    ]
    
    q_idx = st.number_input("Select Question Number:", 1, len(qs), 1) - 1
    
    st.markdown(f"<div class='fun-card'>❓ {qs[q_idx][0]}</div>", unsafe_allow_html=True)
    
    if st.button("🚨 SHOW ANSWER"):
        st.markdown(f"<div class='answer-box'>{qs[q_idx][1]}</div>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.write("**Fastest Team:**")
    fast_team = st.selectbox("Select Team:", list(st.session_state.teams.keys()), key="buzzer_team")
    if st.button("⚡ Give +5 Points"):
        add_points(fast_team, 5)

# === ROUND 4: AUCTION ===
elif menu == "💰 R4: Quick Auction":
    st.markdown("<div class='big-header'>💰 R4: Fix It Fast!</div>", unsafe_allow_html=True)
    st.info("📢 **INSTRUCTION:** Pick the Best Solution. (+30 Pts)")
    
    prob = st.radio("Select Problem:", ["P1: Smelly Water", "P2: High Bill", "P3: Slow Reaction"], horizontal=True)
    
    st.markdown("---")
    
    if "P1" in prob:
        st.markdown("<div class='fun-card'>🤢 Problem: Hostel Water Tastes Bad!</div>", unsafe_allow_html=True)
        st.write("A. Add Perfume")
        st.write("B. **Activated Carbon Filter**")
        st.write("C. Boil it for 10 hours")
        if st.button("✅ REVEAL FIX"):
            st.markdown("<div class='answer-box'>B: Activated Carbon (Traps the smell!)</div>", unsafe_allow_html=True)

    elif "P2" in prob:
        st.markdown("<div class='fun-card'>💸 Problem: Factory Electric Bill is Too High! (Heat Loss)</div>", unsafe_allow_html=True)
        st.write("A. **Thermal Insulation (Blanket)**")
        st.write("B. Open Windows")
        st.write("C. Fire the Accountant")
        if st.button("✅ REVEAL FIX"):
            st.markdown("<div class='answer-box'>A: Thermal Insulation (Keep heat inside!)</div>", unsafe_allow_html=True)

    elif "P3" in prob:
        st.markdown("<div class='fun-card'>🐢 Problem: Reaction is too Slow!</div>", unsafe_allow_html=True)
        st.write("A. Stare at it")
        st.write("B. Cool it down")
        st.write("C. **Add a Catalyst**")
        if st.button("✅ REVEAL FIX"):
            st.markdown("<div class='answer-box'>C: Catalyst (The Speed Booster!)</div>", unsafe_allow_html=True)
            
    st.markdown("---")
    st.write("**Who got it right?**")
    auc_team = st.selectbox("Select Team:", list(st.session_state.teams.keys()), key="auc_team")
    if st.button("💰 Give +30 Points"):
        add_points(auc_team, 30)

# === WINNER ===
elif menu == "🏆 WINNER":
    st.balloons()
    winner = max(st.session_state.teams, key=st.session_state.teams.get)
    st.markdown("<div class='big-header'>🏆 AND THE WINNER IS... 🏆</div>", unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style='text-align:center; padding:50px; background:gold; border-radius:30px; border: 5px solid orange; color:black; animation: pop 1s infinite alternate;'>
        <h1 style='font-size:80px; margin:0;'>{winner}</h1>
        <h2 style='font-size:40px;'>Score: {st.session_state.teams[winner]}</h2>
    </div>
    """, unsafe_allow_html=True)
