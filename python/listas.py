lista = ["a","b","c","d","e"]

#accediendo al primer elemento (indice 0)
primer_elemento = lista [0]
print("primer elemento:", primer_elemento)

#accediendo al primer elemento (indice 1)
segundo_elemento = lista [1]
print("segundo elemento:", segundo_elemento)

#accediendo al primer elemento (indice 2)
tercer_elemento = lista [2]
print("tercer elemento:", tercer_elemento)

#accediendo al primer elemento (indice 3)
cuarto_elemento = lista [3]
print("cuarto elemento:", cuarto_elemento)

#accediendo al primer elemento (indice 4)
quinto_elemento = lista [4]
print("quinto elemento:", quinto_elemento)


lista = ["a","b","c","d","e"]

#usamos la funcion len() para obtener el numero de elementos en la lista
numero_de_elementos = len(lista)
print("numero de elementos en la lista:", numero_de_elementos)

#definimos una lista

lista = ["a","b","c","d","e"]

#usammos una expresion para calcular el indice
indice= 2+1

#accedemos al elemento usando el indice calculado dinamicamente
elemento = lista[indice]

#imprimimos el elemento 
print("elemento en el indice", indice, ":", elemento)



#definimos una lista

lista = ["a","b","c","d","e"]

#cambiamos el elemento en el indice 2 (tercer elemento) por "x"
lista[2] = "x"

#imprimimos la lista actualizada
print("lista despues de cambiar el elemento en el indice 2:" , lista)

#definimos una lista con tres elementos
lista = ["a","b","c"]

#desempaquetamos los elementos de la lista en variables individuales 
variable1, variable2, variable3 = lista

#imprimimos las variables
print("variable1",variable1)
print("variable2",variable2)
print("variable3",variable3)

#definimos un alista con tres elementos

datos = ["juan", 25, "ingeniero"]

#desempaquetamos los elementos de la lista en variables individuales
nombre, edad, profesion = datos

print("nombre:",nombre)
print("edad",edad)
print("profesion",profesion)

#definimos dos lista
lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenamos las dos listas usando el operador +
concatenacion1 = lista1 + lista2

#concatenamos las 2 listas usando el metodo extend()

lista1.extend(lista2)
concatenacion2 = lista1

#imprimimos los resultados
print("concatenacion usando el operador +:",concatenacion1)
print("concatenacion con el extend:",concatenacion2)


