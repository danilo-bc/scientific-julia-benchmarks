using BenchmarkTools
using Random

function minEuclid(symb, constellation)
    ind = zeros(Int, size(symb))
    for ii in eachindex(symb)
        ind[ii] = argmin(abs.(symb[ii] .- constellation))
    end
    return ind
end

function demap(indSymb, bitMap)
    M = size(bitMap)[1]
    b = Int(log2(M))

    decBits = zeros(Int, (length(indSymb), b))
    for i in eachindex(indSymb)
        decBits[i, :] = bitMap[indSymb[i], :]
    end
    return decBits
end

function decimal2bitarray(x, bit_width)
    result = zeros(Int, bit_width)
    i = 1
    pox = 0
    while i <= x
        if i & x != 0
            result[bit_width - pox] = 1
        end
        i <<= 1
        pox += 1
    end
    return result
end

function dec2bitarray(x, bit_width)
    result = zeros(Int, (length(x), bit_width))
    for (pox, number) in enumerate(x)
        result[pox, :] = decimal2bitarray(number, bit_width)
    end
    return result
end

function myQPSKDemodulate(symb_seq)
    M = 4
    constellation = [1+1im, 1-1im, -1+1im, -1-1im]

    indMap = minEuclid(constellation, constellation)
    bitMap = dec2bitarray(indMap .- 1, Int(log2(M)))
    indrx = minEuclid(symb_seq, constellation)
    return demap(indrx, bitMap)'[:]
end

constellation = [1+1im, 1-1im, -1+1im, -1-1im]
println("Julia:")
for n in [10, 100, 1000, 10000, 100000]
    n_syms = n
    sp = Random.Sampler(MersenneTwister, constellation)
    symb_seq = rand(sp, n_syms)
    print("\t$(n_syms) symbols: ")
    @btime myQPSKDemodulate($symb_seq)
end