import streamlit as st

st.title('Sleep All Night')

st.image('./images/background.png')


if st.button('睡眠脑电分析',use_container_width=True,type='primary'):
    st.switch_page('pages/show_eeg.py')
if st.button('睡眠分期',use_container_width=True,type='primary'):
    st.switch_page('pages/sleep_stage.py')
if st.button('睡眠状况分析',use_container_width=True,type='primary'):
    st.switch_page('pages/sleep_analysis.py')
