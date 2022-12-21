import streamlit as st


st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("miages\photo.jpg", width=400)
    
with col2:
    st.title("Dawid Cieślak")
    content = """
    Hi I'm Dawid. I want to become python programmer. Former Automation engeener with around 50 legacy programs to manage and modernize.
    Now I'm workinga as Software localization engeener. Programming is my passion in any language as Automation engeener i was working with Assembly lvl languages.
    I was able to completly rewrite one machine, and update several more. 
    In my current job im Preparing XLM files for translation and checking them aftre translation.
    Currently I'm working with Python in every free momment, It's great fun. Im hoping to find job with Python.
     
    """
    st.info(content)