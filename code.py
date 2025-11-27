# -*- coding: utf-8 -*-
"""
Trabalho Prático de Projeto e Análise de Algoritmos
Problema: Posicionamento Máximo de Peças de Xadrez

Este arquivo é um esqueleto para o trabalho.
A lógica principal de backtracking já está implementada na função 'solve'.

Sua tarefa é:
1. Alterar a SEMENTE_ALUNO para os primeiros 5 dígitos de matrícula.
2. Implementar a lógica de verificação da SUA peça na função 'isSafe'.

"""

import random
import copy # Para copiar o tabuleiro da melhor solução

# ---
# Configurações Globais do Trabalho
# ---

# Tamanho do tabuleiro (N x N)
N = 8

# Percentual de casas que serão bloqueadas (obstáculos)
PERCENTUAL_OBSTACULOS = 10.0 # 10%

# --- TODO: ALUNO ---
# Coloque aqui os primeiros 5 dígitos seu número de matrícula
# Isso garante que seu "tabuleiro aleatório" seja único, mas reprodutível.
SEMENTE_ALUNO = 20221
# --- FIM DO TODO ---


# ---
# Variáveis Globais para guardar a melhor solução
# (Não mexa aqui)
# ---
max_pecas = 0
melhor_tabuleiro = []


def gerar_obstaculos(semente, n, percentual):
    """
    Gera uma lista de obstáculos determinística (baseada na semente).
    Isso garante que, para a mesma semente, os obstáculos sejam sempre os mesmos.
    """
    random.seed(semente)
    
    total_casas = n * n
    num_obstaculos = int(total_casas * (percentual / 100.0))
    
    # Gera todas as coordenadas possíveis
    todas_casas = [(r, c) for r in range(n) for c in range(n)]
    
    # Seleciona 'num_obstaculos' aleatoriamente para serem os obstáculos
    obstaculos = random.sample(todas_casas, num_obstaculos)
    
    print(f"--- Trabalho com Semente: {semente} ---")
    print(f"Obstáculos gerados ({len(obstaculos)}): {obstaculos}")
    print("----------------------------------------")
    
    return obstaculos

def imprimir_tabuleiro(tabuleiro):
    """
    Imprime o tabuleiro no console de forma legível.
    'P' = Peça
    'X' = Obstáculo
    '.' = Casa Vazia
    """
    if not tabuleiro:
        print("Nenhuma solução encontrada.")
        return
        
    for r in range(N):
        # Constrói a string da linha
        linha = []
        for c in range(N):
            if (r, c) in OBSTACULOS:
                linha.append('X')
            elif tabuleiro[r][c] == 'P':
                linha.append('P')
            else:
                linha.append('.')
        print(" ".join(linha))


def isSafe(tabuleiro, r, c, obstaculos_list):
    """
    Verifica se é seguro ("Safe") colocar uma peça na casa (r, c).
    
    Esta é a FUNÇÃO PRINCIPAL que você deve implementar.
    
    Uma posição é "insegura" se:
    1. A casa (r, c) já for um obstáculo.
    2. A peça em (r, c) atacar QUALQUER outra peça que já está no tabuleiro.
    
    Retorna:
        True: Se for seguro colocar a peça.
        False: Se for inseguro (obstáculo ou ataque).
    """

    # 1. Verifica se a casa (r, c) é um obstáculo.
    #    (Esta parte já está pronta)
    if (r, c) in obstaculos_list:
        return False

    # --- TODO: ALUNO ---
    # 2. Implemente a lógica de ataque da SUA PEÇA.
    #    Você deve verificar se a peça em (r, c) ataca
    #    ou é atacada por qualquer outra peça ('P') já colocada.
    
    # AMAZONA: Combina os ataques da RAINHA e do CAVALO
    
    # PARTE 1: ATAQUES COMO RAINHA (linhas, colunas e diagonais)
    
    for i in range(N):
        if tabuleiro[r][i] == 'P':
            return False
    
    for i in range(N):
        if tabuleiro[i][c] == 'P':
            return False
    
    for i in range(N):
        if 0 <= r - i < N and 0 <= c - i < N:
            if tabuleiro[r - i][c - i] == 'P':
                return False
        if 0 <= r + i < N and 0 <= c + i < N:
            if tabuleiro[r + i][c + i] == 'P':
                return False
    
    for i in range(N):
        if 0 <= r - i < N and 0 <= c + i < N:
            if tabuleiro[r - i][c + i] == 'P':
                return False
        if 0 <= r + i < N and 0 <= c - i < N:
            if tabuleiro[r + i][c - i] == 'P':
                return False
    
    # PARTE 2: ATAQUES COMO CAVALO (movimento em "L")
    
    movimentos_cavalo = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        ( 1, -2), ( 1, 2),
        ( 2, -1), ( 2, 1)
    ]
    
    for dr, dc in movimentos_cavalo:
        nr, nc = r + dr, c + dc
        
        if 0 <= nr < N and 0 <= nc < N:
            if tabuleiro[nr][nc] == 'P':
                return False
    
    # --- FIM DO TODO ---

    # Se passou por todas as verificações, a posição é segura
    return True


def solve(index, count, tabuleiro, obstaculos_list):
    """
    Função recursiva principal do Backtracking.
    
    NÃO PRECISA ALTERAR ESTA FUNÇÃO.
    
    'index' é a casa atual que estamos analisando (de 0 a N*N - 1)
    'count' é o número de peças que colocamos ATÉ AGORA
    'tabuleiro' é o estado atual do tabuleiro
    """
    global max_pecas, melhor_tabuleiro

    # --- Caso Base da Recursão ---
    # Se já passamos por todas as casas (index == N*N), paramos.
    if index == N * N:
        # Se o número de peças 'count' desta solução for
        # melhor que o máximo que já encontramos...
        if count > max_pecas:
            max_pecas = count
            # ...salvamos uma CÓPIA PROFUNDA (deepcopy) do tabuleiro.
            melhor_tabuleiro = copy.deepcopy(tabuleiro)
        return # Fim da recursão para este caminho

    # --- Passo Recursivo ---
    
    # Converte o índice 1D (index) para coordenadas 2D (r, c)
    r = index // N
    c = index % N

    # --- Opção 1: Tentar colocar a peça em (r, c) ---
    
    # Verificamos se é seguro colocar a peça aqui.
    # Esta é a "PODA" (Pruning) do backtracking.
    # Se 'isSafe' retornar False, nem tentamos esta "galho" da árvore.
    if isSafe(tabuleiro, r, c, obstaculos_list):
        
        # 1. ESCOLHA: Colocar a peça
        tabuleiro[r][c] = 'P'
        
        # 2. EXPLORE: Chama a recursão para a *próxima* casa (index + 1)
        #    aumentando a contagem de peças.
        solve(index + 1, count + 1, tabuleiro, obstaculos_list)
        
        # 3. DESFAÇA (BACKTRACK): Remove a peça.
        #    Isso é crucial. Voltamos ao estado anterior para que
        #    a "Opção 2" (abaixo) possa ser testada corretamente.
        tabuleiro[r][c] = '.'

    # --- Opção 2: NÃO colocar a peça em (r, c) ---
    
    # 1. ESCOLHA: Não fazer nada (manter a casa vazia).
    # 2. EXPLORE: Chama a recursão para a *próxima* casa (index + 1).
    #    A contagem de peças (count) continua a mesma.
    solve(index + 1, count, tabuleiro, obstaculos_list)


# ---
# Ponto de Entrada Principal do Programa
# ---
if __name__ == "__main__":
    
    # 1. Gera os obstáculos com base na semente do aluno
    OBSTACULOS = gerar_obstaculos(SEMENTE_ALUNO, N, PERCENTUAL_OBSTACULOS)
    
    # 2. Cria um tabuleiro inicial vazio (preenchido com '.')
    tabuleiro_inicial = [['.' for _ in range(N)] for _ in range(N)]
    
    # 3. Inicia o processo de backtracking
    #    Começa na casa 0, com 0 peças, no tabuleiro inicial
    print("Iniciando backtracking... (Isso pode demorar alguns segundos)")
    solve(0, 0, tabuleiro_inicial, OBSTACULOS)
    
    # 4. Imprime os resultados finais
    print("----------------------------------------")
    print("Backtracking concluído.")
    print(f"NÚMERO MÁXIMO DE PEÇAS: {max_pecas}")
    print("----------------------------------------")
    print("Melhor configuração encontrada:")
    imprimir_tabuleiro(melhor_tabuleiro)