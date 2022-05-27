
peso_cemento= 40
peso_yeso= 30
capacidad= 3254
costales_cemento= int(input("Ingrese el numero de costales de cemento: "))
costales_yeso= int(input('Ingrese el numero de costales de yeso":'))
peso_total=0
peso_total+=(costales_cemento*peso_cemento+costales_yeso*peso_yeso)
print(f'El peso total es de : {peso_total}')
print(f'Se puede realizar el envio: {peso_total>capacidad*.50 and peso_total<=capacidad}')


       