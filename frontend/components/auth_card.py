import streamlit as st


def auth_card(content):
    """
    Reusable authentication card.
    """

    with st.container(border=True):
        content()