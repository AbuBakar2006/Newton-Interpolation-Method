## 🎯 Stirling's Interpolation (Central)

This script implements **Stirling's Formula**, a central difference method used when the desired $x$ is near the middle of the dataset.

### 🧠 How the Code Works

1. **Find Origin ($x_0$):** The script automatically scans the `x` array to find the value closest to your input `c`. This index becomes the `mid`.
2. **Calculate $u$:**
   
   $$u = \frac{x - x_0}{h}$$
  
3. **Average Differences:**
   Unlike Forward/Backward methods which pick a single diagonal, Stirling's method takes the average of two differences for odd terms:

$$
D_{avg} = \frac{\Delta y_{-1} + \Delta y_{0}}{2}
$$

### 📊 Dataset Used
The script is currently hardcoded with the following population data:
* **X:** `[20, 30, 40, 50]`
* **Y:** `[512, 439, 346, 243]`

### 💻 Usage
```bash
python stirling.py
