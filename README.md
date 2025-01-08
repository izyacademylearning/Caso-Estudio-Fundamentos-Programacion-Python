# Caso-Estudio-Fundamentos-Programacion-Python

# Gestor de Tareas

Este proyecto es un programa sencillo para gestionar tareas en una lista. Permite agregar, mostrar y eliminar tareas a través de un menú interactivo en la terminal.

## Características

1. **Agregar Tareas**: Los usuarios pueden agregar una tarea ingresando una descripción breve.
2. **Mostrar Tareas**: Se muestran todas las tareas registradas en la lista.
3. **Eliminar Tareas**: Los usuarios pueden eliminar tareas seleccionándolas por su número en la lista.
4. **Menú Interactivo**: Incluye un menú de opciones fácil de usar.

## Requisitos

- Python 3.6 o superior

## Uso

1. Clona este repositorio o copia el archivo a tu máquina local.
2. Ejecuta el programa en la terminal:

   ```bash
   python nombre_del_archivo.py
   ```

3. Usa el menú interactivo para gestionar tus tareas:
   - Opción 1: Agregar una nueva tarea.
   - Opción 2: Mostrar la lista actual de tareas.
   - Opción 3: Eliminar una tarea existente.
   - Opción 4: Salir del programa.

## Estructura del Código

### Funciones Principales

- `agregar_tarea(tareas)`: Solicita al usuario una descripción de la tarea y la agrega a la lista.
- `mostrar_tareas(tareas)`: Muestra todas las tareas almacenadas en la lista con su número correspondiente.
- `eliminar_tarea(tareas)`: Permite al usuario eliminar una tarea seleccionándola por su número.

### Programa Principal

El programa utiliza un bucle `while` para mostrar el menú y manejar las opciones seleccionadas por el usuario hasta que decida salir.

## Ejemplo de Ejecución

```text
Gestor de Tareas
1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Salir
Seleccione una opción (1-4): 1
Ingrese la descripción de la nueva tarea: Comprar leche
Tarea 'Comprar leche' agregada con éxito.

Gestor de Tareas
1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Salir
Seleccione una opción (1-4): 2

Lista de tareas:
1. Comprar leche

Gestor de Tareas
1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Salir
Seleccione una opción (1-4): 3

Ingrese el número de la tarea que desea eliminar: 1
Tarea 'Comprar leche' eliminada con éxito.

Gestor de Tareas
1. Agregar tarea
2. Mostrar tareas
3. Eliminar tarea
4. Salir
Seleccione una opción (1-4): 4
¡Hasta luego!
```

## Mejoras Futuras

- Guardar las tareas en un archivo para que persistan después de cerrar el programa.
- Añadir la opción de editar tareas existentes.
- Implementar una interfaz gráfica para mayor facilidad de uso.

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras, por favor crea un issue o un pull request.

## Licencia

Este proyecto fue desarrollado como parte de un curso en IzyAcademy.

Este proyecto está bajo la Licencia MIT.
