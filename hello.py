from email.mime import image
import streamlit as st

st.set_page_config(
    page_title =  "Application",
    page_icon = "@",
    
)

st.title("Python Web Application")

# Add an image
st.image("https://cdn.wallpapersafari.com/8/85/gb5BPn.jpg", caption="My Image", use_column_width=True)


st.sidebar.success("Options..")