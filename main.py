# Curso: Fundamentos de Tecnología Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Karina Picado Barrantes 

def calcular_promedio(notas):
    return sum(notas) / len(notas)


def main():
    nombre = input("¿Como te llamas? ")
    cantidad = int(input("¿Cuantas notas vas a ingresar?"))


    notas = []
    for i in range(1, cantidad + 1):
        nota = float(input(f"Nota {i}: "))
        notas.append(nota)

    promedio = calcular_promedio(notas)
    print(f"\n{nombre}, tu promedio es: {promedio:.2f}")

    if promedio >= 70:
        print("¡Aprobaste!")
    else:
        print(" Reprobaste. Debes de esforzarte más.")

main()
    


