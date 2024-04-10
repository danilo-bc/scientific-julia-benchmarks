# Adapted from https://www.matecdev.com/posts/julia-python-numba-cython.html
using LoopVectorization
using BenchmarkTools

function quad_trap(f,a,b,N) 
    h = (b-a)/N
    int = h * ( f(a) + f(b) ) / 2
    for k=1:N-1
        xk = (b-a) * k/N + a
        int = int + h*f(xk)
    end
    return int
end

function turbo_quad_trap(f,a,b,N) 
    h = (b-a)/N
    int = h * ( f(a) + f(b) ) / 2
    @turbo for k=1:N-1
        xk = (b-a) * k/N + a
        int = int + h*f(xk)
    end
    return int
end

function func(x)
    return exp(x) - 10
end

turbo_g(p) = turbo_quad_trap( x -> exp(p*x) - 10, -1, 1, 10000)
g(p) = quad_trap( x -> exp(p*x) - 10, -1, 1, 10000)
println("--- Stock Julia")
print("\tQuadrature\t--")
@btime quad_trap(func,-1,1,10000)
print("\tEval g(1)\t--")
@btime g(1)

println("--- With @turbo")
print("\tQuadrature\t--")
@btime turbo_quad_trap(func,-1,1,10000)
print("\tEval g(1)\t--")
@btime turbo_g(1)