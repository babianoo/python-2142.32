"""
Task 7 - Bisection search.

Find a secret number within a known range by repeatedly halving the search
interval, instead of trying every value (exhaustive enumeration). Each step
cuts the remaining possibilities in half, making it much faster.

Focus: while loops, interval halving, and logarithmic search.
"""


def bisection_search(secret: int, low: int = 0, high: int = 1000) -> tuple[bool, int]:
    """Find *secret* in the inclusive range [low, high] using bisection.

    Args:
        secret: The number we are trying to find.
        low: The lower bound of the search range (inclusive).
        high: The upper bound of the search range (inclusive).

    Returns:
        A (found, guesses) tuple. *found* is True if the secret was
        located; *guesses* is the number of bisection steps taken.
    """
    num_guesses = 0

    # Keep halving the interval until the secret is found.
    while low <= high:
        num_guesses += 1
        # Guess the midpoint of the current interval.
        guess = (low + high) // 2

        if guess == secret:
            return True, num_guesses
        elif guess < secret:
            # Secret is in the upper half: move the lower bound up.
            low = guess + 1
        else:
            # Secret is in the lower half: move the upper bound down.
            high = guess - 1

    return False, num_guesses


def main() -> None:
    """Run the example from the task description."""
    secret = 731

    found, guesses = bisection_search(secret)

    if found:
        print(f"Secret number found: {secret}")
    else:
        print("Secret number not found")
    print(f"Number of guesses: {guesses}")


if __name__ == "__main__":
    main()
