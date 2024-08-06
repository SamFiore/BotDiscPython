from data.PlantillaHyV import Enemigo as En, Heroe as He

enemigos = {  # Enemigo conforme agregues, debes cambiar en "index.py" la lista
    'esqueleto': En('esqueleto', 100, 10, True),
    'zombie': En('zombie', 200, 30, False)
}
heroes = {  # Heros conforme agregues, debes cambiar en "index.py" la lista
    'mago': He('mago', 100, 10, 50, 300, 500),
    'caballero': He('caballero', 300, 250, 150, 30, 100)
}
