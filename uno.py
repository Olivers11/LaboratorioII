contador = 0
for i in range(10, 0, -1):
    indent = " "
    if contador != 0: 
        indent = indent * contador 
        string = " " * (i*2)
        print(indent+"*" + string +"*")
    contador += 1


final = " " * contador
print(final + "*")

