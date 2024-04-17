import random
import timeit
def pi_calc():
    j = 0
    i = 1
    n = 10**7
    while i<=n:
        x = random.random()
        y = random.random()
        i = i + 1
        if x**2 + y**2 <= 1:
            j = j+1
    pi = j/n*4
    return pi
print("Regular Python:")
print(timeit.Timer("pi_calc()", globals=globals()).timeit(number=5)/5)

from numba import njit
@njit
def pi_calc_jit():
    j = 0
    i = 1
    n = 10**7
    while i<=n:
        x = random.random()
        y = random.random()
        i = i + 1
        if x**2 + y**2 <= 1:
            j = j+1
    pi = j/n*4
    return pi
# Warm up JIT before benchmarks
pi_calc_jit()
print("Python Numba:")
print(timeit.Timer("pi_calc_jit()", globals=globals()).timeit(number=50)/50)