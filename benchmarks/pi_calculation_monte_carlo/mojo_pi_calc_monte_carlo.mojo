import random
import benchmark

def pi_calc():
    j = 0
    i = 1
    n = 10**7
    while i<=n:
        x = random.random_float64()
        y = random.random_float64()
        i = i + 1
        if x**2 + y**2 <= 1:
            j = j+1
    pi = j/n*4
    return pi

fn pi_calc_simple():
    var j = 0
    var i = 1
    var n = 10**7
    while i<=n:
        var x = random.random_float64()
        var y = random.random_float64()
        i = i + 1
        if x**2 + y**2 <= 1:
            j = j+1
    var pi = j/n*4
    # return pi

fn pi_calc_typed():
    var j: Int = 0
    var i: Int = 1
    var n: Int = 10**7
    while i<=n:
        var x: Float64 = random.random_float64()
        var y: Float64 = random.random_float64()
        i = i + 1
        if x**2 + y**2 <= 1:
            j = j+1
    var pi: Float64 = j/n*4
    # return pi

def main():
    print("Mojo:")
    # var res0 = benchmark.run[pi_calc](max_runtime_secs=1).mean()
    var res1 = benchmark.run[pi_calc_simple](max_runtime_secs=30).mean()
    var res2 = benchmark.run[pi_calc_typed](max_runtime_secs=30).mean()
    # print(f"\tPython: {res0}")
    print(f"\tSimple: {res1}")
    print(f"\tTyped: {res2}")