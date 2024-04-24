import streamlit as st
from read_data import load_person_data, get_person_list

person_dict = load_person_data()
person_names = get_person_list(person_dict)

st.session_state.current_user = st.selectbox(
    'Versuchsperson',
    options = person_names, key="sbVersuchsperson")