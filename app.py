import streamlit as st
from auth import register_user, login_user
from chat import save_message, get_messages
from streamlit_autorefresh import st_autorefresh

st.set_page_config(page_title="Real-Time Chat App")

if "user" not in st.session_state:
    st.session_state.user = None


st.title("💬 Real-Time Chat Application")


menu = st.sidebar.selectbox(
    "Menu",
    ["Login", "Register"]
)

# Register

if menu == "Register":

    st.subheader("Create Account")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):

        if register_user(username, password):
            st.success("Account created successfully")

        else:
            st.error("Username already exists")


# Login

elif menu == "Login":

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if login_user(username, password):

            st.session_state.user = username
            st.success("Login successful")

        else:
            st.error("Invalid credentials")


# Chat Page

if st.session_state.user:

    st.sidebar.success(f"Logged in as {st.session_state.user}")

    if st.sidebar.button("Logout"):
        st.session_state.user = None
        st.experimental_rerun()

    st.header("Chat Room")

    message = st.text_input("Enter message")

    if st.button("Send"):

        save_message(st.session_state.user, message)

    st_autorefresh(interval=3000, key="chatrefresh")

    st.subheader("Messages")

    for msg in get_messages():

        st.write(f"**{msg['user']}**: {msg['message']}")
