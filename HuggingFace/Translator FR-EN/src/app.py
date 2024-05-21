import streamlit as st
import transformers
from transformers import pipeline

translator = pipeline(
    "translation", 
    model="Helsinki-NLP/opus-mt-fr-en", 
)

title = st.title("Tradutor FR to EN")
txt = st.text_area("Setença para traduzir:",)

if st.button("Traduzir"):
    fr_txt = txt
    translation = translator(fr_txt)
    st.write((translation[0]['translation_text']))
	