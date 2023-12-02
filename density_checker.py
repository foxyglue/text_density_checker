import streamlit as st
import re
from PIL import Image

#Make sidebar
img = open('53510.jpg', 'rb').read()  # Membaca gambar sebagai binary
st.sidebar.image(img, use_column_width=True)
st.sidebar.markdown("<h1 style= 'text-align: center;'>Density Checker</h1>", unsafe_allow_html = True)
st.sidebar.markdown("### This is a simple application to show how many a word is being used in text(s).")
st.sidebar.markdown("### You can try this application by copying an article or a journal texts.")


#Main page
st.markdown("<h1 style= 'text-align: center;'>Density Checker</h1>", unsafe_allow_html = True)
st.markdown("---", unsafe_allow_html = True)
text = st.text_area("Paragraph")
col1, col2, col3 = st.columns(3)
words_dict = dict()
if text:
    col1.markdown(f"<h3 style= 'text-align: center;'>Keywords</h3>", unsafe_allow_html = True)
    col2.markdown(f"<h3 style= 'text-align: center;'>Occurances</h3>", unsafe_allow_html = True)
    col3.markdown(f"<h3 style= 'text-align: center;'>Percentages</h3>", unsafe_allow_html = True)
    sim_text = re.sub("[,.?;!&*]", "", text)
    words= sim_text.lower().split(" ")
    t_len = len(words)
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word]+1
        else:
            words_dict[word] = 1
    keys = list(words_dict.keys())
    values = list(words_dict.values())
    for i in range(len(keys)):
        col1.markdown(f"<h5 style= 'text-align: center;'>{keys[i]}</h5>", unsafe_allow_html = True)
        col2.markdown(f"<h5 style= 'text-align: center;'>{values[i]}</h5>", unsafe_allow_html = True)
        col3.markdown(f"<h5 style= 'text-align: center;'>{round((values[i]/t_len)*100)}%</h5>", unsafe_allow_html = True)