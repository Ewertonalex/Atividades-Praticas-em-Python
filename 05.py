#Escreva um programa em Python que simule o controle de uma pista de decolagem de aviões em um aeroporto. Neste programa, o usuário deve ser capaz de realizar as seguintes tarefas:
#Listar o número de aviões aguardando na fila de decolagem;
#Autorizar a decolagem do primeiro avião da fila;
#Adicionar um avião à fila de espera;
#Listar todos os aviões na fila de espera;
#Listar as características do primeiro avião da fila.
# classe que representa um avião
class Aviao:
    # construtor da classe
    def __init__(self, num_voo, companhia, destino):
        self.num_voo = num_voo
        self.companhia = companhia
        self.destino = destino


# classe que representa a fila
class Fila:
    # construtor da classe
    def __init__(self):
        self.elementos = []

    # verifica se está vazia
    def vazia(self):
        return self.elementos == []

    # enfileira um novo elemento
    def enfileirar(self, elemento):
        self.elementos.insert(0, elemento)

    # desenfileira e retorna um elemento
    def desenfileira(self):
        return self.elementos.pop()

    # tamanho da fila
    def tamanho(self):
        return len(self.elementos)

    # lista os elementos da fila
    def listar_elementos(self):
        for i in range(self.tamanho() - 1, -1, -1):
            print("Número do Voo: {0}".format(self.elementos[i].num_voo))
            print("Companhia: {0}".format(self.elementos[i].companhia))
            print("Destino: {0}".format(self.elementos[i].destino))
            print("----------------------------------")

    # observa o primeiro da fila
    def retornar_frente(self):
        if self.vazia():
            return None
        else:
            return self.elementos[self.tamanho() - 1]


def main():
    # cria uma nova fila
    fila = Fila()

    # vamos criar o menu de opções
    while (True):
        print("\n---------- CONTROLE DE DECOLAGENS ----------\n")
        print("1. Listar o número de aviões aguardando na fila de decolagem")
        print("2. Autorizar a decolagem do primeiro avião da fila")
        print("3. Adicionar um avião à fila de espera")
        print("4. Listar todos os aviões na fila de espera")
        print("5. Listar as características do primeiro avião da fila")
        print("6. Sair")
        # vamos ler a opção informada pelo usuário
        opcao = int(input("Sua opção: "))

        if (opcao == 1):  # Lista o número de aviões aguardando na fila
            print("\nNeste momento há {0} aviões na fila de espera.".format(fila.tamanho()))

        elif (opcao == 2):  # autoriza a decolagem do primeiro avião na fila
            if not fila.vazia():
                aviao = fila.desenfileira()
                print("\nDecolagem autorizada do voo n. {0}".format(aviao.num_voo))
            else:
                print("\nFila de decolagem está vazia.")

        elif (opcao == 3):  # adiciona um avião à fila de espera
            # vamos ler os dados do avião
            voo = input("\nNúmero do Voo: ")
            companhia = input("Nome da Companhia: ")
            destino = input("Destino: ")

            # cria o novo avião
            aviao = Aviao(voo, companhia, destino)
            # coloca na fila
            fila.enfileirar(aviao)
            # e exibe uma mensagem de sucesso
            print("\nO avião foi colocado na fila com sucesso.")

        elif (opcao == 4):  # listar aviões na fila de espera
            if fila.vazia():
                print("\nA fila está vazia")
            else:
                print("\nAVIÕES NA FILA DE ESPERA:\n")
                print("----------------------------------")
                fila.listar_elementos()

        elif (opcao == 5):  # caracteristicas do primeiro avião da fila
            aviao = fila.retornar_frente()
            if aviao != None:
                print("\n-------- PRIMEIRO AVIÃO NA FILA ----------")
                print("Número do Voo: {0}".format(aviao.num_voo))
                print("Companhia: {0}".format(aviao.companhia))
                print("Destino: {0}".format(aviao.destino))
            else:
                print("\nA fila está vazia")

        elif (opcao == 6):
            break


if __name__ == "__main__":
    main()