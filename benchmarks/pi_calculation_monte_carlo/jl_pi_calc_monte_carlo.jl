using BenchmarkTools
function pi_calc()
    j = 0
    i = 1
    n = 10^7
    while i<=n
        x = rand()
        y = rand()
        i = i + 1
        if x^2 + y^2 <= 1
            j = j + 1
        end
    end
    pi = j/n*4
    return pi
end
println("Julia including JIT:")
@time pi_calc()
println("Julia @btime:")
@btime pi_calc()