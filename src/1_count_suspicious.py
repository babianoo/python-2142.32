"""
Task 1 - Count suspicious words.

Given a log string of login attempts, count how many times "FAILED" and
"SUCCESS" occur. If there are more failures than successes, print a
warning about suspicious activity.

Focus: for loops, if statements, counters, and str.split().
"""


def count_attempts(log: str) -> tuple[int, int]:
    """Count failed and successful login attempts in *log*.

    Args:
        log: A whitespace-separated string of login outcomes,
             e.g. "LOGIN FAILED SUCCESS".

    Returns:
        A (failed, success) tuple with the two counters.
    """
    failed_count = 0
    success_count = 0

    # split() turns the log into a list of individual words so we can
    # inspect them one at a time.
    for word in log.split():
        if word == "FAILED":
            failed_count += 1
        elif word == "SUCCESS":
            success_count += 1

    return failed_count, success_count


def main() -> None:
    """Run the example from the task description."""
    log = "LOGIN FAILED FAILED SUCCESS FAILED LOGIN FAILED SUCCESS"

    failed_count, success_count = count_attempts(log)

    print(f"Failed attempts: {failed_count}")
    print(f"Successful attempts: {success_count}")

    # Warn only when failures outnumber successes.
    if failed_count > success_count:
        print("Warning: suspicious login activity")


if __name__ == "__main__":
    main()
