import streamlit as st
import spacy_streamlit


st.text("Version : 1.0 ")

models = ["fr_core_news_sm"]
default_text = "La madeleine de Proust."
spacy_streamlit.visualize(models, default_text)



if st.button("Generate"):
    print("ok")
