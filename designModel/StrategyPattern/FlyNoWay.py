from StrategyPattern.FlyBehavior import FlyBehavior

class FlyNoWay(FlyBehavior):

    def fly(self):
        print("I fly no way!")