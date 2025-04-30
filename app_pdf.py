import streamlit as st
from PIL import Image
import pytesseract
from langdetect import detect
from googletrans import Translator
from transformers import pipeline
import PyPDF2
import io

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
# Initialize translator and summarizer
translator = Translator()
summarizer = pipeline("summarization")

st.title("🧠 AI Text Extractor + Language Tools")

uploaded_file = st.file_uploader("Upload a file", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    
    if file_type == "application/pdf":
        with st.spinner("Extracting text from PDF..."):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Extracted Text:")
                st.text_area("Text", text, height=300)
                
                # Language detection
                try:
                    lang = detect(text)
                    st.info(f"Detected Language: {lang}")
                except:
                    st.warning("Could not detect language.")
                    
            with col2:
                # Translation
                if lang != 'en':
                    try:
                        translated = translator.translate(text, dest='en')
                        st.subheader("Translated to English:")
                        st.text_area("English Translation", translated.text, height=300)
                        text = translated.text  # Use for summarization
                    except:
                        st.warning("Translation failed.")
                
                # Summarization
                if len(text.split()) > 20:
                    try:
                        summary = summarizer(text, max_length=100, min_length=25, do_sample=False)[0]['summary_text']
                        st.subheader("Summarized Text:")
                        st.text_area("Summary", summary, height=200)
                    except:
                        st.warning("Summarization failed.")
                else:
                    st.info("Text too short for summarization.")
    
    else:  # Image files
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Extract Text"):
            with st.spinner("Extracting text..."):
                col1, col2 = st.columns(2)

                with col1:
                    text = pytesseract.image_to_string(image)
                    st.subheader("Extracted Text:")
                    st.text_area("Text", text, height=300)

                    # Language detection
                    try:
                        lang = detect(text)
                        st.info(f"Detected Language: {lang}")
                    except:
                        st.warning("Could not detect language.")

                with col2:
                    # Translation
                    if lang != 'en':
                        try:
                            translated = translator.translate(text, dest='en')
                            st.subheader("Translated to English:")
                            st.text_area("English Translation", translated.text, height=300)
                            text = translated.text  # Use for summarization
                        except:
                            st.warning("Translation failed.")
                    
                    # Summarization
                    if len(text.split()) > 20:
                        try:
                            summary = summarizer(text, max_length=100, min_length=25, do_sample=False)[0]['summary_text']
                            st.subheader("Summarized Text:")
                            st.text_area("Summary", summary, height=200)
                        except:
                            st.warning("Summarization failed.")
                    else:
                        st.info("Text too short for summarization.")