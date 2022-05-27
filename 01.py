from typing import List
#1)	Construa uma Pilha utilizando a linguagem Python.
# Dada uma sequência contendo N (N >0) números inteiros, imprimi-la na ordem inversa

def main():
    stack: List[int] = [1,2,3,4,5]
    imprimir_numeros_reais(stack)

def imprimir_numeros_reais(stack):
    for element in stack[::-1]:
        if element > 0:
            print(element)

main()