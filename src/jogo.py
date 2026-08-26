from time import sleep
from src.tabuleiro import Tabuleiro

class Jogo:
    LIMITE_ERROS = 3
    TEMPO_MSG = 1.5

    def __init__(self):

        # Inicializa a classe do tabuleiro
        self.tabuleiro = Tabuleiro()

        self.dificuldade = 0
        self.contagemErros = 0

    def exibirResultado(self, resultado):
        """Exibe a mensagem final de acordo com o resultado. """
        
        if resultado == "LimiteDeErroAtingido":
            print("\nLimite de erros ({}/{}) atingido.".format(self.contagemErros, self.LIMITE_ERROS))
            print("Você perdeu!")
        elif resultado == "TabuleiroCompleto":
            print("\nO tabuleiro foi completado.")
            print("Você ganhou!")

    def jogoTerminou(self):
        """Verifica se alguma condição de fim de jogo foi atingida"""

        if self.contagemErros >= self.LIMITE_ERROS:
            return True, "LimiteDeErroAtingido"
        if self.tabuleiro.tabuleiroCompleto():
            return True, "TabuleiroCompleto"
        
        return False, None
    
    def fazerJogada(self, linha, coluna, numero):
        """Coloca um número numa célula editável, validando as regras e permite 
        substituir jogadas anteriores."""

        # Corrige o intervalo digitado pelo usuário, adequando ao índice
        # usado pelo programa.
        pos = (linha - 1, coluna - 1)

        # Verifica se a posição da jogada é de uma pista
        if pos not in self.tabuleiro.posOcultadas:
            print("\nEssa célula não pode ser alterada!")
            sleep(self.TEMPO_MSG)
            return

        # Salva o valor antigo da célula.
        valorAntigo = self.tabuleiro.grade[pos[0]][pos[1]]

        # Limpa a célula antes de validar.
        self.tabuleiro.grade[pos[0]][pos[1]] = self.tabuleiro.VAZIO

        # Verifica se o novo valor na célula é válido segundo as regras.
        if self.tabuleiro.valido(self.tabuleiro.grade, pos[0], pos[1], numero):
            # Atribui definitivamente o novo valor na célula se for válido.
            self.tabuleiro.grade[pos[0]][pos[1]] = numero

            # Condição que verifica se houve erro de jogada na célula antes.
            if (pos[0],pos[1]) in self.tabuleiro.posNumErrado:
                # Deleta o erro e evita preencher incorretamente em `self.tabuleiro.renderizar`.
                del self.tabuleiro.posNumErrado[pos]
        else:
            # Adiciona/substitui o valor errado num dicionário para renderizar depois.
            self.tabuleiro.posNumErrado[pos] = numero

            # Desfaz a jogada se for inválida.
            self.tabuleiro.grade[pos[0]][pos[1]] = valorAntigo

            # Contabiliza o erro.
            self.contagemErros += 1
            print("\nJogada inválida!")
            sleep(self.TEMPO_MSG)

    def lerDificuldade(self):
        """Lê a dificuldade escolhida, validando o input inserido. """

        # Fica em loop enquanto uma dificuldade válida não for 
        # digitada, ou o programa encerrado.
        while True:

            # Validação básica do input
            try:
                # Lê e armazena a dificuldade desejada.
                inputDificuldade = int(input("1 - Fácil (mais pistas)\n" \
                "2 - Médio \n" \
                "3 - Difícil \n" \
                "4 - Especialista (menos pistas)\n\n" \
                "Insira a dificuldade: "))
            except ValueError:
                # Trata valores que não sejam números.
                print("\nEntrada inválida. Digite um número.\n")
                sleep(self.TEMPO_MSG)
                
                # Repete o loop.
                continue

            # Trata valores fora do intervalo de dificuldades.
            if inputDificuldade not in range(1, 5):
                print("\nEscolha um valor entre 1 e 4.\n")
                sleep(self.TEMPO_MSG)

                # Repete o loop.
                continue

            # Retorna a dificuldade escolhida.
            return inputDificuldade

    def lerJogada(self):
        """Lê a jogada inserida, validando o input digitado. """

        # Fica em loop enquanto o input da jogada não for 
        # digitado corretamente, ou o programa encerrado.
        while True:
            inputLinha = 0
            inputColuna = 0
            inputNumero = 0

            # Lê e armazena a dificuldade desejada.
            inputUsuario = str(input("Insira sua jogada (linha, coluna, número):\n"))

            # Validação básica do input.
            try:
                # Sepra os valores por ",".
                valores = inputUsuario.split(",")

                # Armazena cada um em sua respectiva variável.
                inputLinha = int(valores[0])
                inputColuna = int(valores[1])
                inputNumero = int(valores[2])

                # Validação do intervalo inserido, avança o laço (repete a msg) caso esteja fora do intervalo
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

                # Repete o loop.
                continue

            # Retorna os valores escolhidos pelo usuário separadamente.
            return inputLinha, inputColuna, inputNumero

    def iniciarPartida(self):
        """Conduz o fluxo da partida, pede a dificuldade, gera o tabuleiro
        jogável e executa o loop de jogadas até que o jogo termine."""

        # Lê e armazena a dificuldade.
        self.dificuldade = self.lerDificuldade()

        # Oculta as células conforme a dificuldade escolhida.
        self.tabuleiro.ocultarCelulas(self.dificuldade)

        while True:

            # Exibe o tabuleiro para o usuário.
            self.tabuleiro.renderizar()

            # Exibe a contagem de erros cometidos e o limite.
            print("{}/{} erros".format(self.contagemErros, self.LIMITE_ERROS))

            # Lê e armazena as coordenadas e número escolhido.
            linha, coluna, numero = self.lerJogada()

            # Realiza a jogada com as coordenadas e o número escolhidos.
            self.fazerJogada(linha, coluna, numero)

            # Verifica se alguma condição de término foi atingida
            # e armazena essas condições. 
            terminou, resultado = self.jogoTerminou()

            # Condição que verifica se o jogo terminou.
            if terminou:
                # Se verdadeiro, exibe a mensagem correspondente de término
                self.exibirResultado(resultado)

                # Finaliza a partida
                break