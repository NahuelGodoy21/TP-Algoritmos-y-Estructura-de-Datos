class Superhero:
    def __init__(self, name, year, comic_house, biography):
        self.name = name
        self.year = year
        self.comic_house = comic_house
        self.biography = biography

superheroes = [
    Superhero("Linterna Verde", 1940, "DC", "Un superhéroe con un anillo de poder."),
    Superhero("Wolverine", 1974, "Marvel", "Un mutante con garras y factor de curación."),
    Superhero("Dr. Strange", 1963, "DC", "Un mago poderoso."),
    Superhero("Iron Man", 1963, "Marvel", "Un superhéroe con una armadura."),
    Superhero("Capitana Marvel", 1968, "Marvel", "Una superheroína con traje y superpoderes."),
    Superhero("Mujer Maravilla", 1941, "DC", "Una guerrera amazona con un traje."),
    Superhero("Flash", 1940, "DC", "El hombre más rápido del mundo."),
    Superhero("Star-Lord", 1976, "Marvel", "Un aventurero espacial con un traje."),
    Superhero("Batman", 1939, "DC", "Un vigilante con un traje de murciélago."),
    Superhero("Superman", 1938, "DC", "El hombre de acero."),
]

# a. eliminar el nodo que contiene la información de Linterna Verde
superheroes = [hero for hero in superheroes if hero.name != "Linterna Verde"]

# b. mostrar el año de aparición de Wolverine
wolverine_year = next(hero.year for hero in superheroes if hero.name == "Wolverine")
print(f"Año de aparición de Wolverine: {wolverine_year}")

# c. cambiar la casa de Dr. Strange a Marvel
for hero in superheroes:
    if hero.name == "Dr. Strange":
        hero.comic_house = "Marvel"

# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
heroes_with_traje_or_armadura = [hero.name for hero in superheroes if "traje" in hero.biography or "armadura" in hero.biography]
print(f"Superhéroes con 'traje' o 'armadura' en su biografía: {heroes_with_traje_or_armadura}")

# e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
heroes_before_1963 = [(hero.name, hero.comic_house) for hero in superheroes if hero.year < 1963]
print(f"Superhéroes antes de 1963: {heroes_before_1963}")

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla
houses_of_heroes = {hero.name: hero.comic_house for hero in superheroes if hero.name in ["Capitana Marvel", "Mujer Maravilla"]}
print(f"Casa de Capitana Marvel: {houses_of_heroes.get('Capitana Marvel')}")
print(f"Casa de Mujer Maravilla: {houses_of_heroes.get('Mujer Maravilla')}")

# g. mostrar toda la información de Flash y Star-Lord
info_flash_star_lord = [vars(hero) for hero in superheroes if hero.name in ["Flash", "Star-Lord"]]
print(f"Información de Flash y Star-Lord: {info_flash_star_lord}")

# h. listar los superhéroes que comienzan con la letra B, M y S
heroes_starting_with_BMS = [hero.name for hero in superheroes if hero.name[0] in "BMS"]
print(f"Superhéroes que comienzan con B, M y S: {heroes_starting_with_BMS}")

# i. determinar cuántos superhéroes hay de cada casa de comic
from collections import Counter
heroes_by_comic_house = Counter(hero.comic_house for hero in superheroes)
print(f"Cantidad de superhéroes por casa de comic: {heroes_by_comic_house}")
