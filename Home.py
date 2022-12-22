import streamlit as st
import pandas


st.set_page_config(layout="wide")


col1, col2 = st.columns(2)

with col1:
    st.image("miages/photo.png", width=300)
    
with col2:
    st.title("Dawid Cieślak")
    content = """
    Hi I'm Dawid. I want to become python programmer. Former Automation engeener with around 50 legacy programs to manage and modernize.
    Now I'm workinga as Software localization engeener. Programming is my passion in any language as Automation engeener i was working with Assembly lvl languages.
    I was able to completly rewrite one machine, and update several more. 
    In my current job im Preparing XLM files for translation and checking them aftre translation.
    Currently I'm working with Python in every free momment, It's great fun. Im hoping to find job with It.
     
    """
    st.info(content)
    
st.write("Below you can find some apps written by me. If you like it feel fre to contact me!")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[0::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"], width=250)
        st.write(f"[Go to app]({row['url']})")
        
        
with col4:
    for index, row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"], width=250)
        st.write(f"[Go to app]({row['url']})")