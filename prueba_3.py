import random
import time
import csv
listado_patentes = []
certificados = ['emision de contaminantes', 'anotaciones vigentes','multas']
def grabar():
    sw_grabar = 1
    while sw_grabar == 1:
        certificado_elegido= random.choice(certificados)
        nombre = input("Ingrese su nombre: ")
        tipo = input("Ingrese el tipo de vehiculo: ")
        while True:
            patente = input("Ingrese la patente en formato AAAA-11: ")
            if patente[0:4].isalpha() and patente[4:5]== '-' and patente[5:7].isdigit():
                print("Ingreso bien la patente")
                break
            else:
                print("Mal ingreso de la patente")
        marca = 'a'#
        precio = 123
        multa_monto=12312
        multa_fecha = 'asdadsf'
        fecha = '12397192jalsdkjf'
        listado_patentes.append({'nombre':nombre,'tipo':tipo,'patente':patente,'certificado':certificado_elegido,'marca':marca,'precio':precio,'multa_monto':multa_monto,'fecha_multa':multa_fecha,'fecha':fecha})
        #agregarle al append 'certificados_elegido'

        while True:
            seguir = input("¿Desea seguir ingresando conductores? [SI/NO]").lower()
            if seguir == 'si':
                print("Seguimos ingresando conductores")
                break
            elif seguir == 'no':
                sw_grabar = 0
                print("Volviendo al menú principal")
                time.sleep(1)
                break
            else:
                print("Ingrese una opcion válida")
    print(listado_patentes)



        


def buscar(listado_patentes):
    patente_buscado = input("Ingrese la patente que desea buscar: ")
    patente_filtrada = {i for i in listado_patentes if i['patente'] == patente_buscado}
    for i in patente_filtrada:
        print(f"Tipo: {i['tipo']}\nNombre: {i['nombre']}\nPatente: {i['patente']}\nMarca: {i['marca']}\nPrecio: {i['precio']}")
        print(f"Certificado: {i['certificado']}\nMulta:{i['multa_monto']}\nFecha multa{i['fecha_multa']}")
        print(f"Fecha de registro del vehículo: {i['fecha']}")



def imprimir_certificados(listado_patentes):
    for e in listado_patentes:
        for i in e:
            print(f"Tipo: {i['tipo']}\nNombre: {i['nombre']}\nPatente: {i['patente']}\nMarca: {i['marca']}\nPrecio: {i['precio']}")
            print(f"Certificado: {i['certificado']}\nMulta:{i['multa_monto']}\nFecha multa{i['multa_fecha']}")
            print(f"Fecha de registro del vehículo: {i['fecha']}")
    listado_patentes = list(listado_patentes)
    with open ('datos_vehiculos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows([listado_patentes])




def salir ():
    print('Ha salido del programa correctamente\nCreado por Nicolás Lagos y Bayron Vergara, Adiós!')
    return 1

def main():
    sw_main = 1
    while sw_main == 1:
        print("------------Menú--------------")
        print("1. Grabar trabajadores")
        print("2. Buscar trabajadores")
        print("3. Imprimir certificados")
        print("4. Salir del Programa")
        print('------------------------------')
    
        op = int(input('Ingrese la opción que desea: '))
        if op ==1:
            grabar() #cambiar los nombres de las funciones con el bayron
        elif op == 2:
            buscar(listado_patentes)
        elif op == 3:
            imprimir_certificados(listado_patentes)
        elif op == 4:
            sw_main = salir()
main()