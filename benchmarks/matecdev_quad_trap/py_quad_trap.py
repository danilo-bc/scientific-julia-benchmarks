# Adapted from https://www.matecdev.com/posts/julia-python-numba-cython.html
import math
import numba as nb
import time
import sys
sys.path.append("..")
from common_benchmark import *

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
start_time = time.time()
q1 = quad_trap(func,-1,1,10000)
print(f"\tQuadrature -- {scientific_time(time.time() - start_time)} seconds")

start_time = time.time()
r = g(1)
print(f"\tEval g(1) -- {scientific_time(time.time() - start_time)} seconds")

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
q1 = bjit_quad_trap(bjit_func,-1,1,10000)
start_time = time.time()
q1 = bjit_quad_trap(bjit_func,-1,1,10000)
print(f"\tQuadrature -- {scientific_time(time.time() - start_time)} seconds")

# warm-up JIT
a = bjit_g(1)
start_time = time.time()
r = bjit_g(1)
print(f"\tEval g(1) -- {scientific_time(time.time() - start_time)} seconds")


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
start_time = time.time()
q1 = jit_quad_trap_p(jit_integrand,-1,1,10000, 1)
print(f"\tQuadrature -- {scientific_time(time.time() - start_time)} seconds")

# warm-up JIT
a = jit_g(1)
start_time = time.time()
r = jit_g(1)
print(f"\tEval g(1) -- {scientific_time(time.time() - start_time)} seconds")



