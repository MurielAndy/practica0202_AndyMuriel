#frase

frase = input("Introduce una frase")
longitud = -len(frase)-1
fraseinv = frase[-1 :longitud: -1]
print(fraseinv)