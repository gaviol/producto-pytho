import os

# Nombre del archivo de productos
ARCHIVO_PRODUCTOS = 'productos.txt'

# Lista global para almacenar productos
productos = []

# Función para cargar los datos desde el archivo
def cargar_datos():
    try:
        if os.path.exists(ARCHIVO_PRODUCTOS):
            with open(ARCHIVO_PRODUCTOS, 'r') as file:
                for linea in file:
                    nombre, precio, cantidad = linea.strip().split(',')
                    productos.append({
                        'nombre': nombre,
                        'precio': float(precio),
                        'cantidad': int(cantidad)
                    })
        else:
            print("El archivo productos.txt no existe. Se creará al guardar los datos.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

# Función para guardar los datos en el archivo
def guardar_datos():
    if productos:  # Solo guarda si hay productos en la lista
        try:
            with open(ARCHIVO_PRODUCTOS, 'w') as file:
                for producto in productos:
                    file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
            print("Datos guardados correctamente.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")
    else:
        print("No hay productos para guardar.")

# Función para añadir un producto
def añadir_producto():
    # Validar que el nombre no tenga números
    while True:
        nombre = input("Introduce el nombre del producto: ")
        if not nombre.isalpha():
            print("El nombre del producto no puede contener números ni caracteres especiales. Inténtalo de nuevo.")
        else:
            break
    
    # Validar que el precio sea un número
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            if precio < 0:
                print("El precio no puede ser negativo. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. El precio debe ser un número.")

    # Validar que la cantidad sea un número entero
    while True:
        try:
            cantidad = int(input("Introduce la cantidad del producto: "))
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Inténtalo de nuevo.")
            else:
                break
        except ValueError:
            print("Entrada no válida. La cantidad debe ser un número entero.")
    
    # Añadir el producto a la lista
    productos.append({'nombre': nombre, 'precio': precio, 'cantidad': cantidad})
    print(f"Producto '{nombre}' añadido con éxito.")

# Función para ver todos los productos
def ver_productos():
    if productos:  # Verifica si hay productos en la lista
        print("Lista de productos:")
        for producto in productos:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("No hay productos en el inventario.")  # Mensaje si no hay productos

# Función para actualizar un producto
def actualizar_producto():
    if not productos:
        print("No hay productos para actualizar.\n")
        return

    nombre = input("Introduce el nombre del producto que deseas actualizar (puedes usar una parte del nombre): ")
    encontrado = False

    for producto in productos:
        if nombre.lower() in producto['nombre'].lower():  # Busca coincidencias sin importar mayúsculas/minúsculas
            encontrado = True
            print(f"Producto encontrado: '{producto['nombre']}'")
            nuevo_nombre = input(f"Introduce el nuevo nombre para '{producto['nombre']}' (o deja en blanco para no cambiar): ").strip()
            nuevo_precio = input(f"Introduce el nuevo precio para '{producto['nombre']}' (o deja en blanco para no cambiar): ").strip()
            nueva_cantidad = input(f"Introduce la nueva cantidad para '{producto['nombre']}' (o deja en blanco para no cambiar): ").strip()

            # Solo actualiza si se introduce un nuevo valor válido
            if nuevo_nombre:  # Se cambia solo si hay un nuevo nombre
                producto['nombre'] = nuevo_nombre

            if nuevo_precio:  # Solo actualiza si se introduce un nuevo precio
                try:
                    nuevo_precio_float = float(nuevo_precio)
                    if nuevo_precio_float >= 0:  # Evitar precios negativos
                        producto['precio'] = nuevo_precio_float
                    else:
                        print("El precio no puede ser negativo. No se ha cambiado el precio del producto.")
                except ValueError:
                    print("Precio no válido. No se ha cambiado el precio del producto.")

            if nueva_cantidad:  # Solo actualiza si se introduce una nueva cantidad
                try:
                    nueva_cantidad_int = int(nueva_cantidad)
                    if nueva_cantidad_int >= 0:  # Evitar cantidades negativas
                        producto['cantidad'] = nueva_cantidad_int
                    else:
                        print("La cantidad no puede ser negativa. No se ha cambiado la cantidad del producto.")
                except ValueError:
                    print("Cantidad no válida. No se ha cambiado la cantidad del producto.")

            print(f"Producto '{producto['nombre']}' actualizado.")
            return

    if not encontrado:
        print(f"No se encontró ningún producto que coincida con '{nombre}'.")

# Función para eliminar un producto
def eliminar_producto():
    if not productos:  # Verifica si la lista está vacía
        print("No hay productos en el inventario para eliminar.")
        return

    nombre_producto = input("Introduce el nombre del producto que deseas eliminar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre_producto.lower():
            productos.remove(producto)
            print(f"Producto '{nombre_producto}' eliminado con éxito.")
            return
    
    print(f"No se encontró el producto '{nombre_producto}'.")

# Función principal del menú
def menu():
    cargar_datos()
    while True:
        print("\n--- Menú de Gestión de Productos ---")
        print("1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
