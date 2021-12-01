

species = ["fire","water", "grass"]

class Pokemon:
    def __init__(self, name, species, HP):
        self.name = name
        self.species = species
        self. HP = HP
        self.attacks = []
    
    def learn_atack(self, attack):
        self.attacks.append(attack)   
    
    def __str__(self):
        return f'''Pokemon ({self.name}, {self.species}, {self.HP})'''


Rino = Pokemon("Rino", species[2], 500)
print(Rino)


print(Rino.attacks)

class Attack:
    def __init__(self, name, species, damage):
        self.name = name
        self.species = species 
        damage = damage

SuperSmash = Attack("SuperSmash", species[2], 15)

Rino.learn_atack("SuperSmash")
print(Rino.attacks)
