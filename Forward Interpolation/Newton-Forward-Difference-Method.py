import numpy as np

x = [0.1, 0.2, 0.3, 0.4]
y = [0.62049958, -0.28398668, 0.00660095, 0.24842440]

n = len(x)
D = np.zeros((n, n))

for i in range(n):
    D[i, 0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        D[i, j] = D[i + 1, j - 1] - D[i, j - 1]

print("D=")
print(D)

S = D[0, 0]
c = float(input('Enter x: '))
h = x[1] - x[0]
u = (c - x[0]) / h

for i in range(1, n):
    m = 1
    for j in range(i):
        m *= (u - j)

    fact = 1
    for k in range(1, i + 1):
        fact *= k

    S += (m * D[0, i]) / fact

print('For x = %.1f, y = %.8f' % (c, S))
