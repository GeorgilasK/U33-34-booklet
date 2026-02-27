import streamlit as st
import os
import base64

st.set_page_config(page_title="U33/U34 Booklets", layout="wide")

st.title("📄 Booklet U33/U34")

choice = st.radio("Επιλέξτε Booklet:", ("U33", "U34"), horizontal=True)
pdf_filename = f"{choice}.pdf"

def display_pdf(file):
    if os.path.exists(file):
        with open(file, "rb") as f:
            pdf_data = f.read()
        
        base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
        
        # Χρησιμοποιούμε αντικείμενο <object> αντί για <iframe> 
        # και προσθέτουμε παραμέτρους για τον viewer
        pdf_display = f'''
            <center>
                <object data="data:application/pdf;base64,{base64_pdf}" type="application/pdf" width="100%" height="900px">
                    <embed src="data:application/pdf;base64,{base64_pdf}" type="application/pdf" />
                    <p>Η συσκευή σας δεν υποστηρίζει την απευθείας προβολή. 
                    <a href="data:application/pdf;base64,{base64_pdf}" target="_blank">Πιέστε εδώ για άνοιγμα.</a></p>
                </object>
            </center>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)
    else:
        st.error(f"Το αρχείο {file} δεν βρέθηκε.")

display_pdf(pdf_filename)
