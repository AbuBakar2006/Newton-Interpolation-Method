# 📉 Newton's Forward Interpolation

This script implements **Newton's Forward Difference Formula**, a numerical method used for interpolating values near the **beginning** of a dataset.

#### [⬅️ Back to Main Repository](../README.md)

### 🧠 The Math

This method constructs a forward difference table ($\Delta$) and uses the first value ($y_0$) as the base.

**The Formula:**
$$
P(x) = y_0 + u\Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_0 + \frac{u(u-1)(u-2)}{3!} \Delta^3 y_0 + \dots
$$

Where:
* $u = \frac{x - x_0}{h}$
* $h$ is the step size (interval between $x$ values).

### 📊 Dataset Used

The script is currently hardcoded with the following data points:

| x | y |
| :--- | :--- |
| 0.1 | 0.62049958 |
| 0.2 | -0.28398668 |
| 0.3 | 0.00660095 |
| 0.4 | 0.24842440 |

#### Example Output
```text
D=
[[ 0.62049958 -0.90448626  1.19507389 -1.24641033]
 [-0.28398668  0.29058763 -0.05133644  0.        ]
 [ 0.00660095  0.23925119  0.          0.        ]
 [ 0.2484244   0.          0.          0.        ]]
Enter x: 0.15
For x = 0.15, y = 0.168...
```
