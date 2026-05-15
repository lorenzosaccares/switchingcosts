# 5. Subscription Selection
st.markdown("### Select the type of active subscription at the moment of changing asset:")
st.caption("(You can select only one option)")
sub_choice = st.selectbox(
    "Select Subscription Type", # Nome interno (verrà nascosto)
    options=list(subscriptions.keys()),
    label_visibility="collapsed" # Questo risolve il problema visivo e di ID
)

st.write("")

# 6. Subscription Months Remaining Slider
st.markdown("### Months of subscription remaining at the moment of changing asset:")
st.caption("(Select a value from 0 to 12)")
months_remaining = st.slider(
    "Remaining Months", # Nome interno (verrà nascosto)
    min_value=0, max_value=12, value=0, step=1,
    label_visibility="collapsed" # Questo risolve il problema visivo e di ID
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
# Usiamo il valore corrispondente al tipo di abbonamento scelto
Y = subscriptions[sub_choice] * months_remaining

# Final Total Formula
total_switching_cost = 499.99 + (0.6 * console_cost) + (0.7 * acc_cost_sum) + digital_games_sum + X + Y

# --- Final Display Result (Centered and Big as requested) ---
st.markdown("## The switching costs that would be incurred in the event of an asset change, would be:")
st.markdown(
    f"<h1 style='text-align: center; font-size: 3.5rem; color: #ff4b4b;'>€ {total_switching_cost:.2f}</h1>", 
    unsafe_allow_html=True
)

st.divider()

# --- Display Disclaimers (Less prominent at the bottom) ---
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
