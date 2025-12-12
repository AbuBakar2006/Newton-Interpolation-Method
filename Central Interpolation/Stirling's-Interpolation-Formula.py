import numpy as np

x = [20, 30, 40, 50]
y = [512, 439, 346, 243]

n = len(x)
D = np.zeros((n, n))

for i in range(n):
    D[i, 0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        D[i, j] = D[i + 1, j - 1] - D[i, j - 1]

print("D=")
print(D)

c = float(input('Enter x: '))

mid = 0
min_diff = abs(c - x[0])
for i in range(1, n):
    if abs(c - x[i]) < min_diff:
        min_diff = abs(c - x[i])
        mid = i

print(f"Taking origin x0 at index {mid} (value {x[mid]})")

h = x[1] - x[0]
u = (c - x[mid]) / h

S = D[mid, 0]

for i in range(1, n):
    fact = 1
    for k in range(1, i + 1):
        fact *= k

    if i % 2 != 0:
        k = (i - 1) // 2

        m = u
        for j in range(1, k + 1):
            m *= (u**2 - j**2)

        idx1 = mid - k
        idx2 = mid - k - 1

        if idx2 < 0 or idx1 >= (n - i):
            break

        avg_diff = (D[idx1, i] + D[idx2, i]) / 2
        S += (m * avg_diff) / fact

    else:
        k = i // 2

        m = u**2
        for j in range(1, k):
            m *= (u**2 - j**2)

        idx = mid - k

        if idx < 0 or idx >= (n - i):
            break

        S += (m * D[idx, i]) / fact

print('For x = %.1f, y = %.8f' % (c, S))
