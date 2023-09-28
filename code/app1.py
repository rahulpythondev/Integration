import streamlit as st
from streamlit_cytoscapejs import st_cytoscapejs

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

elements = [
    {"data": {"id": "one", "label": "Node 1"}, "position": {"x": 0, "y": 0}},
    {"data": {"id": "two", "label": "Node 2"}, "position": {"x": 100, "y": 0}},
    {"data": {"source": "one", "target": "two", "label": "Edge from Node1 to Node2"}},
]
stylesheet = [
    {"selector": "node", "style": {"width": 20, "height": 20, "shape": "rectangle"}},
    {"selector": "edge", "style": {"width": 10}},
]

st.title("Hello Cytoscape.js")
clicked_elements = st_cytoscapejs(elements, stylesheet)

if clicked_elements is not None:
    st.write(clicked_elements)