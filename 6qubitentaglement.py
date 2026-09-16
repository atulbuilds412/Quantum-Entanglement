from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

circuit=QuantumCircuit(6,6)

circuit.h(0)

circuit.cx(0,1)
circuit.cx(1,2)
circuit.cx(2,3)
circuit.cx(3,4)
circuit.cx(4,5)
circuit.measure(0,0)
circuit.measure(1,1)
circuit.measure(2,2)
circuit.measure(3,3)
circuit.measure(4,4)
circuit.measure(5,5)

simulator=AerSimulator()
result=simulator.run(circuit).result()
counts=result.get_counts()
print("\n---6-QUBIT CHAIN REACTION COMPLETE")
print(counts)
print("----------------------\n")
print(circuit.draw())
