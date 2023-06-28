import streamlit as st
import spacy_streamlit


st.text("Version : 1.0 ")

models = ["ner_miam_spacy_nlp.tar"]
default_text = "La madeleine de Proust."
spacy_streamlit.visualize(models, default_text)



if st.button("Generate"):
    print("ok")
