# NGULIK OOP PAKE KASUS BU DETIN TENTANG GAME
# objek player 
class Player:
    def __init__(self,name,health=100,energy=100):
        self.name = name 
        self.health = health 
        self.energy = energy
        print('-------------------------------------------------------------')
        print(f'Player created! Your energy is {self.energy} & your health is {self.health}')

    def attack_monster(self,target,damage=1):
        self.damage = damage
        target.health -= damage
        self.energy -= damage

    def show_info(self,target):
        # print(f'Player created! Your energy is {self.energy} & your health is {self.health}')
        # print(f"Monster created! Monster's health is {target.health}")
        print(f"1. {self.name} Attack to dragon!:\ndamage : {self.damage}\nenegry : {self.energy}\ndragon's health : {target.health} left")
        print(f"\n2. Monster Attack to player!\ndamage : {target.damage}\n{self.name}'s health : {self.health} left")

# objek monster
class Monster:
    def __init__(self,health=100):
        self.health = health
        print(f"Monster created! Monster's health is {self.health}")
        print('-------------------------------------------------------------')

    def attack_player(self,target,damage=10):
        self.damage = damage
        target.health -= damage

player1 = Player(name='bruno')
dragon = Monster(health=500)

player1.attack_monster(target=dragon,damage=40)
dragon.attack_player(target=player1)
player1.show_info(target=dragon)
