import numpy as np
import math


def gauss_forward_interpolation(x_values, y_values, x):
    n = len(x_values)

    # 1. Create the forward difference table
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i][j] = diff_table[i + 1][j - 1] - diff_table[i][j - 1]

    # 2. Find the index 'i' closest to the center or such that x_i < x < x_i+1
    # For Gauss Forward, we typically pick the index just before x
    idx = 0
    # Ensure we don't go out of bounds (n-1)
    for i in range(n - 1):
        if x_values[i] <= x < x_values[i + 1]:
            idx = i
            break

    # 3. Calculate u
    h = x_values[1] - x_values[0]
    u = (x - x_values[idx]) / h

    # 4. Apply the Gauss Forward Formula
    # y = y_0 + u(dy_0) + u(u-1)/2! (d^2y_-1) + (u+1)u(u-1)/3! (d^3y_-1) ...

    result = diff_table[idx][0]  # y_0
    u_term = 1

    # Helper to track the factorial denominator
    fact = 1

    # Loop for each order of difference
    for k in range(1, 5):  # Usually up to 4th order or n
        if idx < 0 or idx > n - 1:
            break  # Bounds check

        term_val = 0

        # Determine the coefficient based on the order k
        # k=1: u
        # k=2: u(u-1)
        # k=3: (u+1)u(u-1)
        # k=4: (u+1)u(u-1)(u-2)

        if k == 1:
            u_term = u
        elif k == 2:
            u_term = u * (u - 1)
            idx -= 1  # Shift index up for central difference (y_-1)
        elif k == 3:
            u_term = (u + 1) * u * (u - 1)
        elif k == 4:
            u_term = (u + 1) * u * (u - 1) * (u - 2)
            idx -= 1  # Shift index up (y_-2)

        fact = math.factorial(k)

        # Add to result if we are within table bounds
        # We need diff_table[idx][k]
        if 0 <= idx < n - k:
            term_val = (u_term / fact) * diff_table[idx][k]
            result += term_val

    return result


# --- Example Usage ---
x_values = [1, 2, 3, 4, 5]
# e^x values
y_values = [2.7183, 7.3891, 20.0855, 54.5981, 148.4132]
x_to_interpolate = 2.5

interpolated_value = gauss_forward_interpolation(
    x_values, y_values, x_to_interpolate)

print(f"Interpolating at x = {x_to_interpolate}")
print(f"Calculated Value: {interpolated_value:.4f}")
print(f"Actual e^2.5:     {np.exp(2.5):.4f}")
