import os
import pandas as pd

# Parte 1 del laboratorio

equipo_a = set()
equipo_b = set()

for archivo in sorted(os.listdir('../../datasets/data')):
    ruta = os.path.join('../../datasets/data', archivo)
    df = pd.read_csv(ruta)
    if(archivo.startswith("a")): equipo_a.update(df["jugador"].dropna().astype(str))
    else: equipo_b.update(df["jugador"].dropna().astype(str))

jugadoresExclusiveA = len(equipo_a-equipo_b)
jugadoresExclusiveB = len(equipo_b-equipo_a)

print(f"El equipo A ha tenido a: {jugadoresExclusiveA} jugadores únicos, y el B ha tenido a: {jugadoresExclusiveB} jugadores únicos")

print(f"El equipo A ordenado alfabéticamente: ")
for j in equipo_a:
    print(f"{j}")

print(f"El equipo B ordenado alfabéticamente: ")
for j in equipo_b:
    print(f"{j}")

#Parte 2 del laboratorio

#union de equipos

unionEquiposAB = len(equipo_a.union(equipo_b))

print(f"El número de jugadores distintos que hayan jugado en alguno de los 2 equipos es: {unionEquiposAB}")

#interseccion de equipos

interseccionEquiposAB = equipo_a.intersection(equipo_b)

for j in interseccionEquiposAB:
    print(j)

print(f"El número de jugadores que han pertenecido a ambos clubes es: {len(interseccionEquiposAB)}")

#diferencia entre clubes

diferenciaEquipoAvsB = equipo_a.difference(equipo_b)

print(f"El número de jugadores que han jugado únicamente en el equipo A: ")
for j in diferenciaEquipoAvsB:
    print(j)

#diferencia simétrica

diferenciaSimetricaEquipoAB = equipo_a.symmetric_difference(equipo_b)

print(f"El número de jugadores que han jugado únicamente en alguno de los 2 equipos son: ")
for j in diferenciaSimetricaEquipoAB:
    print(j)

#jugadores leales

universoContemplado = equipo_a.union(equipo_b)

jugadoresLeales = universoContemplado.difference(equipo_a.intersection(equipo_b))

print(f"Los jugadores que no han pasado por ambos clubes son: ")

for j in jugadoresLeales:
    print(j)

#Parte 3
totalUniverso = len(universoContemplado)
jugadoresAmbosEquipos = len(equipo_a.intersection(equipo_b))

porcentajeJugadores = (jugadoresAmbosEquipos/totalUniverso)*100

print(f"El % de jugadores que han compartido club es: {porcentajeJugadores}%")

clubMayorLealtad = len(diferenciaEquipoAvsB)-len(equipo_b.difference(equipo_a))

ganador = "Equipo A" if equipo_a>equipo_b else "Equipo B"

print(fr"El equipo que más lealtad ha obtenido es: {ganador}")





