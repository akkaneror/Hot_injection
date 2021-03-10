import streamlit as st

def get_radio_input(question, selection):
    """
    This function creates questions and
    multiple choice answers in the user interface.
    """
    answer = st.radio(question, selection)
    return answer

def get_slider_input(question, mmin_val, max_val, default_val, interval):
    """
    This function creates questions and
    slider answers in the user interface.
    """
    answer = st.slider(question, mmin_val, max_val, default_val, interval)
    return answer
