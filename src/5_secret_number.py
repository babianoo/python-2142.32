"""
Task 5 - Find the secret number (exhaustive enumeration).

Guess a secret number by trying every integer in order. Also show what
happens when only even numbers are checked.

Focus: exhaustive enumeration, range(), stopping conditions, and break.
"""


def secret_number_exhaustive(secret: int, start: int = 0) -> tuple[bool, int]:
    """Find *secret* by trying every integer from *start* up to *secret*.

    Args:
        secret: The number we are trying to find.
        start: The first number to guess (inclusive).

    Returns:
        A (found, guesses) tuple. *found* is True if the secret was
        located; *guesses* is the number of attempts made.
    """
    guesses = 0

    for guess in range(start, secret + 1):
        guesses += 1
        if guess == secret:
            return True, guesses

    return False, guesses


def secret_number_even_only(secret: int) -> tuple[bool, int]:
    """Find *secret* by checking only even numbers starting from 0.

    Note: this can never find an odd secret (such as 73).

    Args:
        secret: The number we are trying to find.

    Returns:
        A (found, guesses) tuple as described above.
    """
    guess = 0
    guesses = 0

    while guess <= secret:
        guesses += 1
        if guess == secret:
            return True, guesses
        # Skip ahead by 2 so only even numbers are ever checked.
        guess += 2

    return False, guesses


def main() -> None:
    """Run the examples from the task description."""
    secret = 73

    found, guesses = secret_number_exhaustive(secret)
    print(f"Secret number found: {secret}" if found else "Secret not found")
    print(f"Number of guesses: {guesses}")

    print()

    # Only even numbers are checked, so an odd secret is never found.
    found, guesses = secret_number_even_only(secret)
    if found:
        print(f"Secret number found: {secret}")
    else:
        print("Secret not found (odd secrets are never found when "
              "checking only even numbers)")
    print(f"Number of guesses: {guesses}")


if __name__ == "__main__":
    main()
