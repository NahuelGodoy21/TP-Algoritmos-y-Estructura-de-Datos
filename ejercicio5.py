def romano_a_decimal(romano):
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_valor = 0

    for letra in romano:
        valor = valores[letra]
        total += valor
        if prev_valor < valor:
            total -= 2 * prev_valor
        prev_valor = valor

    return total

# Ejemplo de uso
numero_romano = "MMXXIV"
numero_decimal = romano_a_decimal(numero_romano)
print(f"El número romano {numero_romano} en decimal es: {numero_decimal}")
