class LogicGate:
    def __init__(self, label):
        self.label = label
    
    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None 
    
    def get_pin(self):
        return int(input(f"Enter the input for the gate {self.label}"))


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin_a = None
        self.pin_b = None
    
    def get_pin_a(self):
        return int(input(f"Enter the first input for the gate {self.label}"))

    def get_pin_b(self):
        return int(input(f"Enter the second input for the gate {self.label}"))

class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)


    def perform_logic_gate(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 and b == 1:
            return 1
        else:
            return 0
