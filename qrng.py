from qiskit import version
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram, array_to_latex
from qiskit.quantum_info import Statevector
import numpy as np
from matplotlib import pyplot as plt

def rng( lower, upper ):
    numValues = upper - lower + 1
    numQubits = int( np.ceil( np.log2( numValues ) ) )
    qc = QuantumCircuit( numQubits )
    for i in range( numQubits ):
        qc.h(i)
    
    #qc.draw('mpl')
    #plt.show()

    qc.measure_all()
    
    backend = BasicSimulator()
    result = backend.run(qc, shots = 512).result()
    counts = result.get_counts()

    counts_iterator = iter(counts.items())

    # Extract the first key-value pair from the iterator
    first_entry = int(next(counts_iterator)[0], 2) 

    random_number = lower + (first_entry % (upper - lower + 1))

    print( "Random number: ", random_number )

    return counts 

lower = int( input("Lower bound: ") )
upper = int( input("Upper bound: ") )

counts = rng( lower, upper )
decimal_counts = {int(key, 2) : value for key, value in counts.items()}
decimal_counts_adjusted = {lower + k % (upper-lower+1) : v for k,v in decimal_counts.items()}

plot_histogram(decimal_counts_adjusted)