# 🧠 AI Text Extractor + Language Tools

A Streamlit web application that extracts text from images and provides language processing tools including:
- Optical Character Recognition (OCR)
- Language detection
- Translation to English
- Text summarization

## 🛠️ Prerequisites

- Python 3.6+
- Tesseract OCR engine installed on your system
  - Windows: Install from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)
  - Linux: `sudo apt-get install tesseract-ocr`
  - Mac: `brew install tesseract`

## 📦 Installation

1. Clone the repository or download the source code

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install streamlit pillow pytesseract langdetect googletrans==4.0.0-rc1 transformers
```

## 🚀 Running the Application

1. Navigate to the project directory

2. Start the Streamlit server:
```bash
streamlit run app.py
```

3. The application will open in your default web browser (typically at http://localhost:8501)

## 📝 Usage

1. Upload an image containing text (.jpg, .jpeg, or .png)
2. Click "Extract Text" to process the image
3. The app will:
   - Extract text from the image
   - Detect the language
   - Translate to English (if not already in English)
   - Provide a summary (for longer texts)

## ⚠️ Note

Make sure Tesseract OCR is properly installed and accessible from your system's PATH for the text extraction feature to work.