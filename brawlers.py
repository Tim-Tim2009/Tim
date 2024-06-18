#Brawlers
class Brawler():
    def __init__(self, health, speed, damage):
        self.power11_health = health
        self.speed = speed
        self.damage = damage

class Rare(Brawler):
    rarity_out_of_10 = 1
    color = 'green'

class Super_Rare(Brawler):
    rarity_out_of_10 = 3
    color = 'blue'


class Epic(Brawler):
    rarity_out_of_10 = 5
    color = 'purple'

class Mythic(Brawler):
    rarity_out_of_10 = 8
    color = 'red'

class Legendary(Brawler):
    rarity_out_of_10 = 10
    color = 'yellow'

Nita = Rare()
Colt = Rare()
Bull = Rare()
Barley = Rare()
Rosa = Rare()
El_Primo = Rare()
Poco = Rare()
Brock = Rare()

Carl = Super_Rare()
Jessie = Super_Rare()
Rico = Super_Rare()
Jacky = Super_Rare()
Gus = Super_Rare()
A_R_K_A_D = Super_Rare()
Penny = Super_Rare()
Daryll = Super_Rare()
Tick = Super_Rare()
Dynamike = Super_Rare()

Angelo = Epic()
Larry_and_Laurie = Epic()
Hank = Epic()
Maisie = Epic()
Mandy = Epic()
Sam = Epic()
Bonnie = Epic()
Lola = Epic()
Ash = Epic()
Griff = Epic()
Grom = Epic()
Belle = Epic()
Stu = Epic()
Edgar = Epic()
Colette = Epic()
Nani = Epic()
Gael = Epic()
Emz = Epic()
Bea = Epic()
Bibi = Epic()
Frank = Epic()
Pam = Epic()
Piper = Epic()
Bo = Epic()
