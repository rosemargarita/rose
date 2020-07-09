# Ejercicio que define si un estudiante esta aprobado o no
#autor: Rose 

def determinaraprobado(promedio):
    if promedio >=11:
        resultado = "aprobado"
    else:
        resultado ="desaprobado"
    return resultado

promedio = int(input("promedio: "))
print(determinaraprobado(promedio))