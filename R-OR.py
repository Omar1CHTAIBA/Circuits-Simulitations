from qiskit import QuantumCircuit, QuantumRegister
from qiskit.visualization import circuit_drawer
from qiskit.circuit.library import XGate
import matplotlib.pyplot as plt

# Create quantum registers with custom labels
qr_alpha = QuantumRegister(1, name="|bψ>")
qr_beta  = QuantumRegister(1, name="|bϫ>")
qr_1     = QuantumRegister(1, name="|b₁>")

# Build the circuit using these registers
qc = QuantumCircuit(qr_alpha, qr_beta, qr_1)

# --- Pre-processing ---
# Apply X gates to the first two qubits (flip them to prepare for 0-control)
qc.x(qr_alpha[0])
qc.x(qr_beta[0])

# --- Main Operation ---
# Create a controlled-X gate with 2 controls that triggers when both controls are 0.
# This gate will be drawn with open (hollow) control symbols.
or_gate = XGate().control(2, ctrl_state='00')
# Append the custom gate with controls on the first two qubits and target on the third qubit
qc.append(or_gate, [qr_alpha[0], qr_beta[0], qr_1[0]])

# --- Post-processing ---
# Restore the original state of the first two qubits by applying X gates again
qc.x(qr_alpha[0])
qc.x(qr_beta[0])

# Draw the circuit and save it as a PNG image
fig = circuit_drawer(qc, output='mpl')
fig.set_size_inches(10, 3)  # Adjust the size as needed for a nicer layout
fig.savefig('reversible_or.png')
plt.close(fig)
