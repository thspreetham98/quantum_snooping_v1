from qiskit import QuantumCircuit

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
