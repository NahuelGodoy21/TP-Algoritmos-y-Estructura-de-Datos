class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __repr__(self):
        return f"Stack({self.items})"

# Personajes del Episodio V: The Empire Strikes Back
stack_episode_v = Stack()
characters_episode_v = ["Luke Skywalker", "Darth Vader", "Leia Organa", "Han Solo", "Yoda"]
for character in characters_episode_v:
    stack_episode_v.push(character)

# Personajes del Episodio VII: The Force Awakens
stack_episode_vii = Stack()
characters_episode_vii = ["Luke Skywalker", "Leia Organa", "Han Solo", "Kylo Ren", "Rey"]
for character in characters_episode_vii:
    stack_episode_vii.push(character)

# Convertir las pilas a conjuntos para encontrar la intersección
set_episode_v = set(stack_episode_v)
set_episode_vii = set(stack_episode_vii)

# Encontrar la intersección de ambos conjuntos
intersection = set_episode_v.intersection(set_episode_vii)

# Convertir la intersección de vuelta a una pila
intersection_stack = Stack()
for character in intersection:
    intersection_stack.push(character)

# Mostrar el resultado
print("Personajes que aparecen en ambos episodios:")
print(intersection_stack)
