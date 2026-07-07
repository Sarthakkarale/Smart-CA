"""
=========================================================
Smart CA
Financial Profile Wizard Component
=========================================================

Reusable wizard component used by:

• Create Profile
• Edit Profile

Author : Smart CA
"""

import streamlit as st


TOTAL_STEPS = 4


STEP_TITLES = [
    "Personal",
    "Financial",
    "Goals",
    "Review",
]


# ==========================================================
# STEP MANAGEMENT
# ==========================================================

def initialize_wizard():
    """
    Initialize wizard session state.
    """

    if "wizard_step" not in st.session_state:
        st.session_state.wizard_step = 1


def get_current_step() -> int:
    """
    Return current wizard step.
    """

    return st.session_state.wizard_step


def next_step():
    """
    Move to next step.
    """

    if st.session_state.wizard_step < TOTAL_STEPS:
        st.session_state.wizard_step += 1


def previous_step():
    """
    Move to previous step.
    """

    if st.session_state.wizard_step > 1:
        st.session_state.wizard_step -= 1


def reset_wizard():
    """
    Reset wizard.
    """

    st.session_state.wizard_step = 1


# ==========================================================
# HEADER
# ==========================================================

def render_header():
    """
    Wizard title.
    """

    st.title("Create Financial Profile")

    st.caption(
        "Complete your profile to unlock AI-powered financial insights."
    )

    st.write("")
# ==========================================================
# PROGRESS INDICATOR
# ==========================================================

def render_progress():
    """
    Render the 4-step progress indicator.
    """

    current_step = get_current_step()

    st.progress(current_step / TOTAL_STEPS)

    st.write("")

    cols = st.columns(TOTAL_STEPS)

    for index, col in enumerate(cols):

        step_number = index + 1

        with col:

            if step_number < current_step:

                st.success(f"✓ Step {step_number}")

            elif step_number == current_step:

                st.info(f"● Step {step_number}")

            else:

                st.caption(f"Step {step_number}")

            st.markdown(
                f"""
<div style="
text-align:center;
font-weight:600;
font-size:15px;
margin-top:8px;
">
{STEP_TITLES[index]}
</div>
                """,
                unsafe_allow_html=True,
            )

    st.write("")
    st.divider()


# ==========================================================
# NAVIGATION BUTTONS
# ==========================================================

def render_navigation(
    show_previous: bool = True,
    show_next: bool = True,
    next_label: str = "Next →",
    previous_label: str = "← Previous",
):
    """
    Render wizard navigation buttons.

    Returns
    -------
    tuple(bool, bool)
        (previous_clicked, next_clicked)
    """

    previous_clicked = False
    next_clicked = False

    left, spacer, right = st.columns([1, 3, 1])

    with left:

        if show_previous:

            previous_clicked = st.button(
                previous_label,
                use_container_width=True,
                key=f"wizard_prev_{get_current_step()}",
            )

    with right:

        if show_next:

            next_clicked = st.button(
                next_label,
                use_container_width=True,
                key=f"wizard_next_{get_current_step()}",
            )

    return previous_clicked, next_clicked


# ==========================================================
# STEP TITLE
# ==========================================================

def render_step_title(
    title: str,
    subtitle: str,
):
    """
    Display section heading for the current step.
    """

    st.subheader(title)

    st.caption(subtitle)

    st.write("")
# ==========================================================
# VALIDATION
# ==========================================================

def validate_step(step: int) -> bool:
    """
    Validate current wizard step.

    NOTE:
    Actual field validation will be added during
    backend integration in Sprint 2.

    Parameters
    ----------
    step : int

    Returns
    -------
    bool
    """

    return True


# ==========================================================
# SAVE BUTTON
# ==========================================================

def render_submit_button(
    label: str = "Save Financial Profile",
):
    """
    Render final submit button.

    Returns
    -------
    bool
    """

    st.write("")
    st.divider()
    st.write("")

    left, center, right = st.columns([1, 2, 1])

    with center:

        submitted = st.button(
            label,
            use_container_width=True,
            type="primary",
            key="wizard_submit_button",
        )

    return submitted


# ==========================================================
# STEP BADGE
# ==========================================================

def render_step_badge():
    """
    Display current step badge.
    """

    current = get_current_step()

    st.caption(
        f"Step {current} of {TOTAL_STEPS}"
    )


# ==========================================================
# COMPLETION MESSAGE
# ==========================================================

def render_completion():
    """
    Success message shown after profile creation.
    """

    st.success(
        """
🎉 Financial Profile Completed Successfully!

Your profile is now ready.

In Sprint 2 this data will be submitted
to the FastAPI backend.
        """
    )


# ==========================================================
# WIZARD CONTAINER
# ==========================================================

def render_wizard_header():
    """
    Render complete wizard header.
    """

    initialize_wizard()

    render_header()

    render_step_badge()

    render_progress()


# ==========================================================
# PUBLIC API
# ==========================================================

__all__ = [

    "initialize_wizard",

    "get_current_step",

    "next_step",

    "previous_step",

    "reset_wizard",

    "render_header",

    "render_progress",

    "render_navigation",

    "render_step_title",

    "render_submit_button",

    "render_completion",

    "render_wizard_header",

]