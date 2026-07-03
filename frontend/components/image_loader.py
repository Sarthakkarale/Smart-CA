from pathlib import Path
import streamlit as st

IMAGE_DIR = Path(__file__).parent.parent / "assets" / "images"


def show_logo(width=180):
    path = IMAGE_DIR / "logo.png"
    if path.exists():
        st.image(str(path), width=width)


def show_login_hero(width=420):
    path = IMAGE_DIR / "login_hero.png"
    if path.exists():
        st.image(str(path), width=width)


def show_google_icon():
    path = IMAGE_DIR / "google.png"
    if path.exists():
        st.image(str(path), width=20)