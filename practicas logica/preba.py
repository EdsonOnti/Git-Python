def max_producto(lista=None):
    if lista is None:
        entrada = input("Ingresa cuatro números separados por espacios: ")
        lista = [int(num) for num in entrada.split()]

    maximo_producto = max([lista[i] * lista[j] for i in range(len(lista)) for j in range(i, len(lista)) if i != j])

    return maximo_producto
print(max_producto())