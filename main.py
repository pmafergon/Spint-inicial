# ****entrada del ticket de compra****
import datetime as dt

def entradaticket(totalproductos):
    producto = input("Ingrese el producto: ")
    uds = int(input("Ingrese el número de unidades: "))
    if uds < 0:
        for i in totalproductos:
            if i == producto:
                print(f"Se va a proceder a la devolución de {uds*(-1)} uds de {producto}")
                precio = float(input("Ingrese el precio unitario del poducto: "))
                a = [f"{uds} uds - {producto} - {precio} €"]
                ticket=[a]
                precio = precio * uds
                total=[precio]
                return ticket, total, producto
        else:
            print("Este producto no se puede devolver porque no se encuentra en el ticket del cliente, vuelva a ingresar el producto comprado")
            return [],[],[]
    else:
        precio = float(input("Ingrese el precio unitario del producto: "))
        a = [f"{uds} uds - {producto} - {precio} €"]
        ticket=[a]
        precio = precio * uds
        total=[precio]
        
        return ticket, total, producto

ticketcliente = []
totalcliente = []
totalproductos=[]
ti, to, pro = entradaticket(totalproductos)
ticketcliente.append(ti)
totalcliente += to
totalproductos.append(pro)

control = True

while control:
    seguir = input("¿Desea añadir otro producto? S/N: ")
    if seguir.lower() == "s":
        ti, to, pro = entradaticket(totalproductos)
        ticketcliente.append(ti)
        totalcliente += to
        totalproductos.append(pro)
    elif seguir.lower() == "n":
        control = False
    else:
        print(
            'Algo falló, por favor, ingrese "S" si desea añadir otro producto, "N" para finalizar el programa'
            )

for i in range(len(ticketcliente)):
    if ticketcliente[i]  != []:
        print(ticketcliente[i], end="\n")
print(f"El precio total del ticket es {sum(totalcliente)}€")
fecha=dt.datetime.today()
print(f"Fecha de compra: {fecha.strftime('%d-%m-%Y, %H:%M')}")
