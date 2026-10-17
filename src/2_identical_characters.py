"""
Task 2 - Find the longest sequence of identical characters.

Given a string, find the longest consecutive run of the same character.
The task forbids the built-in max() function, so the "best run so far"
is tracked manually inside the loop.

Focus: loops, adjacent-character comparison, tracking current/best result.
"""


def find_longest_sequence(s: str) -> tuple[str, int]:
    """Return the longest run of identical characters in *s*.

    Args:
        s: The input string to scan.

    Returns:
        A (sequence, length) tuple where *sequence* is the longest run
        of the same character (e.g. "cccc") and *length* is its size.
    """
    # An empty string contains no runs at all.
    if not s:
        return "", 0

    # Track the best (longest) run found so far.
    best_char = s[0]
    best_len = 1

    # Track the run currently being counted.
    current_char = s[0]
    current_len = 1

    # Walk over the remaining characters, comparing each one against
    # the character we are currently counting.
    for char in s[1:]:
        if char == current_char:
            # Same character: keep extending the current run.
            current_len += 1
        else:
            # New character: start a fresh run of length 1.
            current_char = char
            current_len = 1

        # If the current run beats the best so far, remember it.
        if current_len > best_len:
            best_len = current_len
            best_char = current_char

    return best_char * best_len, best_len


def main() -> None:
    """Run the example from the task description."""
    s = "aaabbccccdaa"

    sequence, length = find_longest_sequence(s)

    print(f"Longest sequence: {sequence}")
    print(f"Length: {length}")


if __name__ == "__main__":
    main()
