"""Inicio de proyecto 1 en codigo python"""
print("Bienvenidos al mundo de la programacion")

usuario1 = "jhonnatan"
clave1 = 10

usuario = input("Digite el usuario de ingreso: ")
clave = int(input("Digite la clave de ingreso: "))

if usuario == usuario1 and clave == clave1:
    print("Acceso concedido")
else:
    print("Acceso Denegado")