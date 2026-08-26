from src.jogo import Jogo

def iniciarJogo():
    """Cria uma nova instância do jogo e inicia a partida."""
    jogo = Jogo()
    jogo.iniciarPartida()

def perguntarJogarNovamente():
    """Pergunta ao usuário se deseja jogar novamente. Trata respostas inválidas"""

    while True:
        resposta = input("\nDeseja jogar novamente? (s/n)").strip().lower()
        if resposta == "s":
            return True
        elif resposta == 'n':
            return False
        else:
            print("Resposta inválida! Digite `s` para SIM ou `n` para NÃO!")

def main():
    """Controla a "vida" do programa, iniciando partidas quando optado pelo usuário. Inicia automaticamente
    a partida na primeira execução do programa"""

    jogarNovamente = True

    while jogarNovamente:
        iniciarJogo()
        jogarNovamente = perguntarJogarNovamente()

    print("Obrigado por jogar!")

main()