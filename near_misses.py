"""
Title: Fermat's Last Theorem Near Misses
Source file: near_misses.py

External input files required: none
External output files created: none

Programmers:
    Khamruddin Javeed (khamruddinjaveedmo@lewisu.edu)
    Partner: N/A (working individually)

Course: CPSC-60500-004
Date completed: TBD

Program description:
    This program interacts with the user to search for "near misses" of the
    equation x^n + y^n = z^n for n > 2. The user provides:
        - n: the exponent (3 ≤ n ≤ 11)
        - k: the upper bound for x and y (k > 10)
    The program will systematically check integer pairs (x, y) where
    10 ≤ x, y ≤ k, compute x^n + y^n, find the closest integer z that
    "almost" satisfies x^n + y^n = z^n, and track the smallest relative
    miss. The search logic will be implemented in later steps.

Resources used:
    none yet

Language & version:
    Python 3.12

How to run (short):
    python near_misses.py
"""


def get_exponent_n():
    """
    Prompt the user for the exponent n.
    Ensures n is an integer and 3 <= n <= 11.
    Keeps asking until a valid value is entered.

    Returns:
        int: a valid exponent n in the range [3, 11].
    """
    while True:
        raw = input("Enter the exponent n (an integer between 3 and 11, inclusive): ")

        try:
            n = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number between 3 and 11.\n")
            continue

        if 3 <= n <= 11:
            return n
        else:
            print("Out of range. n must be between 3 and 11 (inclusive). Please try again.\n")


def get_k_limit():
    """
    Prompt the user for the upper limit k.
    Ensures k is an integer greater than 10.
    Keeps asking until a valid value is entered.

    Returns:
        int: a valid upper limit k > 10.
    """
    while True:
        raw = input("Enter the upper limit k for x and y (an integer greater than 10): ")

        try:
            k = int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number greater than 10.\n")
            continue

        if k > 10:
            return k
        else:
            print("Out of range. k must be greater than 10. Please try again.\n")


def main():
    """
    Main program entry point.
    - Print an introduction
    - Ask the user for n (3–11)
    - Ask the user for k (>10)
    - For now, just echo the values back
      (the near-miss search will be added in the next step).
    """
    print("=== Fermat's Last Theorem Near Miss Search ===\n")

    # Get validated exponent n from the user
    n = get_exponent_n()

    # Get validated upper limit k from the user
    k = get_k_limit()

    # Confirm inputs to the user
    print("\nYou entered:")
    print(f"  Exponent n = {n}")
    print(f"  Upper limit k = {k}\n")

    print("Next step (not yet implemented): search for near misses using these values.")

    # Pause at the end so user can see the output (optional but nice for UX)
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()
