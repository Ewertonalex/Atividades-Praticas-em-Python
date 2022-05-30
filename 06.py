
lista = [1, 2, 3, 4, 5, 6]
print("A lista inicial é: ", lista)

#Verificando se o 4 existe na lista:
numero = int(input("Entre com o numero para saber se está na lista: "))

if numero in lista:
    print("O número {} está na lista!".format(numero))
else:
    print("O número {} não está na lista!".format(numero))

# Adiciona item na lista.
add = int(input("Entre com o numero para adicionar a lista: "))
lista.append(add)
print("Adicionando o número {} a lista: ".format(add), lista)


# Removendo item da Lista.
rmv = int(input("Entre com o numero para remover da lista: "))
lista.remove(rmv)
print("Removendo o número {} da lista: ".format(add), lista)

