from temporizador import Temporizador
from time import sleep


def formato(valores):
    return '{:02d} : {:02d} : {:02d}'.format(valores[0], valores[1], valores[2])


t = Temporizador()
time = [0,0,5]          #<--- Ingresar el valor del temporizador
t.iniciar(time)
tf = formato(time) 


while True:             #Retroceder
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.5)
    if tiempo == "00 : 00 : 00":
        break
    t.retroceder()

while True:             #Avanzar
    t.avanzar()
    tiempo = t.mostrar_tiempo()
    print tiempo
    sleep(0.5)
    if tiempo == tf:
        break

