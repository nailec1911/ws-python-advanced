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
- error handling
- coding tips (range, reversed, enumerate, zip, map)
- lambda
- decorator
- generators (yield)

---
layout: full
---

# **Venv**

<v-clicks>

- Environnement virtuel
- Isole les dépendances
- Règle les conflits de version


## Pour le créer


- ``python -m venv myenv`` -> créer le dossier myenv (contient les lib et l'interpreter)
- ``source myenv/bin/activate`` -> 'active' l'environnement virtuel
- ``pip install <package>`` -> instale les paquets dans l'env, pas global


## Sortir

- ``deactivate`` -> sortir de l'environnement
- ``rm -rf myenv`` -> delete le venv
</v-clicks>

---
layout: full
---

## Sauvegarder les dépendances

<v-clicks>

- ``pip freeze > requirements.txt`` : sauvegarde tout les paquets installés
- ``pip install -r requirements.txt`` : recréer l'environment

## Spécifier une version

``python3.9 -m venv myenv``

## Tips

- les paquets installé localement ne sont pas mis dans le venv
- `pip list` : liste les paquets installé
- `pip show <package>` : donne des informations sur le paquet
</v-clicks>

---
layout: full
---

# **Type hints**

<v-clicks>

- Rends le code plus lisible
- Ajoute de l'autocompletion
- Permet un linting plus efficace (**mypy**)
- **ne change rien à l'éxécution**


````md magic-move {lines: true}
```python
def greet(name):  
    return f"Hello, {name}"
a = 12
```
```python
def greet(name: str) -> str:
    return f"Hello, {name}"
a: int = 12
```
````

````md magic-move {lines: true}
```python
from typing import List, Dict, Tuple

def process_data(data):
    return sum(d["value"] for d in data), len(data)  
```
```python
from typing import List, Dict, Tuple

def process_data(data: List[Dict[str, int]]) -> Tuple[int, int]:
    return sum(d["value"] for d in data), len(data)
```
````
</v-clicks>

---
layout: full
---

# Tips

<v-click>

- ``Union`` deux types en un
```python
from typing import Union  

def parse_value(value: Union[str, int]) -> int:  
    if isinstance(value, str):  
        return int(value)  
    return value  
```

</v-click>
<v-click>

- ``Optional``
```python
from typing import Optional  

def find_item(items: List[str], target: str) -> Optional[int]:
    if target in items
        return items.index(target)  
    return None
```
</v-click>

---
layout: full
---

# Tips

<v-click>

- ``Callable``
```python
from typing import Callable  

def apply_function(func: Callable[[int, int], int], a: int, b: int) -> int:  
    return func(a, b)  

result = apply_function(lambda x, y: x + y, 5, 3)  
print(result)  # 8  
```

</v-click>

<v-clicks>

## mypy

- Install : ``pip intall mypy``
- Run :  ``mypy your_script.py``

```python
def add(a: int, b: int) -> int:  
    return a + b  

print(add(3, "4"))  # Error caught by mypy
```
</v-clicks>

---
layout: full
---

# Paramètres

<v-clicks>

- default
```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Charlie")  # Output: Hello, Charlie!
greet("Charlie", "Hi")  # Output: Hi, Charlie!
```

- Keywords
```python
def greet(name, message="Hello", complement=""):
    print(f"{message}, {name} {complement}!")

greet("Charlie")  # Output: Hello, Charlie!
greet("Charlie", message="Hi")  # Output: Hi, Charlie!
greet("Charlie", complement="noob")  # Output: Hello, Charlie noob!
greet("Charlie", message="Hi", complement="noob")  # Output: Hi, Charlie noob!
```
</v-clicks>


---
layout: full
---

# Paramètres


### **Unpacking**

<v-clicks>

- ``*`` -> list, tuples
```python
def add(a, b, c):
    return a + b + c

nums = [2, 3, 4]
print(multiply(*nums))  # Output: 9
```


- ``**`` -> dict
```python
def greet(name, message):
    print(f"{message}, {name}!")

details = {"name": "Alice", "message": "Hello"}
greet(**details)  # Output: Hello, Alice!
```
</v-clicks>


---
layout: full
---

# Error handling

<v-clicks>

- **Try-except** : catch les erreurs
```python
try:
    x = int(input("Enter a number: "))  # This will raise an exception if input is not a number
    print(f"The number is {x}")
except ValueError:
    print("That's not a valid number!")
```

- Erreur spécifique
```python
try:
    x = int(input("Enter a number: ")) # can raise a ValueError
    result = 10 / x  # can raise ZeroDivisionError
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input!")
```

</v-clicks>

---
layout: full
---

# Error handling

- ``else`` : s'execute si il n'y a pas eu d'erreur
- ``finally`` : s'execute dans tout les cas

```python
try:
    file = open("example.txt", "r")  # Try to open a file
    print(file.read())
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully.")  # Only executes if no exception occurs
finally:
    print("Closing the file.")  # Always executes
    if 'file' in locals():
        file.close()
```

---
layout: full
---

# Error handling

- ``raise`` : throw des erreurs
``` python
def validate_arg(arg: int):
    if arg < 10:
        raise ValueError("arg must be > to 10!")
    print("Valid arg.")

try:
    validate_arg(15)
except ValueError as e:
    print(f"Error: {e}")
```

---
layout: full
---

# Error handling

- Erreur custom
```python
class NegativeValueError(Exception):
    pass

def check_positive(number):
    if number < 0:
        raise NegativeValueError("Number must be positive!")

try:
    check_positive(-5)
except NegativeValueError as e:
    print(f"Caught custom exception: {e}")
```

- ``as`` : assigne l'exception a une variable
- ``from`` : permet d'cnhainer les exceptions (en gardant le contexte)
```python
try:
    ...
except FileNotFoundError as e:
    raise ValueError("something happened") from e




---
layout: center
class: text-center
---

# Fin

Cassez vous

<PoweredBySlidev mt-10 />
