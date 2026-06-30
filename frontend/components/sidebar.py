import streamlit as st
from streamlit_option_menu import option_menu


def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <div style="text-align:center;padding-top:10px;padding-bottom:25px;">
                <h2 style="margin-bottom:0;color:white;">
                    💼 Smart CA
                </h2>
                <p style="color:#CBD5E1;font-size:14px;">
                    AI Financial Advisor
                </p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        selected = option_menu(
            menu_title=None,
            options=[
                "Dashboard",
                "Financial Profile",
                "Documents",
                "AI Advisor",
                "Reports",
                "Settings",
                "Logout",
            ],
            icons=[
                "house-fill",
                "person-fill",
                "file-earmark-text-fill",
                "robot",
                "bar-chart-fill",
                "gear-fill",
                "box-arrow-right",
            ],
            default_index=0,
            styles={
                "container": {
                    "padding": "0!important",
                    "background-color": "#0F172A",
                },
                "icon": {
                    "color": "#CBD5E1",
                    "font-size": "18px",
                },
                "nav-link": {
                    "font-size": "15px",
                    "text-align": "left",
                    "margin": "6px",
                    "padding": "12px",
                    "border-radius": "10px",
                    "--hover-color": "#1E293B",
                },
                "nav-link-selected": {
                    "background-color": "#6D5EF8",
                    "color": "white",
                },
            },
        )

        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown(
            """
            <div style="
                background:#1E293B;
                padding:18px;
                border-radius:15px;
                text-align:center;
            ">
                <h4 style="color:white;">
                    Smart CA
                </h4>

                <p style="color:#CBD5E1;font-size:13px;">
                    Your AI Powered
                    Financial Assistant
                </p>

            </div>
            """,
            unsafe_allow_html=True,
        )

    return selected
