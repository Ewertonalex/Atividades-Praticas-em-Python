#Construa uma Fila de Prioridade utilizando a linguagem Python em que
# sejam implementadas as funções para inserção de um novo elemento (inteiro)
# na fila e a remoção do elemento de mais alta prioridade
class FilaPrioridade(object):
    # construtor da classe
    def __init__(self):
        self.queue = []

    # verifica se a fila está vazia
    def vazia(self):
        return len(self.queue) == 0

    # método usado para enfileirar um novo elemento
    def enfileirar(self, elemento):
        self.queue.append(elemento)

    # desenfileira um elemento baseado em sua prioridade
    def desenfileirar(self):
        try:
            max_valor = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[max_valor]:
                    max_valor = i

            elemento = self.queue[max_valor]
            del self.queue[max_valor]
            return elemento
        except IndexError:
            print("Erro")


def main():
    # cria uma nova fila de prioridade
    fila = FilaPrioridade()

    # vamos inserir quatro elementos
    fila.enfileirar(17)
    fila.enfileirar(13)
    fila.enfileirar(1)
    fila.enfileirar(7)

    # vamos desenfileirar de acordo com as prioridades
    while not fila.vazia():
        print("Elemento desenfileirado: ", fila.desenfileirar())


if __name__ == "__main__":
    main()