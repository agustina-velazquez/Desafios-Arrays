#sirve para permitir al usuario ingresar su lista manualmente, pasando el tamaño como parametro
def cargar_lista(tamaño)->list:
    '''permite cargar una lista secuencialmente
    '''
    lista = []
    for i in range(tamaño):
        numero = int(input(f"Ingrese valor para la posicion {i}: "))
        lista += [numero]
    
    return lista


def recortar_lista(lista: list):
    '''es una función auxiliar que recibe una lista 
    y la recorta donde encuentre el primer elemento
    que sea False
    '''
    for i in range(len(lista)):
        if lista[i] == False:
            indice_final = i
            break
        else: 
            indice_final = len(lista)
    
    lista = lista[0: indice_final]

    return lista



def devolver_interseccion(lista_1: list, lista_2: list)->list:
    '''recibe 2 listas y retorna una nueva lista con 
    la intersección entre ambas
    '''
    if len(lista_1) > len(lista_2):
        maximo = len(lista_2)
    else:
        maximo = len(lista_1)

    lista_retorno = [False] * maximo

    indice_retorno = 0

    for i in range(len(lista_1)):
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                lista_retorno[indice_retorno] = lista_1[i]
                indice_retorno += 1
                break

    lista_retorno = recortar_lista(lista_retorno)


    return lista_retorno


def devolver_diferencia(lista_1: list, lista_2: list)->list:
    '''recibe 2 listas y retorna la primer lista pasada
    como parametro menos la segunda lista pasada como
    parametro
    '''
    
    maximo = len(lista_1) #porque hacemos lista_1 - lista_2
    lista_retorno = [False] * maximo
    indice_retorno = 0

    for i in range(maximo):
        bandera = False
        for j in range(len(lista_2)):
            if lista_1[i] == lista_2[j]:
                bandera = True
                break

        if bandera == False:
            lista_retorno[indice_retorno] = lista_1[i]
            indice_retorno += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno


def devolver_union(lista_1: list, lista_2: list)->list:

    '''recibe 2 listas, y retorna la unión de las mismas
    sin tener en cuenta las repeticiones
    '''

    maximo = len(lista_1) + len(lista_2)
    lista_retorno = [False] * maximo

    for i in range (len(lista_1)):
        lista_retorno[i] = lista_1[i]

    indice_retorno = len(lista_1)

    for j in range(len(lista_2)):
        bandera = False
        for i in range(len(lista_1)):
            if lista_1[i] == lista_2[j]:
                bandera = True
                break

        if bandera == False:
            lista_retorno[indice_retorno] = lista_2[j]
            indice_retorno += 1

    lista_retorno = recortar_lista(lista_retorno)

    return lista_retorno





