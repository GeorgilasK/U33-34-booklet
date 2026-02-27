import streamlit as st
import os

st.set_page_config(page_title="U33-34 Booklet", layout="wide")

pdf_filename = "U33-34.booklet.pdf"

st.title("📄 Προβολή Booklet U33-34")

if os.path.exists(pdf_filename):
    # Διαβάζουμε το αρχείο
    with open(pdf_filename, "rb") as f:
        pdf_bytes = f.read()

    # Εμφάνιση οδηγιών για το Search
    st.info("🔍 Για αναζήτηση: Πατήστε Ctrl+F (PC) ή το εικονίδιο του φακού στον viewer.")

    # Χρήση iframe για προβολή χωρίς κουμπί download
    # Σημείωση: Προσθέτουμε το #toolbar=0 αν θέλουμε να κρύψουμε τα εργαλεία της Google, 
    # αλλά εμείς θέλουμε το toolbar για να έχει ο χρήστης το Search.
    
    import base64
    base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
    
    # Το width="100%" και height="1000" εξασφαλίζουν ότι θα φαίνεται σαν σελίδα
    pdf_display = f'''
        <iframe 
            src="data:application/pdf;base64,{base64_pdf}" 
            width="100%" 
            height="1000" 
            type="application/pdf"
            style="border:none;">
        </iframe>
    '''
    
    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.error(f"Το αρχείο {pdf_filename} δεν βρέθηκε.")
