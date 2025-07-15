import streamlit as st
from gtts import gTTS
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Translate & Speak", layout="centered")
st.title("Text to Speech Converter 🗣️")

languages = {
    'English': 'en',
    'Hindi': 'hi',
    'Bengali': 'bn',
    'Tamil': 'ta',
    'Telugu': 'te',
    'French': 'fr',
    'German': 'de',
    'Punjabi': 'pa',
    'Gujarati': 'gu',
    'Marathi': 'mr',
    'Kannada': 'kn',
    'Malayalam': 'ml',
    'Urdu': 'ur',
    'Spanish': 'es'
}

lang_name = st.selectbox("Choose language to translate and speak", list(languages.keys()))
lang_code = languages[lang_name]

text = st.text_area("Enter text in English")

if st.button("Translate & Speak"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        try:
            # Translate from English to selected language
            translated = GoogleTranslator(source='en', target=lang_code).translate(text)
            st.success(f"Translated Text ({lang_name}): {translated}")

            # Convert to speech
            tts = gTTS(text=translated, lang=lang_code)
            tts.save("translated.mp3")

            # Play audio
            with open("translated.mp3", "rb") as audio_file:
                audio = audio_file.read()
                st.audio(audio, format='audio/mp3')
                st.download_button("Download", audio, file_name="translated.mp3")
        except Exception as e:
            st.error(f"❌ Error: {e}")
