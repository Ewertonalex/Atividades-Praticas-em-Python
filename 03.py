#Construa um programa em Python de acordo com situação problema descrita: Um grupo
#de soldados está cercado e não há esperança de vitória, porém existe somente um cavalo
#disponível para escapar e buscar por reforços. Para determinar qual soldado deve escapar
#para encontrar ajuda, eles formam um círculo (Fila Circular) e sorteiam um número de um
#chapéu. Começando por um soldado sorteado aleatoriamente, uma contagem é realizada
#até o número sorteado. Quando a contagem terminar, o soldado em que a contagem
#parou é removido do círculo, um novo número é sorteado e a contagem recomeça no
#soldado seguinte ao que foi eliminado. A cada rodada, portanto, o círculo diminui em um,
#até que somente um soldado reste e seja escolhido para a tarefa.



def soldadoCirculo(soldado, step=2):
    if step <= 1:
        print("Digite um valor maior que 1 !")
    else:
        step -= 1
        kill = step
        while len(soldado) > 1:
            print("O Soldado",soldado.pop(kill),"foi sorteado, está fora da Fila!")
            kill = (kill + step) % len(soldado)
        print("\n======== O Soldado",soldado[0], "foi o ganhador e escapou! ========")


num = int(input("== REGRAS DO SORTEIO ==\nCada soldado receberá um número, de acordo com a quantidade escolhida."
                "\nCada número será colocado em chapéu, à medida que um soldado for sorteado,"
                "\nele vai sair da fila, o último número no chapéu será o soldado que vai escapar!"
                "\n\nQue começem os jogos..."
                "\n\nEntão digite qual a quantidade de soldados no Grupo:  "))
soldados = [i for i in range(1, num + 1)]
soldadoCirculo(soldados)
