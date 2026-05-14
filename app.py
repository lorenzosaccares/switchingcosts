import streamlit as st

st.title("Calcolatore Interattivo")
st.write("Muovi gli slider per vedere la somma in tempo reale!")

# Creazione degli slider
valore1 = st.slider("Seleziona il primo valore", 0, 100, 50)
valore2 = st.slider("Seleziona il secondo valore", 0, 100, 25)
valore3 = st.slider("Seleziona il terzo valore", 0, 100, 10)

# Calcolo della somma
somma = valore1 + valore2 + valore3

# Visualizzazione del risultato
st.header(f"La somma totale è: {somma}")
