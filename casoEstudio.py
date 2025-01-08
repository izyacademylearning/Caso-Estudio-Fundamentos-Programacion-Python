# Definición de funciones
def agregar_tarea(tareas):
    """Agrega una nueva tarea a la lista de tareas."""
    tarea = input("Ingrese la descripción de la nueva tarea: ").strip()
    if tarea:
        tareas.append(tarea)
        print(f"Tarea '{tarea}' agregada con éxito.")
    else:
        print("La tarea no puede estar vacía.")

def mostrar_tareas(tareas):
    """Muestra todas las tareas de la lista."""
    if tareas:
        print("\nLista de tareas:")
        for i, tarea in enumerate(tareas, 1):
            print(f"{i}. {tarea}")
    else:
        print("No hay tareas en la lista.")

def eliminar_tarea(tareas):
    """Elimina una tarea de la lista por su número."""
    mostrar_tareas(tareas)
    if not tareas:
        return
    try:
        num_tarea = int(input("\nIngrese el número de la tarea que desea eliminar: "))
        if 1 <= num_tarea <= len(tareas):
            tarea_eliminada = tareas.pop(num_tarea - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada con éxito.")
        else:
            print("Número inválido. Por favor, ingrese un número válido.")
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

# Programa principal
tareas = []

while True:
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ").strip()
    if opcion == "1":
        agregar_tarea(tareas)
    elif opcion == "2":
        mostrar_tareas(tareas)
    elif opcion == "3":
        eliminar_tarea(tareas)
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")
