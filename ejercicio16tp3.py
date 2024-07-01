class Pokemon:
    def __init__(self, name, level, type, subtype):
        self.name = name
        self.level = level
        self.type = type
        self.subtype = subtype

class Trainer:
    def __init__(self, name, tournaments_won, battles_lost, battles_won, pokemons):
        self.name = name
        self.tournaments_won = tournaments_won
        self.battles_lost = battles_lost
        self.battles_won = battles_won
        self.pokemons = pokemons

trainers = [
    Trainer("Ash", 5, 10, 40, [Pokemon("Pikachu", 70, "Electric", ""), Pokemon("Charizard", 80, "Fire", "Flying")]),
    Trainer("Misty", 3, 20, 50, [Pokemon("Starmie", 65, "Water", "Psychic"), Pokemon("Gyarados", 85, "Water", "Flying")]),
    Trainer("Brock", 1, 30, 30, [Pokemon("Onix", 75, "Rock", "Ground"), Pokemon("Geodude", 55, "Rock", "Ground")]),
    Trainer("Gary", 4, 5, 35, [Pokemon("Blastoise", 90, "Water", ""), Pokemon("Umbreon", 85, "Dark", "")])
]

# a. obtener la cantidad de Pokémons de un determinado entrenador
def cantidad_pokemons(entrenador):
    for trainer in trainers:
        if trainer.name == entrenador:
            return len(trainer.pokemons)
    return 0

# b. listar los entrenadores que hayan ganado más de tres torneos
def entrenadores_mas_de_tres_torneos():
    return [trainer.name for trainer in trainers if trainer.tournaments_won > 3]

# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados
def pokemon_mayor_nivel_mejor_entrenador():
    best_trainer = max(trainers, key=lambda trainer: trainer.tournaments_won)
    best_pokemon = max(best_trainer.pokemons, key=lambda pokemon: pokemon.level)
    return best_pokemon.name

# d. mostrar todos los datos de un entrenador y sus Pokémons
def mostrar_entrenador_y_pokemons(entrenador):
    for trainer in trainers:
        if trainer.name == entrenador:
            print(f"Entrenador: {trainer.name}, Torneos ganados: {trainer.tournaments_won}, Batallas perdidas: {trainer.battles_lost}, Batallas ganadas: {trainer.battles_won}")
            for pokemon in trainer.pokemons:
                print(f"  Pokémon: {pokemon.name}, Nivel: {pokemon.level}, Tipo: {pokemon.type}, Subtipo: {pokemon.subtype}")
            return
    print("Entrenador no encontrado")

# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %
def entrenadores_porcentaje_ganados_mayor_79():
    return [trainer.name for trainer in trainers if (trainer.battles_won / (trainer.battles_won + trainer.battles_lost)) > 0.79]

# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador (tipo y subtipo)
def entrenadores_tipo_fuego_planta_agua_volador():
    return [trainer.name for trainer in trainers if any((pokemon.type == "Fire" and pokemon.subtype == "Plant") or (pokemon.type == "Water" and pokemon.subtype == "Flying") for pokemon in trainer.pokemons)]

# g. el promedio de nivel de los Pokémons de un determinado entrenador
def promedio_nivel_pokemons(entrenador):
    for trainer in trainers:
        if trainer.name == entrenador:
            total_level = sum(pokemon.level for pokemon in trainer.pokemons)
            return total_level / len(trainer.pokemons)
    return 0

# h. determinar cuántos entrenadores tienen a un determinado Pokémon
def cantidad_entrenadores_con_pokemon(pokemon_name):
    return sum(1 for trainer in trainers if any(pokemon.name == pokemon_name for pokemon in trainer.pokemons))

# i. mostrar los entrenadores que tienen Pokémons repetidos
def entrenadores_pokemons_repetidos():
    return [trainer.name for trainer in trainers if len(trainer.pokemons) != len(set(pokemon.name for pokemon in trainer.pokemons))]

# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull
def entrenadores_con_pokemons_especificos():
    especificos = {"Tyrantrum", "Terrakion", "Wingull"}
    return [trainer.name for trainer in trainers if any(pokemon.name in especificos for pokemon in trainer.pokemons)]

# k. determinar si un entrenador “X” tiene al Pokémon “Y”
def entrenador_tiene_pokemon(entrenador, pokemon):
    for trainer in trainers:
        if trainer.name == entrenador:
            for p in trainer.pokemons:
                if p.name == pokemon:
                    print(f"Entrenador: {trainer.name}, Torneos ganados: {trainer.tournaments_won}, Batallas perdidas: {trainer.battles_lost}, Batallas ganadas: {trainer.battles_won}")
                    print(f"  Pokémon: {p.name}, Nivel: {p.level}, Tipo: {p.type}, Subtipo: {p.subtype}")
                    return True
    return False

# Ejemplos de uso:
print(f"Cantidad de Pokémons de Ash: {cantidad_pokemons('Ash')}")
print(f"Entrenadores con más de tres torneos ganados: {entrenadores_mas_de_tres_torneos()}")
print(f"Pokémon de mayor nivel del entrenador con más torneos ganados: {pokemon_mayor_nivel_mejor_entrenador()}")
mostrar_entrenador_y_pokemons('Ash')
print(f"Entrenadores con más del 79% de batallas ganadas: {entrenadores_porcentaje_ganados_mayor_79()}")
print(f"Entrenadores con tipo Fuego/Planta o Agua/Volador: {entrenadores_tipo_fuego_planta_agua_volador()}")
print(f"Promedio de nivel de los Pokémons de Ash: {promedio_nivel_pokemons('Ash')}")
print(f"Entrenadores que tienen a Pikachu: {cantidad_entrenadores_con_pokemon('Pikachu')}")
print(f"Entrenadores con Pokémons repetidos: {entrenadores_pokemons_repetidos()}")
print(f"Entrenadores con Tyrantrum, Terrakion o Wingull: {entrenadores_con_pokemons_especificos()}")
print(f"Ash tiene a Pikachu: {entrenador_tiene_pokemon('Ash', 'Pikachu')}")
