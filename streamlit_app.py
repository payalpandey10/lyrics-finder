
import streamlit as st

st.set_page_config(page_title="Lyrics App", layout="centered")

st.title("🎵 Lyrics Finder App")
song = st.text_input("Enter song name")

if st.button("Get Lyrics"):
    if song:
        st.success(f"Lyrics for **{song}** will be shown here.")
        st.write("🎶 Sample lyrics line 1\n🎶 Sample lyrics line 2")
    else:
        st.error("Please enter a song name!")
