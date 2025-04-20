# data.py
# This file contains all data loading and preprocessing logic for the Streamlit app

import pandas as pd
import streamlit as st

# ------------------------
# Load and Cache Data
# ------------------------
@st.cache_data
def load_data():
    """
    Loads cleaned expenditure and program inventory data from the project folder.
    Returns two pandas DataFrames: exp_data, prog_data.
    """
    exp = pd.read_csv("../cleaned_outputs/cleaned_expenditure_status.csv")
    prog = pd.read_csv("../cleaned_outputs/cleaned_program_inventory.csv")

    # Clean column names in program data for consistency
    prog.columns = prog.columns.str.strip().str.lower().str.replace(" ", "_")

    return exp, prog