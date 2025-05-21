#valida que un numero este dentro de cierto rango
def validar_numero(numero, minimo, maximo)->bool:
    if minimo < numero and numero < maximo:
        return True
    else:
        return False
    
#decide si un número es positivo o no
def ver_positividad(numero: int)->bool:
    if numero >= 0:
        positividad = True
    else:
        positividad = False

    return positividad

#decide si un número es par o no
def es_par(numero: int)->bool:
    if numero % 2 == 0:
        return True
    else:
        return False
    
#print(es_par(5))

#print(validar_numero(98,-100,100))

