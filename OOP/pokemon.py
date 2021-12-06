import random

import time
from os import system

species = ["fire","water", "grass"]

class Pokemon:

    counter = 0  # <Propiedades de la clase
    xp_rate = 1  # <Propiedades de la clase

    @classmethod     #DECORATOR 
    def set_xp_rate(cls, xp_rate):
        cls.xp_rate = xp_rate

    
    # def set_counter():
    #     Pokemon.counter += 1

    def __init__(self, name, species, HP):
        self.name = name
        self.species = species
        self. HP = HP
        self.attacks = []
        self.is_alive = True
        Pokemon.counter += 1
    
    def learn_attack(self, attack):
        self.attacks.append(attack)
    
    def receive_damage(self, attack):
        self.HP -= attack.damage
        if self.HP <= 0:
            self.is_alive = False
            print("\n"*2, "TU POKEMON HA VUELTO A SU POKE-BOLA".center(85))
    
    
    def __str__(self):
        return f'''Pokemon ({self.name}, {self.species}, {self.HP})'''


class Attack:

    def __init__(self, name, species, damage):
        self.name = name
        self.species = species 
        self.damage = damage


    def __repr__(self):
        return f'''Attack ({self.name}, {self.species}, {self.damage})'''

# Pokemons:

Rino = Pokemon("Rino", species[2], 500.00)
Charmander = Pokemon("Charmander", species[0], 100.00)

# ATTACKS :

# Rino attacks: 

SuperSmash = Attack("SuperSmash", species[2], 45.00)
DeepGoring = Attack("DeepGoring", species[1], 25.00)
RinoDash = Attack("Dash", species[0], 20.00 )

# Charmander attacks :
Flame = Attack("Flame", species[0], 80.00)
Firethrower = Attack("Firethrower", species[0], 150.00)
CharmaPunch = Attack("CharmaPunch", species[2], 70.00 )

# New attacks
# Rino:
Rino.learn_attack(SuperSmash)
Rino.learn_attack(DeepGoring)
Rino.learn_attack(RinoDash)
# Charmander
Charmander.learn_attack(Firethrower)
Charmander.learn_attack(Flame)
Charmander.learn_attack(CharmaPunch)

# Charmander.receive_damage(Rino.attacks[0])  


# v1.0 exp_rate = 1 
# print(Pokemon.xp_rate)

# v1.0 exp_rate = 1.3

# Pokemon.set_xp_rate(1.3)
# print(Pokemon.xp_rate)

user = ""

while user != "q":
    
    print("\n", "Rino", Rino.HP, "vs", "Charmander",Charmander.HP, "\n")
    print(f"Escoge tu ataque " + "\n")
    for i, attack in enumerate(Rino.attacks):
        print(f"{i + 1}. {attack.name}")

    user_index = int(input(" ")) - 1
    attack_chosen = Rino.attacks[user_index]
    Charmander.receive_damage(attack_chosen)
    
    Charmander_attack  = random.choice(Charmander.attacks)
    print(f"Charmander ataca {Charmander_attack.name} y te quita {Charmander_attack.damage} pts de vida")
    Rino.receive_damage(Charmander_attack)
    if Charmander.is_alive == False:
        print("\n"* 2, "GAME OVER")
        input(f"Pulsa Q para salir: ")

    # system("cls")
user = "q"
