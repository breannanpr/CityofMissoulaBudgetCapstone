# Defines and applies custom CSS styles for the Streamlit app

def apply_custom_styles():
    import streamlit as st

    # Inject custom CSS styles into the Streamlit app
    st.markdown("""
        <style>
            /* Customize slider text color to match brand */
            .stSlider > div {
                color: #70002e; /* Griz maroon */
            }

            /* Primary button styling for consistency across pages */
            .stButton > button {
                border-radius: 8px;
                background-color: #1D3C34; /* Lubrecht green */
                color: white;
                padding: 0.5em 1.5em;
            }

            /* Button hover effect for user interaction feedback */
            .stButton > button:hover {
                background-color: #ED8B00; /* Copper climb */
            }

            /* Ensure consistent branding across all headers */
            h1, h2, h3, h4 {
                color: #70002e; /* Griz maroon */
            }

            /* Styling for the welcome block or highlighted text sections */
            .title-text {
                background-color: rgba(255,255,255,0.92);
                padding: 1rem;
                border-radius: 10px;
                max-width: 850px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.2);
            }

            /* Improve list readability */
            ul {
                line-height: 1.5em;
            }

            /* Adjust font size for impact evaluation feedback */
            .impact-check {
                font-size: 1.1em;
            }

            /* Style and space the optional "Next Page" button */
            .next-button-container {
                text-align: center;
                margin-top: 2rem;
            }

            /* Header image styling - reduce vertical space usage */
            .stImage > img {
                max-height: 150px; /* Control height of top banner */
                object-fit: cover;  /* Ensure clean aspect ratio */
                width: 90%; /* Full-width responsiveness */
            }
        </style>
    """, unsafe_allow_html=True)
