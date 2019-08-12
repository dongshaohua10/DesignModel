import abc
from StrategyPattern.FlyBehavior import FlyBehavior


class DuckModel(metaclass=abc.ABCMeta):

    def __init__(self):
        self.flyBehavior = FlyBehavior()

    def swim(self):
        print("I can swim!")

    def performFly(self):
        self.flyBehavior.fly()

    def setFlyBehavior(self, obj:FlyBehavior):
        self.flyBehavior = obj

    @abc.abstractmethod
    def display(self):
        pass
