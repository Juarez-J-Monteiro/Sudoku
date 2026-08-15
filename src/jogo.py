from time import sleep
from src.tabuleiro import Tabuleiro

class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()

    def verificaJogada(self):
        pass
    
    def fazerJogada(self):
        pass

    def iniciarPartida(self):
        while True:
            inputUsuario = str(input("Insira sua jogada (linha, coluna, número):\n"))

            # Validacao do input
            try:
                valores = inputUsuario.split(",")
                inputLinha = int(valores[0])
                inputColuna = int(valores[1])
                inputNumero = int(valores[2])

                # Validacao do intervalo inserido, avança o laço caso esteja fora do intervalo
                if not (1 <= inputLinha <= 9):
                    print("\n[Erro]: A LINHA escolhida ({}) nao existe. Escolha de 1 a 9.\n".format(inputLinha))
                    continue
                elif not (1 <= inputColuna <= 9):
                    print("\n[Erro]: A COLUNA escolhida ({}) nao existe. Escolha de 1 a 9.\n".format(inputColuna))
                    continue
                elif not (1 <= inputNumero <= 9):
                    print("\n[Erro]: O NUMERO escolhido ({}) nao existe. Escolha de 1 a 9.\n".format(inputNumero))
                    continue
                
            # Trata erro de formato invalido no input
            except Exception:
                print("\n[Erro] Entrada inválida: '{}'\n".format(inputUsuario))
                inputUsuario = ""
                continue

            self.tabuleiro.exibirTabuleiro()
            # print("L: {}, C: {}, N: {}".format(inputLinha, inputColuna, inputNumero))
