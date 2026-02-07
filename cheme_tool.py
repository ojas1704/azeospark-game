import streamlit as st
import time
import random

# --- 1. PAGE CONFIGURATION & STYLING ---
st.set_page_config(
    page_title="AzeoSpark: Fun Edition",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for a clean, game-show look
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        border: 2px solid #4CAF50;
        height: 3.5em;
        font-size: 20px !important;
        background-color: #f0f2f6;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #e8f5e9;
        border-color: #2e7d32;
        transform: scale(1.02);
    }
    .big-font {
        font-size: 32px !important;
        font-weight: 800;
        color: #1565C0;
        text-align: center;
    }
    .score-card {
        padding: 15px;
        background: linear-gradient(135deg, #ffffff 0%, #f0f2f6 100%);
        border-radius: 15px;
        text-align: center;
        border: 2px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    .winner-banner {
        padding: 20px;
        background-color: #FFD700;
        color: #000;
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        border-radius: 20px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
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

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1253/1253696.png", width=80)
    st.title("⚡ AzeoSpark")
    
    st.markdown("### 🏆 Live Scores")
    for team, score in st.session_state.teams.items():
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; padding:5px; background:white; border-radius:5px; margin-bottom:5px;">
            <strong>{team}</strong> <span>{score} pts</span>
        </div>
        """, unsafe_allow_html=True)
    
    with st.expander("👮 Host Controls (Manual Score)"):
        team_adj = st.selectbox("Team", list(st.session_state.teams.keys()))
        points_adj = st.number_input("Points (+/-)", value=0, step=5)
        if st.button("Update"):
            add_points(team_adj, points_adj)
            st.rerun()
            
    if st.button("🗑️ Reset All Scores"):
        for t in st.session_state.teams:
            st.session_state.teams[t] = 0
        st.rerun()

    st.markdown("---")
    menu = st.radio("Select Round:", 
        ["🏠 Start Here", 
         "🏭 R1: Guess the Number", 
         "🚨 R2: Crisis Manager", 
         "⚡ R3: Rapid Fire (Yes/No)", 
         "❌ R4: Fact or Myth",
         "💰 R5: Engineering Auction",
         "🏆 Declare Winner"])

# --- 4. GAME LOGIC ---

# === HOME ===
if menu == "🏠 Start Here":
    st.markdown("<div class='big-font'>Welcome to AzeoSpark! 🚀</div>", unsafe_allow_html=True)
    st.markdown("""
    ### 👋 Host Instructions
    1.  **Teams:** Divide audience into **4 Teams** (Alpha, Beta, Gamma, Delta).
    2.  **Display:** Show this screen on the projector.
    3.  **Gameplay:** Use the sidebar to move between rounds.
    4.  **Scoring:** Click the buttons to award points automatically.
    
    ---
    ### 🎮 The Game Plan
    * **🏭 Round 1:** Guess the Number (Closest wins).
    * **🚨 Round 2:** Crisis Manager (Pick the safest action).
    * **⚡ Round 3:** Rapid Fire (Fast Yes/No questions).
    * **❌ Round 4:** Fact or Myth (Error vs Eureka).
    * **💰 Round 5:** Auction (Spend budget to fix problems).
    """)

# === ROUND 1: GUESS THE NUMBER ===
elif menu == "🏭 R1: Guess the Number":
    st.header("🏭 Round 1: Guess the Number")
    st.info("📝 **Rule:** Teams write down their guess. The closest team gets **10 Points**.")
    
    tab1, tab2, tab3 = st.tabs(["Question 1", "Question 2", "Question 3"])
    
    with tab1:
        st.subheader("💧 Water & Oil")
        st.markdown("### To process 1 Barrel of Crude Oil, how many LITERS of water does a refinery use?")
        st.caption("Hint: It's more than a bathtub (150L) but less than a swimming pool.")
        if st.button("👁️ Reveal Answer Q1"):
            st.success("✅ **Answer: ~250 to 350 Liters**")
            
    with tab2:
        st.subheader("🔥 It's Getting Hot")
        st.markdown("### Inside a massive furnace to make plastics (Steam Cracker), what is the temperature in °C?")
        st.caption("Hint: Lava is around 1200°C. Your oven is 200°C.")
        if st.button("👁️ Reveal Answer Q2"):
            st.success("✅ **Answer: ~850°C**")

    with tab3:
        st.subheader("🏗️ Skyscraper Towers")
        st.markdown("### How tall (in meters) is the tallest distillation column in the world?")
        st.caption("Hint: The Qutub Minar is 73 meters.")
        if st.button("👁️ Reveal Answer Q3"):
            st.success("✅ **Answer: ~110 to 120 Meters**")

# === ROUND 2: CRISIS MANAGER ===
elif menu == "🚨 R2: Crisis Manager":
    st.header("🚨 Round 2: Crisis Manager")
    st.info("📢 **Rule:** Read the scenario. Teams pick the **SAFE** action. (+20 Points)")
    
    active_team = st.selectbox("Which team answered correctly?", list(st.session_state.teams.keys()), key="wr_team")
    
    scenario = st.radio("Choose Scenario:", [
        "A: Reactor getting too hot!",
        "B: Rotten Egg Smell (Gas Leak)",
        "C: Pump making loud crashing noise"
    ])
    
    st.divider()
    
    if "Reactor" in scenario:
        st.error("🔥 **ALARM:** The Chemical Reactor is overheating rapidly! Cooling failed.")
        st.markdown("**What do you do FIRST?**")
        st.markdown("1. Call the manager to ask for permission.")
        st.markdown("2. **Open the Emergency Dump Valve (Stop the reaction).**")
        st.markdown("3. Read the instruction manual.")
        
        if st.button("Show Solution A"):
            st.success("✅ **Correct:** Dump the chemicals! Safety first, permission later.")
            if st.button(f"Give 20 pts to {active_team}"): add_points(active_team, 20)

    elif "Rotten Egg" in scenario:
        st.error("☠️ **ALARM:** Strong 'Rotten Egg' smell (H2S Gas) detected.")
        st.markdown("**What do you do FIRST?**")
        st.markdown("1. Hold your breath and try to find the leak.")
        st.markdown("2. **Run away (Upwind) & put on a breathing mask.**")
        st.markdown("3. Spray perfume to hide the smell.")
        
        if st.button("Show Solution B"):
            st.success("✅ **Correct:** Evacuate! H2S is deadly.")
            if st.button(f"Give 20 pts to {active_team}"): add_points(active_team, 20)
                
    elif "Pump" in scenario:
        st.warning("🔊 **ALARM:** The water pump sounds like it's crushing rocks.")
        st.markdown("**What do you do FIRST?**")
        st.markdown("1. Turn up the music so you can't hear it.")
        st.markdown("2. **Check if the tank feeding it is empty.**")
        st.markdown("3. Run the pump faster.")
        
        if st.button("Show Solution C"):
            st.success("✅ **Correct:** The pump is 'starving' (Cavitation). Check the supply.")
            if st.button(f"Give 20 pts to {active_team}"): add_points(active_team, 20)

# === ROUND 3: RAPID FIRE ===
elif menu == "⚡ R3: Rapid Fire (Yes/No)":
    st.header("⚡ Round 3: Rapid Fire")
    st.info("📢 **Rule:** Host reads the question. Team shouts YES or NO. (+5 Points)")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🟢 Easy Set")
        st.write("1. Does sound travel faster in water than air? **(YES)**")
        st.write("2. Is Gold a metal? **(YES)**")
        st.write("3. Does water expand when it freezes into ice? **(YES)**")
        st.write("4. Is the 'Lead' in a pencil actually Graphite? **(YES)**")
        st.write("5. Is air a pure element? **(NO - It's a mixture)**")
    
    with col2:
        st.markdown("### 🟡 Medium Set")
        st.write("6. Is pH of pure water 7? **(YES)**")
        st.write("7. Is Dry Ice made of frozen water? **(NO - Frozen CO2)**")
        st.write("8. Is Mercury liquid at room temperature? **(YES)**")
        st.write("9. Is 'Rotten Egg' smell Carbon Monoxide? **(NO - H2S)**")
        st.write("10. Is Natural Gas mostly Methane? **(YES)**")

# === ROUND 4: FACT OR MYTH ===
elif menu == "❌ R4: Fact or Myth":
    st.header("❌ Round 4: Fact or Myth?")
    st.info("📢 **Rule:** Is the statement **ERROR (False)** or **EUREKA (True)**? (+10 Points)")
    
    team_ee = st.selectbox("Winning Team:", list(st.session_state.teams.keys()), key="ee_team")
    
    stmt = st.selectbox("Select Statement:", [
        "1. We can freeze water just by boiling it (in a vacuum).",
        "2. A Catalyst gets used up in a reaction.",
        "3. Steam is an Ideal Gas.",
        "4. Hot air is heavier than cold air."
    ])
    
    st.markdown(f"### 🗣️ Statement:\n# \"{stmt[3:]}\"")
    
    if st.button("Reveal Truth"):
        if "1." in stmt:
            st.success("✅ **EUREKA (True)!** In a vacuum, evaporation cools water until it freezes.")
        elif "2." in stmt:
            st.error("❌ **ERROR (False)!** Catalysts speed up reactions but stay unchanged.")
        elif "3." in stmt:
            st.error("❌ **ERROR (False)!** Steam has forces between molecules.")
        elif "4." in stmt:
            st.error("❌ **ERROR (False)!** Hot air rises because it is lighter (less dense).")
            
    if st.button(f"Award 10 pts to {team_ee}"):
        add_points(team_ee, 10)

# === ROUND 5: AUCTION ===
elif menu == "💰 R5: Engineering Auction":
    st.header("💰 Round 5: Engineering Auction")
    st.info("📢 **Rule:** Choose the **BEST** solution to fix the problem. (+30 Points)")
    
    prob = st.radio("Select Problem:", [
        "P1: Hostel water smells bad.",
        "P2: Factory bill is too high (losing heat).",
        "P3: Chemical reaction is too slow."
    ])
    
    st.markdown("---")
    
    if "P1" in prob:
        st.markdown("### 💧 Options:")
        st.markdown("A. Add Perfume to the water.")
        st.markdown("B. **Use an Activated Carbon Filter.**")
        st.markdown("C. Stir the water really fast.")
        if st.button("Reveal P1 Answer"):
            st.success("✅ **B is Correct!** Carbon traps smells and chemicals.")

    elif "P2" in prob:
        st.markdown("### 🔥 Options:")
        st.markdown("A. **Wrap pipes in Thermal Insulation.**")
        st.markdown("B. Open the windows.")
        st.markdown("C. Ignore it.")
        if st.button("Reveal P2 Answer"):
            st.success("✅ **A is Correct!** Insulation keeps heat inside like a blanket.")

    elif "P3" in prob:
        st.markdown("### ⚗️ Options:")
        st.markdown("A. Add water.")
        st.markdown("B. Cool it down.")
        st.markdown("C. **Add a Catalyst.**")
        if st.button("Reveal P3 Answer"):
            st.success("✅ **C is Correct!** Catalysts make reactions faster.")

# === DECLARE WINNER ===
elif menu == "🏆 Declare Winner":
    st.header("🏆 The Ultimate Champion")
    
    # Find max score
    scores = st.session_state.teams
    winner = max(scores, key=scores.get)
    max_score = scores[winner]
    
    if st.button("🎉 REVEAL WINNER 🎉"):
        st.markdown(f"<div class='winner-banner'>👑 {winner} 👑</div>", unsafe_allow_html=True)
        st.markdown(f"<h2 style='text-align:center'>Score: {max_score}</h2>", unsafe_allow_html=True)
        st.balloons()
        
