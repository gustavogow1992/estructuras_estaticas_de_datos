"""Escribe un programa en Python que pida al usuario su nombre y su año de nacimiento"""

año_actual = 2026

nombre = input("Introduce tu nombre: ")
año_nacimiento = int(input("Introduce tu año de nacimiento: "))

edad = año_actual - año_nacimiento

print(f"Hola, mi nombre es {nombre}. Nací en el año {año_nacimiento}.")
print(f"Actualmente tengo {edad} años y estoy aprendiendo a programar.")
