class Tabuleiro:
    VAZIO = '.'

    def __init__(self):
        self.tamanho = 9
        self.grade = self.gerarTabuleiro()

    def gerarTabuleiro(self):
        gradeTemporaria = [[self.VAZIO for _ in range(self.tamanho)] for _ in range(self.tamanho)]
        return gradeTemporaria

    def renderizar(self):
        print('\n')

        linhasTexto = []

        # Os lacos abaixo percorrem todas as células e linhas da grade original,  
        # adicionando as delimitacoes do tabuleiro onde necessário

        # Laco que percorre as linhas da grade original
        for i, linha in enumerate(self.grade):

            # Condicao para delimitacao, garantindo separacao correta
            if i != 0 and i % 3 == 0: 
                # Adiciona a delimitacao horizontal do tabuleiro
                linhasTexto.append("-" * 21) 

            celulas = [] # lista temporaria de celulas
            # Laço que percorre as células de cada linha
            for j, valor in enumerate(linha):
                # Condicao para delimitacao, garantindo separacao correta
                if j != 0 and j % 3 == 0:
                    # Adiciona a delimitacao vertical do tabuleiro
                    celulas.append("|") 
                celulas.append(str(valor))

            # Junta as células já formatados com as delimatacoes verticais do tabuleiro  
            # na matriz que será impressa
            linhasTexto.append(' '.join(celulas)) 
        
        print('\n'.join(linhasTexto)) # imprime o tabuleiro totalmente formatado