import streamlit as st
import pandas


st.set_page_config(
    layout="wide",
    page_title="Portfolio",
    page_icon="miages/briefcase.png"
    )


col1, col2 = st.columns(2)

with col1:
    st.image("miages/photo.png", width=300)
    
with col2:
    st.title("Dawid Cieślak")
    content = f"""
    Hi I'm Dawid. I want to become python programmer. Former Automation engeener with around 50 legacy programs to manage and modernize.
    Now I'm workinga as Software localization engeener. Programming is my passion in any language as Automation engeener i was working with Assembly lvl languages.
    I was able to completly rewrite one machine, and update several more. 
    In my current job im Preparing XLM files for translation and checking them aftre translation.
    Currently I'm working with Python in every free momment, It's great fun. Im hoping to find job with It.
    You cand find my [cv here.](https://canthar90.github.io/cv_site/) 
     
    """
    st.info(content)
    
st.info("Below you can find some apps written by me. If you like it feel fre to contact me!")

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

st.info("Below you can find short description and links to repos.")   
     
col5, col6 = st.columns(2)
gits_df = pandas.read_csv("gits.csv", sep=";")    
    
with col5:
    for index, row in gits_df[0::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"], width=250)
        st.write(f"[Go to repo]({row['url']})")
        
        
with col6:
    for index, row in gits_df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"], width=250)
        st.write(f"[Go to repo]({row['url']})")


st.markdown("<p style='text-align: center;'>I would like to attribute Freepic <a href='https://www.freepik.com'>Visit Freepick</a></h1>", unsafe_allow_html=True)