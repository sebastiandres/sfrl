import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt

def display():
    c1, c2 = st.columns([9,1])
    if c2.button("Logout"):
        st.session_state["login"]=""
    c1.title("Welcome to uScore")
    action = st.sidebar.selectbox("Please select action:", options=["Data Status", "Received Data", "Metrics"])
    if action == "Data Status":
        st.header("Data Status")
        df = pd.DataFrame(columns = ["Institution", "Year", "Layout type", "Date", "Status"],
                             data = [  
                                ["SUAD", "2021/20", "Institution", "-", "Not sent"],
                                ["SUAD", "2020/19", "Institution", "01 Nov 2021", "OK"],
                                ["SUAD", "2019/18", "Institution", "01 Nov 2021", "Has error"],
                                ["SUAD", "2021/20", "Program", "-", "Not sent"],
                                ["SUAD", "2020/19", "Program", "01 Nov 2021", "OK"],
                                ["SUAD", "2019/18", "Program", "01 Nov 2021", "Has error"],
                                    ])
        st.table(df)
    elif action == "Received Data":
        st.header("Received data")
        hei = st.multiselect("Select institutions", ["SUAD", "ADP"])
        if hei:
            layout = st.selectbox("Data Layout", ["Institution", "Program"])
            if layout == "Institution":
                df = pd.read_csv("data/suad_institution.csv", dtype=str)
            else:
                df = pd.read_csv("data/suad_programs.csv", dtype=str)
            st.write(df.head(25))
    elif action == "Metrics":
        st.header("Metric of overall system")
        st.header(action)
        st.image("images/pbi.png")
