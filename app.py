import streamlit as st

# --- Page Config & Custom CSS ---
# Imposta la configurazione base della pagina
st.set_page_config(page_title="Switching Costs Calculator", page_icon="🎮")

# Iniezione del CSS personalizzato per i colori richiesti
st.markdown("""
    <style>
    /* Colore testo principale */
    html, body, [class*="css"]  {
        color: #2c2c2c;
    }
    
    /* Colore primario per i titoli (Blu PlayStation) */
    h1, h2, h3 {
        color: #0101ba !important;
    }
    
    /* Colore secondario per i divisori (Giallo/Oro) */
    hr {
        border-bottom-color: #fcbf00 !important;
        border-bottom-width: 3px !important;
    }
    
    /* Stile per i messaggi di avviso/caption */
    .st-emotion-cache-1y4p8pa {
        color: #0101ba;
        font-weight: 500;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Banner Image ---
# Immagine di repertorio a tema PS5 da Unsplash (gratuita e sicura)
st.image("https://images.unsplash.com/photo-1606813907291-d86efa9b94db?q=80&w=2000&auto=format&fit=crop", use_column_width=True)

# --- Data Dictionaries ---
consoles = {
    "PS5 Standard - € 499.99": 499.99,
    "PS5 Digital - € 399.99": 399.99,
    "PS5 Slim Standard - € 549.99": 549.99,
    "PS5 Slim Digital - € 449.99": 449.99,
    "PS5 Pro - € 799.99": 799.99
}

accessories = {
    "Blu-Ray player - € 119.99": 119.99,
    "PS Controller - € 79.99": 79.99,
    "PlayStation Portal Remote Player - € 249.99": 249.99,
    "PULSE Wireless Headset - € 219.99": 219.99,
    "PULSE Elite Wireless Headset - € 149.99": 149.99
}

games = {
    "EA SPORTS FC 26 - € 79.99": 79.99,
    "GTA V - € 19.99": 19.99,
    "Minecraft - € 19.99": 19.99,
    "Baldur's Gate 3 - € 69.99": 69.99,
    "Elden Ring - € 59.99": 59.99,
    "Clair Obscur: Expedition 33 - € 49.99": 49.99,
    "God of War: Ragnarok - € 79.99": 79.99,
    "Marvel's Spiderman 2 - € 79.99": 79.99,
    "The Last of US: Parte I - € 79.99": 79.99,
    "The Last of US: Parte II - € 79.99": 79.99,
    "Hollow Knight: Silksong - € 19.99": 19.99,
    "DEATH STRANDING 2 - € 79.99": 79.99,
    "Red Dead Redemption 2 - € 59.99": 59.99,
    "Horizon Forbidden West - € 79.99": 79.99,
    "Gran Turismo 7 - € 79.99": 79.99,
    "Demon's Souls - € 79.99": 79.99
}

subscriptions = {
    "Essential - € 8.99/month": 8.99,
    "Extra - € 13.99/month": 13.99,
    "Premium - € 16.99/month": 16.99,
    "None": 0.00
}

# --- UI Layout ---
st.title("Switching Costs Calculator for a PS5 user")
st.markdown("##### *...who decides to swap their PS5 for an Xbox Series X costing € 499.99*")
st.divider()

# 1. Console Selection
st.markdown("### 🎮 Select the PS5 version you bought :")
st.caption("(You can select only one option)")
console_choice = st.selectbox(
    "console_sel", 
    options=list(consoles.keys()),
    label_visibility="collapsed",
    key="unique_console_key"
)

st.write("") 

# 2. Accessories Selection
st.markdown("### 🎧 Select the accessories you bought :")
st.caption("(You can select multiple options)")
acc_choices = st.multiselect(
    "acc_sel",
    options=list(accessories.keys()),
    label_visibility="collapsed",
    key="unique_acc_key"
)

st.write("")

# 3. Digital Games Selection
st.markdown("### 🛒 Select the videogames you bought on the Digital Store :")
st.caption("(You can select multiple options)")
digital_choices = st.multiselect(
    "digital_sel",
    options=list(games.keys()),
    label_visibility="collapsed",
    key="unique_digital_key"
)

st.write("")

# 4. Physical Games Selection (Conditional Logic)
show_physical = False
if console_choice in ["PS5 Standard - € 499.99", "PS5 Slim Standard - € 549.99", "PS5 Pro - € 799.99"]:
    show_physical = True

for acc in acc_choices:
    if "Blu-Ray player" in acc:
        show_physical = True

# Absolute override for original Digital edition
if console_choice == "PS5 Digital - € 399.99":
    show_physical = False

physical_choices = []
if show_physical:
    st.markdown("### 💿 Select the videogames you bought on physical version and you are gonna re-sell :")
    st.markdown(f"<span style='color: #0101ba; font-weight: bold;'>**You can only select this option if your console has the Blu-Ray Player**</span>", unsafe_allow_html=True)
    st.caption("(You can select multiple options)")
    physical_choices = st.multiselect(
        "physical_sel",
        options=list(games.keys()),
        label_visibility="collapsed",
        key="unique_physical_key"
    )
    st.write("")

# 5. Subscription Selection
st.markdown("### 💳 Select the type of active subscription at the moment of changing asset:")
st.caption("(You can select only one option)")
sub_choice = st.selectbox(
    "sub_sel",
    options=list(subscriptions.keys()),
    label_visibility="collapsed",
    key="unique_sub_key"
)

st.write("")

# 6. Subscription Months Remaining Slider
st.markdown("### ⏳ Months of subscription remaining at the moment of changing asset:")
st.caption("(Select a value from 0 to 12)")
months_remaining = st.slider(
    "slider_sel",
    min_value=0, max_value=12, value=0, step=1,
    label_visibility="collapsed",
    key="unique_slider_key"
)

st.divider()

# --- Calculations ---
console_cost = consoles[console_choice]
acc_cost_sum = sum(accessories[a] for a in acc_choices)
digital_games_sum = sum(games[g] for g in digital_choices)

X = 0.0
if show_physical:
    X = 0.7 * sum(games[g] for g in physical_choices)

Y = subscriptions[sub_choice] * months_remaining

total_switching_cost = 499.99 + (0.6 * console_cost) + (0.7 * acc_cost_sum) + digital_games_sum + X + Y

# --- Final Display Result ---
st.markdown("## The switching costs that would be incurred in the event of an asset change, would be :")

# Riquadro personalizzato per il risultato finale usando i tuoi tre colori
st.markdown(
    f"""
    <div style="
        background-color: #2c2c2c; 
        padding: 30px; 
        border-radius: 15px; 
        border: 4px solid #fcbf00; 
        text-align: center; 
        box-shadow: 4px 4px 15px rgba(0,0,0,0.3);
        margin-top: 20px;
        margin-bottom: 20px;">
        <h1 style='font-size: 4rem; color: #fcbf00 !important; margin: 0; text-shadow: 2px 2px #0101ba;'>
            € {total_switching_cost:.2f}
        </h1>
    </div>
    """, 
    unsafe_allow_html=True
)

st.divider()

# --- Display Disclaimers ---
st.caption("**Calculation Specifications:**")
st.caption("""
- Standard non-discounted prices from the official PlayStation site (05/26) have been reported.
- It was calculated that the purchased console is sold at 40% of its full price.
- It was calculated that the accessories are sold at 30% of their full price.
- It was calculated that the physical videogames are sold at 30% of their full price.
- It was calculated that, as an alternative, an Xbox Series X console is purchased at the price of € 499.99.
- The switching costs were calculated as the direct sum of the amounts spent on purchases, net of the resale of assets at a lower price.
- Possible bundles, discounts, network costs (loss of network effects), learning costs, non-recoverable virtual currencies, and other possible incalculable costs have been ignored.
""")
