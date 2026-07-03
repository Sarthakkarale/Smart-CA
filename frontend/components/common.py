import streamlit as st


# ==========================================================
# PAGE TITLE
# ==========================================================

def page_title(title: str, subtitle: str = ""):
    """
    Display a page title with optional subtitle.
    """

    st.title(title)

    if subtitle:
        st.caption(subtitle)


# ==========================================================
# SECTION TITLE
# ==========================================================

def section_title(title: str):
    """
    Display a section heading.
    """

    st.subheader(title)


# ==========================================================
# DIVIDER
# ==========================================================

def divider(label: str = "OR"):
    """
    Display a divider with centered text.
    """

    left, middle, right = st.columns([4, 1, 4])

    with left:
        st.divider()

    with middle:
        st.markdown(
            f"<div style='text-align:center; color:#64748B; font-weight:600;'>{label}</div>",
            unsafe_allow_html=True,
        )

    with right:
        st.divider()


# ==========================================================
# SPACER
# ==========================================================

def spacer(lines: int = 1):
    """
    Add vertical spacing.
    """

    for _ in range(lines):
        st.write("")


# ==========================================================
# INFO MESSAGE
# ==========================================================

def info_box(message: str):
    st.info(message)


# ==========================================================
# SUCCESS MESSAGE
# ==========================================================

def success_box(message: str):
    st.success(message)


# ==========================================================
# ERROR MESSAGE
# ==========================================================

def error_box(message: str):
    st.error(message)