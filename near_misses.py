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
    The program systematically checks all integer pairs (x, y) where
    10 ≤ x, y ≤ k, computes x^n + y^n, finds the closest integer z that
    "almost" satisfies x^n + y^n = z^n, and tracks the smallest relative
    miss. Each time a new best near miss is found, it is printed. When all
    combinations are exhausted, the best (smallest) relative miss is printed
    last so the user can review it.

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


def find_near_misses(n, k):
    """
    Perform the near-miss search for the given exponent n and upper limit k.

    For each integer pair (x, y) with 10 <= x, y <= k, this function:
      - Computes S = x^n + y^n
      - Finds nearby integers z and z+1 such that their n-th powers
        "bracket" S (z^n <= S <= (z+1)^n)
      - Computes the absolute miss and the relative miss (miss / S)
    It tracks and returns the best (smallest) relative miss found.

    Args:
        n (int): the exponent, with 3 <= n <= 11.
        k (int): the upper bound for x and y, with k > 10.

    Returns:
        dict: information about the best near miss found, including:
            {
                "x": int,
                "y": int,
                "z": int,
                "n": int,
                "sum_powers": int,
                "closest_power": int,
                "miss": int,
                "relative_miss": float
            }
    """
    # Track the smallest relative miss and its details
    best_relative_miss = None
    best_result = None

    # Loop over all allowed x values
    for x in range(10, k + 1):
        # Loop over all allowed y values
        for y in range(10, k + 1):
            # Compute x^n + y^n for this pair
            sum_powers = (x ** n) + (y ** n)

            # Approximate n-th root of sum_powers to get initial z
            approx_root = int(sum_powers ** (1.0 / n))
            if approx_root < 1:
                approx_root = 1

            z = approx_root

            # Move z up until (z+1)^n is greater than S, so z and z+1 bracket S
            while (z + 1) ** n <= sum_powers:
                z += 1

            # Just in case z^n overshoots, move z down
            while z > 1 and (z ** n) > sum_powers:
                z -= 1

            # Powers on each side of S
            lower_power = z ** n
            upper_power = (z + 1) ** n

            # Miss from below and above
            miss_from_lower = sum_powers - lower_power
            miss_from_upper = upper_power - sum_powers

            # Choose the closer one as the actual miss
            if miss_from_lower <= miss_from_upper:
                miss = miss_from_lower
                closest_power = lower_power
                closest_z = z
            else:
                miss = miss_from_upper
                closest_power = upper_power
                closest_z = z + 1

            # Relative miss (fraction of the sum)
            relative_miss = miss / sum_powers

            # If this is the first or a better near miss, update best
            if best_relative_miss is None or relative_miss < best_relative_miss:
                best_relative_miss = relative_miss
                best_result = {
                    "x": x,
                    "y": y,
                    "z": closest_z,
                    "n": n,
                    "sum_powers": sum_powers,
                    "closest_power": closest_power,
                    "miss": miss,
                    "relative_miss": relative_miss,
                }

                # Print this new best near miss with clear labels
                percent = relative_miss * 100.0
                print("New best near miss found:")
                print(f"  x = {x}, y = {y}, z = {closest_z}, n = {n}")
                print(f"  x^n + y^n = {sum_powers}")
                print(f"  Closest z^n (or (z+1)^n) = {closest_power}")
                print(f"  Absolute miss = {miss}")
                print(f"  Relative miss = {relative_miss:.8f} ({percent:.6f}%)\n")

    return best_result


def main():
    """
    Main program entry point.
    - Ask the user for n (3–11)
    - Ask the user for k (>10)
    - Search for near misses
    - Print the final/best near miss last
    - Pause so the user can review the output
    """
    print("=== Fermat's Last Theorem Near Miss Search ===")
    print("This program searches for 'near misses' of the equation:")
    print("    x^n + y^n = z^n  (for n > 2)")
    print("It checks integer pairs (x, y) and finds z that makes the")
    print("left-hand side as close as possible to some z^n.\n")

    # Get validated exponent n from the user
    n = get_exponent_n()

    # Get validated upper limit k from the user
    k = get_k_limit()

    # Confirm inputs
    print("\nYou entered:")
    print(f"  Exponent n = {n}")
    print(f"  Upper limit k = {k}\n")

    print("Searching for near misses... (this may take some time for large k)\n")

    # Run the near miss search
    best = find_near_misses(n, k)

    # Print final/best result clearly at the end
    if best is not None:
        final_percent = best["relative_miss"] * 100.0
        print("=== Final / Best Near Miss Found ===")
        print(f"  x = {best['x']}, y = {best['y']}, z = {best['z']}, n = {best['n']}")
        print(f"  x^n + y^n = {best['sum_powers']}")
        print(f"  Closest z^n (or (z+1)^n) = {best['closest_power']}")
        print(f"  Absolute miss = {best['miss']}")
        print(f"  Relative miss = {best['relative_miss']:.8f} ({final_percent:.6f}%)")
        print("  (This is the smallest relative miss found for the given n and k.)")
    else:
        print("No near miss was found (this should not normally occur for these ranges).")

    # Pause at the end for user to review output
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()