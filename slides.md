---
theme: default
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Object in Python
# info: |
  # Slidev Starter Template

# apply unocss classes to the current slide
class: text-center
# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
---

# Object in Python

---
layout: full
---

# Summary

- venv
- typing
- params in function (default, kwargs, unpacking)
- coding tips (range, reversed, enumerate, zip, map)
- lambda
- decorator
- generators (yield)

---
layout: full
---

# Venv

<v-clicks>

- Isole les dépendances
- évite les conflits de version

</v-clicks>
<v-click>

```python {all|1-8|2-4|5-7|all}
    class Voiture:
        def __init__(self, marque, couleur): # optionel
            self.marque = marque  # Attribut
            self.couleur = couleur  # Attribut

        def demarrer(self):  # Méthode 
            print(f"La voiture {self.marque} démarre.")

    ma_voiture = Voiture("Tesla", "rouge")
    ma_voiture.demarrer()
    print(ma_voiture.marque)
```

</v-click>

---
layout: two-cols
---

# **Syntaxe Python**

<v-click>

### **1. `class`**

- définit une nouvelle **classe**.
- **PascalCase**.

<br>
</v-click>
<v-click>

### **2. `__init__`**

- Appelée automatiquement à de la création.
- initialise l'objet.

<br>
</v-click>
<v-click>

### **3. Le Paramètre `self`**

- Représente l'instance actuelle.
- Premier paramètre de toutes les méthodes de la classe.

</v-click>

::right::


```python
    class Voiture:
        def __init__(self, marque, couleur):
            self.marque = marque  # Attribut
            self.couleur = couleur  # Attribut

        def demarrer(self):  # Méthode 
            print(f"La voiture {self.marque} démarre.")

    ma_voiture = Voiture("Tesla", "rouge")
    ma_voiture.demarrer()
    print(ma_voiture.marque)
```

---
layout: full
---

# Test Yourself

````md magic-move {lines: true}
```python
compte = CompteBancaire("Jean Dupont", 1000)  # Crée un compte avec 1000€
compte.deposer(500)  # Ajoute 500€ au solde
compte.retirer(200)  # Retire 200€ du solde
compte.afficher_solde()  # Affiche : "Le solde de Jean Dupont est de 1300€."
```
```python
class CompteBancaire:
    def __init__(self, name, amount):
        self.amount = amount
        self.name = name

    def deposer(self, value):
        self.amount += value

    def retirer(self, value):
        self.amount -= value

    def afficher_solde(self):
        print(f"Le solde de Jean Dupont est de {self.amount}€."")

compte = CompteBancaire("Jean Dupont", 1000)  # Crée un compte avec 1000€
compte.deposer(500)  # Ajoute 500€ au solde
compte.retirer(200)  # Retire 200€ du solde
compte.afficher_solde()  # Affiche : "Le solde de Jean Dupont est de 1300€."
```
````

---
layout: center
---

# **L'Héritage**


- Créer une nouvelle classe à partir d'une classe existante.
- La classe **enfant** hérite des **attributs** et **méthodes** de la classe **parent**.
- **modifie ou étend** le comportement d’une classe existante sans dupliquer le code.

## **`super()` :**

- permet à la classe enfant de réutiliser la classe parent.
  - `super().__init__()`

---

### **Classe Parent :** `Animal`

<v-click>

```python {all|1-4|1-8|1-12|1-16|all}
class Animal:
    def __init__(self, nom):
        self.nom = nom
        self.food = 0

    def manger(self):
        self.food += 1
        print(f"{self.nom} mange")

    def parler(self):
        print(f"{self.nom} parle")

class Chien(Animal):
    def __init__(self, nom, race):
        super().__init__(nom)
        self.race = race

    def parler(self):
        print(f"{self.nom} {race} aboie.")

# Créer un objet Chien
mon_chien = Chien("Rex", "berger")
mon_chien.mange()
mon_chien.parler()  # Affiche : "Rex berger aboie."
```

</v-click>

---
layout: full
---

# Test Yourself

````md magic-move {lines: true}
```python
spaceship = Vehicle(10000)
spaceship.speed_up(300)
print(spaceship.speed) # display : 300
voiture = Car(200)
voiture.speed_up(30) # display : "c'est la course"
print(voiture.speed) # display "30"
voiture.drift() # display: "deja vu: delivering sushi at kmh"
```
```python
class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed
        self.speed = 0

    def speed_up(self, accel):
        self.speed += accel

class Car(Vehicle):
    def speed_up(self, accel):
        print("c'est la course")
        return super().speed_up(accel)

    def drift(self):
        print(f"deja vu: delivering sushi at {self.speed} kmh")

spaceship = Vehicle(10000)
spaceship.speed_up(300)
print(spaceship.speed) # display : 300
voiture = Car(200)
voiture.speed_up(30) # display : "c'est la course"
print(voiture.speed) # display "30"
voiture.drift() # display: "deja vu: delivering sushi at kmh"
```
````

---
layout: full
---

# Polymorphisme

<v-clicks>

- Handle différentes classes de la même manière
- Override les fonctions abstraites

```python {1-4|1-8|1-12|all}
class Animal:
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("Aboie")

class Chat(Animal):
    def parler(self):
        print("Miaule")

class Ours(Animal):
    pass

animaux = [Animal(), Chien(), Chat(), Ours()]
for animal in animaux:
    animal.parler()
# Output: "Aboie", "Miaule"
```

</v-clicks>

---
layout: full
---

# Classe abstraites

- Ne peuvent pas être instanciée

```python {1-6|1-10|1-14|all}
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        print("Aboie")

class Ours(Animal):
    pass

# a = Animal()
# o = Ours()
animaux = [Chien()]
for animal in animaux:
    animal.parler()
# Output: "Aboie", "Miaule"
```

---
layout: full
---

# Membres privés

- Membre innaccessibles hors de la classe

```python
class Compte:
    def __init__(self, solde):
        self.__solde = solde  # Private attribute

    def deposer(self, montant):
        self.__solde += montant

    def afficher_solde(self):
        print(f"Solde: {self.__solde}")

compte = Compte(100)
compte.deposer(50)
compte.afficher_solde()  # Output: Solde: 150
```

---
layout: full
---

# Methodes magiques et Overload

- méthode spécialles `__str__`, `__add__`, `__len__` ... utilisées par le python.
- permet aux objets de se comporter comme des built-in

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3)  # Output: (4, 6)
```

---
layout: two-cols

---

# Exercice

1. Attributes:
    - x and y (coordinates of the vector).
2. Magic Methods to Implement:
    - `__add__`: Add two vectors (vector addition).
    - `__sub__`: Subtract one vector from another.
    - `__mul__`: Multiply a vector by a scalar (e.g., v1 * 3).
    - `__str__`: Return a readable string representation of the vector (e.g., "(3, 4)").
3. Bonus:
    - `print(3 * v1)`
    - `print(v1 == v2)`

::right::

```python
v1 = Vector(2, 3)
v2 = Vector(1, 4)

v3 = v1 + v2
print(v3)  # Output: (3, 7)
v4 = v1 - v2
print(v4)  # Output: (1, -1)
v5 = v1 * 3
print(v5)  # Output: (6, 9)
print(v1)  # Output: (2, 3)
```

```
> python3 vector.py
(3, 7)
(1, -1)
(6, 9)
(2, 3)
```

---
layout: center
class: text-center
---

# Fin

Cassez vous

<PoweredBySlidev mt-10 />
