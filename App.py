import streamlit as st
import os

st.set_page_config(page_title="U33-34 Booklet", layout="centered")

pdf_filename = "U33-34.booklet.pdf"

st.title("📄 Σύστημα Αρχείων U33-34")

if os.path.exists(pdf_filename):
    st.success("Το έγγραφο φορτώθηκε επιτυχώς!")
    
    with open(pdf_filename, "rb") as f:
        pdf_data = f.read()
    
    # Αυτό το κουμπί είναι το πιο σταθερό για κινητά
    st.download_button(
        label="📖 Άνοιγμα / Λήψη Booklet",
        data=pdf_data,
        file_name=pdf_filename,
        mime="application/pdf",
        use_container_width=True
    )

    st.info("💡 Μόλις ανοίξει το αρχείο, πατήστε το εικονίδιο 'Μεγένθυση' ή 'Φακό' για αναζήτηση.")

    # Εμφάνιση Προεπισκόπησης (μόνο αν ο browser το υποστηρίζει)
    st.write("---")
    st.subheader("Προεπισκόπηση")
    import base64
    base64_pdf = base64.b64encode(pdf_data).decode('utf-8')
    pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="600" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.error(f"❌ Το αρχείο '{pdf_filename}' δεν βρέθηκε στο GitHub.")
    st.write("Βεβαιωθείτε ότι το αρχείο είναι στον ίδιο φάκελο με το App.py")
