personajes = ['Darth Vader','Han Solo','Obi Wan','Darth Maul','Yoda','Chewbacca','Luke']


def Barrido(pos = 0):

    if (pos >= len(personajes)):
        return
    else:
        print(personajes[pos])
        Barrido(pos + 1)

Barrido()

def Buscar_Yoda(pos = 0):
    if(personajes[pos] == 'Yoda'):
        print ('Yoda está en el vector, en la posicion', pos)
    else:  
        Buscar_Yoda(pos + 1)

Buscar_Yoda()