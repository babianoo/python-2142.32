"""
Task 4 - Find all perfect cubes.

Ask the user for a positive integer n and print every perfect cube
(1^3, 2^3, ...) that is less than or equal to n, along with a total.

Focus: while/for loops, powers, and counters.
"""


def find_perfect_cubes(n: int) -> list[int]:
    """Return every perfect cube from 1 up to and including n.

    Args:
        n: The inclusive upper bound for the cubes.

    Returns:
        A list of perfect cubes in ascending order.
    """
    cubes = []

    # Start at 1^3 and keep raising i until i^3 exceeds n.
    i = 1
    while i ** 3 <= n:
        cubes.append(i ** 3)
        i += 1

    return cubes


def main() -> None:
    """Ask the user for n and print the perfect cubes up to n."""
    n = int(input("Enter n: "))

    cubes = find_perfect_cubes(n)

    for cube in cubes:
        print(cube)

    print(f"Total perfect cubes: {len(cubes)}")


if __name__ == "__main__":
    main()
