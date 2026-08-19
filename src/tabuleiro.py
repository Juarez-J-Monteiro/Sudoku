import random

class Tabuleiro:
    VAZIO = '.'

    def __init__(self):
        self.tamanho = 9
        self.grade = self.gerarTabuleiro()

    def gerarTabuleiro(self):
        tamanho = self.tamanho
        tamanhoSubQuadrado = int(tamanho ** 0.5)
        # Gera uma grade de um tamanho pré-definido, preenchendo cada célula com "."
        grade = [[self.VAZIO for _ in range(tamanho)] for _ in range(tamanho)]

        # Verifica se um número é válido em (x,y) posição. (True == válido, falso == inválido)
        def valido(linha, coluna, valor):
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

        # Função recursiva que preenche o tabuleiro com números aleatórios, percorrendo
        # célula por célula: avança coluna por coluna dentro da linha atual e ao
        # terminar a última coluna, passa para a próxima linha (validando cada número).
        def preencher(linha=0, coluna=0):
            # Caso base da recursão: quando a linha ultrapassa o índice máximo válido
            # (linha 9, onde as linhas vão de 0 a 8), significa
            # que todas as células foram preenchidas com sucesso.
            if linha == tamanho:
                return True

            # Calcula qual será a próxima célula a ser visitada.
            # Se chegou na última coluna, avança pra próxima linha e volta a coluna pro início;
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
                if valido(linha, coluna, valor):
                    # Ao encontrar um valor válido, ele o fixa na célula e chama preencher() para a
                    # próxima posição, funciona como se fosse um checkpoint: se o resto do tabuleiro 
                    # puder ser resolvido a partir daqui, a função retorna verdadeiro e a solução 
                    # se propaga.
                    grade[linha][coluna] = valor

                    # Chama a si mesmo tentando preencher a nova célula
                    if preencher(proxima_linha, proxima_coluna):
                        return True # Retorna verdadeiro e a solução se propaga.
                    
                    # Se a chamada recursiva acima retornar False, significa que o algoritmo chegou a
                    # um beco sem saída, onde nenhum valor é válido na posição, então o valor testado 
                    # é desfeito (volta a VAZIO) e o loop tenta o próximo valor da lista embaralhada,
                    # sem precisar reiniciar as células anteriores.
                    grade[linha][coluna] = self.VAZIO

            return False

        preencher()
        return grade

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