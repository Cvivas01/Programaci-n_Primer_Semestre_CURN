mascotas = ["perro", "gato", "conejo"]
continuar = True

while continuar:
    print("\n--- Catalogo DE LA TIENDA ---")
    print("1 - Ver mascotas")
    print("2 - Agregar nueva mascota")
    print("3 - Buscar si una mascota está en la tienda")
    print("4 - Salir")

   
    Opcion_Selecionada = input("Seleccione una opción: ")

    if Opcion_Selecionada == "1":
        print("\nMascotas disponibles en la tienda:")
        for m in mascotas:
            print(m)
            
    elif Opcion_Selecionada == "2":
        nueva_mascota = input("Ingrese el nombre de la nueva mascota: ")
        mascotas.append(nueva_mascota)
        print(f"{nueva_mascota} ha sido agregada a la tienda.")
        print("\nMascotas actualizadas en la tienda:")
        for m in mascotas:
            print(m)
        
    elif Opcion_Selecionada == "3":
        mascota_a_buscar = input("Ingrese el nombre de la mascota que desea buscar: ")
        if mascota_a_buscar in mascotas:
            print(f"{mascota_a_buscar} está disponible en la tienda.")
        else:
            print(f"{mascota_a_buscar} no se encuentra en la tienda.")
            
    elif Opcion_Selecionada == "4":
        print("Gracias por visitar la tienda. ¡Hasta luego!")
    continuar = False