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
    st.title("City of Missoula - Expenditure Budget Training Tool")
    st.markdown("""
    Welcome to the City of Missoula's interactive training tool. This resource was created to help users understand how budgeted expenditures align with the City's strategic pillars and to provide insight into priority-based budgeting in practice. 
    A few important notes before you being: 
    - This tool presents budgeted expenditures only, not actual spending. 
    - Transfers have been excluded to avoid double counting, and revenues are not shown. 
    - The interactive dashboard data views reflect a single fiscal year at a time. 
    - The information is drawn from program inventory sheets completed by budget managers for every budgeted expenditure across the City.  
    
    While this is not a comprehensive view of the full City budget, it offers valuable context about how resources are allocated to support strategic budget priorities. 
                
    Use the navigation above to explore background context, interact with real program data, and try your hand at making funding decisions! 
                
    You may also advance to the next page by selecting the next button at the bottom of each page. 
    """)
    next_button(pages_list)

# ------------------
# Background Page
# ------------------
def page_background(pages_list):
    st.header("Background & Purpose of This Tool")
    st.markdown("""
    This internal training tool is built using real data from the City of Missoula's budget process. It's designed to help staff better understand how the City's values are reflected in budget decisions.

    This tool will help you:
    - Build familiarity with **program-level budgeting**
    - Demonstrate how **strategic priorities influence financial choices**
    - Practice **navigating public data** and consider **budget trade-offs**

    This tool includes visualizations, a hands-on activity, and a lined dashboard with the most recent fiscal year's data. 
    """)
    next_button(pages_list)

# ------------------
# Dashboard Page
# ------------------
def page_dashboard(pages_list):
    st.header("Explore the Program Inventory and Budget Dashboard")

    st.markdown("""
This interactive dashboard displays program-level budget data alongside key qualitative attributes from the City's program inventory, including:

- Mandates (legal or regulatory requirements)
- Service level requirements set by third parties
- Community reliance
- Trends in service demand
- Program risk and sustainability
- Alignment with strategic priorities

Use the slicers and filters to explore how budgeted expenditures relate to these attributes. This will help build context before you dive into the training activity.
""")

    # Embedded Power BI dashboard from secure gov.us environment
    st.markdown("""
<iframe title="Final_Dashboard_20250428"
    width="100%" height="650"
    src="https://app.powerbigov.us/view?r=eyJrIjoiMTYxNmYxYTgtYjhjZC00YjdhLTliOTItMDY3YmEzODY0ZTczIiwidCI6Ijc4MGM5OGZhLTc3ZDYtNGMwZi05NzJhLTM5YjQ5MGE0ZjY0MSJ9"
    frameborder="0" allowFullScreen="true">
</iframe>
""", unsafe_allow_html=True)

    next_button(pages_list)

# ------------------
# Training Tool Page
# ------------------
def page_training_tool(pages_list):
    st.header("Make Your Budget Decisions")
    st.markdown("""
    Now it's your turn to allocate some of the remaining funding across the City of Missoula's four strategic pillars. 
    
    Keep in mind that in the dashboard you were able to see how nearly half of the City's total budget is already committed to mandated services and legally required obligations, your task is to decide how to allocate the remaining resources.
    
    As you make your choices, you'll receive immediate feedback on how your budget reflects City priorities, highlighting potential trade-offs, risks, and areas of alignment.
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
        elif safety < 30:
            impact.append("⚠️ Low funding may impact emergency services and public health.")

        if community >= 35:
            impact.append("✅ Clear priority on community design and livability.")
        elif community < 30:
            impact.append("⚠️ Risk of underfunding quality of life and placemaking programs.")

        if resilience >= 25:
            impact.append("✅ Emphasis on internal systems and sustainable operations.")
        elif resilience < 20:
            impact.append("⚠️ Low investment in internal infrastructure may reduce efficiency.")

        if economy >= 15:
            impact.append("✅ Support for business development and economic resilience.")
        elif economy < 10:
            impact.append("⚠️ Limited focus on local economic growth and jobs.")

        if total > 100:
            impact.append("⚠️ Your allocation exceeds 100%. Please rebalance.")

        if total < 100:
            impact.append("You still have some budget left! See if you can allocate more towards some of the strategic goals.")

        for line in impact:
            st.markdown(f"- {line}")
    next_button(pages_list)


# ------------------
# Learn More Page
# ------------------
def page_learn_more(pages_list):
    st.header("Learn More About This Project")
    st.markdown("""
    This interactive tool was developed as part of a Master of Science, Business Analytics (MSBA) Capstone project at the University of Montana.
                
    For further in depth information about Missoula's budget process, you can dive into the [City of Missoula's Budget online.](https://www.ci.missoula.mt.us/budget)
                
    #### 🔬 Data Sources
    - City of Missoula Program Inventory
    - Departmental Expenditure Status

    #### 🎓 Final Project Deliverables
    - Streamlit digital product (this internal training app!)
    - A comprehensive written product that details the entire data engineering and analysis process, from start to finish. (Located within the GitHub Repository)
    - Interactive Power BI Dashboard (embedded views provided within this training app)

    #### 📂 GitHub Repository
    [View the entire codebase and supporting project materials](https://github.com/breannanpr/CityofMissoulaBudgetCapstone)
                
    #### 👩‍💻 About the Data Engineering Analyst
    [**Breanna Niekamp**](https://www.linkedin.com/in/breanna-niekamp/) is a data engineer/analyst based in the local area of Missoula, Montana, 
    who blends storytelling, strategy and data design thinking to help increase communication transparancy
    surrounding projects that involve informed data-driven business decisions.
    
    #### Feedback and Technical Support
    Do you have any feedback you'd like to submit about this training module? [Feel free to share your thoughts, suggestions and any technical errors!](https://docs.google.com/forms/d/e/1FAIpQLSdOltLVM-Sb7vrwDpKbwmf82047GzrqpWmDYE8fHGUFD-22lw/viewform?usp=header) 

    """, unsafe_allow_html=True)