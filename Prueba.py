import csv
import math
import random

salarios = {}

empleados = [
    "Juan Pérez” , ”María García” , ”Carlos López” , ”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"
    ] 

def asignar_paga():
    for empleado in empleados:
        salario = random.randint(300000, 2500000)
        salarios[empleado] = salario

def clasificacion_salarios():
    clasificados = {
        "Por_bajo_de_800k": [],
        "medio_800k_y_2millones": [],
        "sobre_2millones": [],
        }

    for empleado, salario in salarios.items():
        if salario < 800000:
            clasificados["Por_bajo_de_800k"].append((empleado, salario))
        elif 800000 <= salario <= 2000000:
            clasificados["medio_800k_y_2millones"].append((empleado, salario))
        else:
            clasificados["sobre_2millones"].append((empleado, salario))
    
    total_salarios = 0
    for rango, lista in clasificados.items():
        total_salarios += sum(salario for _, salario in lista)
        print("")
        if rango == 'Por_bajo_de_800k':
            print('Por Debajo de $800000 mil pesos: ')
            print("")
        else:
            if rango == 'medio_800k_y_2millones':
                print('En medio de $800000 mil y $2000000 millones: ')
                print("")
            else:
                print('Sobre los $2000000 millones de pesos: ')
                print("")
        print(f"Total de empleados en el rango: {len(lista)}")
        for empleado,  salario in lista:
            print(f"{empleado}, salario: ${salario}")
    print("")
    print(f"Total acumulando todos los salarios de empleados: ${total_salarios}")

def ver_estadisticasSueldos():
    salarios_valores = list(salarios.values())
    salario_mas_ALTO = max(salarios_valores)
    salario_mas_BAJO = min(salarios_valores)
    promedio = sum(salarios_valores) / len(salarios_valores)
    media_geometrica = math.exp(sum(math.log(salario)for salario in salarios_valores)/ len(salarios_valores))

    print(f"Salario Mas Alto: ${salario_mas_ALTO}")
    print("")
    print(f"Salario Mas Bajo: ${salario_mas_BAJO}")
    print("")
    print(f"Promedio de Salarios entre Empleados: ${promedio}")
    print("")
    print(f"Media Geometrica : ${media_geometrica}")

def informes_salarios():
    with open('informes_salarios.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre Empleado", "Salario Brut", "Descuento a la Salud", "Descuento AFP", "Salario Liquido"])

        for empleado, salario in salarios.items():
            descuento_salud = salario * 0.07
            descuento_afp = salario * 0.12
            salario_liquido = salario - descuento_salud - descuento_afp
            print(f"Nombre empleado: {empleado}")
            print(f"Salario Bruto : ${salario}")
            print(f"Descuento Salud: ${descuento_salud}")
            print(f"Descuento AFP: ${descuento_afp}")
            print(f"Salario Liquido: ${salario_liquido}")

            writer .writerow([empleado, salario, descuento_salud, descuento_afp, salario_liquido])

def menu_principal():
    while True:
        print("""
            Menu De Empleados
        1. Asignar Sueldos Aleatorios
        2. Clasificar Sueldos
        3. Ver Estadisticas
        4. Reporte de Sueldos
        5. Salir
     """)
        opcion = input("Seleccione una Opcion: ")
        print("")

        if opcion == '1':
            asignar_paga()
            print("Salarios Aleatoriamente Asignados")
        elif opcion == '2':
            clasificacion_salarios
        elif opcion == '3':
            ver_estadisticasSueldos()
        elif opcion == '4':
            informes_salarios()
        elif opcion == '5':
            print(""" Finalizando Programa... Desarrollado por Simon Castellano RUT 21.975.188-5""")
            break
        else:
            print("Error ingrese una opcion del 1 al 5")
if __name__ == "__main__":
    menu_principal()


        
