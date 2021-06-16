from lista import Lista

personajes = ['Thor','Iron Man','Hulk','Captain America','Black Widow','Scalet Witch']
personajes_auxiliar = ['Black Widow', 'Hulk','Rocket Racoonn','Loki']

lista1 = Lista()

for personaje in personajes:
    lista1.insertar(personaje)

for personaje in personajes_auxiliar:
    if (lista1.busqueda(personaje) == -1):
        lista1.insertar(personaje)

posicion_thor = lista1.busqueda('Thor')
if (posicion_thor != -1):
    print('Thor se encuentra en la posicion numero', posicion_thor, 'de la lista')

posicion = lista1.busqueda('Scalet Witch')
lista1.modificar_elemento(posicion,'Scarlet Witch')

lista1.barrido()        # Punto D

lista1.barrido_inverso()    # Punto D

lista1.obtener_elemento(7)    # Punto E
lista1.barrido_iniciales()      # Punto F


personajes_completos = [
    {'name': 'Thor','año':1983,'heroe':True},
    {'name':'Iron Man','año':1970,'heroe':True},
    {'name':'Hulk','año':1967,'heroe':True},
    {'name':'Captain America','año':1956,'heroe':True},
    {'name':'Black Widow','año':1988,'heroe':True},
    {'name':'Scarlet Witch','año':1975,'heroe':True},
    {'name':'Rocket Racoon','año':1992,'heroe':True},
    {'name':'Loki','año':1983,'heroe':False}
]

lista2 = Lista()

# Punto G
def Ordenar_nombre():
    for personaje in personajes_completos:
        lista2.insertar(personaje,'name')



def Ordenar_año():
    for personaje in personajes_completos:
        lista2.insertar(personaje,'año')

Ordenar_nombre()
Ordenar_año()
lista2.barrido()