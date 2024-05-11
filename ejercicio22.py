def usar_la_fuerza(mochila, objetos_sacados=0):
    if not mochila:
        # Si la mochila está vacía, no hay sable de luz
        return False, objetos_sacados
    elif mochila[0] == "sable de luz":
        # Si el primer objeto es un sable de luz, lo encontramos
        return True, objetos_sacados + 1
    else:
        # Si no es un sable de luz, lo sacamos y seguimos buscando
        return usar_la_fuerza(mochila[1:], objetos_sacados + 1)

# Ejemplo de uso:
mochila = ["ropa", "comida", "botiquín", "sable de luz", "libro"]
encontrado, objetos_necesarios = usar_la_fuerza(mochila)
if encontrado:
    print("¡El Jedi encontró un sable de luz en la mochila!")
    print("Se necesitaron {} objetos sacados para encontrarlo.".format(objetos_necesarios))
else:
    print("El Jedi no encontró un sable de luz en la mochila.")
