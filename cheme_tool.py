import streamlit as st
import plotly.graph_objects as go
import time
import random
import math

# --- 1. PAGE CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="AzeoSpark: Team Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for that "Game" feel
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        border: 2px solid #4CAF50;
        height: 3em;
        font-size: 18px !important;
    }
    .big-font {
        font-size: 24px !important;
        font-weight: bold;
        color: #1E88E5;
    }
    .score-box {
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #FFC107;
        margin-bottom: 20px;
    }
    h1, h2, h3 {
        color: #0d47a1;
    }
    .stRadio > label {
        font-weight: bold;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)

# --- 2. SESSION STATE & TEAM SCORING ---
# Initialize Teams if not present
if 'teams' not in st.session_state:
    st.session_state.teams = {
        "Team Alpha": 0,
        "Team Beta": 0,
        "Team Gamma": 0,
        "Team Delta": 0
    }

# Function to add points
def add_points(team_name, points):
    st.session_state.teams[team_name] += points
    st.toast(f"⭐ {points} points to {team_name}!", icon="🎉")

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1253/1253696.png", width=100)
    st.title("⚡ AzeoSpark Teams")
    
    # LIVE SCOREBOARD
    st.markdown("### 🏆 Live Scoreboard")
    for team, score in st.session_state.teams.items():
        st.markdown(f"**{team}:** {score}")
    
    # Manual Score Adjustment (Host Control)
    with st.expander("👮 Host Controls (Adjust Score)"):
        team_adj = st.selectbox("Select Team", list(st.session_state.teams.keys()))
        points_adj = st.number_input("Points", value=0, step=5)
        if st.button("Update Score"):
            add_points(team_adj, points_adj)
            st.rerun()
            
    if st.button("🔄 Reset ALL Scores"):
        for t in st.session_state.teams:
            st.session_state.teams[t] = 0
        st.rerun()

    st.markdown("---")
    menu = st.radio("Select Round:", 
        ["🏠 Home", 
         "🏭 Round 1: Order of Magnitude", 
         "🚨 Round 2: The War Room", 
         "⚡ Round 3: Lightning Fire", 
         "❌ Round 4: Error or Eureka",
         "💰 Round 5: Engineering Auction",
         "🔔 Tie-Breaker: Ultimate Buzzer"])

# --- 4. GAME LOGIC ---

# === HOME PAGE ===
if menu == "🏠 Home":
    st.title("Welcome to AzeoSpark Team Edition! 🚀")
    st.markdown("""
    ### 🏁 Instructions for the Host
    1.  **Divide Students** into 4 Teams (Alpha, Beta, Gamma, Delta).
    2.  **Project this Screen** on the main board.
    3.  **Navigate** through the rounds using the sidebar.
    4.  **Scoring:** * Some games auto-score if you select the team first.
        * For verbal answers (like Buzzer round), use the **Host Controls** in the sidebar to award points manually.
    
    #### 🎮 The Rounds:
    * **🏭 Round 1: Order of Magnitude:** Guess the scale (Closest Team wins).
    * **🚨 Round 2: The War Room:** Crisis Management Scenarios.
    * **⚡ Round 3: Lightning Fire:** Rapid Yes/No questions.
    * **❌ Round 4: Error or Eureka:** Fact vs Myth.
    * **💰 Round 5: Engineering Auction:** Spend budget to fix problems.
    * **🔔 Tie-Breaker:** Sudden death questions.
    """)

# === ROUND 1: ORDER OF MAGNITUDE ===
elif menu == "🏭 Round 1: Order of Magnitude":
    st.header("🏭 Round 1: Order of Magnitude")
    st.markdown("**Instructions:** Ask the question. Teams write down their guess. The closest team gets +10 Points.")
    
    tab1, tab2, tab3 = st.tabs(["Question 1", "Question 2", "Question 3"])
    
    with tab1:
        st.subheader("💧 Water Usage")
        st.markdown("### How many LITERS of water does a refinery use per barrel of crude oil?")
        if st.button("Reveal Answer Q1"):
            st.success("✅ **Answer:** ~250 - 350 Liters")
            st.info("Award **10 points** to the closest team using Host Controls.")

    with tab2:
        st.subheader("🔥 Furnace Heat")
        st.markdown("### What is the temperature (°C) inside a Steam Cracker furnace?")
        if st.button("Reveal Answer Q2"):
            st.success("✅ **Answer:** ~850°C")
            st.info("Award **10 points** to the closest team using Host Controls.")

    with tab3:
        st.subheader("🏗️ Tower Height")
        st.markdown("### How tall (in meters) is the tallest distillation column in the world?")
        if st.button("Reveal Answer Q3"):
            st.success("✅ **Answer:** ~110 - 120 Meters")
            st.info("Award **10 points** to the closest team using Host Controls.")

# === ROUND 2: THE WAR ROOM ===
elif menu == "🚨 Round 2: The War Room":
    st.header("🚨 Round 2: The War Room")
    st.markdown("**Instructions:** Read the Alarm Scenario. Teams must pick the **ONE BEST ACTION**. (+20 Points)")
    
    active_team = st.selectbox("Select Team Answering:", list(st.session_state.teams.keys()), key="wr_team")
    
    scenario = st.radio("Select Scenario:", [
        "Scenario A: Reactor Overheating",
        "Scenario B: Toxic Gas Leak (H2S)",
        "Scenario C: Pump Making Loud Noise"
    ])
    
    st.divider()
    
    if scenario == "Scenario A: Reactor Overheating":
        st.error("🔥 **ALARM:** CSTR Temp rising fast! Cooling water failed.")
        st.markdown("**Options:**")
        st.markdown("1. Call Manager to discuss.")
        st.markdown("2. **Open Emergency Dump / Quench.**")
        st.markdown("3. Check the pump manual.")
        
        if st.button("Reveal Solution A"):
            st.success("✅ **Correct Action:** Open Emergency Dump / Quench.")
            if st.button(f"Award 20 pts to {active_team}"):
                add_points(active_team, 20)

    elif scenario == "Scenario B: Toxic Gas Leak (H2S)":
        st.error("☠️ **ALARM:** H2S Detector reads 15 PPM.")
        st.markdown("**Options:**")
        st.markdown("1. Hold breath and close valve.")
        st.markdown("2. **Evacuate Upwind & Don Breathing Apparatus.**")
        st.markdown("3. Run Downwind.")
        
        if st.button("Reveal Solution B"):
            st.success("✅ **Correct Action:** Evacuate Upwind & Don Breathing Apparatus.")
            if st.button(f"Award 20 pts to {active_team}"):
                add_points(active_team, 20)
                
    elif scenario == "Scenario C: Pump Making Loud Noise":
        st.warning("🔊 **ALARM:** Pump sounds like gravel (Cavitation).")
        st.markdown("**Options:**")
        st.markdown("1. Close Discharge Valve slightly.")
        st.markdown("2. **Check Suction Tank Level / Open Suction Valve.**")
        st.markdown("3. Increase Motor Speed.")
        
        if st.button("Reveal Solution C"):
            st.success("✅ **Correct Action:** Check Suction Tank Level (Fix NPSH).")
            if st.button(f"Award 20 pts to {active_team}"):
                add_points(active_team, 20)

# === ROUND 3: LIGHTNING FIRE ===
elif menu == "⚡ Round 3: Lightning Fire":
    st.header("⚡ Round 3: Lightning Fire (Rapid Fire)")
    st.markdown("**Instructions:** Host reads questions. Teams shout YES or NO. Host marks score manually.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Set 1")
        st.write("1. Sound travels faster in water than air? **(YES)**")
        st.write("2. Is Gold the most ductile metal? **(YES)**")
        st.write("3. Does Adiabatic mean Constant Temp? **(NO - Constant Heat)**")
        st.write("4. Is Diamond an isotope of Carbon? **(NO - Allotrope)**")
        st.write("5. Does water expand when it freezes? **(YES)**")
    
    with col2:
        st.markdown("### Set 2")
        st.write("6. Is pH of pure water 7? **(YES)**")
        st.write("7. Is Dry Ice solid CO2? **(YES)**")
        st.write("8. Is Mercury liquid at room temp? **(YES)**")
        st.write("9. Is 'Rotten Egg' smell Carbon Monoxide? **(NO - H2S)**")
        st.write("10. Is Natural Gas mostly Methane? **(YES)**")

# === ROUND 4: ERROR OR EUREKA ===
elif menu == "❌ Round 4: Error or Eureka":
    st.header("❌ Round 4: Error or Eureka")
    st.markdown("**Instructions:** Teams must decide if the statement is **ERROR (False)** or **EUREKA (True)**.")
    
    active_team_ee = st.selectbox("Select Team Answering:", list(st.session_state.teams.keys()), key="ee_team")
    
    stmt = st.selectbox("Select Statement:", [
        "1. Increasing pressure ALWAYS increases conversion in gas reactions.",
        "2. A Catalyst speeds reaction but doesn't change Equilibrium.",
        "3. Steam is an Ideal Gas.",
        "4. Viscosity of a GAS increases with Temperature."
    ])
    
    st.info(f"🗣️ Statement: **{stmt}**")
    
    if st.button("Reveal Answer"):
        if "1." in stmt:
            st.error("❌ **ERROR!** Only true if moles decrease.")
        elif "2." in stmt:
            st.success("✅ **EUREKA!** True.")
        elif "3." in stmt:
            st.error("❌ **ERROR!** Steam has intermolecular forces.")
        elif "4." in stmt:
            st.success("✅ **EUREKA!** True (Molecular collisions increase).")
            
    if st.button(f"Award 10 pts to {active_team_ee}"):
        add_points(active_team_ee, 10)

# === ROUND 5: ENGINEERING AUCTION ===
elif menu == "💰 Round 5: Engineering Auction":
    st.header("💰 Round 5: Engineering Auction")
    st.markdown("**Instructions:** Present the problem. Teams pick the **Best Solution**. (+30 Points)")
    
    prob = st.radio("Select Problem:", [
        "Problem 1: Hostel water smells bad.",
        "Problem 2: Boiler using too much fuel.",
        "Problem 3: Reaction is too slow."
    ])
    
    st.markdown("---")
    
    if prob == "Problem 1: Hostel water smells bad.":
        st.markdown("### 💧 Options:")
        st.markdown("A. Add Perfume")
        st.markdown("B. **Activated Carbon Filter**")
        st.markdown("C. Increase Turbidity")
        if st.button("Reveal P1"):
            st.success("✅ **B is Correct!** Activated Carbon removes odors.")

    elif prob == "Problem 2: Boiler using too much fuel.":
        st.markdown("### 🔥 Options:")
        st.markdown("A. **Thermal Insulation**")
        st.markdown("B. Increase Excess Air")
        st.markdown("C. Ignore Maintenance")
        if st.button("Reveal P2"):
            st.success("✅ **A is Correct!** Insulation stops heat loss.")

    elif prob == "Problem 3: Reaction is too slow.":
        st.markdown("### ⚗️ Options:")
        st.markdown("A. Reduce Concentration")
        st.markdown("B. Lower Temperature")
        st.markdown("C. **Add Catalyst**")
        if st.button("Reveal P3"):
            st.success("✅ **C is Correct!** Catalysts speed up rates.")

# === TIE-BREAKER ===
elif menu == "🔔 Tie-Breaker: Ultimate Buzzer":
    st.header("🔔 Ultimate Buzzer Round")
    st.markdown("### ⚡ Sudden Death! First team to shout wins.")
    
    q_buzz = st.selectbox("Select Question:", [
        "Q1: What is the 'King of Chemicals'?",
        "Q2: Which metal is used for Galvanizing?",
        "Q3: What does 'LPG' stand for?",
        "Q4: Is Distillation based on Boiling Point difference?"
    ])
    
    st.markdown(f"# ❓ {q_buzz}")
    
    if st.button("Show Answer"):
        if "Q1" in q_buzz: st.success("Sulfuric Acid (H2SO4)")
        if "Q2" in q_buzz: st.success("Zinc")
        if "Q3" in q_buzz: st.success("Liquefied Petroleum Gas")
        if "Q4" in q_buzz: st.success("YES")

# --- FOOTER ---
st.markdown("---")
st.markdown("*Created for AzeoSpark 2025 | Dept of Chemical Engineering*")
