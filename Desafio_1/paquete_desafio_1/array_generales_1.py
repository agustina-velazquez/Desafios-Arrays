from .especificas import *
#opcion 1
def ingresar_numeros(cantidad_numeros: int, minimo:int, maximo:int)->list:
    
    numeros = []

    while len(numeros)<cantidad_numeros:
        numero = int(input("Ingrese un número: "))
        if validar_numero(numero, minimo,maximo) == True:
            numeros += [numero]
        else:
            print("Ingrese número dentro del rango")
    
    return numeros


#opcion 2
def cantidad_positivos_negativos(lista: list)->str:

    positivos = 0
    negativos = 0

    for i in range(len(lista)):
        if ver_positividad(lista[i]):
            positivos += 1
        else:
            negativos += 1

    return print(f"Hay {positivos} positivos y {negativos} negativos")

    
#opcion 3
def sumar_pares(lista: list)->int:

    suma = 0

    for i in range(len(lista)):
        if es_par(lista[i]):
            suma += lista[i]
    
    return suma

#opcion 4
def buscar_mayor_impar(lista: list)->int:

    maximo = 0

    for i in range(len(lista)):
        if lista[i] > maximo and es_par(lista[i])==False:
            maximo = lista[i]
    
    return maximo


#opcion 5
def mostrar_numeros(lista: list)->str:
    for i in range(len(lista)):
       print(lista[i])
    
    return print(f"Así fueron ingresados los números")
    
#opcion 6
def mostrar_pares(lista: list)->list:
    lista_pares = []
    for i in range(len(lista)):
        if es_par(lista[i]):
            lista_pares += [lista[i]]

    return lista_pares

#opcion 7
#en realidad no muestra las posiciones, sino los vales en las posiciones impares.
#Pero no se me ocurre como nombrarla sin que sea muy largo el nombre
def mostrar_posiciones_impares(lista: list)->list:
    lista_num_posiciones_impares = []
    for i in range(len(lista)):
        if es_par(i)==False:
            lista_num_posiciones_impares += [lista[i]]
    
    return lista_num_posiciones_impares

#print(ingresar_numeros(10,-1000,1000))



