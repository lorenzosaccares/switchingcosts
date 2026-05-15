import streamlit as st

# --- Data Dictionaries ---
# Storing the exact options and their corresponding float prices for calculation
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
    "PULSE Wireless Headset - € 219.99": 219.99, # Translated "Auricolari"
    "PULSE Elite Wireless Headset - € 149.99": 149.99 # Translated "Auricolari"
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
    # Added a few extra famous PS5 titles
    "Horizon Forbidden West - € 79.99": 79.99,
    "Gran Turismo 7 - € 79.99": 79.99,
    "Demon's Souls - € 79.99": 79.99
}

subscriptions = {
    "Essential": 8.99,
    "Extra": 13.99,
    "Premium": 16.99,
    "None": 0.00
}

# --- UI Layout ---
st.title("Switching Costs Calculator: PS5 to Xbox Series X")

# 1. Console Selection
st.caption("(You can select only one option)")
console_choice = st.selectbox(
    "Select the PS5 version you bought :",
    options=list(consoles.keys())
)

# 2. Accessories Selection
st.caption("(You can select multiple options)")
acc_choices = st.multiselect(
    "Select the accessories you bought :",
    options=list(accessories.keys())
)

# 3. Digital Games Selection
st.caption("(You can select multiple options)")
digital_choices = st.multiselect(
    "Select the videogames you bought on the Digital Store :",
    options=list(games.keys())
)

# 4. Physical Games Selection (Conditional Logic)
show_physical = False

# Condition 1: Picked a disc-drive console
if console_choice in ["PS5 Standard - € 499.99", "PS5 Slim Standard - € 549.99", "PS5 Pro - € 799.99"]:
    show_physical = True

# Condition 2: Picked the external Blu-Ray player accessory
for acc in acc_choices:
    if "Blu-Ray player" in acc:
        show_physical = True

physical_choices = []
if show_physical:
    st.caption("(You can select multiple options)")
    physical_choices = st.multiselect(
        "Select the videogames you bought on physical version and you are gonna re-sell :",
        options=list(games.keys())
    )

# 5. Subscription Selection
st.caption("(You can select only one option)")
sub_choice = st.selectbox(
    "Select the type of active subscription at the moment of changing asset:",
    options=list(subscriptions.keys())
)

# 6. Subscription Months Remaining Slider
months_remaining = st.slider(
    "Months of subscription remaining at the moment of changing asset:",
    min_value=0, max_value=12, value=0, step=1
)

st.divider()

# --- Calculations ---
console_cost = consoles[console_choice]
acc_cost_sum = sum(accessories[a] for a in acc_choices)
digital_games_sum = sum(games[g] for g in digital_choices)

# Variable X Logic
X = 0.0
if show_physical:
    X = 0.7 * sum(games[g] for g in physical_choices)

# Variable Y Logic
Y = subscriptions[sub_choice] * months_remaining

# Final Total Formula
total_switching_cost = 499.99 + (0.6 * console_cost) + (0.7 * acc_cost_sum) + digital_games_sum + X + Y

# --- Display Disclaimers ---
st.markdown("### Calculation Specifications")
st.markdown("""
* Standard non-discounted prices from the official PlayStation site (05/26) have been reported.
* It was calculated that the purchased console is sold at 40% of its full price.
* It was calculated that the accessories are sold at 30% of their full price.
* It was calculated that the physical videogames are sold at 30% of their full price.
* It was calculated that, as an alternative, an Xbox Series X console is purchased at the price of € 499.99.
* The switching costs were calculated as the direct sum of the amounts spent on purchases, net of the resale of assets at a lower price.
* Possible bundles, discounts, network costs (loss of network effects), learning costs, non-recoverable virtual currencies, and other possible incalculable costs have been ignored.
""")

st.divider()

# --- Final Display Result ---
st.subheader(f"The switching costs that would be incurred in the event of an asset change, would be : € {total_switching_cost:.2f}")
