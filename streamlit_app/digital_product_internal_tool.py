# This is the main digital product internal tool Streamlit app entry point that controls page layout, navigation, and routing

import streamlit as st
import os
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
st.set_page_config(page_title="City of Missoula Expenditure Status Training Tool", layout="wide")
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
header_img_path = os.path.join("streamlit_app", "assets", "welcome_missoula.jpg")
st.image(header_img_path, use_container_width=True)

# ----------------------------
# Horizontal Navigation Bar
# ----------------------------
st.markdown("## Welcome")
nav_cols = st.columns(len(page_names))
for i, name in enumerate(page_names):
    if nav_cols[i].button(name):
        st.session_state['current_page'] = i
        st.rerun()

# ----------------------------
# Load the Selected Page Content
# ----------------------------
pages[page_names[st.session_state['current_page']]](page_names)