import streamlit as st
import pages.page1
import pages.page2
import pages.page3

# Title of the app
st.title("My Multipage Streamlit App")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Go to", ("Page 1", "Page 2", "Page 3"))

# Navigation logic
if options == "Page 1":
    pages.page1.app()
elif options == "Page 2":
    pages.page2.app()
elif options == "Page 3":
    pages.page3.app()
