from qiskit import version
from qiskit import QuantumCircuit
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import plot_histogram, array_to_latex
from qiskit.quantum_info import Statevector
import numpy as np
from matplotlib import pyplot as plt

numQubits = 3
qc = QuantumCircuit(numQubits)
qc.draw('mpl')
# plt.show()

qc.x(0)

# ideal simulations
kets = Statevector(qc).data
probabilities = np.round(np.abs(np.real(np.square(kets))),4)
counts = {np.binary_repr(i, width=qc.num_qubits): probabilities[i] for i in range(np.power(2, qc.num_qubits))}
plot_histogram(counts)

plt.show()