import streamlit as st
import pdfplumber  # New library for PDF reading

# Streamlit Page Configuration
st.set_page_config(
    page_title="Problem Extractor",
    page_icon="imgs/lb.jpg",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get help": "https://github.com/AdieLaine/Streamly",
        "Report a bug": "https://github.com/AdieLaine/Streamly",
        "About": """
            ## Problem Extractor
            ### Using AI to Identify Problems from PDFs

            The Problem Extractor accepts PDF documents and uses AI to generate problem summaries or insights.
        """
    }
)

# Streamlit Title
st.title("Problem Extractor")

def extract_text_from_pdf(pdf_file):
    """Extracts text from a PDF file using pdfplumber."""
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def run_ai_algorithm(text):
    # Placeholder AI algorithm
    result = "Processed output of AI Algorithm"  # Replace this with actual algorithm logic
    return result

def main():
    uploaded_pdf = st.file_uploader("Upload a PDF file", type="pdf")

    if uploaded_pdf is not None:
        st.info("Extracting text from PDF...")
        extracted_text = extract_text_from_pdf(uploaded_pdf)
        
        # Display extracted text (optional)
        with st.expander("Extracted Text"):
            st.write(extracted_text)
        
        # Run AI algorithm
        st.info("Running AI algorithm...")
        output = run_ai_algorithm(extracted_text)
        
        # Display AI-generated output
        st.subheader("AI-Generated Output")
        st.write(output)

if __name__ == "__main__":
    main()
