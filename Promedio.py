# 1. Captura de tres calificaciones decimales
cal1 = float(input("Ingresa la primera calificación: "))
cal2 = float(input("Ingresa la segunda calificación: "))
cal3 = float(input("Ingresa la tercera calificación: "))

# 2. Cálculo del promedio
promedio = (cal1 + cal2 + cal3) / 3

# 3. Mostrar el promedio
print("\nEl promedio es:", promedio)

# 4. Mensaje según promedio
if promedio >= 70:
    print("¡Felicidades! Aprobaste")
else:
    print("Lo siento, necesitas estudiar más")
