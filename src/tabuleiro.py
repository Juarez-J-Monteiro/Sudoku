class Tabuleiro:
    VAZIO = '.'

    def __init__(self):
        self.tamanho = 9
        self.grade = self.gerarTabuleiro()

    def gerarTabuleiro(self):
        gradeTemporaria = [[self.VAZIO for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        return gradeTemporaria

    def exibirTabuleiro(self):
        print('\n')

        linhasTexto = []
        for i, linha in enumerate(self.grade):
            if i != 0 and i % 3 == 0:
                linhasTexto.append("-" * 21)
            
            celulas = []
            for j, valor in enumerate(linha):
                if j != 0 and j % 3 == 0:
                    celulas.append("|")
                celulas.append(str(valor) if valor != 0 else ".")
            
            linhasTexto.append(' '.join(celulas))
        
        print('\n'.join(linhasTexto))