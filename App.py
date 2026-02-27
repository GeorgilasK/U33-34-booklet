import streamlit as st
import base64
import os

st.set_page_config(page_title="U33/U34", layout="centered")

choice = st.radio("Επιλέξτε αρχείο:", ("U33", "U34"), horizontal=True)
pdf_filename = f"{choice}.pdf"

if os.path.exists(pdf_filename):
    with open(pdf_filename, "rb") as f:
        pdf_data = f.read()
    
    b64 = base64.b64encode(pdf_data).decode()
    
    # Αυτό δημιουργεί ένα link που ανοίγει το PDF σε νέο tab 
    # και ενεργοποιεί τον native viewer του iPhone
    href = f'<a href="data:application/pdf;base64,{b64}" target="_blank" style="display: inline-block; padding: 15px 25px; font-size: 20px; cursor: pointer; text-align: center; text-decoration: none; outline: none; color: #fff; background-color: #4CAF50; border: none; border-radius: 15px; width: 100%;">🔍 Άνοιγμα {choice} (Full Scroll & Search)</a>'
    
    st.markdown(href, unsafe_allow_html=True)
    st.write("---")
    st.caption("Σημείωση: Μετά το άνοιγμα, πατήστε το εικονίδιο αναζήτησης του browser.")
