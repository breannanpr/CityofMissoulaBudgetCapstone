## Environment and Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# ------------------------
# Page Setup + Styling
# ------------------------

st.set_page_config(page_title="You Be the Budget Director", layout="wide")

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

# Inject custom CSS styles

st.markdown(f"""
    <style>
        .sidebar .sidebar-content {{ background-color: {COLORS['wheat']}; }}
        .block-container {{ padding-top: 2rem; }}
        .stSlider > div {{ color: {COLORS['griz_maroon']}; }}
        .stButton > button {{ border-radius: 8px; background-color: {COLORS['lubrecht_green']}; color: white; padding: 0.5em 1.5em; }}
        .stButton > button:hover {{ background-color: {COLORS['copper_climb']}; }}
        h1, h2, h3, h4 {{ color: {COLORS['griz_maroon']}; }}
        .title-text {{ background-color: rgba(255,255,255,0.92); padding: 1rem; border-radius: 10px; max-width: 850px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2); }}
        ul {{ line-height: 1.5em; }}
        .impact-check {{ font-size: 1.1em; }}
        .next-button-container {{ text-align: center; margin-top: 2rem; }}
    </style>
""", unsafe_allow_html=True)

# ------------------------
# Initialize Session State
# ------------------------

if 'housing' not in st.session_state:
    st.session_state.update({
        'housing': 20, 'climate': 20, 'equity': 20, 'safety': 20, 'submitted': False
    })

if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 0

# ------------------------
# Load Data Once (cached)
# ------------------------

@st.cache_data
def load_data():
    exp = pd.read_csv("cleaned_outputs/cleaned_expenditure_status.csv")
    prog = pd.read_csv("cleaned_outputs/cleaned_program_inventory.csv")
    prog.columns = prog.columns.str.strip().str.lower().str.replace(" ", "_")
    return exp, prog

exp_data, prog_data = load_data()

# ------------------------
# Navigation + Pages
# ------------------------
pages = [
    "Welcome", "Landscape", "Strategy in Action",
    "Moves", "Impact", "Data Cleaning Deep Dive",
    "Insights", "Learn More"
]

# Create page functions
def page_welcome():
    st.image("assets/welcome_missoula.jpg", use_column_width=True)
    st.markdown(f"""<div class="title-text">
        <h1 style="text-shadow: 1px 1px 2px {COLORS['snowbowl_silver']};">You Be the Budget Director</h1>
        <h3>Welcome to an interactive budget simulator rooted in transparency, data, and strategy.</h3>
        <p>This tool empowers users to experience the complex trade-offs of public budgeting through real program data from the City of Missoula.</p>
        <ul>
            <li>A formal written product (linked)</li>
            <li>A live presentation and defense</li>
            <li>This digital product</li>
            <li>A future interactive Power BI dashboard</li>
        </ul>
        <p>Navigate using the sidebar or the "Next Page" button below.</p>
    </div>""", unsafe_allow_html=True)
    next_button()

def page_landscape():
    st.header("Understanding Missoula's Program Landscape")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Mandated vs Non-Mandated")
        sns.countplot(data=prog_data, x="mandate_e41_yn", palette=[COLORS['glacier_sky'], COLORS['copper_climb']])
        st.pyplot(plt.gcf()); plt.clf()
    with col2:
        st.subheader("Risk Levels")
        sns.countplot(data=prog_data, y="risk_e93_type", palette="rocket")
        st.pyplot(plt.gcf()); plt.clf()
    st.subheader("Top Departments by Program Count")
    dept_counts = prog_data['department_h6'].value_counts().nlargest(10)
    dept_counts[::-1].plot(kind='barh', color=sns.color_palette("viridis", 10))
    st.pyplot(plt.gcf()); plt.clf()
    next_button()

def page_strategy():
    st.header("How Programs Align With Strategic Goals")
    top_programs = prog_data.sort_values(by="personnel_g27", ascending=False).head(10)
    st.dataframe(top_programs[["program_title_h8", "personnel_g27", "ftes_h36", "strategic_goal_e66_name"]])
    high_risk = prog_data[(prog_data['risk_e93_type'] != 'Low/No Risk') & (prog_data['total_expenditures_g33'] > 1_000_000)]
    st.subheader("High-Risk, High-Budget Programs")
    st.dataframe(high_risk.head(10))
    st.subheader("FTE vs Personnel Cost")
    fig, ax = plt.subplots()
    sns.scatterplot(data=prog_data, x="ftes_h36", y="personnel_g27", hue="risk_e93_type", ax=ax)
    st.pyplot(fig)
    next_button()

def page_moves():
    st.header("Allocate Your Budget")
    st.markdown("Adjust the sliders to reflect your funding priorities across four key strategy pillars.")

    st.slider("Housing & Affordability", 0, 100, key='housing')
    st.slider("Climate & Sustainability", 0, 100, key='climate')
    st.slider("Equity & Inclusion", 0, 100, key='equity')
    st.slider("Public Safety & Services", 0, 100, key='safety')

    total = st.session_state['housing'] + st.session_state['climate'] + st.session_state['equity'] + st.session_state['safety']
    st.metric("Total Allocated", f"{total}%")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Submit Allocation"):
            st.session_state['submitted'] = True
            st.success("Submitted! Go to 'See the Impact'.")
    with col2:
        if st.button("Reset Allocation"):
            st.session_state.update({ 'housing': 20, 'climate': 20, 'equity': 20, 'safety': 20, 'submitted': False })
            st.success("Allocation reset.")

    next_button()

def page_impact():
    st.image("assets/missoula_city_snow.JPG", use_column_width=True)
    st.header("Your Budget Impact")

    if st.session_state['submitted']:
        st.success("Here's how your budget reflects your values:")

        impact = []
        if st.session_state['housing'] > 30:
            impact.append("✅ Strong investment in affordable housing and homelessness support")
        if st.session_state['climate'] > 25:
            impact.append("✅ Funding aligned with Missoula's climate action goals")
        if st.session_state['equity'] > 25:
            impact.append("✅ Equity is a driving factor in your budget choices")
        if st.session_state['safety'] < 15:
            impact.append("⚠️ Public safety may be underfunded")
        if sum([st.session_state[k] for k in ['housing', 'climate', 'equity', 'safety']]) > 100:
            impact.append("⚠️ Your allocation exceeds 100%")

        for line in impact:
            st.markdown(f"- {line}")
    else:
        st.info("Please submit your allocation in the previous section to see your impact.")

    next_button()

def page_cleaning():
    st.header("The Data Journey: Cleaning and Transformation")
    st.markdown("This section walks through how raw, inconsistent municipal data was transformed into clean, analysis-ready structure.")

    st.subheader("Step 1: Normalize Column Names")
    st.code("prog.columns = prog.columns.str.strip().str.lower().str.replace(' ', '_')")

    st.subheader("Step 2: Preview Cleaned Program Inventory")
    st.dataframe(prog_data.head())

    st.subheader("Step 3: Clean Object Codes and Join Descriptions")
    st.code("exp_data['full_code'] = exp_data['fund_no'].astype(str) + '-' + exp_data['object_code'].astype(str)")

    st.subheader("Step 4: Aggregated Program-Level Spending")
    summary = exp_data.groupby('department')['adjusted_appropriation'].sum().reset_index()
    st.dataframe(summary.sort_values(by='adjusted_appropriation', ascending=False).head(10))

    st.subheader("Step 5: Before and After Cleaning Example")
    raw_df = pd.DataFrame({"account_description": [" PERSONAL SERVICES  ", "contracted SERVICES", "UTILITY SERVICES"]})
    cleaned_df = raw_df.copy()
    cleaned_df['account_description'] = cleaned_df['account_description'].str.title().str.strip()
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Original**")
        st.dataframe(raw_df)
    with col2:
        st.markdown("**Cleaned**")
        st.dataframe(cleaned_df)

    next_button()

def page_insights():
    st.header("What We Learned")
    st.markdown("""
    After evaluating program-level risks, mandates, and spending, key trends emerged:
    - Programs aligned with strategic goals often have higher personnel costs and FTE counts.
    - Risk profiles correlate with budget concentration — high-risk programs often dominate top spending.
    - Non-mandated programs provide opportunities for innovation but are often less funded.
    """)

    st.subheader("Total Expenditures by Department")
    dept_spend = exp_data.groupby("department")["adjusted_appropriation"].sum().sort_values(ascending=True).tail(10)
    dept_spend.plot(kind='barh', color=COLORS['griz_maroon'])
    st.pyplot(plt.gcf()); plt.clf()

    st.subheader("Trends by Strategic Goal")
    goal_counts = prog_data['strategic_goal_e66_name'].value_counts().nlargest(10)
    sns.barplot(x=goal_counts.values, y=goal_counts.index, palette="crest")
    st.pyplot(plt.gcf()); plt.clf()

    next_button()

def page_learn_more():
    st.image("assets/downtown_river.jpg", use_column_width=True)
    st.header("About This Project")
    st.markdown("""
    This interactive simulator was developed as part of the final MSBA Capstone project at the University of Montana.

    #### 🎓 Project Deliverables
    - Streamlit digital product (this app!)
    - A written product ([View the document](#))
    - A capstone presentation (March 30)
    - Future Power BI dashboard extension

    #### 🔬 Data Sources
    - City of Missoula Program Inventory (2023)
    - Departmental Expenditure Status (FY24)

    #### 👩‍💻 About the Analyst
    <img src='assets/analyst.jpg' width='150'/>
    **Breni Niekamp** is a civic-focused data analyst who blends storytelling, strategy, and design thinking to help local governments make transparent, informed budget decisions.

    #### 📂 GitHub Repository
    [View the codebase](https://github.com/YOUR_GITHUB_REPO)
    """, unsafe_allow_html=True)

    next_button()

# Dictionary of all page functions
page_functions = {
    "Welcome": page_welcome,
    "Landscape": page_landscape,
    "Strategy": page_strategy,
    "Moves": page_moves,
    "Impact": page_impact,
    "Data Cleaning Deep Dive": page_cleaning,
    "Insights": page_insights,
    "Learn More": page_learn_more,
}

## Top Dropdown navigation for greater accessibility and mobile friendly execution
st.markdown("## Navigation")
selected_page = st.selectbox("Choose a page", pages, index=st.session_state['current_page'])
st.session_state['current_page'] = pages.index(selected_page)

# Run the selected page
page_functions[selected_page]()