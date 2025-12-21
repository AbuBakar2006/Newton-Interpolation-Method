## 🎯 Gauss Forward Interpolation (Central)

This script implements **Gauss Forward Formula**, a central difference method used when the desired $x$ lies slightly to the **right** of the central value in the dataset ($0 < p < 1$).



#### [⬅️ Back to Main Repository](../../README.md)

### 🧠 How the Code Works

1. **Find Origin ($x_0$):** The script scans `x_values` to find the index just before the target $x$.
2. **Calculate $u$:**
   
   $$u = \frac{x - x_0}{h}$$

3. **Zigzag Path:**
   Unlike the Backward method, Gauss Forward starts by moving **forward** (down) in the table. The script adjusts the row index dynamically:
   * **Odd Terms ($k=1, 3$):** Stay at the same row (uses $\Delta y_0, \Delta^3 y_{-1}$).
   * **Even Terms ($k=2, 4$):** Move UP one row (uses $\Delta^2 y_{-1}, \Delta^4 y_{-2}$).

### 📊 Dataset Used
The script is currently hardcoded with the following exponential data ($y=e^x$):
* **X:** `[1, 2, 3, 4, 5]`
* **Y:** `[2.7183, 7.3891, 20.0855, 54.5981, 148.4132]`
* **Target:** $x = 2.5$

### 💻 Usage
```bash
python Gauss-Forward-Interpolation.py
