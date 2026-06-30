import streamlit as st


def show_navbar(page_title: str, user_name: str = "User"):
    """
    Top navigation bar for all pages.
    """

    col1, col2 = st.columns([8, 2])

    with col1:
        st.markdown(
            f"""
            <div style="padding-top:8px;">
                <div class="page-title">
                    {page_title}
                </div>

                <div class="page-subtitle">
                    Welcome back 👋
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:

        st.markdown(
            f"""
            <div style="
                display:flex;
                justify-content:flex-end;
                align-items:center;
                gap:15px;
                padding-top:18px;
            ">

                <div style="
                    font-size:22px;
                    cursor:pointer;
                ">
                    🔔
                </div>

                <div style="
                    background:white;
                    border-radius:50px;
                    padding:8px 15px;
                    box-shadow:0 5px 18px rgba(0,0,0,.08);
                    font-weight:600;
                    color:#1E293B;
                ">
                    👤 {user_name}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<hr>", unsafe_allow_html=True)