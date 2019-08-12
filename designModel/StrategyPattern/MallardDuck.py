from StrategyPattern.DuckModel import DuckModel
from StrategyPattern.FlyWithWings import FlyWithWings



class MallardDuck(DuckModel):

    def __init__(self):
        self.flyBehavior = FlyWithWings()

    def display(self):
    	print("I am Mallar duck!")
