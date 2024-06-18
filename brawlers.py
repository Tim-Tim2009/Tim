#Brawlers
class Brawler():
    def __init__(self, health, speed, damage):
        self.power11_health = health
        self.speed = speed
        self.damage = damage

class Rare(Brawler):
    rarity_out_of_10 = 1

class Super_Rare(Brawler):
    rarity_out_of_10 = 3

class Epic(Brawler):
    rarity_out_of_10 = 5

class Mythic(Brawler):
    rarity_out_of_10 = 8

class Legendary(Brawler):
    rarity_out_of_10 = 10

Nita = Rare()
Colt = Rare()
Bull = Rare()
Barley = Rare()
Rosa = Rare()
El_Primo = Rare()
Poco = Rare()

Carl = Super_Rare()
Jessie = Super_Rare()
Rico = Super_Rare()
Jacky = Super_Rare()
