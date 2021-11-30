import streamlit as st
import pandas as pd

#st.set_page_config(page_title="ADEK | uScore", page_icon="adek.jpg")
#st.set_page_config(page_title="ADEK | uScore")
st.set_page_config(page_title="ADEK uScore", layout="wide")
df = pd.read_csv("users.csv")
auth_users = list(df["users"])


if "login" not in st.session_state:
    st.session_state["login"] = ""

if st.session_state["login"] == "":
    _, c, _ = st.columns([3,3,3])
    c.title("Welcome to uScore")
    c.write("Made by uPlanner for ADEK")
    username = c.text_input("Username:")
    password = c.text_input("Password:", value="", type="password")
    #_, c,_ = st.columns([3, 3, 3])
    if c.button("Login"):
        if username == "":
            st.error("Please provide a valid email")
        elif password == "":
            st.error("Wrong password")
        elif username not in auth_users:
            st.warning("Unauthorized used. Please contact uscore_support@adek.gov.ae for requesting access.")
        elif username in auth_users:
            if "@adek" in username:
                st.session_state["login"] = "adek"
            else:
                st.session_state["login"] = "suad"
elif st.session_state["login"] == "adek":
    from adek import display
    display()
elif st.session_state["login"] == "suad":
    from hei import display
    display()
else:
    st.warning("Unknown state")