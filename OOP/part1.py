class Hero: #template 
    pass

hero1 = Hero() #object
hero2 = Hero()
hero3 = Hero()

hero1.name = "Moskov"
hero1.health = 100

hero2.name = "Miya"
hero2.health = 200

hero3.name = "Bruno"
hero3.health = 250

print('data ke-1 =')
print(hero1)
print(hero1.__dict__)
print(hero1.name,'\n')

print('data ke-2 =')
print(hero2)
print(hero2.__dict__)
print(hero2.name,'\n')

print('data ke-3 =')
print(hero3)
print(hero3.__dict__)
print(hero3.name,'\n')