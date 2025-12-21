## 🎯 Gauss Backward Interpolation (Central)

This script implements **Gauss Backward Formula**, a central difference method used when the desired $x$ lies slightly to the left of the central value in the dataset.

#### [⬅️ Back to Main Repository](../../README.md)

### 🧠 How the Code Works

1. **Find Origin ($x_0$):** The script automatically scans the `x_values` array to find the optimal central index `idx`.
2. **Calculate $u$:**
   
   $$u = \frac{x - x_0}{h}$$

3. **Zigzag Path:**
   Unlike the Forward method, Gauss Backward moves **upward** into the table earlier. The script adjusts the row index dynamically:
   * **Odd Terms ($k=1, 3$):** Move UP one row (`curr_idx -= 1`).
   * **Even Terms ($k=2, 4$):** Stay at the same row.

### 📊 Dataset Used
The script is currently hardcoded with the following exponential data ($y=e^x$):
* **X:** `[1, 2, 3, 4, 5]`
* **Y:** `[2.7183, 7.3891, 20.0855, 54.5981, 148.4132]`

### 💻 Usage
```bash
python Gauss-Backward-Interpolation.py
