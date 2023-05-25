# Dado el siguiente listado:

peliculas = [
    {
        'titulo': 'El padrino',
        'año': 1972,
        'genero': 'Drama',
        'duracion': 175
    },
    {
        'titulo': 'Pulp Fiction',
        'año': 1994,
        'genero': 'Crimen',
        'duracion': 154
    },
    {
        'titulo': 'El señor de los anillos: El retorno del rey',
        'año': 2003,
        'genero': 'Fantasía',
        'duracion': 201
    },
    {
        'titulo': 'El bueno, el malo y el feo',
        'año': 1966,
        'genero': 'Western',
        'duracion': 161
    },
    {
        'titulo': 'El origen',
        'año': 2010,
        'genero': 'Ciencia ficción',
        'duracion': 148
    },
    {
        'titulo': 'La lista de Schindler',
        'año': 1993,
        'genero': 'Drama',
        'duracion': 195
    },
    {
        'titulo': 'Cadena perpetua',
        'año': 1994,
        'genero': 'Drama',
        'duracion': 142
    },
    {
        'titulo': 'Casablanca',
        'año': 1942,
        'genero': 'Romance',
        'duracion': 102
    },
    {
        'titulo': 'Interestelar',
        'año': 2014,
        'genero': 'Ciencia ficción',
        'duracion': 169
    },
    {
        'titulo': 'Forrest Gump',
        'año': 1994,
        'genero': 'Drama',
        'duracion': 142
    },
    {
        'titulo': 'El sexto sentido',
        'año': 1999,
        'genero': 'Suspenso',
        'duracion': 107
    },
    {
        'titulo': 'Matrix',
        'año': 1999,
        'genero': 'Ciencia ficción',
        'duracion': 136
    },
    {
        'titulo': 'El rey león',
        'año': 1994,
        'genero': 'Animación',
        'duracion': 88
    },
    {
        'titulo': 'Gladiador',
        'año': 2000,
        'genero': 'Acción',
        'duracion': 155
    },
    {
        'titulo': 'Titanic',
        'año': 1997,
        'genero': 'Drama',
        'duracion': 194
    },
    {
        'titulo': 'El club de la pelea',
        'año': 1999,
        'genero': 'Drama',
        'duracion': 139
    },
    {
        'titulo': 'La vida es bella',
        'año': 1997,
        'genero': 'Comedia',
        'duracion': 116
    },
    {
        'titulo': 'Volver al futuro',
        'año': 1985,
        'genero': 'Ciencia ficción',
        'duracion': 116
    },
    {
        'titulo': 'Inception',
        'año': 2010,
        'genero': 'Ciencia ficción',
        'duracion': 148
    },
    {
        'titulo': 'Los increíbles',
        'año': 2004,
        'genero': 'Animación',
        'duracion': 115
    }
]

"""
1 - Imprimir las peliculas entre los años 1990 hasta 2010
2 - Mostrar solo las de Ciencia ficción
3 - Mostrar la pelicula de menor duracion, la de mayor duracion y ya que estamos mostrar el promedio de duracion de todas las peliculas

"""

#Creamos la funcion que reemplaza lo que hasta ahora veniamos haciendo con el bucle While. Esta servira para pedirle input al usuario y luego derivarnos a la funcion correspondiente dependiendo de la seleccion que este haya hecho o terminar el programa.
def inputUsuario ():  
    decision = input("""
                    Bienvenido al filtrador de peliculas.
                    Presione 1 para mostrar en pantalla las peliculas estrenadas entre 1990 y 2010.
                    Presione 2 para mostrar todas las peliculas de Ciencia Ficcion en nuestro catalogo.
                    Presione 3 para mostrar la pelicula de menor duracion, la de mayor duracion y el promedio de duracion de todas nuestras peliculas disponibles.
                    Presione x para salir.
                    """)
    if decision == "1":
        peliculasFecha(1990,2010) #Llamamos a la funcion que busca peliculas segun su fecha de estreno.
        inputUsuario() #Llamamos nuevamente a la funcion inputUsuario para que se vuelva a ejecutar nuestro entorno de interaccion con el usuario hasta que este decida salir del programa.
    elif decision == '2':
        peliculasGenero('Ciencia ficción') #Repetimos el proceso de decision uno pero para las demas funciones
        inputUsuario()
    elif decision == '3':
        peliculasDuracion()
        inputUsuario()
    elif decision == 'x':
        print('Gracias por haber utilizado nuestro programa')
    else:
        print('Por favor, ingrese una opcion valida.')
        inputUsuario()

#Creamos la funcion que buscara peliculas estrenadas entre dos fechas. Para poder modificar las fechas, le asignamos a la funcion dos parametros que incluso, podriamos pedir
#al usuario que las ingrese antes de ejecutar la funcion. En este caso, llamaremos a la funcion cuando el usuario ingrese 1 como su decision en inputUsuario y buscara peliculas
#solo entre 1990 y 2010.
def peliculasFecha (primeraFecha,segundaFecha):
    print(f'Las peliculas estrenadas entre {primeraFecha} y {segundaFecha} son:')
    for pelicula in peliculas: #Creamos un bucle for que busque en cada elemento de "peliculas". En este caso, llamamos al diccionario "pelicula".
#Creamos un condicional que, por cada pelicula, se fije en su fecha de estreno. De ser mayor o igual al primer parametro ingresado Y menor o igual al segundo parametro ingresado,
#se imprimira en pantalla el titulo de la pelicula, su fecha de estreno, genero y duracion. Si no le damos formato, se imprimiran como diccionario y queda poco prolijo.
        if pelicula['año']  >= primeraFecha and pelicula['año'] <= segundaFecha:
            print(f'### Nombre: {pelicula["titulo"]}. Año de Estreno: {pelicula["año"]}. Genero: {pelicula["genero"]}. Duracion (min.):{pelicula["duracion"]}.')




#Creamos la funcion que buscara las peliculas por genero. Para hacer dinamica la seleccion del genero, lo ingresamos como parametro en la funcion. Si quisieramos, podriamos hacer
#que el usuario ingrese el genero que desea ver como un input y luego utilizar este input como parametro de la funcion. En este caso, solamente buscaremos las que son de Ciencia Ficcion.
def peliculasGenero (genero):
    print(f'Las peliculas que tenemos en nuestro catalogo del genero {genero} son:')
    for pelicula in peliculas: #Nuevamente creamos un bucle for que busque en cada elemento de "peliculas". Al igual que antes, llamamos al diccionario "pelicula".
#Creamos un condicional que, por cada pelicula, se fije si su genero es igual que el genero ingresado. De ser asi, se imprimiran sus datos en pantalla al igual que en la funcion
# peliculasFecha().
        if pelicula['genero'] == genero:
            print(f'### Nombre: {pelicula["titulo"]}. Año de Estreno: {pelicula["año"]}. Genero: {pelicula["genero"]}. Duracion (min.):{pelicula["duracion"]}.')


#Creamos la funcion que buscara la pelicula de mayor duracion, de menor duracion y el promedio de duracion de las mismas. Para ello, tendremos que crear dentro de la funcion
#una variable, en este caso "listaDuraciones" que tendra formato de lista. Alli agregaremos la duracion de cada pelicula mediante un bucle for. 
# Una vez hecho esto, buscamos el indice de la de mayor duracion y mostramos en pantalla los datos de la pelicula que comparta el indice en la lista "peliculas".
#Hacemos lo mismo para la de menor duracion. Por ultimo, obtenemos el promedio de duracion de todas las peliculas y lo mostramos en pantalla.
def peliculasDuracion ():
    listaDuraciones = []
    for pelicula in peliculas:
        listaDuraciones.append(pelicula['duracion'])
#Con la funcion max buscamos cual es la duracion mayor de la lista que acabamos de crear.
    mayorDuracion = max(listaDuraciones)
#Con la funcion index buscamos el indice de la mayor duracion en listaDuraciones
    indiceMayorDuracion = listaDuraciones.index(mayorDuracion)
#Utilizamos el mismo indice para mostrar la informacion correspondiente de la pelicula encontrada en "peliculas".
    print(f'La pelicula de mayor duracion es {peliculas[indiceMayorDuracion]["titulo"]}. Año de Estreno: {peliculas[indiceMayorDuracion]["año"]}. Genero: {peliculas[indiceMayorDuracion]["genero"]}. Duracion (min.):{peliculas[indiceMayorDuracion]["duracion"]}.')
#Hacemos el mismo proceso para la de menor duracion
    menorDuracion = min(listaDuraciones)
    indiceMenorDuracion = listaDuraciones.index(menorDuracion)
    print(f'La pelicula de menor duracion es {peliculas[indiceMenorDuracion]["titulo"]}. Año de Estreno: {peliculas[indiceMenorDuracion]["año"]}. Genero: {peliculas[indiceMenorDuracion]["genero"]}. Duracion (min.):{peliculas[indiceMenorDuracion]["duracion"]}.')
#Creamos una variable en la cual sumamos todas las duraciones de las peliculas utilizando un bucle for.
    totalDuraciones = 0
    for duracion in listaDuraciones:
        totalDuraciones = totalDuraciones + duracion
#Dividimos el total de las duraciones por la cantidad de peliculas y lo mostramos en pantalla.
    promedioDuraciones = totalDuraciones / len(listaDuraciones)
    print(f'La duracion promedio de las peliculas de nuestro catalogo es de {promedioDuraciones} minutos.')



inputUsuario() #Ejecutamos a la funcion por primera vez para dar inicio al programa.