from components.auth_layout import auth_layout
from components.auth_branding import branding_panel
from components.login_form import login_form


def login_page():

    auth_layout(
        left_content=lambda: branding_panel(
            title="Welcome Back!",
            subtitle="Login to continue to your Smart CA account.",
        ),
        right_content=login_form,
    )