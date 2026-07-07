"""
=========================================================
Smart CA
Authentication Layout Component
=========================================================

Shared layout used by:

• Login Page
• Register Page

This component renders the split authentication screen
with a branding panel on the left and a form container
on the right.
"""

from pathlib import Path

import streamlit as st


LOGO_PATH = Path("assets/images/logo.png")
LOGIN_IMAGE = Path("assets/images/login.png")


def render_auth_layout(
    *,
    title: str,
    subtitle: str,
    form_renderer,
):
    """
    Render authentication layout.

    Parameters
    ----------
    title : str
        Right panel title.

    subtitle : str
        Right panel subtitle.

    form_renderer : Callable
        Function responsible for rendering
        the form content.
    """

    left_col, right_col = st.columns(
        [1.15, 0.85],
        gap="large",
    )

    # =====================================================
    # LEFT PANEL
    # =====================================================

    with left_col:

        with st.container():

            if LOGO_PATH.exists():

                st.image(
                    str(LOGO_PATH),
                    width=72,
                )

            else:

                st.markdown("# 💼 Smart CA")

            st.markdown(
                """
### AI Powered Financial Assistant
                """
            )

            st.write("")

            st.markdown(
                """
Manage your finances smarter using one intelligent platform.

✔ Tax Planning

✔ Budget Management

✔ Investment Tracking

✔ Government Schemes

✔ AI Financial Insights
                """
            )

            st.write("")

            if LOGIN_IMAGE.exists():

                st.image(
                    str(LOGIN_IMAGE),
                    use_container_width=True,
                )

            st.success(
                "Your information is encrypted and secured."
            )

    # =====================================================
    # RIGHT PANEL
    # =====================================================

    with right_col:

        with st.container():

            st.subheader(title)

            st.caption(subtitle)

            st.write("")

            form_renderer()
    # =====================================================
# BRANDING CARD
# =====================================================

def render_branding_card():
    """
    Display branding and trust information
    on the left panel.
    """

    st.markdown("---")

    st.markdown("### Why Smart CA?")

    features = [
        "📊 AI Powered Financial Analysis",
        "💰 Smart Budget Tracking",
        "📈 Investment Portfolio Insights",
        "🧾 Income Tax Planning",
        "📂 Secure Document Management",
        "🏦 Government Scheme Recommendations",
    ]

    for feature in features:
        st.write(feature)

    st.write("")

    st.info(
        """
        🔒 **Enterprise Grade Security**

        Your financial data is encrypted and protected
        using secure authentication and modern security
        practices.
        """
    )


# =====================================================
# FOOTER
# =====================================================

def render_footer():
    """
    Shared authentication footer.
    """

    st.write("")

    st.divider()

    st.caption(
        "© 2026 Smart CA • AI Powered Financial Assistant"
    )

    st.caption(
        "Made for Middle Class Families ❤️"
    )


# =====================================================
# COMPLETE AUTH SCREEN
# =====================================================

def render_auth_screen(
    *,
    title: str,
    subtitle: str,
    form_renderer,
):
    """
    Complete authentication page.

    This combines

    • Left Branding Panel
    • Right Authentication Card
    • Footer

    Parameters
    ----------
    title
        Card heading

    subtitle
        Card description

    form_renderer
        Function that renders
        login/register form.
    """

    render_auth_layout(
        title=title,
        subtitle=subtitle,
        form_renderer=form_renderer,
    )

    render_footer()