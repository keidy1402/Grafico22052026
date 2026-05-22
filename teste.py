import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.set_page_config(layout="wide")

st.title("Mapa de Periculosidade do Rio de Janeiro")

st.write(
    "Mapa fictício de risco por bairros do Rio de Janeiro."
)

# -----------------------------
# Dados fictícios
# -----------------------------

dados = pd.DataFrame({
    "bairro": [
        "Copacabana",
        "Tijuca",
        "Santa Teresa",
        "Barra da Tijuca",
        "Leblon",
        "Botafogo",
        "Centro",
        "Jacarepaguá"
    ],
    "score": [7.5, 6.2, 5.8, 4.1, 3.5, 5.0, 7.0, 6.5],
    "lat": [
        -22.9711,
        -22.9245,
        -22.9152,
        -23.0004,
        -22.9839,
        -22.9519,
        -22.9035,
        -22.9658
    ],
    "lon": [
        -43.1822,
        -43.2416,
        -43.1889,
        -43.3659,
        -43.2249,
        -43.1803,
        -43.2096,
        -43.3919
    ]
})

# -----------------------------
# Criar mapa
# -----------------------------

mapa = folium.Map(
    location=[-22.9068, -43.1729],
    zoom_start=11
)

# -----------------------------
# Adicionar círculos
# -----------------------------

for _, row in dados.iterrows():

    if row["score"] >= 7:
        cor = "red"
    elif row["score"] >= 5:
        cor = "orange"
    else:
        cor = "green"

    folium.CircleMarker(
        location=[row["lat"], row["lon"]],
        radius=row["score"] * 2,
        popup=f"""
        <b>Bairro:</b> {row['bairro']}<br>
        <b>Score:</b> {row['score']}
        """,
        color=cor,
        fill=True,
        fill_color=cor,
        fill_opacity=0.7
    ).add_to(mapa)

# -----------------------------
# Exibir no Streamlit
# -----------------------------

st_folium(mapa, width=1200, height=700)
st_folium(m, width=1200, height=700)
