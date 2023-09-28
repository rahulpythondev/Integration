import streamlit as st
from barfi import st_barfi, Block

# Title and page config
st.set_page_config(
    layout='wide',
    page_title="Demo React Flow",
    initial_sidebar_state="collapsed"
)

# CSS to hide Streamlit elements
hide_streamlit_style = """
<style>
    div.block-container {padding-top:2rem;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

feed = Block(name='Input')
feed.add_input(name="Hello")

result = Block(name='Result')
result.add_output()

barfi_result = st_barfi(base_blocks=[feed, result])

if barfi_result:
    st.write(barfi_result)