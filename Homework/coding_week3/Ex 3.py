from math import factorial
def piR (n):
    a = 2 * (2 ** 0.5) / 9801.0
    k = 0
    b = 0
    while k <= n:
        b += (factorial(4 * k) * (1103.0 + 26390.0 * k)) / ((factorial(k))**4 * 396.0 ** (4.0 *k))
        k += 1
    return 1.0 / (a * b)