import random

class Tabuleiro:
    VAZIO = '.'

    def __init__(self):
        self.tamanho = 9
        self.grade = self.gerarTabuleiro()
        self.posOcultadas = None

    def valido(self, grade, linha: int, coluna, valor):
        """Verifica se um número é válido em (x,y) posição. 
        (True == válido, falso == inválido)"""

        tamanho = self.tamanho
        tamanhoSubQuadrado = int(tamanho ** 0.5)
        
        # Verifica linha
        if valor in grade[linha]:
            return False
        
        # Verifica coluna
        for i in range(tamanho):
            if grade[i][coluna] == valor:
                return False
            
        # Verifica se o valor já está posicionado no subquadrado correspondente
        inicioLinha = (linha // tamanhoSubQuadrado) * tamanhoSubQuadrado
        inicioColuna = (coluna // tamanhoSubQuadrado) * tamanhoSubQuadrado
        for i in range(inicioLinha, inicioLinha + tamanhoSubQuadrado):
            for j in range(inicioColuna, inicioColuna + tamanhoSubQuadrado):
                if grade[i][j] == valor:
                    # Retorna falso caso o valor seja encontrado (posição inválida)
                    return False
        # Retorna verdadeiro caso o valor não seja encontrado (posição válida)
        return True

    def preencher(self, grade, linha=0, coluna=0):
        """Preenche recursivamente o tabuleiro com números aleatórios, percorrendo
        célula por célula: avança coluna por coluna dentro da linha atual e ao
        terminar a última coluna, passa para a próxima linha (validando cada número)."""
        
        tamanho = self.tamanho
        # Caso base da recursão: quando a linha ultrapassa o índice máximo válido
        # (linha 9, onde as linhas vão de 0 a 8), significa
        # que todas as células foram preenchidas com sucesso.
        if linha == tamanho:
            return True

        # Calcula qual será a próxima célula a ser visitada.
        # Se chegou na última coluna, avança pra próxima linha e volta a coluna pro início,
        # caso contrário, apenas avança uma coluna na mesma linha.
        if coluna == tamanho - 1:
            proxima_linha = linha + 1
            proxima_coluna = 0
        else:
            proxima_linha = linha
            proxima_coluna = coluna + 1

        # Cria uma lista com os valores possíveis, de 1 até 9
        valores = list(range(1, 10))
        # Embaralha a lista garantindo que o tabuleiro seja diferente a cada execução
        random.shuffle(valores)

        # Para célula atual, percorre os valores na lista embaralhada.
        for valor in valores:
            # Verifica se ele é válido (não repete na linha, coluna ou bloco).
            if self.valido(grade, linha, coluna, valor):
                # Ao encontrar um valor válido, ele o fixa na célula e chama preencher() para a
                # próxima posição, funciona como se fosse um checkpoint: se o resto do tabuleiro 
                # puder ser resolvido a partir daqui, a função retorna verdadeiro e a solução 
                # se propaga.
                grade[linha][coluna] = valor

                # Chama a si mesmo tentando preencher a nova célula
                if self.preencher(grade, proxima_linha, proxima_coluna):
                    return True # Retorna verdadeiro e a solução se propaga.
                
                # Se a chamada recursiva acima retornar False, significa que o algoritmo chegou a
                # um beco sem saída, onde nenhum valor é válido na posição, então o valor testado 
                # é desfeito (volta a VAZIO) e o loop tenta o próximo valor da lista embaralhada,
                # sem precisar reiniciar as células anteriores.
                grade[linha][coluna] = self.VAZIO

        return False
        
    def gerarTabuleiro(self):
        """Gera o tabuleiro inicial válido"""

        tamanho = self.tamanho

        # Gera uma grade de um tamanho pré-definido, preenchendo cada célula com "."
        grade = [[self.VAZIO for _ in range(tamanho)] for _ in range(tamanho)]

        # Chama a função responsável por preencher o tabuleiro de forma válida
        self.preencher(grade)

        # Retorna o tabuleiro preenchido e válido
        return grade

    def ocultarCelulas(self, dificuldade):
        # Lista das dificuldades com seus limites mínimos e máximos de ocultações.
        dificuldades = {
            1: (41, 45), # 36-40 pistas
            2: (46, 51), # 30-35 pistas
            3: (52, 57), # 24-29 pistas
            4: (58, 64)  # 17-23 pistas
        }

        # Caso a dificuldade seja inválida mesmo depois das validações no input, assume a dificuldade
        # fácil como padrão e gera um aviso.
        if dificuldade not in dificuldades:
            print("Aviso: dificuldade '{}' inválida, usando padrão (fácil).".format(dificuldade))
            dificuldade = 1

        # Atribui os valores mínimos e máximos com base na dificuldade escolhida
        minimo, maximo = dificuldades[dificuldade]
        # Gera o número de ocultações com base nos limites
        quantidade = random.randint(minimo, maximo)

        posicoes = []
        # Salva as posições ocultadas para uso futuro de validação
        self.posOcultadas = posicoes

        # Laço que percorre a quantidade de células a serem ocultadas
        for i in range(quantidade):
            while True:

                # Gera uma coordenada aleatória
                x = random.randint(0, 8)
                y = random.randint(0, 8)

                # Verifica se a coordenada gerada já existe na lista
                if (x, y) not in posicoes:

                    # Se não existir, adiciona a coordenada gerada na lista
                    posicoes.append((x, y))
                    break # Para o while e avança o laço for

        # Percorre a lista das coordenadas geradas e aplica a ocultação no tabuleiro
        for i in range(len(posicoes)):
            x = posicoes[i][0]
            y = posicoes[i][1]
            self.grade[x][y] = '.'

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