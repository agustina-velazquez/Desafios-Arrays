
from paquete_desafio_1.array_generales_1 import *

ejecutar_menu = True

while ejecutar_menu == True:
    print("Opciones del Menú")
    print("1.Ingresar datos.")
    print("2.Cantidad de positivos y negativos.")
    print("3.Suma de números pares.")   
    print("4.Mayor número impar.")
    print("5.Listar los números ingresados.")
    print("6.Listar los numeros pares.")
    print("7.Listar los números en posiciones impares.")
    print("8.Salir del programa.")
    opcion = int(input("Ingrese la opción que desea ejecutar: "))
    
    if opcion == 1:
        lista = ingresar_numeros(10,-1000,1000)
        print(lista)
        opcion = int(input("Ingrese la opción que desea ejecutar"))
    
        match opcion:
    
            case 2:
                print(cantidad_positivos_negativos(lista))
            case 3:
                print(f"la suma de los números pares es: {sumar_pares(lista)}")
            case 4:
                print(f"El mayor número par ingresado es: {buscar_mayor_impar(lista)}")
            case 5: 
                mostrar_numeros(lista)
            case 6:
                print(f"Los números pares son: {mostrar_pares(lista)}")
            case 7:
                print(f"Los números en posiciones impares son: {mostrar_posiciones_impares(lista)}")
            case 8:
                ejecutar_menu = False

    else:
        print("Primero debe ingresar la opción 1.")
        



