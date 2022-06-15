productos=[[1, "maiz grano", 285.55],[2, "pepino", 334.72], [3, "tomate verde", 129]] 
venta_productos = [
[2, 122], 
[1, 89], 
[1, 22], 
[3, 48], 
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]
cajas=int(input("Ingrese el numero de cajas: "))
id=int(input("Ingrese el id del producto: "))
if id> len(productos):
  print("Id incorrecto")
for producto in productos:
  if producto[0] == id:
    print(f"El producto es {producto[1]}")
    print(f"El precio por caja es de {producto[2]}")
    venta_productos.append([id, cajas])
    subtotal= producto[2]* cajas
    if cajas<= 100:
      subtotal+= 1500
    
    total_cajas= 0
    for venta in venta_productos:
        total_cajas+=venta[1]
    if total_cajas > 1500:
       subtotal*=0.8
    print(f"El total de cajas es:  {total_cajas}")
    print(f"Aplica descuento del 20%: {total_cajas>1500}")
    print(f"El costo total de su pedido es de: {subtotal}")

