import streamlit as st
import spacy_streamlit


st.text("Version : 1.0 ")
st.markdown('# Darespresso')
st.divider()
st.info('Prenez le café avec Proust', icon="ℹ️")
st.divider()

models = ["model-best","ner_miam_spacy_nlp"]
default_text = "La madeleine de Proust."
visualizers = ["ner"]
spacy_streamlit.visualize(models=models, default_text=default_text, visualizers=visualizers,show_visualizer_select=True)