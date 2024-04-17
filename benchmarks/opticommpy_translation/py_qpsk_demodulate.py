from optic.utils import dec2bitarray
from optic.comm.modulation import minEuclid, demap
import numpy as np
import timeit
import sys
sys.path.append("..")
from common_benchmark import *

def myQPSKDemodulate(symb_seq):
    M = 4
    constellation = np.array([1+1j, 1-1j, -1+1j, -1-1j])

    indMap = minEuclid(constellation, constellation)
    bitMap = dec2bitarray(indMap, int(np.log2(M)))
    indrx  = minEuclid(symb_seq, constellation)
    return demap(indrx, bitMap)

if __name__ == '__main__':
    constellation = np.array([1+1j, 1-1j, -1+1j, -1-1j])
    print(f"Python:")
    for n in [10, 100, 1000, 10000, 100000]:
        n_iterations = 10000
        n_syms = n
        symb_seq = np.random.choice(constellation, n_syms)
        # Warm up JIT for internal functions
        myQPSKDemodulate(constellation)
        exec_time = timeit.timeit(lambda: myQPSKDemodulate(symb_seq), number=n_iterations)
        print(f'\tMean of {n_iterations} for {n_syms} symbols: {scientific_time(exec_time / n_iterations)}')