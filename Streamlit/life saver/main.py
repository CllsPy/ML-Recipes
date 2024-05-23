import base64
import pandas as pd
import streamlit as st
from pathlib import Path

# Settings
st.set_page_config(
		 page_title="Save your time!",
		 layout="wide",
		 initial_sidebar_state="expanded",
)


st.write("# Insira os dados")

# Colunas
col1, col2 = st.columns(2)
temp_instagram = col1.number_input("Horas por semana no Instagram", min_value=0, max_value=24)
temp_youtube = col2.number_input("Horas por semana no YouTube", min_value=0, max_value=24)

# Math
per_month = (temp_instagram + temp_youtube) * 4
per_year = (temp_instagram + temp_youtube) * 52

# Display
st.write("## Tempo Total")
col1, col2, col3 = st.columns(3)
col1.metric(label="Tempo gasto com redes sociais por mês", value=f"{per_month} horas")
col2.metric(label="Tempo gasto com redes sociais por ano", value=f"{per_year} horas")

df = {
	
	"Anos da sua vida":80,
	"Tempo restante de vida": 80 - (per_year * 80/8760),
	
}

data = pd.DataFrame(df, index=["Anos"])
st.bar_chart(data["Tempo restante de vida"])


