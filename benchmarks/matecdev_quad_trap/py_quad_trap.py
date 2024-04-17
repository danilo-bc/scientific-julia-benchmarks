# Adapted from https://www.matecdev.com/posts/julia-python-numba-cython.html
import math
import numba as nb
import time
import timeit
import sys
sys.path.append("..")
from common_benchmark import *

n_iterations = 100
######## Pure Python
def quad_trap(f,a,b,N):
    h = (b-a)/N
    integral = h * ( f(a) + f(b) ) / 2
    for k in range(N):
        xk = (b-a) * k/N + a
        integral = integral + h*f(xk)
    return integral

def func(x):
    return math.exp(x) - 10

def g(p): 
    def integrand(x):
        return math.exp(p*x) - 10
    return quad_trap(integrand, -1, 1, 10000) 

print("Pure Python:")
q1 = quad_trap(func,-1,1,10000)
print(f"\tQuadrature -- {scientific_time(timeit.Timer(lambda: quad_trap(func,-1,1,10000), globals=globals()).timeit(number=n_iterations)/n_iterations)}")
print(f"\tEval g(1) -- {scientific_time(timeit.Timer(lambda: g(1), globals=globals()).timeit(number=n_iterations)/n_iterations)}")

######## with bad Numba JIT
@nb.njit
def bjit_quad_trap(f,a,b,N):
    h = (b-a)/N
    integral = h * ( f(a) + f(b) ) / 2
    for k in range(N):
        xk = (b-a) * k/N + a
        integral = integral + h*f(xk)
    return integral

@nb.njit(nb.float64(nb.float64))
def bjit_func(x):
    return math.exp(x) - 10

def bjit_g(p): 
    @nb.njit(nb.float64(nb.float64))
    def bjit_integrand(x):
        return math.exp(p*x) - 10
    return bjit_quad_trap(bjit_integrand, -1, 1, 10000) 

print("Bad Numba: ")
# warm-up JIT
bjit_quad_trap(bjit_func,-1,1,10000)
print(f"\tQuadrature -- {scientific_time(timeit.Timer(lambda: bjit_quad_trap(bjit_func,-1,1,10000), globals=globals()).timeit(number=n_iterations)/n_iterations)}")

# warm-up JIT
bjit_g(1)
print(f"\tEval g(1) -- {scientific_time(timeit.Timer(lambda: bjit_g(1), globals=globals()).timeit(number=n_iterations)/n_iterations)}")


######## With proper Numba JIT
@nb.njit
def jit_quad_trap_p(f,a,b,N,p):
    h = (b-a)/N
    integral = h * ( f(a,p) + f(b,p) ) / 2
    for k in range(N):
        xk = (b-a) * k/N + a
        integral = integral + h*f(xk,p)
    return integral

@nb.njit(nb.float64(nb.float64, nb.float64))
def jit_integrand(x, p):
    return math.exp(p*x) - 10

def jit_g(p):
    return jit_quad_trap_p(jit_integrand, -1, 1, 10000, p)

print("Good Numba: ")
# warm-up JIT
q1 = jit_quad_trap_p(jit_integrand,-1,1,10000, 1)
print(f"\tQuadrature -- {scientific_time(timeit.Timer(lambda: jit_quad_trap_p(jit_integrand,-1,1,10000, 1), globals=globals()).timeit(number=n_iterations)/n_iterations)}")

# warm-up JIT
jit_g(1)
print(f"\tEval g(1) -- {scientific_time(timeit.Timer(lambda: jit_g(1), globals=globals()).timeit(number=n_iterations)/n_iterations)}")



