# here is an abstract class
# abc is abstract base class
from abc import ABCMeta, abstractmethod

class AbsctractShape(): # this is an abstract class
    __metaclass__ = ABCMeta
    @abstractmethod
    def __str__(self):
        pass # we never put any functionality into an ABC
    @property
    @abstractmethod
    def shape_name():
        pass # no actual body to the property method
