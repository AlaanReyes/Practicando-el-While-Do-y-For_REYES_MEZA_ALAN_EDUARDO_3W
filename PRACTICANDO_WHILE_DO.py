print("Welcome to PRACTICANDO WHILE DO!")  # BIENVENIDA AL PROGRAMADOR 
print(" ")  # ESPACIO

print("REYES MEZA ALAN EDUARDO :   3W")  # INFO DE PRACTICA Y PROGRAMADOR 
print(" ")  # ESPACIO
i = 1
while i < 6:
  print(i)
  i += 1

#Salir cuado i es igual a 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


#Continua una vez que i es igual a 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


#Mensaje desplegado cuando sea falso
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

  print(" ")

# Mostrar números del 1 al 5
print("Contando del 1 al 5:")
i = 1
while i < 6:
    print(i)
    i += 1

    print(" ")

# Sumar números hasta que la suma exceda 10
print("Sumando números hasta que la suma exceda 10:")
suma = 0
i = 1
while suma <= 10:
    suma += i
    print(f"Suma: {suma} (agregando {i})")
    i += 1

    print(" ")
# Contar hacia atrás
print("Contando hacia atrás desde 5:")
i = 5
while i > 0:
    print(i)
    i -= 1

    print(" ")

# Mensaje final
print("¡Gracias por practicar con bucles!")

print(" ")




#Ejemplos con For:

#Muestra cada fruta de la lista.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  print(" ")

#a traves de las letras de la palabra "banana":
for x in "banana":
  print(x)
  print(" ")

#salir cuando x es banana

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

  print(" ")

# cascara

equipo1 = "PADRES"
equipo2 = "DODGERS"
carreras_equipo1 = 0
carreras_equipo2 = 0

# Mostrar la bienvenida a los participantes al juego 
print(f"¡final de MLB ENTRE {equipo1} y {equipo2}!")

# Simular el juego
turno = 1
while turno <= 1:  # Final a un juego
    print(f"\nEntrada {turno}:")
    
    # Turno del equipo 1
    print(f"Turno de {equipo1}:")
    carreras_anotadas = int(input("¿Cuantas carreras anotó el equipo 1 en esta entrada? "))
    carreras_equipo1 += carreras_anotadas
    print(f"Total de carreras de {equipo1}: {carreras_equipo1}")

    print(" ")

    # Turno del equipo 2
    print(f"Turno de {equipo2}:")
    carreras_anotadas = int(input("¿Cuantas carreras anoto el equipo 2 en esta entrada? "))
    carreras_equipo2 += carreras_anotadas
    print(f"Total de carreras de {equipo2}: {carreras_equipo2}")
    
    print(" ")
    turno += 1  # subir un el turno

# Mostrar resultado final
print("\nResultado Final:")
print(f"{equipo1} anoto: {carreras_equipo1} carreras.")
print(f"{equipo2} anoto: {carreras_equipo2} carreras.")

print(" ")

# saber el ganador
if carreras_equipo1 > carreras_equipo2:
    print(f"¡{equipo1} gano el juego!")
elif carreras_equipo2 > carreras_equipo1:
    print(f"¡{equipo2} gano el juego!")
else:
    print("¡Esto queda empatado!")

print(" ")

# Mensaje cuando termine el juego
print("¡gracias por jugar, espero se hayan divertido!")










