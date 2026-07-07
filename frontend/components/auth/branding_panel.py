"""
=========================================================
Smart CA
Branding Panel
=========================================================
Reusable branding panel for all authentication screens.
"""

from pathlib import Path
import streamlit as st


# ---------------------------------------------------------
# Assets
# ---------------------------------------------------------

LOGO = Path("assets/images/logo.png")
ILLUSTRATION = Path("assets/images/login.png")


FEATURES = [
    "AI Powered Financial Planning",
    "Income & Expense Tracking",
    "Investment Portfolio Management",
    "Income Tax Planning",
    "Government Scheme Guidance",
]


# ---------------------------------------------------------
# Branding Panel
# ---------------------------------------------------------

def render_branding_panel():
    """
    Left branding panel.
    """

    # Logo
    if LOGO.exists():
        st.image(str(LOGO), width=70)
    else:
        st.markdown("# 💼 Smart CA")

    st.write("")

    st.title("Smart CA")

    st.caption("AI Powered Financial Assistant")

    st.write("")

    st.markdown(
        """
Manage your finances confidently using AI.

Track income, optimize taxes,
grow investments, and receive
personalized financial guidance.
"""
    )

    st.write("")

    st.subheader("Features")

    for feature in FEATURES:
        st.success(feature)

    st.write("")

    st.info(
        """
🔒 Bank-grade security

Your financial data is encrypted
and protected using secure authentication.
"""
    )

    st.write("")

    if ILLUSTRATION.exists():

        st.image(
            str(ILLUSTRATION),
            use_container_width=True,
        )

    st.caption(
        "Trusted by families across India."
    )