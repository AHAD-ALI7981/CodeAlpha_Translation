import streamlit as st
from deep_translator import GoogleTranslator

st.title("🌍 Language Translation Tool")

text = st.text_area("Enter text to translate:")

languages = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate"):
    translated = GoogleTranslator(
        source=languages[source_lang],
        target=languages[target_lang]
    ).translate(text)

    st.success("Translated Text:")
    st.write(translated)