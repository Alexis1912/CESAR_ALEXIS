from Pila.Pila import Pila
from ListaEnlazada.ListaSimple import ListaSimple

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Operaciones con Lista Simple")
    print("2. Operaciones con Pila")
    print("3. Salir")

def mostrar_menu_listas():
    print("\n--- Menú de Operaciones con Lista Simple ---")
    print("1. Insertar al inicio")
    print("2. Insertar al final")
    print("3. Eliminar dato")
    print("4. Mostrar lista")
    print("5. Volver al menú principal")

def operaciones_listas():
    lista = ListaSimple()
    while True:
        mostrar_menu_listas()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            data = input("Ingrese el elemento a insertar al inicio: ")
            lista.insertar_inicio(data)
            print(f"Elemento {data} insertado al inicio.")
        elif opcion == "2":
            data = input("Ingrese el elemento a insertar al final: ")
            lista.insertar_final(data)
            print(f"Elemento {data} insertado al final.")
        elif opcion == "3":
            try:
                print("\n--- ELIMINAR ELEMENTO ---")
                print(f"Lista actual: {lista}")
        
                valor = input("Ingrese el valor a eliminar: ")     
                elemento_eliminado = lista.eliminar(valor)       
                if elemento_eliminado is not None:
                    print(f"\n✓ Elemento '{elemento_eliminado}' eliminado con éxito.")
                    print(f"Lista actualizada:{lista}")
                else:
                    print("\n✗ El elemento no fue encontrado en la lista.")         
            except ValueError:
                print("\nError: El valor ingresado no es válido.")
        elif opcion == "4":
            lista.mostrar()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def mostrar_menu_pila():
    print("\n--- Menú de Operaciones con Pilas ---")
    print("1. Apilar elemento")
    print("2. Desapilar elemento")
    print("3. Ver cima")
    print("4. Mostrar pila")
    print("5. Volver al menú principal")

def operaciones_pila():
    pila = Pila()
    while True:
        mostrar_menu_pila()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            data = input("Ingrese el elemento a apilar: ")
            pila.apilar(data)
            print(f"Elemento {data} apilado.")
        elif opcion == "2":
            elemento = pila.desapilar()
            if elemento is not None:
                print(f"Elemento {elemento} desapilado.")
        elif opcion == "3":
            cima = pila.ver_cima()
            if cima is not None:
                print(f"Elemento en la cima: {cima}")
        elif opcion == "4":
            pila.mostrar_pila()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def main():
    while True:
        mostrar_menu_principal()
        opcion_principal = input("Seleccione una opción: ")

        if opcion_principal == "1":
            operaciones_listas()
        elif opcion_principal == "2":
            operaciones_pila()
        elif opcion_principal == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()