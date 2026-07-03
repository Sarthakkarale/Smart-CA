from components.auth_layout import auth_layout
from components.auth_branding import branding_panel
from components.register_form import register_form


def register_page():

    auth_layout(
        left_content=lambda: branding_panel(
            title="Welcome!",
            subtitle="Create your Smart CA account to get started.",
        ),
        right_content=register_form,
    )