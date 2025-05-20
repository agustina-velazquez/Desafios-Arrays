from paquete_desafio_2.funciones_desfio import *
print("Productos comprados por el usuario A")
lista_a = cargar_lista(4)

print("Productos comprados por el usuario B")
lista_b = cargar_lista(5)

print("Estos sos los productos comprados por A y B: ")
print(f"Productos de A: {lista_a}")    
print(f"Productos de B: {lista_b}")

productos_en_comun = devolver_interseccion(lista_a, lista_b)

print("Productos en común: ")
print(f"Ambos usuarios han comprado esta lista de productos: {productos_en_comun} ")

productos_exclusivos_a = devolver_diferencia(lista_a, lista_b)
productos_exclusivos_b = devolver_diferencia(lista_b, lista_a)

print("Productos exclusivos: ")
print(f"Productos exlusivos de A: {productos_exclusivos_a}")
print(f"Productos exclusivos de B: {productos_exclusivos_b}")

catalogo_total = devolver_union(lista_a, lista_b)

print("Catálogo total: ")
print(f"Productos comprados entre A y B: {catalogo_total}")

print("Recomendaciones: ")
print(f"Productos sugeridos para A: {productos_exclusivos_b}")
print(f"Prodcutos sugeridos para B: {productos_exclusivos_a}")