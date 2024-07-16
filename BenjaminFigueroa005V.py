import random




trabajadores = [
    "juan perez",
    "maria garcia",
    "Carlos Lopez",
    "Ana Martinez",
    "Pedro Rodriguez",
    "Laura Hernandez",
    "Miguel Sanchez",
    "Isabel Gomez",
    "Francisco Diaz",
    "Elena Fernandez",
    ]



while True:
    print("1. Asignar sueldos aleatorio")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    opcion = input("que accion desea realizar: ")

    if opcion == "1":
        sueldos ={}
        for i in trabajadores:
            
            sueldos[i] = random.randint(300000,2500000)

            sueldos_menoresa8 =[ sueldos[i]< 800000 ]
            print(sueldos_menoresa8)



    elif opcion == "2":
    
        #print(f"Sueldos menores a $800.000 TOTAL: {}\n")
        
        #print("Nombre empleado\t\tSueldo")

        #print(f"Sueldos entre $800.000 y $2.000.000\nTOTAL: {}\n")

        #print(f"Sueldos superiores a $2.000.000\nTOTAL: {}\n")

        #print(f"TOTAL SUELDOS: $ {}")
        print(sueldos_menoresa8)
        print(sueldos)
        pass

    elif opcion == "3":
        pass

    elif opcion == "4":
        pass

    elif opcion == "5":
        print("Finalizando el programa...\nDesarrollado por Benjamin Figueroa\nRUT 20.238.268-1")
        break


