import streamlit as st
import base64
import os

st.set_page_config(page_title="U33-34 Viewer", layout="centered")

pdf_filename = "U33-34.booklet.pdf"

def get_pdf_display(file):
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    # Δημιουργεί ένα link που ανοίγει το PDF απευθείας στον browser
    pdf_display = f'<a href="data:application/pdf;base64,{base64_pdf}" target="_blank" style="text-decoration: none;"><div style="background-color: #ff4b4b; color: white; padding: 20px; text-align: center; border-radius: 10px; font-size: 20px; font-weight: bold;">📥 Πάτησε εδώ για άνοιγμα του Booklet (Search Enabled)</div></a>'
    return pdf_display

st.title("📄 Σύστημα Αρχείων U33-34")

if os.path.exists(pdf_filename):
    st.markdown("### Το έγγραφο είναι έτοιμο!")
    st.info("Μόλις ανοίξει, μπορείτε να χρησιμοποιήσετε την αναζήτηση του browser (φακός ή Ctrl+F).")
    
    # Εμφάνιση του κουμπιού
    st.markdown(get_pdf_display(pdf_filename), unsafe_allow_html=True)
    
    # Προαιρετικά: Εμφάνιση και από κάτω (Embed)
    st.write("---")
    with open(pdf_filename, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    st.markdown(f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf"></iframe>', unsafe_allow_html=True)
else:
    st.error(f"Το αρχείο {pdf_filename} δεν βρέθηκε στο GitHub.")
