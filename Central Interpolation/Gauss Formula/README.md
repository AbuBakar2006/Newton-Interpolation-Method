# 📉 Gauss Central Difference Formulas

Welcome to the **Gauss Interpolation** module. This directory contains implementations for Central Difference Interpolation methods, which are used to find function values near the **center** of a data set.

Unlike Newton's Forward (used for the start of a table) or Backward (used for the end), Gauss formulas provide higher accuracy when the interpolated value lies near the mean ($x_0$).


## 📂 Project Structure

This module is divided into two specific implementations. Click below to navigate:

| Method | Description | Target Range ($p$) |
| :--- | :--- | :--- |
| **[Gauss Forward Method](./Gauss%20Forward%20Method)** | Uses the central value and moves **forward** in the difference table. | $0 < p < 1$ |
| **[Gauss Backward Method](./Gauss%20Backward%20Method)** | Uses the central value and moves **backward** in the difference table. | $-1 < p < 0$ |

## 📐 Mathematical Theory

Central difference methods rely on the parameter $p$ (or $u$), calculated as:

$$p = \frac{x - x_0}{h}$$

Where:
* $x$ = The value to be interpolated.
* $x_0$ = The central value from the table (closest to $x$).
* $h$ = The step size (difference between $x$ values).

### 1. Gauss Forward Formula
Used when the value lies **to the right** of the central value (positive $p$).
It follows the "zigzag" path going **down-then-up** through the difference table.

$$y_p = y_0 + p\Delta y_0 + \frac{p(p-1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-1} + \dots$$

### 2. Gauss Backward Formula
Used when the value lies **to the left** of the central value (negative $p$).
It follows the "zigzag" path going **up-then-down** through the difference table.

$$y_p = y_0 + p\Delta y_{-1} + \frac{p(p+1)}{2!}\Delta^2 y_{-1} + \frac{(p+1)p(p-1)}{3!}\Delta^3 y_{-2} + \dots$$

## 🚀 Features

* **Dynamic Table Generation:** Both scripts automatically calculate the Central Difference Table.
* **Automatic Selection:** The logic helps determine convergence based on the location of $x$.
* **Python Implementation:** Built using standard Python libraries.

## 💻 Dependencies

To run the scripts inside the sub-folders, you will need:

* **Python 3.x**
* **NumPy** (for array handling)

```bash
pip install numpy
```
