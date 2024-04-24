import streamlit as st
from PIL import Image
import os
from read_data import load_person_data, get_person_list, get_imgae_path

st.title("EKG APP")
st.write("## Choose subject:")


person_dict = load_person_data()
person_names = get_person_list(person_dict)

st.session_state.current_user = st.selectbox(
    'Subject:',
    options = person_names, key="sbVersuchsperson")

image = Image.open(get_imgae_path(person_dict, st.session_state.current_user))

st.image(image, caption=st.session_state.current_user)
st.write("The name of the subject is: " + st.session_state.current_user)
st.write("The image path is: " + get_imgae_path(person_dict, st.session_state.current_user))

st.write("Authors: Alexander Kometer, Georg Sagmeister")

