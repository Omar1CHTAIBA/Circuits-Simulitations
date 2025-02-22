from qiskit import QuantumCircuit, QuantumRegister
from qiskit.visualization import circuit_drawer

# Create quantum registers with custom labels
qr1 = QuantumRegister(1, name="|b1>")
qr2 = QuantumRegister(1, name="|b2>")
qr3 = QuantumRegister(1, name="|b3>")

# Build the quantum circuit using these registers
qc = QuantumCircuit(qr1, qr2, qr3)

# Apply an X gate to the qubit in the second register (|b2>)
qc.x(qr2[0])

# Save the circuit diagram as a PNG image.
# The 'circuit_drawer' function with output='mpl' saves the image to the file specified by 'filename'.
circuit_drawer(qc, output='mpl', filename='circuit.png')
