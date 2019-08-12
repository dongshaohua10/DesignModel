from StrategyPattern.MallardDuck import MallardDuck
from StrategyPattern.ReadHeadDuck import ReadHeadDuck
from StrategyPattern.FlyNoWay import FlyNoWay
from StrategyPattern.FlyRocket import FlyRocket

def main():
    duck = ReadHeadDuck()
    duck.setFlyBehavior(FlyRocket())
    duck.display()
    duck.performFly()
    duck.swim()

if __name__ == '__main__':
    main()