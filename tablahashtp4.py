class Pokemon:
    def __init__(self, number, name, types, level):
        self.number = number
        self.name = name
        self.types = types
        self.level = level

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return key % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append(value)

    def get_values_by_key(self, key):
        index = self.hash_function(key)
        return self.table[index]

class PokemonManager:
    def __init__(self):
        self.type_table = HashTable(20)  # Using 20 as an arbitrary size
        self.number_table = HashTable(10)
        self.level_table = HashTable(10)
        
    def add_pokemon(self, pokemon):
        # Insert into type_table
        for pokemon_type in pokemon.types:
            self.type_table.insert(hash(pokemon_type), pokemon)
        
        # Insert into number_table
        self.number_table.insert(pokemon.number % 10, pokemon)
        
        # Insert into level_table
        self.level_table.insert(pokemon.level % 10, pokemon)
    
    def get_pokemons_by_number_ending(self, endings):
        results = []
        for ending in endings:
            results.extend(self.number_table.get_values_by_key(ending))
        return results

    def get_pokemons_by_level_multiple(self, multiples):
        results = []
        for i in range(10):
            if any(i % multiple == 0 for multiple in multiples):
                results.extend(self.level_table.get_values_by_key(i))
        return results

    def get_pokemons_by_types(self, types):
        results = []
        for pokemon_type in types:
            results.extend(self.type_table.get_values_by_key(hash(pokemon_type)))
        return results

# Ejemplo de uso
manager = PokemonManager()

# Añadir Pokémons
manager.add_pokemon(Pokemon(1, "Bulbasaur", ["Planta", "Veneno"], 5))
manager.add_pokemon(Pokemon(4, "Charmander", ["Fuego"], 8))
manager.add_pokemon(Pokemon(7, "Squirtle", ["Agua"], 10))
manager.add_pokemon(Pokemon(25, "Pikachu", ["Eléctrico"], 12))
manager.add_pokemon(Pokemon(37, "Vulpix", ["Fuego"], 20))
manager.add_pokemon(Pokemon(58, "Growlithe", ["Fuego"], 15))

# Mostrar todos los Pokémons cuyos números terminan en 3, 7 y 9
print("Pokémons con números terminados en 3, 7 y 9:")
for pokemon in manager.get_pokemons_by_number_ending([3, 7, 9]):
    print(vars(pokemon))

# Mostrar todos los Pokémons cuyos niveles son múltiplos de 2, 5 y 10
print("\nPokémons con niveles múltiplos de 2, 5 y 10:")
for pokemon in manager.get_pokemons_by_level_multiple([2, 5, 10]):
    print(vars(pokemon))

# Mostrar todos los Pokémons de los siguientes tipos: Acero, Fuego, Eléctrico, Hielo
print("\nPokémons de tipos Acero, Fuego, Eléctrico, Hielo:")
for pokemon in manager.get_pokemons_by_types(["Acero", "Fuego", "Eléctrico", "Hielo"]):
    print(vars(pokemon))
