class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
            self._size = 0
        else:
            raise ValueError('capacity can not be negative')

    def __str__(self):
        return self._size * '🍪'


    def deposit(self, n):
        if (self._size + n) > self.capacity:
            raise ValueError('exceeded max jar capacity')
        self._size += n


    def withdraw(self, n):
        if n > self.size:
            raise ValueError('not enought cookies in the jar')
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

