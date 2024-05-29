class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def __len__(self):
        return self.size

def find_positions(stack, names):
    temp_stack = Stack()
    positions = {name: None for name in names}
    position = 1

    while not stack.is_empty():
        character = stack.pop()
        temp_stack.push(character)
        if character['name'] in names:
            positions[character['name']] = position
        position += 1

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return positions

def characters_in_more_than_n_movies(stack, n):
    temp_stack = Stack()
    characters = []

    while not stack.is_empty():
        character = stack.pop()
        temp_stack.push(character)
        if character['movies'] > n:
            characters.append((character['name'], character['movies']))

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return characters

def movies_of_character(stack, character_name):
    temp_stack = Stack()
    movies = None

    while not stack.is_empty():
        character = stack.pop()
        temp_stack.push(character)
        if character['name'] == character_name:
            movies = character['movies']
            break

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return movies

def characters_starting_with(stack, letters):
    temp_stack = Stack()
    characters = []

    while not stack.is_empty():
        character = stack.pop()
        temp_stack.push(character)
        if character['name'][0] in letters:
            characters.append(character['name'])

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return characters

# New example usage
mcu_stack = Stack()
mcu_stack.push({'name': 'Iron Man', 'movies': 10})
mcu_stack.push({'name': 'Captain America', 'movies': 9})
mcu_stack.push({'name': 'Thor', 'movies': 8})
mcu_stack.push({'name': 'Black Widow', 'movies': 7})
mcu_stack.push({'name': 'Hulk', 'movies': 5})
mcu_stack.push({'name': 'Hawkeye', 'movies': 4})
mcu_stack.push({'name': 'Rocket Raccoon', 'movies': 6})
mcu_stack.push({'name': 'Groot', 'movies': 5})
mcu_stack.push({'name': 'Doctor Strange', 'movies': 4})
mcu_stack.push({'name': 'Scarlet Witch', 'movies': 5})
mcu_stack.push({'name': 'Spider-Man', 'movies': 5})
mcu_stack.push({'name': 'Ant-Man', 'movies': 3})
mcu_stack.push({'name': 'Black Panther', 'movies': 4})
mcu_stack.push({'name': 'Star-Lord', 'movies': 4})
mcu_stack.push({'name': 'Gamora', 'movies': 4})

# a. Determine positions of Rocket Raccoon and Groot
positions = find_positions(mcu_stack, ['Rocket Raccoon', 'Groot'])
print("Positions of Rocket Raccoon and Groot:", positions)

# b. Determine characters in more than 5 movies
characters_more_than_5 = characters_in_more_than_n_movies(mcu_stack, 5)
print("Characters in more than 5 movies:", characters_more_than_5)

# c. Determine movies Black Widow appeared in
black_widow_movies = movies_of_character(mcu_stack, 'Black Widow')
print("Movies Black Widow appeared in:", black_widow_movies)

# d. Show characters whose names start with C, D, and G
characters_with_specific_letters = characters_starting_with(mcu_stack, ['C', 'D', 'G'])
print("Characters starting with C, D, and G:", characters_with_specific_letters)
