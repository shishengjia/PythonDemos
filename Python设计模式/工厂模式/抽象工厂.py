# -*- coding: utf-8 -*-
"""
用于创建一系列相关事物对象的工厂方法
抽象工厂设计模式是抽象方法的一种泛化。概括来说，一个抽象工厂是（逻辑上的）一组工
厂方法，其中的每个工厂方法负责产生不同种类的对象

因为抽象工厂模式是工厂方法模式的一种泛化，所以它能提供相同的好处：让对象的创建更
容易追踪；将对象创建与使用解耦；提供优化内存占用和应用性能的潜力

通常一开始时使用工厂方法，因为它更简单。如果后来发现应用需要许多工厂方法，那么将创建
一系列对象的过程合并在一起更合理，从而最终引入抽象工厂。
"""


class Frog:
    """
    青蛙
    interact_with()用于描述青蛙与障碍物（比如，虫子、迷宫或其他青蛙）之间的交互
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Frog encounters {} and {}'.format(self, obstacle, obstacle.action()))


class Bug:
    """
    虫子
    """
    def __str__(self):
        return 'a bug'

    def action(self):
        return 'eats it'


class FrogWorld:
    """
    FrogWorld是一个抽象工厂，其主要职责是创建游戏的主人公和障碍物。区分创建方法并
    使其名字通用（比如，make_character()和make_obstacle()），这让我们可以动态改变当前
    激活的工厂（也因此改变了当前激活的游戏），而无需进行任何代码变更。在一门静态语言中，
    抽象工厂是一个抽象类/接口，具备一些空方法，但在Python中无需如此，因为类型是在运行时检
    测的
    """
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-----Frog World-----'

    def make_character(self):
        return Frog(self.player_name)

    def make_obstacle(self):
        return Bug()


class Wizard:
    """
    术士
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print('{} the Wizard battles against {} and {}'.format(self, obstacle, obstacle.action()))


class Ork:
    """
    怪兽
    """
    def __str__(self):
        return 'an evil ork'

    def action(self):
        return 'kills it'


class WizardWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return '\n\n\t-----Wizard World-----'

    def make_character(self):
        return Wizard(self.player_name)

    def make_obstacle(self):
        return Ork()


class GameEnvironment:
    """
    游戏主入口
    """
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_obstacle()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    """
    验证年龄的有效性,返回一个布尔标志和年龄
    """
    try:
        age = input('Welcome {}. How old are you? '.format(name))
        age = int(age)
    except ValueError as err:
        print('Age {} is invalid, please try again...'.format(age))
        return False, age
    return True, age


def main():
    name = input("Hello, What's your name?")
    valid_input = False
    age = 0
    while not valid_input:
        valid_input, age = validate_age(name)

    # 根据年龄选择对应游戏
    game_world = FrogWorld if age < 18 else WizardWorld
    # 游戏环境初始化，创建角色和敌人
    environment = GameEnvironment(game_world(name))
    # 开玩
    environment.play()

if __name__ == '__main__':
    main()
