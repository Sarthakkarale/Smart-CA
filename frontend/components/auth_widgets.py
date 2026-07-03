import streamlit as st

from components.common import spacer


# ==========================================================
# APP LOGO
# ==========================================================

def app_logo():

    st.markdown("# 💼 Smart CA")

    st.caption("AI Powered Financial Platform")


# ==========================================================
# HERO SECTION
# ==========================================================

def hero_section():

    spacer()

    st.header("Financial Intelligence")

    st.header("Made Simple")

    st.write(
        """
        Manage your taxes, investments,
        financial planning and reports
        from one intelligent platform.
        """
    )

    spacer()


# ==========================================================
# FEATURE CARD
# ==========================================================

def feature_card(icon, title, description):

    with st.container(border=True):

        col1, col2 = st.columns([1,5])

        with col1:
            st.markdown(f"## {icon}")

        with col2:

            st.markdown(f"**{title}**")

            st.caption(description)


# ==========================================================
# FEATURE SECTION
# ==========================================================

def feature_section():

    feature_card(
        "🔒",
        "Bank Grade Security",
        "Your financial data stays encrypted."
    )

    spacer()

    feature_card(
        "📊",
        "Smart Analytics",
        "Track tax, income and investments."
    )

    spacer()

    feature_card(
        "🤖",
        "AI Advisor",
        "Get intelligent financial suggestions."
    )


# ==========================================================
# STATS CARD
# ==========================================================

def stats_card():

    spacer(2)

    with st.container(border=True):

        st.caption("Estimated Tax Saving")

        st.metric(
            label="This Year",
            value="₹ 8.45 Lakh",
            delta="+18%"
        )

        st.progress(72)


# ==========================================================
# COMPLETE LEFT PANEL
# ==========================================================

def branding():

    app_logo()

    hero_section()

    feature_section()

    stats_card()