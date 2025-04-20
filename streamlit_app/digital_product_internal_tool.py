# This is the main digital product internal tool Streamlit app entry point that controls page layout, navigation, and routing

import streamlit as st
from pages import (
    page_welcome,
    page_background,
    page_dashboard,
    page_training_tool,
    page_learn_more
)
from style import apply_custom_styles

# ----------------------------
# App Config & Styling Setup
# ----------------------------
st.set_page_config(page_title="You Be the Budget Director", layout="wide")
apply_custom_styles()  # Inject custom CSS and colors

# ----------------------------
# Session State Init (if needed)
# ----------------------------
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 0

# ----------------------------
# Define Navigation Pages
# ----------------------------
pages = {
    "Welcome": page_welcome,
    "Background": page_background,
    "Dashboard": page_dashboard,
    "Training Tool": page_training_tool,
    "Learn More": page_learn_more
}

page_names = list(pages.keys())

# ----------------------------
# Header Image (small banner)
# ----------------------------
st.image("../assets/welcome_missoula.jpg", use_container_width=True)

# ----------------------------
# Horizontal Navigation Bar
# ----------------------------
st.markdown("## Navigate")
selected_page = st.selectbox("Choose a page", page_names, index=st.session_state['current_page'], key="page_selector")
st.session_state['current_page'] = page_names.index(selected_page)

# ----------------------------
# Load the Selected Page Content
# ----------------------------
pages[selected_page]()