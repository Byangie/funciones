#Funciones_ejemplo14
#Confeccionar una función que reciba un string como párametro y en forma opcional un segundo string con un caracte. La función debe mostrar el string subrayado conn el caracter que indica el segundo parámetro

def titulo_subrayado(titulo,caracter="*"):
    print(titulo)
    print(caracter*len(titulo))

#Bloque principal

titulo_subrayado("Sistea de Administracion")
titulo_subrayado("ventas","-")
