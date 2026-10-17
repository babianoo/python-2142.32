"""
Task 3 - Password strength check.

Determine whether a password is "strong" by using loops to verify it
contains at least one uppercase letter, one lowercase letter, one digit,
and is at least 8 characters long.

Focus: loops over strings, Boolean flags, and conditions.
"""


def is_strong_password(password: str) -> bool:
    """Return True if *password* meets all strength requirements.

    A strong password must:
      * be at least 8 characters long,
      * contain at least one uppercase letter,
      * contain at least one lowercase letter, and
      * contain at least one digit.

    Args:
        password: The password string to evaluate.

    Returns:
        True if the password is strong, False otherwise.
    """
    # Minimum length requirement.
    if len(password) < 8:
        return False

    # Boolean flags tracking which character classes we have seen.
    has_lowercase = False
    has_uppercase = False
    has_digit = False

    # Loop over every character and update the relevant flag(s).
    for char in password:
        if char.islower():
            has_lowercase = True
        if char.isupper():
            has_uppercase = True
        if char.isdigit():
            has_digit = True

    # Strong only if every required character class was present.
    return has_lowercase and has_uppercase and has_digit


def main() -> None:
    """Ask the user for a password and report its strength."""
    password = input("Enter password: ")

    if is_strong_password(password):
        print("Password is strong")
    else:
        print("Password is weak")


if __name__ == "__main__":
    main()
