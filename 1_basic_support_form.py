import streamlit as st

with st.form("my_form"):
    st.write("Submit a support case")
    text_val = st.text_area("Describe your problem?")

    submitted = st.form_submit_button("Submit")
    if submitted:
        # TODO check for related support cases and articles
        st.write("Submitted!")
