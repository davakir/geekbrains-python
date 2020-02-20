from abc import ABC, abstractmethod
from math import ceil


class AbstractClothes(ABC):
    @abstractmethod
    def get_tissue_consumption(self):
        pass


class Coat(AbstractClothes):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return ceil(self.__size)

    def get_tissue_consumption(self):
        return ceil(self.size / 6.5 + 0.5)


class Suit(AbstractClothes):
    def __init__(self, length):
        self.__length = length

    @property
    def length(self):
        return ceil(self.__length)

    def get_tissue_consumption(self):
        return ceil(2 * self.length + 0.3)


coat = Coat(46.5)
print(f'Расход ткани на пальто: {coat.get_tissue_consumption()} метров')

suit = Suit(155)
print(f'Расход ткани на костюм {suit.get_tissue_consumption()} метров')
