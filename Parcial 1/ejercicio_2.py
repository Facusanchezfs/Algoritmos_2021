from cola import Cola
from pila import Pila

class Notificacion(object):
    def __init__(self, hora, app, mensaje):
        self.hora = hora
        self.app = app
        self.mensaje = mensaje

notificacion1 = Notificacion('19:45','Instagram','Hola')
notificacion2 = Notificacion('09:23','Twitter', 'Python te ha seguido')
notificacion3 = Notificacion('00:00','Twitter','Jose ha indicado que le gusta un tweet')
notificacion4 = Notificacion('12:15','Facebook','Manolo ha puesto "me gusta" a tu última foto')
notificacion5 = Notificacion('23:23','Instagram','Maria ha comenzado a seguirte')
pila1 = Pila()
cola1 = Cola()


cola1.arribo(notificacion1)
cola1.arribo(notificacion2)
cola1.arribo(notificacion3)
cola1.arribo(notificacion4)
cola1.arribo(notificacion5)

def facebook():         # Punto C
    for n in range(0,cola1.tamanio()):
        aux = cola1.atencion()
        if ('Facebook' != aux.app):
            cola1.arribo(aux)




def Mensaje():          # Punto D
    for n in range (0,cola1.tamanio()):
        aux = cola1.atencion()
        if (aux.app == 'Twitter'):
            buscado = 'Python'
            mensaje = aux.mensaje
            if (0 == mensaje.find(buscado)):
                print(mensaje)
        cola1.arribo(aux)


Mensaje()

def Instagram():        # Punto E
    for n in range (0,cola1.tamanio()):
        aux = cola1.atencion()
        if (aux.app == 'Instagram'):
            pila1.apilar(aux)
    while (not pila1.pila_vacia()):
        print(pila1.elemento_cima().mensaje,'a las', pila1.elemento_cima().hora)
        pila1.desapilar()

Instagram()