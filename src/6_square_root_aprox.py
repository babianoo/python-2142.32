"""
Task 6 - Approximate a square root.

Approximate the square root of a positive number using incremental
approximation (adding a small increment each step) rather than math.sqrt().

Focus: while loops, approximation, epsilon (tolerance), and computational
cost.
"""


def approximate_square_root(number: float, epsilon: float = 0.01,
                            increment: float = 0.001) -> tuple[float, int]:
    """Approximate the square root of *number* by incremental stepping.

    Args:
        number: The (non-negative) number to take the square root of.
        epsilon: The acceptable error margin for the approximation.
        increment: How much to add to the guess on each step.

    Returns:
        A (guess, num_guesses) tuple with the final approximation and
        the number of steps taken.
    """
    num_guesses = 0
    current_guess = 0.0

    # Keep stepping up while we are still below the target and not yet
    # within epsilon of it.
    while (abs(current_guess ** 2 - number) >= epsilon
           and current_guess ** 2 <= number):
        current_guess += increment
        num_guesses += 1

    return current_guess, num_guesses


def main() -> None:
    """Ask the user for a number and print its approximate square root."""
    number = float(input("Enter number: "))

    if number < 0:
        print(f"Can't find the square root of a negative number {number}")
        return

    # Experiment: change *increment* (e.g. 0.01, 0.001, 0.0001) to see
    # the trade-off between speed and precision.
    guess, guesses = approximate_square_root(number, epsilon=0.01,
                                             increment=0.001)

    print(f"Approximate square root: {guess:.4f}")
    print(f"Number of guesses: {guesses}")


if __name__ == "__main__":
    main()
