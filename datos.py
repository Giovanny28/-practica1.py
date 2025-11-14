# Captura de datos
nombre = input("Ingresa tu nombre completo: ")
edad = int(input("Ingresa tu edad (entero): "))
estatura = float(input("Ingresa tu estatura (decimal): "))
gusta_programar = input("¿Te gusta programar? (True/False): ")

# Conversión a tipo booleano
if gusta_programar == "True":
    gusta_programar = True
else:
    gusta_programar = False

# Mostrar datos capturados
print("\n--- Datos capturados ---")
print("Nombre completo:", nombre)
print("Edad:", edad)
print("Estatura:", estatura)
print("¿Le gusta programar?:", gusta_programar)

# Mostrar tipos de datos
print("\n--- Tipos de datos ---")
print("Tipo de 'nombre':", type(nombre))
print("Tipo de 'edad':", type(edad))
print("Tipo de 'estatura':", type(estatura))
print("Tipo de 'gusta_programar':", type(gusta_programar))
