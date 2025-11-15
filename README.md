# Fermat's Last Theorem Near Misses

## Overview

This program searches for **“near misses”** to Fermat’s Last Theorem:

> xⁿ + yⁿ = zⁿ, for n > 2

Fermat’s Last Theorem says there are **no** natural number solutions for this equation when n > 2.  
Instead of looking for exact solutions, this program looks for **near misses**:

- We search integer pairs (x, y) where `10 ≤ x, y ≤ k`
- For each pair, we compute `S = xⁿ + yⁿ`
- We find the closest integer `z` such that `zⁿ` or `(z + 1)ⁿ` is closest to `S`
- We compute:
  - **Absolute miss** = distance between `S` and the closest power
  - **Relative miss** = `miss / S` (also shown as a percentage)

The program prints every time a **new best (smallest) relative miss** is found, and then prints the **final/best near miss** at the end.

---

## Inputs

When the program starts, the interactive user is prompted for:

1. **Exponent n**
   - Must be an integer
   - Constraint: `3 ≤ n ≤ 11`
   - The program re-prompts until a valid value is entered.

2. **Upper limit k**
   - Must be an integer
   - Constraint: `k > 10`
   - Defines the search range `10 ≤ x, y ≤ k`
   - The program re-prompts until a valid value is entered.

Invalid inputs (non-integers, out-of-range values) are handled gracefully with clear messages.

---

## Running the Program (Python)

### Requirements

- Python 3.10+ (tested with Python 3.12)
- No external libraries required

### How to run

From a terminal/command prompt in the project directory:

```bash
python near_misses.py
