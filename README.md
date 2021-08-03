# Tarea-Buda
Tarea de Buda para proceso de postulación

## Problema: 

Escribe un programa que permita calcular la ruta con menor cantidad de estaciones entre dos estaciones de una red de metro. En la red de metro algunas estaciones pueden tener un color asociado (Rojo o Verde) que indica que un tren exprés de color Rojo pasará solo por estaciones sin color o Roja.

## Solución:

En el caso de tener un metro no exprés, es posible ver la red de metro como un grafo no dirijido con pesos, donde cada arista tiene peso de una unidad. El problema se reduce a encontrar la ruta más corta entre dos nodos de este grafo.

En caso de tener un tren exprés, digamos verde, podemos sacar todos los nodos rojos de la red de manera que el metro ahora parará en todas las estaciones y el problema es equivalente al de un metro no exprés. Para hacer lo anterior cambiamos el grafo de la red no dirigido por uno dirigido, en donde una arista tendrá el valor de 1 si para en la siguiente estación y 0 si no.

Finalmente para encontrar la ruta más corta en un grafo dirigido con pesos no negaivos desde un punto se utiliza el algoritmo Dijkstra.

## Formato de archivo de entrada

El archivo con el input debe tener el siguiente formato:

En la primera línea tendrá dos numeros `n_station` y `n_connection`, la cantidad de estaciones y la cantidad de caminos entre estaciones respectivamente.

La siguiente línea tiene `n_station` caracteres separados por espacio, el i-ésimo caracter corresponde al color de la i-ésima estación. Si el caracter es `V` la estación es verde, si es `R` es roja y si es `*` no tiene color.

Las siguientes `n_connection` lineas tienen dos números `i` y `j` indicando que la i-ésima estación está conectada con la j-ésima estación.

Luego vendrá una linea con dos números `start_station` y `end_station`, la estación donde se inicia el trayecto y se finaliza.

Finalmente la última posee un solo caracter indicando el color del metro el cual puede ser `V` si el metro es exprés y verde, `R` si es exprés y rojo o `*` si no es exprés.

A modo de ejemplo, el archivo de input para la red del enunciado y un metro rojo es:


> 9 9
> 
> \* \* \* \* \* \* V R V
> 
> 1 2
> 
> 2 3
> 
> 3 4
> 
> 4 5
> 
> 5 6
> 
> 6 9
> 
> 9 8
> 
> 8 7
> 
> 7 3
> 
> 1 6
> 
> R


## Testeo solución

Para probar la solución se debe ejecutar en consola:

`$python3 main.py < in.txt > out.txt`

En el comando anterior `in.txt` es la ruta hasta el archivo de entrada y `out.txt` es la ruta donde se quiere guardar el resultado.

Se agregó el archivo `testcase_generator.py` para generar casos de prueba de manera aleatoria, para crear un caso de prueba se puede ejecutar:

`$python3 testcase_generator.py > in.txt `

