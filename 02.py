from typing import List
#2)	Desenvolva um programa em Python utilizando uma Pilha de acordo com a situação problema:
#Armazene as placas dos carros (apenas os números) que estão estacionados numa rua sem saída estreita.
#Dado uma placa verifique se o carro está estacionado na rua. Caso esteja, informe a sequência de carros que deverá
#ser retirada para que o carro em questão consiga sair.

def main():
    stack: List[int] = [1015, 1014, 1013, 1012, 1011]
    placa = 10
    print(conseguir_sair(stack, placa))

def conseguir_sair(stack, placa):
    carros_para_retirar = 0
    for element in stack[::-1]:
        if element != placa:
            carros_para_retirar += 1
        elif element == placa:
            return carros_para_retirar

    return 'Não existe nenhum carro com essa placa'

main()