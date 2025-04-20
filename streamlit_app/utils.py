# Contains optional reusable helper functions for the app

import streamlit as st

# ------------------------
# Navigation Helper
# ------------------------
def next_button(pages_list):
    """
    Displays a "Next Page" button and increments the page index in session state.
    To use: pass in the list of page names used in the app's nav order.
    """
    idx = st.session_state.get("current_page", 0)
    if idx < len(pages_list) - 1:
        if st.button("➡️ Next Page"):
            st.session_state["current_page"] = idx + 1
            st.rerun()