import streamlit as st
import time
import random

# --- 1. PAGE CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="AzeoSpark: Grand Finale",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for high-contrast, professional game look
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        border: 2px solid #1E88E5;
        height: 3em;
        font-size: 18px !important;
        background-color: #E3F2FD;
        color: #0D47A1;
    }
    .stButton>button:hover {
        background-color: #2196F3;
        color: white;
        border-color: #1565C0;
    }
    .big-header {
        font-size: 40px !important;
        font-weight: 900;
        color: #D32F2F;
        text-align: center;
        text-shadow: 2px 2px 4px #00000020;
    }
    .question-box {
        padding: 20px;
        background-color: #FFF3E0;
        border-left: 10px solid #FF9800;
        border-radius: 5px;
        font-size: 24px;
        font-weight: bold;
        color: #3E2723;
        margin-bottom: 20px;
    }
    .answer-box {
        padding: 15px;
        background-color: #E8F5E9;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        color: #1B5E20;
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SESSION STATE & TEAM SCORING ---
if 'teams' not in st.session_state:
    st.session_state.teams = {
        "Team Alpha": 0,
        "Team Beta": 0,
        "Team Gamma": 0,
        "Team Delta": 0
    }

def add_points(team_name, points):
    st.session_state.teams[team_name] += points
    st.toast(f"⭐ {points} points to {team_name}!", icon="🎉")

# --- 3. SIDEBAR CONTROLS ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1253/1253696.png", width=80)
    st.title("⚡ CONTROL PANEL")
    
    st.markdown("### 📊 Scoreboard")
    for team, score in st.session_state.teams.items():
        st.markdown(f"**{team}:** `{score}`")
    
    with st.expander("👮 Manual Score Adjust"):
        t_sel = st.selectbox("Team", list(st.session_state.teams.keys()))
        p_val = st.number_input("Points", value=0, step=5)
        if st.button("Apply Points"):
            add_points(t_sel, p_val)
            st.rerun()

    if st.button("🗑️ RESET GAME"):
        for t in st.session_state.teams:
            st.session_state.teams[t] = 0
        st.rerun()

    st.divider()
    menu = st.radio("Select Stage:", 
        ["🏠 LOBBY", 
         "🏭 R1: Guess the Scale", 
         "🚨 R2: War Room", 
         "❌ R3: Fact or Myth",
         "💰 R4: The Auction",
         "🌡️ R5: Heat Exchanger Hustle",
         "🔔 R6: Ultimate Buzzer",
         "🏆 CHAMPION"])

# --- 4. GAME CONTENT ---

# === LOBBY ===
if menu == "🏠 LOBBY":
    st.markdown("<div class='big-header'>AZEO SPARK 2026</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align: center; font-size: 20px;'>
    <b>Welcome Engineers!</b><br>
    The game is about to begin.<br><br>
    <b>THE RULES:</b><br>
    1. No shouting answers unless asked.<br>
    2. Host's decision is final.<br>
    3. Think like an Engineer!
    </div>
    """, unsafe_allow_html=True)

# === ROUND 1: SCALE ===
elif menu == "🏭 R1: Guess the Scale":
    st.header("🏭 Round 1: Order of Magnitude")
    st.info("📝 Teams write answer on whiteboard. Closest wins +10.")
    
    q = st.radio("Select Question:", ["Q1: Water Usage", "Q2: Furnace Temp", "Q3: Tower Height"], horizontal=True)
    
    st.markdown("---")
    
    if "Q1" in q:
        st.markdown("<div class='question-box'>How many LITERS of water does a refinery use to process 1 Barrel of Crude Oil?</div>", unsafe_allow_html=True)
        if st.button("👁️ REVEAL ANSWER"):
            st.markdown("<div class='answer-box'>✅ ~250 to 350 Liters</div>", unsafe_allow_html=True)

    elif "Q2" in q:
        st.markdown("<div class='question-box'>What is the temperature (°C) inside a Steam Cracker Furnace?</div>", unsafe_allow_html=True)
        if st.button("👁️ REVEAL ANSWER"):
            st.markdown("<div class='answer-box'>✅ ~850 °C</div>", unsafe_allow_html=True)

    elif "Q3" in q:
        st.markdown("<div class='question-box'>How tall (meters) is the tallest Distillation Column?</div>", unsafe_allow_html=True)
        if st.button("👁️ REVEAL ANSWER"):
            st.markdown("<div class='answer-box'>✅ ~110 to 120 Meters</div>", unsafe_allow_html=True)

# === ROUND 2: WAR ROOM ===
elif menu == "🚨 R2: War Room":
    st.header("🚨 Round 2: The War Room")
    st.info("📢 Pick the ONE safe action. (+20 Points)")
    
    active_team = st.selectbox("Correct Team:", list(st.session_state.teams.keys()))
    
    scen = st.selectbox("Scenario:", ["A: Reactor Runaway", "B: Toxic H2S Leak", "C: Pump Cavitation"])
    
    st.markdown("---")
    
    if "Reactor" in scen:
        st.markdown("<div class='question-box'>🔥 ALARM: Reactor Overheating! Cooling lost. What is Priority #1?</div>", unsafe_allow_html=True)
        st.write("A. Call Manager")
        st.write("B. Open Emergency Dump/Quench")
        st.write("C. Read Manual")
        if st.button("👁️ REVEAL SOLUTION"):
            st.markdown("<div class='answer-box'>✅ B: DUMP THE REACTOR! (Safety First)</div>", unsafe_allow_html=True)
            if st.button("Award +20"): add_points(active_team, 20)

    elif "H2S" in scen:
        st.markdown("<div class='question-box'>☠️ ALARM: Rotten Egg Smell (H2S). What is Priority #1?</div>", unsafe_allow_html=True)
        st.write("A. Find the leak")
        st.write("B. Evacuate Upwind + Breathing Apparatus")
        st.write("C. Spray Perfume")
        if st.button("👁️ REVEAL SOLUTION"):
            st.markdown("<div class='answer-box'>✅ B: EVACUATE UPWIND! (H2S kills)</div>", unsafe_allow_html=True)
            if st.button("Award +20"): add_points(active_team, 20)
            
    elif "Pump" in scen:
        st.markdown("<div class='question-box'>🔊 ALARM: Pump sounds like crushing rocks. What is Priority #1?</div>", unsafe_allow_html=True)
        st.write("A. Ignore it")
        st.write("B. Check Suction Tank Level")
        st.write("C. Increase Speed")
        if st.button("👁️ REVEAL SOLUTION"):
            st.markdown("<div class='answer-box'>✅ B: CHECK SUCTION! (It's Cavitation)</div>", unsafe_allow_html=True)
            if st.button("Award +20"): add_points(active_team, 20)

# === ROUND 3: FACT OR MYTH ===
elif menu == "❌ R3: Fact or Myth":
    st.header("❌ Round 3: Fact or Myth")
    st.info("📢 Is it Error (False) or Eureka (True)? (+10 Points)")
    
    t_ee = st.selectbox("Winner:", list(st.session_state.teams.keys()))
    
    fact = st.selectbox("Statement:", ["1. Boiling Water Freeze", "2. Catalyst Consumed", "3. Steam Ideal Gas", "4. Hot Air Heavy"])
    
    st.markdown("---")
    
    if "1." in fact:
        st.markdown("<div class='question-box'>\"We can freeze water just by boiling it (in a vacuum).\"</div>", unsafe_allow_html=True)
        if st.button("Reveal Truth"):
            st.markdown("<div class='answer-box'>✅ EUREKA (True)! Evaporative cooling.</div>", unsafe_allow_html=True)
            if st.button("Award +10"): add_points(t_ee, 10)
    
    elif "2." in fact:
        st.markdown("<div class='question-box'>\"A Catalyst gets used up/consumed in a reaction.\"</div>", unsafe_allow_html=True)
        if st.button("Reveal Truth"):
            st.markdown("<div class='answer-box'>❌ ERROR (False)! It remains unchanged.</div>", unsafe_allow_html=True)
            if st.button("Award +10"): add_points(t_ee, 10)
            
    elif "3." in fact:
        st.markdown("<div class='question-box'>\"Steam is an Ideal Gas.\"</div>", unsafe_allow_html=True)
        if st.button("Reveal Truth"):
            st.markdown("<div class='answer-box'>❌ ERROR (False)! Far from ideal.</div>", unsafe_allow_html=True)
            if st.button("Award +10"): add_points(t_ee, 10)
            
    elif "4." in fact:
        st.markdown("<div class='question-box'>\"Hot air is heavier than cold air.\"</div>", unsafe_allow_html=True)
        if st.button("Reveal Truth"):
            st.markdown("<div class='answer-box'>❌ ERROR (False)! Hot air rises (Lighter).</div>", unsafe_allow_html=True)
            if st.button("Award +10"): add_points(t_ee, 10)

# === ROUND 4: AUCTION ===
elif menu == "💰 R4: The Auction":
    st.header("💰 Round 4: Engineering Auction")
    st.info("📢 Pick the BEST solution. (+30 Points)")
    
    prob = st.radio("Problem:", ["P1: Bad Water", "P2: High Fuel Bill", "P3: Slow Reaction"], horizontal=True)
    st.markdown("---")
    
    if "P1" in prob:
        st.markdown("<div class='question-box'>Problem: Hostel drinking water smells bad.</div>", unsafe_allow_html=True)
        st.write("A. Add Perfume")
        st.write("B. Activated Carbon Filter")
        st.write("C. Stir it")
        if st.button("Reveal P1"):
            st.markdown("<div class='answer-box'>✅ B: Activated Carbon (Removes Odor)</div>", unsafe_allow_html=True)

    elif "P2" in prob:
        st.markdown("<div class='question-box'>Problem: Factory Fuel Bill is too high (Heat Loss).</div>", unsafe_allow_html=True)
        st.write("A. Thermal Insulation")
        st.write("B. Open Windows")
        st.write("C. Ignore it")
        if st.button("Reveal P2"):
            st.markdown("<div class='answer-box'>✅ A: Thermal Insulation (Stops Heat Loss)</div>", unsafe_allow_html=True)

    elif "P3" in prob:
        st.markdown("<div class='question-box'>Problem: Reaction is too slow.</div>", unsafe_allow_html=True)
        st.write("A. Add Water")
        st.write("B. Cool it")
        st.write("C. Add Catalyst")
        if st.button("Reveal P3"):
            st.markdown("<div class='answer-box'>✅ C: Add Catalyst (Speeds up rate)</div>", unsafe_allow_html=True)

# === ROUND 5: HEAT EXCHANGER HUSTLE ===
elif menu == "🌡️ R5: Heat Exchanger Hustle":
    st.header("🌡️ Round 5: Heat Exchanger Hustle")
    st.info("📢 Thermal Design Challenge! (+20 Points)")
    
    t_hx = st.selectbox("Correct Team:", list(st.session_state.teams.keys()), key="hx_team")
    
    hx_q = st.selectbox("Design Decision:", [
        "Case 1: Where to put Corrosive Acid?",
        "Case 2: Where to put High Pressure Steam?",
        "Case 3: Cleaning a Dirty Fluid"
    ])
    
    st.markdown("---")
    
    if "Case 1" in hx_q:
        st.markdown("<div class='question-box'>You have Corrosive Acid and Clean Water. Where does the Acid go?</div>", unsafe_allow_html=True)
        st.write("Option A: Shell Side")
        st.write("Option B: Tube Side")
        if st.button("Reveal Design 1"):
            st.markdown("<div class='answer-box'>✅ TUBE SIDE! (Cheaper to replace tubes than shell)</div>", unsafe_allow_html=True)
            if st.button("Award +20"): add_points(t_hx, 20)

    elif "Case 2" in hx_q:
        st.markdown("<div class='question-box'>You have High Pressure Steam (40 bar) and Low Pressure Oil. Where does Steam go?</div>", unsafe_allow_html=True)
        st.write("Option A: Shell Side")
        st.write("Option B: Tube Side")
        if st.button("Reveal Design 2"):
            st.markdown("<div class='answer-box'>✅ TUBE SIDE! (Tubes handle pressure better)</div>", unsafe_allow_html=True)
            if st.button("Award +20"): add_points(t_hx, 20)

    elif "Case 3" in hx_q:
        st.markdown("<div class='question-box'>Which TEMA type is best for a fluid that needs frequent mechanical cleaning?</div>", unsafe_allow_html=True)
        st.write("Option A: U-Tube (Type U)")
        st.write("Option B: Fixed Tubesheet (Type BEM)")
        st.write("Option C: Floating Head (Type AES)")
        if st.button("Reveal Design 3"):
            st.markdown("<div class='answer-box'>✅ C: Floating Head (Bundle removable + Straight tubes)</div>", unsafe_allow_html=True)
            if st.button("Award +20"): add_points(t_hx, 20)

# === ROUND 6: ULTIMATE BUZZER ===
elif menu == "🔔 R6: Ultimate Buzzer":
    st.header("🔔 Round 6: Ultimate Buzzer")
    st.info("📢 Sudden Death! First to shout wins.")
    
    buzz_q = st.selectbox("Question:", [
        "Q1: King of Chemicals?",
        "Q2: Metal for Galvanizing?",
        "Q3: Full form of LPG?",
        "Q4: Boiling Point Separation is called?"
    ])
    
    st.markdown(f"<div class='question-box'>{buzz_q}</div>", unsafe_allow_html=True)
    
    if st.button("REVEAL ANSWER"):
        if "Q1" in buzz_q: st.markdown("<div class='answer-box'>Sulfuric Acid (H2SO4)</div>", unsafe_allow_html=True)
        if "Q2" in buzz_q: st.markdown("<div class='answer-box'>Zinc</div>", unsafe_allow_html=True)
        if "Q3" in buzz_q: st.markdown("<div class='answer-box'>Liquefied Petroleum Gas</div>", unsafe_allow_html=True)
        if "Q4" in buzz_q: st.markdown("<div class='answer-box'>Distillation</div>", unsafe_allow_html=True)

# === CHAMPION ===
elif menu == "🏆 CHAMPION":
    st.balloons()
    st.markdown("<div class='big-header'>🏆 THE WINNER IS... 🏆</div>", unsafe_allow_html=True)
    
    scores = st.session_state.teams
    winner = max(scores, key=scores.get)
    max_score = scores[winner]
    
    st.markdown(f"""
    <div style='text-align:center; padding:50px; background:gold; border-radius:20px; color:black;'>
        <h1 style='font-size:80px;'>{winner}</h1>
        <h2>Score: {max_score}</h2>
    </div>
    """, unsafe_allow_html=True)
