
from random import randint
class Player(object):
    __slots__ = ('_name','_hp')
    def __init__(self,name,hp):
        self._name = name
        self._hp = hp
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp if self._hp >0 else 0

    @hp.setter
    def name(self,hp):
        self._hp = hp
    def __str__(self):
        return '{}还有血量：{}'.format(self._name,self._hp if self._hp > 0 else 0)

class Hero(Player):
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp
    def attack(self,other):
        hurtnum = randint(10,21)
        print('{}攻击了{}，{}失去了{}血'.format(self._name,other._name,other._name,hurtnum))
        other._hp -= hurtnum
    def Magic(self,other):
        magicnum = randint(30, 41)
        if self._mp >=30 :
            print('{}使用流星火攻击了{}，{}失去了{}血'.format(self._name, other._name, other._name, magicnum))
            other._hp -= magicnum
            self._mp -= 30
        else:
            print('{}魔力不足，攻击了{}，{}失去了{}血').format(self._name, other._name, other._name, hurtnum)
    def __str__(self):
        return '{}还有血量：{}，还有魔力：{}'.format(self._name,self._hp if self._hp > 0 else 0,self._mp)

class Master(Player):
    def __init__(self,name,hp):
        super().__init__(name,hp)
    def attack(self,other):
        hurtnum = randint(20,31)
        print('{}攻击了{}，{}失去了{}血'.format(self._name,other._name,other._name,hurtnum))
        other._hp -= hurtnum

if __name__ == '__main__':
    Hero1 = Hero('乐乐',100,100)
    Master1 = Master('添怡',100)
    while Hero1.hp > 0 and Master1.hp > 0 :
        if randint(1,3) % 2 != 0 :
            if randint(1,11) <= 7:
                Hero1.attack(Master1)
                print(Master1)
            else:
                Hero1.Magic(Master1)
                print(Master1)
        else:
            Master1.attack(Hero1)
            print(Hero1)
    if Hero1.hp > 0 :
        print('{}胜利'.format(Hero1._name))
    else:
        print('game over')
