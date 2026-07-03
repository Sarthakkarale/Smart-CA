from pathlib import Path
import streamlit as st


def branding_panel(
    title="Welcome Back!",
    subtitle="Login to continue to your Smart CA account.",
):
    """
    Smart CA Branding Panel
    Reusable for Login, Register, Forgot Password, etc.
    """

    # ==================================================
    # Logo
    # ==================================================

    logo_col, text_col = st.columns(
        [1, 5],
        vertical_alignment="center",
    )

    with logo_col:

        logo = Path("assets/images/logo_icon.png")

        if logo.exists():
            st.image(
                str(logo),
                width=42,
            )

    with text_col:

        st.subheader("Smart CA")
        st.caption("AI Powered Financial Advisor")

    st.write("")

    # ==================================================
    # Heading
    # ==================================================

    st.header(title)

    st.write(subtitle)

    st.write(
        """
Manage your taxes, investments,
financial planning, OCR document analysis,
AI insights and reports from one
intelligent platform.
"""
    )

    st.write("")

    # ==================================================
    # Illustration
    # ==================================================

    illustration = Path(
        "assets/images/login_illustration.png"
    )

    if illustration.exists():

        st.image(
            str(illustration),
            width=280,
        )

    st.write("")

    # ==================================================
    # Footer
    # ==================================================

    st.caption(
        "Your financial security is our priority."
    )