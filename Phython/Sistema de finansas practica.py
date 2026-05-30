Ventas = []


print("\n sistemas de finasas ")
print("1. Agregar venta")
print("2. Mostrar ventas")
print("3. reporte de ventas")
print("4. Salir")

Repeticion = True
while Repeticion:

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese cuanto llevara de ese producto: "))
        precio = float(input("Ingrese el precio del producto: "))
        total =  cantidad * precio
        Ventas.append({"producto": producto, "cantidad": cantidad, "precio": precio, "total": total})

    elif opcion == "2":
        for venta in Ventas:
            print(f"Producto: {venta['producto']}, Cantidad: {venta['cantidad']}, Precio: {venta['precio']}, Total: {venta['total']}")

    elif opcion == "3":
       
        total_ventas = 0.0
        
        for venta in Ventas:
            total_ventas = total_ventas + venta["total"]
            
        print(f"Total de ventas: {total_ventas}")
    
    elif opcion == "4":
        print("Saliendo del sistema de finanzas")
        
        Repeticion = False


     
      
                   


 


