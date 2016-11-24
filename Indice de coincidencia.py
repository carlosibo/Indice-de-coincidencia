
texto = raw_input("Introduzca un texto para hallar su indice de coincidencia: ")
letras = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
contador_letras = []
x = 0
while x < len(letras):
    contador = 0
    for letra in texto:
        if letra == letras[x]:
            contador = contador +1
    x = x + 1
    contador_letras.append(contador)
indice = 0
y = 0
while y < len(letras):
    indice = indice + contador_letras[y]*(contador_letras[y]-1)
    y= y+1
denominador = len(texto)*(len(texto)-1)
indice = float(indice)
denominador = float(denominador)

resultado = indice/denominador

print ("El indice de coincidencia es", "{0:.4f}".format(resultado))
