import streamlit as st
import pandas as pd 
from matplotlib import pyplot as plt
import streamlit.components.v1 as components

def display():
    c1, c2 = st.columns([9,1])
    c1.title("Welcome to uScore")
    if c2.button("Logout"):
        st.session_state["login"]=""
    action = st.sidebar.selectbox("Select action", 
             ["Data status", "Upload institutional data", "Upload program data", "Check uploaded data", "See indicators", "Help"])
    if action == "Data status":
        st.header(action)
        st.warning("Must send institution and program data for 2021/20 year before Dec 31th, 2021.")
    elif action == "Upload institutional data":
        st.header(action)
        st.file_uploader("Institutional Data", type=["csv"])
        with st.expander("Help with institutional data"):
            st.write("The format is the following:")
            st.download_button(label='csv template', data=b"1001", file_name="csv_template.csv", key="institution")
            st.write("An example with dummy data:")
            st.download_button(label='csv example', data=b"1001", file_name="csv_example.csv", key="institution")
    elif action == "Upload program data":
        st.header(action)
        st.file_uploader("Program Data", type=["csv"])
        with st.expander("Help with program data"):
            st.write("The format is the following:")
            st.download_button(label='csv template', data=b"1001", file_name="csv_template.csv", key="program")
            st.write("An example with dummy data:")
            st.download_button(label='csv example', data=b"1001", file_name="csv_example.csv", key="program")
    elif action == "Check uploaded data":
        st.header(action)
        st.subheader("Institution data")
        df = pd.DataFrame(columns = ["Institution data", "Year", "Status"],
                    data = [  
                    ["SUAD", "2019/18", "18-10-2021 (user@mail)"],
                    ["SUAD", "2020/19", "18-10-2021 (user@mail)"],
                    ["SUAD", "2021/20", "-"],
                    ])
        st.table(df)
        st.subheader("Program data")
        df = pd.DataFrame(columns = ["Institution data", "Year", "Status"],
                    data = [  
                    ["SUAD", "2019/18", "18-10-2021 (user@mail)"],
                    ["SUAD", "2020/19", "18-10-2021 (user@mail)"],
                    ["SUAD", "2021/20", "-"],
                    ])
        st.table(df)
    elif action == "See indicators":
        st.header(action)
        st.image("images/pbi.png")
    elif action == "Help":
        st.header(action)
        with st.expander("FAQ"):
            st.write("Lorem Ipsum")
        with st.expander("Troubleshooting"):
            st.write("Lorem Ipsum")
            