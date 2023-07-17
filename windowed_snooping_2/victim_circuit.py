from qiskit import QuantumCircuit

class VictimCircuit(QuantumCircuit):
    def __init__(self, cnots_applied):
        super.__init__()
        self.cnots_applied = cnots_applied

    def get_name(self):
        depth = self.depth()
        return 'depth_{}/{}'.format(depth, self.cnots_applied)

        