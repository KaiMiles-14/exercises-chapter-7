import numpy as np
from example_code.groups import Group

class SymmetricGroup(Group):
    symbol = "S"

    def __init__(self, n):
        super().__init__()
        self.n = n

    def validate_element(self, element):
        if not isinstance(element, np.ndarray):
            raise ValueError("Group element must be a numpy.ndarray.")
        if len(element) != self.n:
            raise ValueError(f"Group element must have length {self.n}.")

    def group_operation(self, a, b):
        self.validate_element(a)
        self.validate_element(b)
        return a[b]