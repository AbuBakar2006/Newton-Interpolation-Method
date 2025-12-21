import numpy as np
import math


def gauss_backward_interpolation(x_values, y_values, x):
    n = len(x_values)

    # 1. Create the standard forward difference table
    # (It is easier to implement Gauss using a standard table and adjusting indices)
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # 2. Find the central index
    # For Gauss Backward, we usually pick the index just AFTER x if x is > mid
    # But conventionally, we pick the nearest index to start.
    idx = 0
    for i in range(n - 1):
        if x_values[i] <= x < x_values[i + 1]:
            idx = i + 1  # Start at the value just after x for backward path dominance
            # However, standard formula centers at idx and goes UP first.
            # Let's align with the standard form where x_0 is the center.
            if abs(x - x_values[i]) < abs(x - x_values[i+1]):
                idx = i
            else:
                idx = i + 1
            break

    # 3. Calculate u
    h = x_values[1] - x_values[0]
    u = (x - x_values[idx]) / h

    # 4. Apply Gauss Backward Formula
    # Path: y_0 -> dy_-1 -> d^2y_-1 -> d^3y_-2 -> d^4y_-2 ...

    result = diff_table[idx][0]  # y_0

    u_term = 1
    fact = 1

    # We need to track the current row index in the table
    curr_idx = idx

    for k in range(1, 5):  # Up to 4th order
        if curr_idx < 0:
            break

        # Coefficient Logic:
        # k=1: u
        # k=2: u(u+1)
        # k=3: (u+1)u(u-1)
        # k=4: (u+1)u(u-1)(u+2)

        if k == 1:
            u_term = u
            curr_idx -= 1  # Move UP for first difference (y_-1)
        elif k == 2:
            u_term = u * (u + 1)
            # Stay at same row for 2nd difference (y_-1)
        elif k == 3:
            u_term = (u + 1) * u * (u - 1)
            curr_idx -= 1  # Move UP for 3rd difference (y_-2)
        elif k == 4:
            u_term = (u + 1) * u * (u - 1) * (u + 2)
            # Stay at same row for 4th difference (y_-2)

        fact = math.factorial(k)

        # Check bounds before accessing table
        if 0 <= curr_idx < n - k:
            term_val = (u_term / fact) * diff_table[curr_idx][k]
            result += term_val

    return result


# --- Example Usage ---
x_vals = [1, 2, 3, 4, 5]
y_vals = [2.7183, 7.3891, 20.0855, 54.5981, 148.4132]
x_target = 3.5

val = gauss_backward_interpolation(x_vals, y_vals, x_target)

print(f"Interpolating at x = {x_target}")
print(f"Gauss Backward Result: {val:.4f}")
print(f"Actual e^3.5:          {np.exp(3.5):.4f}")
