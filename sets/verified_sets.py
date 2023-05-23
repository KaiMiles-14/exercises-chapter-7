

from collections.abc import Iterable


class VerifiedSet(set):

    def _verify(self, value):
        raise NotImplementedError
    
    def add(self, value):
        self._verify(value)
        super().add(value)
    
    def update(self, value):
        for item in value:
            self._verify(item)
        super().update(value)
    
    def symmetric_difference_update(self, value):
        for item in value:
            self._verify(item)
        super().symmetric_difference_update(value)
    
    def union(self, *sets):
        new_set = self.__class__(self)
        for s in sets:
            new_set.update(s)
        return new_set

    def intersection(self, *sets):
        new_set = self.__class__(self)
        new_set.intersection_update(*sets)
        return new_set

    def difference(self, *sets):
        new_set = self.__class__(self)
        new_set.difference_update(*sets)
        return new_set

    def symmetric_difference(self, other):
        new_set = self.__class__(self)
        new_set.symmetric_difference_update(other)
        return new_set

    def copy(self):
        new_set = self.__class__(self)
        return new_set
