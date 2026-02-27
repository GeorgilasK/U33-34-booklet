import streamlit as st
import os
import base64

# Ρύθμιση σελίδας για να πιάνει όλο το πλάτος
st.set_page_config(page_title="U33/U34 Booklets", layout="wide")

st.title("📄 Επιλογή Booklet")

# Δημιουργία μενού επιλογής στο πλάι ή στο κέντρο
choice = st.radio(
    "Επιλέξτε το έγγραφο που θέλετε να δείτε:",
    ("U33", "U34"),
    horizontal=True
)

# Ορισμός ονόματος αρχείου βάσει επιλογής
pdf_filename = f"{choice}.pdf"

def displayPDF(file):
    if os.path.exists(file):
        with open(file, "rb") as f:
            pdf_bytes = f.read()
        
        # Μετατροπή σε base64 για προβολή
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        
        # Οδηγίες αναζήτησης
        st.info(f"🔍 Αναζήτηση στο {choice}: Πατήστε Ctrl+F ή τον μεγεθυντικό φακό.")

        # HTML κώδικας για το iframe
        pdf_display = f'''
            <iframe 
                src="data:application/pdf;base64,{base64_pdf}" 
                width="100%" 
                height="900" 
                style="border: 2px solid #eeeeee;"
                type="application/pdf">
            </iframe>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error(f"⚠️ Το αρχείο {file} δεν βρέθηκε στο GitHub. Βεβαιωθείτε ότι το ονομάσατε ακριβώς έτσι.")

# Εκτέλεση της συνάρτησης
displayPDF(pdf_filename)
