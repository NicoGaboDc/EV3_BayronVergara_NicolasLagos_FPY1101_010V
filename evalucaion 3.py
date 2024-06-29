listado_patentes=[]
def patentes():
    sw =1
    while sw == 1:
        tipo=input("Ingrese tipo de vehiculo: ")
        patente=input("Ingrese patente del vehiculo en formato AAAA-11: ")
        while True :
            marca=str(input("Ingrese marca del vehiculo: "))
            if 2 > len(marca):
                print("El nombre de la marca es inferior a lo requerido, debe ser superior a 2 caracteres, vuelva a intentarlo .")
            elif 15 < len(marca):
                print("El nombre de la marca es superior a lo requerido, debe ser inferior a 15 caracteres, vuelva a intentarlo.")
            else:
                break
        while True:
            precio = int(input("Ingrese precio del vehiculo: "))
            if precio < 5000000:
                print("El precio del vehiculo es inferior a lo requqerido, debe ser superior a 5 millones.")
            else:
                break
        multa_monto=int(input("Ingrese el monto de la multa: "))
        multa_fecha=input("Ingrese la fecha de la multa en formato dd/mm/aaaa: ")
        fecha=input("Ingrese fecha del registro del vehiculo en formato dd/mm/aaaa: ")
        nombre=input("Ingrese el nombre del dueño del vehiculo: ")

        listado_patentes.append({"tipo":tipo,"patente":patente,"marca":marca,"precio":precio,
                                 "multa":multa_monto,"fecha multa": multa_fecha,"fecha de registro":fecha,"dueño":nombre})
        validacion=input("Desea grabar otro vehiculo ? [si/no]").lower()
        if validacion == "si":
            sw = 1
        elif validacion == "no":
            sw = 0
        else:
            print("La respuesta no es valida.")
patentes()
print(listado_patentes)