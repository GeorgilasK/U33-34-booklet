import streamlit as st
import base64

st.set_page_config(page_title="PDF Viewer", layout="wide")

st.title("📄 Οδηγός / Έγγραφο Συναδέλφων")

def displayPDF(file):
    # Διάβασμα του αρχείου
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding του PDF σε ένα iframe
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="1000" type="application/pdf"></iframe>'
    
    # Εμφάνιση
    st.markdown(pdf_display, unsafe_allow_html=True)

# Το όνομα του αρχείου σου στο GitHub
pdf_filename = "U33-34.booklet.pdf" 

displayPDF(pdf_filename)
