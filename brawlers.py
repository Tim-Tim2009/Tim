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
Colt = Rare(5600, 'Normal', 4320, 'Long')
Bull = Rare(10000, 'Fast', 4400, 'Normal')
Barley = Rare(4800, 'Normal', 3200, 'Long')
Rosa = Rare(10800, 'Fast', 2760, 'Short')
El_Primo = Rare(11400, 'Fast', 3040, 'Short')
Poco = Rare(7400, 'Normal', 1520, 'Long')
Brock = Rare(4800, 'Normal', 2320, 'Long')

Carl = Super_Rare(8000, 'Normal', 2960, 'Long')
Jessie = Super_Rare(6000, 'Normal', 2120, 'Long')
Rico = Super_Rare(5600, 'Normal', 3200, 'Very Long')
Jacky = Super_Rare(10000, 'Fast', 2280, 'Short')
Gus = Super_Rare(6400, 'Normal', 1880, 'Very Long')
A_R_K_A_D = Super_Rare(10000, 'Very Slow', 3840, 'Very Long')
Penny = Super_Rare(6400, 'Normal', 1960, 'Long')
Darryl = Super_Rare(10600, 'Fast', 4800, 'Normal')
Tick = Super_Rare(4400, 'Normal', 3840, 'Long')
Dynamike = Super_Rare(5600, 'Fast', 3200, 'Long')

Angelo = Epic(6000, 'Very Fast', 4400, 'Very Long')
Larry_and_Laurie = Epic()
Hank = Epic()
Maisie = Epic()
Mandy = Epic()
Sam = Epic()
Bonnie = Epic(9600, 'Slow', 2000, 'Long')
Lola = Epic()
Ash = Epic(10400, 'Normal', 3200, 'Normal')
Griff = Epic()
Grom = Epic()
Belle = Epic(5200, 'Normal', 2080, 'Very Long')
Stu = Epic()
Edgar = Epic()
Colette = Epic(6800, 'Normal', 1000, 'Long')
Nani = Epic()
Gael = Epic()
Emz = Epic()
Bea = Epic(4800, 'Normal', 4400, 'Very Long')
Bibi = Epic(9600, 'Very Fast', 2800, 'Short')
Frank = Epic()
Pam = Epic()
Piper = Epic()
Bo = Epic(7200, 'Normal', 3600, 'Long')

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
