"""
=========================================================
Smart CA
Global Theme Loader
=========================================================

Loads the global stylesheet for the entire application.

Every page automatically gets the same UI.
"""

from pathlib import Path
import streamlit as st


CSS_FILE = Path("assets/styles.css")


def load_theme():
    """
    Load global CSS.
    """

    if CSS_FILE.exists():

        with open(CSS_FILE, encoding="utf-8") as css:

            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True,
            )

    else:

        st.warning(
            "styles.css not found."
        )