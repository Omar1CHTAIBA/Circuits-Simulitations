#-----XOR------

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.visualization import circuit_drawer
import matplotlib.pyplot as plt

# Create quantum registers with custom labels
qr_control = QuantumRegister(1, name="|bₐ>")  # Control qubit
qr_target = QuantumRegister(1, name="|bψ>")    # Target qubit

# Build the circuit using these registers
qc = QuantumCircuit(qr_control, qr_target)

# --- CNOT Operation ---
# Apply CNOT gate (control on |bₐ> and target on |b₁>)
qc.cx(qr_control[0], qr_target[0])

# Draw the circuit and save it as a PNG image
fig = circuit_drawer(qc, output='mpl')
fig.set_size_inches(10, 3)  # Adjust the size as needed for a nicer layout
fig.savefig(r'images\CNOT.png')
plt.close(fig)
