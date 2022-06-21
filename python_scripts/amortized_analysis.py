''' Amortized analysis '''

'''
    Amortized analysis finds an upper bound on runtime by imposing an artificial cost on each
operation in a sequence of operations, and then combining each of these costs. The artificial
cost of a sequence takes in to account that the initial expensive operations can make
subsequent operations cheaper.
'''

'''
    For example, if a list is sorted it should
make any subsequent find operations quicker. Amortized analysis can take into account the
state change of data structures because it analyzes sequences of operations, rather
then simply aggregating single operations.
'''


'''
    Average case analysis finds the average running time based on some assumptions
regarding the relative frequencies of various input values. Using real-world data, or data
that replicates the distribution of real-world data, is many times on a particular data
distribution and the average running time is calculated.
'''

'''
    Benchmarking is simply having an agreed set of typical inputs that are used to measure
performance. Both benchmarking and average time analysis rely on having some domain
knowledge. We need to know what the typical or expected datasets are. Ultimately we will
try to find ways to improve performance by fine-tuning to a very specific application
setting
'''

def nest(n):
    for i in range(n):
        for j in range(n):
            i+j
            
import timeit

def test2(n):
    ls = []
    for n in range(n):
        t = timeit.timeit(f'nest({str(n)})', setup='from __main__ import nest', number=1)
        ls.append(t)
    return ls    

import matplotlib.pyplot as plt
n=1000
plt.plot(test2(n))
plt.plot([x*x/10000000 for x in range(n)])