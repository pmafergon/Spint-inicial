# ****entrada del ticket de compra****


def entradaticket():
    ticket = []
    total = []

    producto = input("Ingrese el producto: ")
    uds = int(input("Ingrese el número de unidades: "))
    precio = float(input("Ingrese el precio unitario del poducto: "))
    a = [f"{uds} - {producto} - {precio}"]
    ticket.append(a)
    precio = precio * uds
    total.append(precio)
    return ticket, total


ticketcliente = []
totalcliente = []
b, tot = entradaticket()
ticketcliente.append(b)
totalcliente += tot

control = True

while control:
    seguir = input("¿Desea añadir otro producto? S/N: ")
    if seguir.lower() == "s":
        b, tot = entradaticket()
        ticketcliente.append(b)
        totalcliente += tot
    elif seguir.lower() == "n":
        control = False
    else:
        print(
            'Algo falló, por favor, ingrese "S" si desea añadir otro producto, "N" para finalizar el programa'
        )

for i in range(len(ticketcliente)):
    print(ticketcliente[i], end="\n")
print(f"El precio total del ticket es {sum(totalcliente)}€")
