# 📉 Newton's Backward Interpolation

This script implements **Newton's Backward Difference Formula**, a numerical method used for interpolating values near the **end** of a dataset.

#### [⬅️ Back to Main Repository](../README.md)

## 🧠 The Math

Unlike the Forward method, this approach uses the **last** value ($y_n$) as the starting point and traces the difference table upwards.

**The Formula:**
$$
P(x) = y_n + u\nabla y_n + \frac{u(u+1)}{2!} \nabla^2 y_n + \frac{u(u+1)(u+2)}{3!} \nabla^3 y_n + \dots
$$

Where:
* $u = \frac{x - x_n}{h}$ (Note: $x_n$ is the last x value).
* $\nabla$ represents the backward difference operator.

## 📊 Dataset Used

The data appears to follow the exponential function $y = e^{2x}$.

| x | y |
| :--- | :--- |
| 0.00 | 1.00000 |
| 0.25 | 1.64872 |
| 0.50 | 2.71828 |
| 0.75 | 4.48169 |
