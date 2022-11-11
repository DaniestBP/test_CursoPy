# ABSTRACTION, ENCAPSULATION,INHERITANCE, POLYMORPHISM

# ENCAPSULATION: Un ejemplo son los metodos de las listas. pertenecen solo a los elementos 'listas'. Programacion mas compacta.
# ABSTRACTION: Ejemplo las APIs, son sabemos el lenguaje de las bases de datos de las APIs, pero podemos interactuar o manejar sus datos. 


## Instance attributes
"""
class Nane_of_class:
    def __init__(self, attribute):
        self.attribute = attribute
"""        

class Dog:
    def __init__(self, name, breed, age, owner):
        self.name = name     #
        self.breed = breed   # Valores constantes como la raza puede que no sean utiles pues siempre van a ser iguales(en ppio)
        self.age = age
        self.owner = owner
    
    def bark(self):
        return "Guau!"

    def birthday(self):
        self.age += 1

    def change_owner(self, new_owner):
        self.owner = new_owner


Bul = Dog("Bul", "Chucho", 11, "Daniel")

print(Bul.owner)
Bul.birthday()
print(Bul.age)
Bul.change_owner("Juan")
print(Bul.owner)    
print(Bul.name)
