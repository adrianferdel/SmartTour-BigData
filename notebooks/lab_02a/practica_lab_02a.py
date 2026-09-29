import os
import pandas as pd

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




