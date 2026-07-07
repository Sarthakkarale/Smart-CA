"""
=========================================================
Smart CA
Sidebar Component
=========================================================

Reusable sidebar navigation.

Used by:
- Dashboard
- Profile
- Reports
- Tax
- Investments
- Settings
"""

import streamlit as st

from utils.router import (
    navigate,
    get_current_page,
)


MENU_ITEMS = [
    ("dashboard", "🏠", "Dashboard"),
    ("profile", "👤", "Profile"),
    ("investments", "📈", "Investments"),
    ("tax", "🧾", "Tax Planning"),
    ("reports", "📊", "Reports"),
    ("settings", "⚙️", "Settings"),
]


def render_sidebar():
    """
    Render application sidebar.
    """

    with st.sidebar:

        st.markdown("")

        st.image(
            "assets/images/logo.png",
            width=70,
        )

        st.markdown(
            """
# Smart CA
AI Powered Financial Assistant
            """
        )

        st.divider()

        current = get_current_page()

        for page, icon, title in MENU_ITEMS:

            active = current == page

            label = f"{icon}  {title}"

            if active:
                label = f"✅ {icon}  {title}"

            if st.button(
                label,
                use_container_width=True,
                key=f"sidebar_{page}",
            ):
                navigate(page)

        st.divider()

        st.info(
            """
💡 Tip

Complete your Financial Profile
to unlock personalized AI
recommendations.
            """
        )
        # ==================================================
        # USER SECTION
        # ==================================================

        st.markdown("---")

        user_name = st.session_state.get(
            "user_name",
            "Guest User",
        )

        user_email = st.session_state.get(
            "user_email",
            "guest@smartca.ai",
        )

        col1, col2 = st.columns([1, 3])

        with col1:
            st.markdown("👤")

        with col2:
            st.markdown(
                f"""
**{user_name}**

<small style="color:#64748B;">
{user_email}
</small>
                """,
                unsafe_allow_html=True,
            )

        st.write("")

        # ==================================================
        # QUICK ACTIONS
        # ==================================================

        st.caption("Quick Actions")

        quick_col1, quick_col2 = st.columns(2)

        with quick_col1:

            if st.button(
                "➕ Add Income",
                use_container_width=True,
                key="quick_income",
            ):
                st.info("Income module coming soon.")

        with quick_col2:

            if st.button(
                "📂 Upload",
                use_container_width=True,
                key="quick_upload",
            ):
                st.info("Document upload coming soon.")

        st.write("")

        # ==================================================
        # LOGOUT
        # ==================================================

        st.divider()

        if st.button(
            "🚪 Logout",
            use_container_width=True,
            key="logout_button",
        ):

            st.session_state.current_page = "login"

            st.session_state.is_authenticated = False

            st.session_state.access_token = None

            st.session_state.refresh_token = None

            st.rerun()

        # ==================================================
        # FOOTER
        # ==================================================

        st.markdown("---")

        st.caption("Smart CA")

        st.caption("Version 1.0.0")

        st.caption("AI Powered Financial Assistant")