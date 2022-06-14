productos=[[1, "maiz grano", 285.55],[2, "pepino", 334.72], [3, "tomate verde", 129]] 
cajas=int(input("Ingrese el numero de cajas: "))
id=int(input("Ingrese el id del producto: "))
if id> len(productos):
  print("Id incorrecto")
for producto in productos:
  if producto[0] == id:
    print(f"El producto es {producto[1]}")
    print(f"El precio por caja es de {producto[2]}")
    subtotal= producto[2]* cajas
    if cajas<= 100:
      subtotal+= 1500
    print(f"El costo total de su pedido es de: {subtotal}")
  