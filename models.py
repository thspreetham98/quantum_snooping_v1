from qiskit import QuantumCircuit
import uuid


class VictimCircuit(QuantumCircuit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cnots_applied = []
    
    def __str__(self):
        depth = self.depth()
        return 'depth_{}/{}'.format(depth, self.cnots_applied)
    
    def cx(self, ctrl, target):
        super().cx(ctrl, target)
        self.cnots_applied.append((ctrl, target))



class VictimParams:
    def __init__(self, no_of_qubits, max_circuit_depth, cnot_vals, no_of_circuits_per_cnot_val):
        self.no_of_qubits = no_of_qubits
        self.max_circuit_depth = max_circuit_depth
        self.cnot_vals = cnot_vals
        self.no_of_circuits_per_cnot_val = no_of_circuits_per_cnot_val
        self.uuid: uuid.UUID = uuid.uuid4()
