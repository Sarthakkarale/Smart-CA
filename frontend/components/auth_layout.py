import streamlit as st
from assets.theme import (
    LEFT_COLUMN_RATIO,
    RIGHT_COLUMN_RATIO,
)


def auth_layout(left_content, right_content):

    left, right = st.columns(
        [LEFT_COLUMN_RATIO, RIGHT_COLUMN_RATIO],
        gap="large",
        vertical_alignment="center",
    )

    with left:
        left_content()

    with right:
        st.write("")
        right_content()