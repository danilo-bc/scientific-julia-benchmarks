# Adapted from https://www.matecdev.com/posts/julia-python-numba-cython.html
import math
import numba as nb
import time

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
    @nb.njit(nb.float64(nb.float64))
    def integrand(x):
        return math.exp(p*x) - 10
    return quad_trap(integrand, -1, 1, 10000) 
print("Pure Python:")
start_time = time.time()
q1 = quad_trap(func,-1,1,10000)
print("Quadrature -- %s seconds --" % (time.time() - start_time))

start_time = time.time()
r = g(1)
print("Eval g(1) -- %s seconds --" % (time.time() - start_time))


@nb.njit   
def jit_quad_trap(f,a,b,N):
    h = (b-a)/N
    integral = h * ( f(a) + f(b) ) / 2
    for k in range(N):
        xk = (b-a) * k/N + a
        integral = integral + h*f(xk)
    return integral

@nb.njit(nb.float64(nb.float64))
def jit_func(x):
    return math.exp(x) - 10

def jit_g(p): 
    @nb.njit(nb.float64(nb.float64))
    def integrand(x):
        return math.exp(p*x) - 10
    return jit_quad_trap(integrand, -1, 1, 10000) 

print("Numba: ")
# warm-up JIT
q1 = jit_quad_trap(jit_func,-1,1,10000)
start_time = time.time()
q1 = jit_quad_trap(jit_func,-1,1,10000)
print("Quadrature -- %s seconds --" % (time.time() - start_time))

# warm-up JIT
a = jit_g(1)
start_time = time.time()
r = jit_g(1)
print("Eval g(1) -- %s seconds --" % (time.time() - start_time))