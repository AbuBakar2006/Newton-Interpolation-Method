import numpy as np

x = [0, 0.25, 0.5, 0.75]
y = [1, 1.64872, 2.71828, 4.48169]

n = len(x)
D = np.zeros((n, n))

for i in range(n):
    D[i, 0] = y[i]

for j in range(1, n):
    for i in range(n - j):
        D[i, j] = D[i + 1, j - 1] - D[i, j - 1]

print("D=")
print(D)

S = D[n - 1, 0]

c = float(input('Enter x: '))
h = x[1] - x[0]

u = (c - x[n - 1]) / h

for i in range(1, n):
    m = 1
    for j in range(i):
        m *= (u + j)

    fact = 1
    for k in range(1, i + 1):
        fact *= k

    S += (m * D[n - 1 - i, i]) / fact

print('For x = %.1f, y = %.8f' % (c, S))
