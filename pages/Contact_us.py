import streamlit as st


st.header("Contact Me")

with st.form("contact_form"):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your message here")
    button = st.form_submit_button("Submit")
    if button:
        user_message = user_message + '\n' + user_email
        print("I was pressed")