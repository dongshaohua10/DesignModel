from StrategyPattern.DuckModel import DuckModel
from StrategyPattern.FlyNoWay import FlyNoWay

class ReadHeadDuck(DuckModel):

    def __init__(self):
        self.flyBehavior = FlyNoWay()

    def display(self):
        print("I am Redhead duck!")