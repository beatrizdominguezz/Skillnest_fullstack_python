# Listas
# 🎯 Objetivos
# Reconocer la sintaxis de las listas en Python
# Aprender cómo crear y consultar una lista

# Familiarizarse con los métodos integrados de las listas
# Una lista o arreglo (array en inglés), es una estructura de datos
# que permite guardar un conjunto de valores. Imagina que las listas
# son cajoneras, en donde cada cajón del mueble guarda cierta
# información.Para definir una lista colocamos corchetes [ ], y dentro ingresamos los valores separados por comas. Las listas son dinámicas, es decir que podemos agregar o eliminar datos en el momento que necesitemos; también son mutables, es decir que sus elementos pueden ser modificados.

lista_vacia = [] #Listas, arrays, Matriz []
lista_compras = ['tomate', 'pan', 'queso', 'jamón']
# A diferencia de otros lenguajes, las listas en Python
# pueden tener distintos tipos de datos, cadenas,
# números, inclusive otras listas o tuplas.

lista_especial = [1, 2, ['a', 'b', 'c'], True]
# Otra característica interesante de las listas en 
# Python es que puedes combinarlas y duplicar valores
# de una manera muy sencilla utilizando los operadores
# + y *. Si “sumas” dos listas, se creará una nueva
# lista que contiene todos los valores de ambas listas
# combinadas. De igual manera, si “multiplicas” una
# lista por un número entero, copiará todos los
# valores esa cantidad de veces y creará una nueva
# lista con todos los valores copiados. 

#Veamos el siguiente ejemplo:

# verso1 = ['dale', 'a', 'tu', 'cuerpo']
# verso2 = ['alegria', 'macarena']
# estrofa = verso1 + verso2
# print(estrofa)

# cancion = 3 * estrofa
# print(cancion)
# Si ejecutamos el código anterior, tendríamos algo como esto:

# A través de concatenación y multiplicación de listas,
# escribe la canción "Dale a tu cuerpo alegría, Macarena"
# completa
# Estructura de la canción:
# Coro x3
# Estrofa x2
# Coro x4

coro = ['Que', 'tu', 'cuerpo', 'es', 'pa', 'darle', 'alegría', 'y', 'cosa', 'buena']
estrofa = ['dale', 'a', 'tu', 'cuerpo', 'alegria', 'macarena']
coro2 = ['Eh', 'Macarena', '(¡ay!)']
cancion = [3 * coro + 2 * estrofa + 4 * coro2]
print(cancion)




# 🗂️ Acceder a los valores
# Regresando a la analogía de la cajonera, cada cajón está numerado comenzando por el 0. Nuestro primer cajón (índice 0) tiene “pantalones”, el segundo cajón (índice 1) tiene “camisas”, y así por cada cajón. Cada cajón está representado por un número, al cual lo conocemos como índice; este sirve como dirección/posición única que apunta a cada ítem dentro del mueble. Para acceder a ellos lo haremos de la siguiente manera:

cajonera = ["pantalones", "camisetas", "calcetines"]
print(cajonera[0]) #Accedemos al cajón con índice 0. Imprime: "pantalones"
print(cajonera[1]) #Accedemos al cajón con índice 1. Imprime: "camisetas"
print(cajonera[2]) #Accedemos al cajón con índice 2. Imprime: "calcetines"
cajonera[1] = "sueters" #Cambiamos el valor del cajón con índice 1
print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines']

# 🧰 Manipular listas
# Como mencionamos anteriormente, las listas son dinámicas,
# por lo que a través de la función .append() podemos agregar
# elementos. Esta función agrega un nuevo elemento al final de 
#la lista dada.

# cajonera.append("vestidos") #Agregamos "vestidos" al final de la lista
# print(cajonera) #Imprime: ['pantalones', 'sueters', 'calcetines', 'vestidos']
# ✂️ Slicing

# Añadir 4 elementos a la cajonera.

cajonera.append("blusas")
cajonera.append("faldas")
cajonera.append("pijamas")
cajonera.append("dinero")

print(", ".join(cajonera)) #Imprime: 'pantalones', 'sueters', 'calcetines', 'vestidos'
# Algo de gran utilidad en Python es algo llamado 
# Slicing o “Troceado”, que nos permite regresar una
# copia de parte de nuestra lista en base a índices
# específicos. La síntaxis utilizada es: [x:y],
# donde x es el índice inicial y y el índice final.

lista_grande = [2, 4, 6, 8, 10, 12, 14, 16]
print(lista_grande[3:]) #Imprime:[8, 10, 12, 14, 16]
print(lista_grande[:6]) #Imprime:[2, 4, 6, 8, 10, 12]
print(lista_grande[3:6]) #Imprime:[8, 10, 12]

# Ejercicio: Crear una lista de números del 3 al
# al 30 de 3 en 3 y utilizar slicing para imprimir
# los siguientes rangos.
# 1.- Entre 9 y 15
# 2.- Superiores a 21
# 3.- inferiores a 18
# 4.- entre 15 y 27

# 🛠️ Funciones integradas
# Existen múltiples funciones integradas que pueden utilizarse para secuencias todas las secuencias, incluídas tuplas y cadenas. Pero, ¿a qué nos referimos con secuencia? Piensa en una secuencia como cualquier cosa sobre la que podamos recorrer. A continuación te presentamos una función que utilizarás constantemente:

# len(secuencia): Regresa la cantidad de elementos en la secuencia.
vocales = ['a', 'e', 'i', 'o', 'u']
print(len(vocales)) #Imprime: 5

# Ejemplos:
numerosAleatorios = [2, 20, 5, 33, 1, 67]
# 📏 Ejemplos de funciones para secuencias
# len(secuencia): devuelve la longitud (cantidad de elementos) de una secuencia.
print("Largo de variables es: ", len( numerosAleatorios))
# max(secuencia): devuelve el valor más alto en una secuencia.
print("Número más alto: ",max( numerosAleatorios))
# min(secuencia): devuelve el valor más bajo en una secuencia.
print("Número más bajo: ",min( numerosAleatorios))
# sorted(secuencia): devuelve una secuencia ordenada.
print("Número más bajo: ", sorted( numerosAleatorios))

# Encuentra más funciones integradas que te pueden ser de utilidad aquí.

# 🧪 Métodos específicos de Listas
# Ya vimos que con el método .append() agregamos elementos al final de nuestra lista, este es un ejemplo de un método integrado para listas. Los métodos que veremos a continuación son únicamente para listas y no podrán ser utilizados para otros tipos de datos. La sintaxis de estos métodos es colocar primero la lista, seguida de un punto y después el método, como por ejemplo:

frozen = ["Elsa", "Anna", "Olaf"]
# frozen.pop() #Sintaxis: nombre_lista.funcion()
print(frozen) #Imprime: ['Elsa', 'Anna']

listaSeries = ["One Piece", "Moriarty the Patriot", "Lord of Mysteries", "Twisted Wonderland", "Jojos Bizarre Adventure"]

# Algunos métodos comunes para las listas son:

# list.append(valor): añade un valor al final de la lista.

# list.pop(índice): elimina un valor en la posición dada. Si no se pasa ningún parámetro, se eliminará el último valor en la lista.

# list.index(valor): devuelve el índice (posición) del valor dado si existe en la lista y genera un error si no existe.

# list.reverse(): invierte el orden de los elementos, en su lugar.*

# list.sort(): ordena los elementos de menor a mayor, o alfabéticamente para cadenas.