x = input("<escribe tu edad: ")

if int(x) > 26:
    print("Por mayor")
elif int(x) == 26:
    print("En el limite")
else:
    print("Por menor")

y = input("Escribe un Color:")

if y == 'red' or y == 'blue' or y == 'yellow':
    print("Colores primarios")
else:
    print("Colores Secundarios")

