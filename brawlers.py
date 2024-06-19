#Brawlers
class Brawler():
    def __init__(self, health, speed, damage, attack_range):
        self.power11_health = health
        self.speed = speed
        self.damage = damage
        self.range = attack_range

class Starter(Brawler):
    rarity_out_of_10 = 0
    color = "None"

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

Shelly = Starter(7400, 'Fast', 3000, 'Long')

Nita = Rare(8000, 'Normal', 1920, 'Normal')
Colt = Rare(5600, 'Normal', , 'Long')
Bull = Rare(10000, 'Fast', 4400, 'Normal')
Barley = Rare(4800, 'Normal', 3200, 'Long')
Rosa = Rare(10800, 'Fast', 2760, 'Short')
El_Primo = Rare()
Poco = Rare(7400, 'Normal', 1520, 'Long')
Brock = Rare(4800, 'Normal', 2320, 'Long')

Carl = Super_Rare()
Jessie = Super_Rare()
Rico = Super_Rare()
Jacky = Super_Rare()
Gus = Super_Rare()
A_R_K_A_D = Super_Rare(10000, 'Very_Slow', 3840, 'Very_Long')
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

Lily = Mythic()
Melody = Mythic()
Mico = Mythic()
Charlie = Mythic()
Chuck = Mythic()
Doug = Mythic()
Willow = Mythic()
R_T = Mythic()
Gray = Mythic()
Buster = Mythic()
Otis = Mythic()
Janet = Mythic()
Eve = Mythic()
Fang = Mythic()
Buzz = Mythic()
Squeak = Mythic()
Ruffs = Mythic()
Byron = Mythic()
Lou = Mythic()
Wally = Mythic()
Max = Mythic()
Mr_P = Mythic()
Gene = Mythic()
Tara = Mythic()
Mortis = Mythic()

Draco = Legendary()
Kit = Legendary()
Cordelius = Legendary()
Chester = Legendary()
Meg = Legendary()
Amber = Legendary()
Surge = Legendary()
Sandy = Legendary()
Leon = Legendary()
Crow = Legendary()
Spike = Legendary()
