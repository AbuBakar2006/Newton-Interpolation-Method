# 📉 Newton's Interpolation Methods

A collection of numerical analysis algorithms implemented to perform polynomial interpolation. This project covers Forward, Backward, and Central difference methods used to estimate unknown values from a set of discrete data points.

## 📂 Repository Structure

The project is divided into three specific interpolation techniques:

```text
📂 Newton-Interpolation-Method/
├── 📁 Forward Interpolation/   # Logic for Newton's Forward Difference formula
├── 📁 Backward Interpolation/  # Logic for Newton's Backward Difference formula
└── 📁 Central Interpolation/   # Logic for Central Difference (Gauss/Stirling)
    ├── 📁 Stirling Formula/
    └── 📁 Gauss Formula/
        ├── 📁 Gauss Forward/
        └── 📁 Gauss Backward/

```

## 🛠️ Requirements

* **Python 3.x**
* **NumPy** (Used for creating the difference tables)

To install the dependency:
```bash
pip install numpy
```
### 🚀 How to Run
* Navigate to the folder of the method you want to use.
* Run the script.
* Enter the $x$ value you want to interpolate when prompted.

## 🧮 Algorithm Details

#### Forward Interpolation
Constructs a difference table and applies the formula starting from the first value ($y_0$)


$$
P(x) = y_0 + u\Delta y_0 + \frac{u(u-1)}{2!} \Delta^2 y_0 + \dots
$$ 

---

#### Backward Interpolation
Constructs the table but applies the formula starting from the last value ($y_n$).

$$
P(x) = y_n + u\nabla y_n + \frac{u(u+1)}{2!} \nabla^2 y_n + \dots
$$

---

#### Stirling's Formula (Central)
This implementation finds the origin ($x_0$) closest to your input, then calculates the value using the average of the differences above and below the central line.

---

