# Contains all the content and logic for each page of the Streamlit app

import streamlit as st
# from data import load_data  # Temporarily commented out until deployment paths are finalized
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
from utils import next_button

# ------------------
# Welcome Page
# ------------------
def page_welcome(pages_list):
    st.title("Expenditure Status Training Tool")
    st.markdown("""
    Welcome to an interactive training tool designed for the City of Missoula, to help you understand expenditures within the city and how priority based budgeting practices work within the City of Missoula. It is especially important to note the following:
    - This tool only provides information available based on the expenditure budet information
    - This tool does not provide a comprehensive view of the budget for Missoula, MT. 
    - This training focuses solely on providing context for the expenditure information. 
    
    Use the navigation above to explore background context, interact with real program data, and try your hand at making funding decisions!
    """)
    next_button(pages_list)

# ------------------
# Background Page
# ------------------
def page_background(pages_list):
    st.header("Background and About This Tool")
    st.markdown("""
    This internal training tool is built around real data from the City of Missoula's budget process. 

    It aims to:
    - Build familiarity with program-level budgeting
    - Show how values are reflected in financial choices
    - Practice navigating public data and making trade-off decisions

    You’ll find visualizations, a hands-on activity, and a linked dashboard to support learning and most recently updated fiscal year data.
    """)
    next_button(pages_list)

# ------------------
# Dashboard Page
# ------------------
def page_dashboard(pages_list):
    st.header("Explore the Budget Dashboard")
    st.markdown("""
    Below is an interactive dashboard (Power BI) that displays program expenditures, risks, mandates, and alignment with city strategies.

    Use it to explore trends before doing the training activity. [This is a placeholder until the dashboard is available publically on the City's Instance of Power BI!]
    """)

    # Embed Power BI dashboard (replace src with actual embed link when ready)
    # st.components.v1.iframe("https://app.powerbi.com/view?r=YOUR_EMBED_LINK", height=600, scrolling=True)
    next_button(pages_list)

# ------------------
# Training Tool Page
# ------------------
def page_training_tool(pages_list):
    st.header("Make Your Budget Decisions")
    st.markdown("""
    Allocate funding across key strategy areas. After submitting, you'll immediately see how your choices align with City of Missoula priorities.
    
    Remember, since nearly half of your total budget is already consumed by mandated and required by law or other requirements you are working with what is left. 
    """)

    # Sliders for allocation
    categories = {
        "Community Design & Livability": "community",
        "Community Safety, Health and Well-Being": "safety",
        "Organizational Excellence and Resilience": "resilience",
        "Economic Health": "economy"
    }

    for label, key in categories.items():
        st.slider(label, 0, 100, key=key)

    total = sum(st.session_state.get(key, 0) for key in categories.values())
    st.metric("Total Allocated", f"{total}%")

    if any(st.session_state.get(k, 0) > 0 for k in categories.values()):
        st.success("Here’s how your budget reflects your values:")
        impact = []

        # Evaluate each strategy area
        safety = st.session_state['safety']
        community = st.session_state['community']
        resilience = st.session_state['resilience']
        economy = st.session_state['economy']

        # Add conditional feedback logic
        if safety >= 40:
            impact.append("✅ Strong investment in community safety and well-being.")
        elif safety < 20:
            impact.append("⚠️ Low funding may impact emergency services and public health.")

        if community >= 35:
            impact.append("✅ Clear priority on community design and livability.")
        elif community < 15:
            impact.append("⚠️ Risk of underfunding quality of life and placemaking programs.")

        if resilience >= 25:
            impact.append("✅ Emphasis on internal systems and sustainable operations.")
        elif resilience < 10:
            impact.append("⚠️ Low investment in internal infrastructure may reduce efficiency.")

        if economy >= 15:
            impact.append("✅ Support for business development and economic resilience.")
        elif economy < 5:
            impact.append("⚠️ Limited focus on local economic growth and jobs.")

        if total > 100:
            impact.append("⚠️ Your allocation exceeds 100%. Please rebalance.")

        for line in impact:
            st.markdown(f"- {line}")
    next_button(pages_list)


# ------------------
# Learn More Page
# ------------------
def page_learn_more(pages_list):
    st.header("Learn More About This Project")
    st.markdown("""
    This interactive simulator was developed as part of the final Master of Science, Business Analytics (MSBA) Capstone project at the University of Montana.

    #### 🎓 Final Project Deliverables
    - Streamlit digital product (this internal training app!)
    - A written product that details the entire data engineering and analysis process, from start to finish. ([View the document](LINKPLACEHOLDER for Final City Link))
    - Power BI Interactive Dashboard Tool (embedded views provided within this training app)

    #### 🔬 Data Sources from Current Fiscal Year (if viewing prior to June 30 of current year)
    - City of Missoula Program Inventory
    - Departmental Expenditure Status

    #### 👩‍💻 About the Data Engineering Analyst:
    **Breanna Niekamp** is a data engineer/analyst based in the local area of Missoula, Montana, 
    who blends storytelling, strategy and design thinking to help increase transparancy communication
    surrounding priority-based informed budget decisions. 

    #### 📂 GitHub Repository:
    [View the codebase](https://github.com/breannanpr/CityofMissoulaBudgetCapstone)
    """, unsafe_allow_html=True)

