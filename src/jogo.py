from time import sleep
from src.tabuleiro import Tabuleiro

class Jogo:
    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.dificuldade = 0
        self.contagemErros = 0

    def verificaJogada(self):
        pass
    
    def fazerJogada(self, linha, coluna, numero):
        """Coloca um número numa célula editável, validando as regras e permite 
        substituir jogadas anteriores."""

        pos = (linha - 1, coluna - 1)

        # Verifica se a posição da jogada é de uma pista
        if pos not in self.tabuleiro.posOcultadas:
            print("Essa célula não pode ser alterada!")
            return

        # Salva o valor antigo da célula
        valorAntigo = self.tabuleiro.grade[pos[0]][pos[1]]

        # Limpa a célula antes de validar
        self.tabuleiro.grade[pos[0]][pos[1]] = self.tabuleiro.VAZIO

        # Verifica se o novo valor na célula é valida segundo as regras.
        if self.tabuleiro.valido(self.tabuleiro.grade, pos[0], pos[1], numero):
            # Atribui definitivamente o novo valor na célula se for válido.
            self.tabuleiro.grade[pos[0]][pos[1]] = numero
        else:
            # Desfaz a jogada se for inválida.
            self.tabuleiro.grade[pos[0]][pos[1]] = valorAntigo

            # Contabiliza o erro.
            self.contagemErros += 1
            print("\nJogada inválida!")
            sleep(1.5)

    def lerDificuldade(self):
        while True:
            try:
                inputDificuldade = int(input("1 - Fácil (mais pistas)\n" \
                "2 - Médio \n" \
                "3 - Difícil \n" \
                "4 - Especialista (menos pistas)\n\n" \
                "Insira a dificuldade: "))
            except ValueError:
                print("\nEntrada inválida. Digite um número.\n")
                sleep(1.5)
                continue

            if inputDificuldade not in range(1, 4):
                print("\nEscolha um valor entre 1 e 4.\n")
                sleep(1.5)
                continue

            return inputDificuldade

    def lerJogada(self):
        while True:
            inputLinha = 0
            inputColuna = 0
            inputNumero = 0

            inputUsuario = str(input("Insira sua jogada (linha, coluna, número):\n"))

            # Validacao basica do input
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

            return inputLinha, inputColuna, inputNumero

    def iniciarPartida(self):
        self.dificuldade = self.lerDificuldade()
        self.tabuleiro.ocultarCelulas(self.dificuldade)

        while True:
            self.tabuleiro.renderizar()

            linha, coluna, numero = self.lerJogada()

            self.fazerJogada(linha, coluna, numero)

        # print("L: {}, C: {}, N: {}".format(inputLinha, inputColuna, inputNumero))
