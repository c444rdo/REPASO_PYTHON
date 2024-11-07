# Este programa evalúa la nota almacenada en la variable 'nota' y determina su equivalente en base a los rangos establecidos.
# Imprime la calificación correspondiente a la nota.

nota = 7  # Cambiar el valor para probar con otras notas
if 0 <= nota < 5:
    print("SUSPENSO")
elif 5 <= nota < 6:
    print("SUFICIENTE")
elif 6 <= nota < 7:
    print("BIEN")
elif 7 <= nota < 9:
    print("NOTABLE")
elif 9 <= nota <= 10:
    print("SOBRESALIENTE")
else:
    print("NOTA NO VÁLIDA")

# datos propios:
print("Martínez Estrada Ricardo / NO. de control: 1193 / 07.11.2024 / Repaso Python")
print(" ")