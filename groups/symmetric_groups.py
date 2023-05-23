import numpy as np
from example_code.groups import Group

class SymmetricGroup(Group):
    symbol = "S"

    def __init__(self, n):
        super().__init__(n)
        self.n = n

    def _validate(self, value):
        if not isinstance(value, np.ndarray):
            raise ValueError("Group element must be a numpy.ndarray.")
        if len(value) != self.n:
            raise ValueError(f"Group element must have length {self.n}.")

    def operation(self, a, b):
        self._validate(a)
        self._validate(b)
        return a[b]