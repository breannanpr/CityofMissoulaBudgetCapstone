# style.py
# Contains custom colors and CSS for consistent branding across the Streamlit app

import streamlit as st

# ------------------------
# University of Montana Brand Colors
# ------------------------
COLORS = {
    "griz_maroon": "#70002e",
    "sunset_red": "#F9423A",
    "copper_climb": "#ED8B00",
    "wheat": "#EFE8D4",
    "trail_sign_tan": "#DFD1A7",
    "lubrecht_green": "#1D3C34",
    "glacier_sky": "#BBDDE6",
    "snowbowl_silver": "#BBDDE6"
}

# ------------------------
# Custom CSS Injection Function
# ------------------------
def apply_custom_styles():
    """
    Injects custom CSS to style elements consistently across the app.
    Should be called once at the top of main.py.
    """
    st.markdown(f"""
        <style>
            .block-container {{ padding-top: 2rem; }}
            .stSlider > div {{ color: {COLORS['griz_maroon']}; }}
            .stButton > button {{ 
                border-radius: 8px; 
                background-color: {COLORS['lubrecht_green']}; 
                color: white; 
                padding: 0.5em 1.5em; 
            }}
            .stButton > button:hover {{ background-color: {COLORS['copper_climb']}; }}
            h1, h2, h3, h4 {{ color: {COLORS['griz_maroon']}; }}
            .title-text {{ 
                background-color: rgba(255,255,255,0.92); 
                padding: 1rem; 
                border-radius: 10px; 
                max-width: 850px; 
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2); 
            }}
            ul {{ line-height: 1.5em; }}
            .impact-check {{ font-size: 1.1em; }}
            .next-button-container {{ text-align: center; margin-top: 2rem; }}
        </style>
    """, unsafe_allow_html=True)