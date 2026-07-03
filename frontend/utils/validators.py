"""
Validation utilities for Smart CA.
"""

import re


def validate_email(email: str) -> tuple[bool, str]:
    """Validate email address."""

    email = email.strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if not email:
        return False, "Email is required."

    if not re.match(pattern, email):
        return False, "Invalid email address."

    return True, ""


def validate_password(password: str) -> tuple[bool, str]:
    """Validate password."""

    if len(password) < 8:
        return False, "Password must be at least 8 characters."

    return True, ""


def validate_phone(phone: str) -> tuple[bool, str]:
    """Validate phone number."""

    phone = phone.strip()

    if not phone:
        return False, "Phone number is required."

    if not phone.isdigit():
        return False, "Phone number should contain only digits."

    if len(phone) != 10:
        return False, "Phone number must contain 10 digits."

    return True, ""


def validate_name(name: str) -> tuple[bool, str]:
    """Validate full name."""

    name = name.strip()

    if len(name) < 2:
        return False, "Full name is required."

    return True, ""