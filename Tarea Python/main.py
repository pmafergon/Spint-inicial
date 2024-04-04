# ****entrada del ticket de compra****
import datetime as dt

def entradaticket(totalproductos):
    print(header)
    producto = input("Ingrese el producto: ")
    print("")
    uds = int(input("Ingrese el número de unidades: "))
    print("")
    if uds < 0:
        for i in totalproductos:
            if i == producto:
                print("")
                print(f"Se va a proceder a la devolución de {uds*(-1)} uds de {producto}")
                print("")
                precio = float(input("Ingrese el precio unitario del poducto: "))
                print("")
                a = [f"{uds} uds - {producto} - {precio} €"]
                ticket=[a]
                precio = precio * uds
                total=[precio]
                return ticket, total, producto
        else:
            print("Este producto no se puede devolver porque no se encuentra en el ticket del cliente, vuelva a ingresar el producto comprado")
            print("")
            return [],[],[]
    else:
        precio = float(input("Ingrese el precio unitario del producto: "))
        print("")
        a = [f"{uds} uds - {producto} - {precio} €"]
        ticket=[a]
        precio = precio * uds
        total=[precio]
        
        return ticket, total, producto
header="---------------------------"
ticketcliente = []
totalcliente = []
totalproductos=[]

print(header)
print(" Bienvenido al programa  ")
print(header)
print("¿Qué función desea realizar?")
print(header)
print("Selecciona 1 para ver el ticket del problema")
print("Selecciona 2 para utilizar la caja registradora")
print("Selecciona otra tecla para salir")
print(header)
print("")
seleccion = input("Escriba aquí: ")
print("")


if seleccion == "2":
    
    ti, to, pro = entradaticket(totalproductos)
    ticketcliente.append(ti)
    totalcliente += to
    totalproductos.append(pro)
    control = True


    while control:
        seguir = input("¿Desea añadir otro producto? S/N: ")
        print("")
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
            print("")
    print(header)
    print("El ticket es el siguiente: ")
    for i in range(len(ticketcliente)):
        if ticketcliente[i]  != []:
            print(ticketcliente[i], end="\n")
    
    print("")
    print(f"El precio total del ticket es {sum(totalcliente)*1.16}€")
    print("")
    fecha=dt.datetime.today()
    print(f"Fecha de compra: {fecha.strftime('%d-%m-%Y, %H:%M')}")
    print(header)

elif seleccion == "1":
    ticket = ["1-filete de ternera-30.23", "4-coca cola-4.20","-2-coca cola-1.40","1-pan-0.90"]
    print(ticket, sep = "\n")
    
    totalcliente=[]
    
    for i in ticket:
        
        a=i.split("-")
        
        if a[0] != "":
            b = float(a[0]) * float(a[2])
        else:
            b= float(a[1]) * float(a[3]) * -1
            print(b)
        
        totalcliente.append(b)
        
    print(f"El precio total del ticket es {sum(totalcliente)*1.16}€")
    fecha=dt.datetime.today()
    print(f"Fecha de compra: {fecha.strftime('%d-%m-%Y, %H:%M')}")

else:
    
    print(header)
    print("El programa ha finalizado")
    print(header)
    
    