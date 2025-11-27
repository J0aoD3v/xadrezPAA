# Trabalho Final de PAA - Amazona
**Aluno:** João CFMC  
**Data da Apresentação:** 27/11/2025  
**Peça:** Amazona (ataca como Rainha E como Cavalo)

---

## 📋 Visão Geral do Problema

O objetivo é encontrar o **número máximo de Amazonas** que podem ser posicionadas em um tabuleiro NxN (8x8), onde:
- Nenhuma Amazona pode atacar outra
- Nenhuma Amazona pode ser colocada em casas bloqueadas (obstáculos)

---

## 🎯 A Peça Amazona

A Amazona é uma peça híbrida que combina dois padrões de ataque:

### 1. Ataque como RAINHA:
- **Horizontal**: toda a linha
- **Vertical**: toda a coluna
- **Diagonal Principal**: direção ↘ e ↖
- **Diagonal Secundária**: direção ↙ e ↗

### 2. Ataque como CAVALO:
- Movimento em "L": 2 casas em uma direção + 1 casa perpendicular
- 8 movimentos possíveis: `(±2, ±1)` e `(±1, ±2)`

```
Exemplo de ataque do Cavalo:
    . . . . .
    . . X . X
    . X . . .
    . . C . .     C = Cavalo/Amazona
    . X . . .
    . . X . X
    . . . . .
```

---

## 🔧 Estrutura do Código

### **Constantes Globais**

```python
N = 8  # Tamanho do tabuleiro (8x8)
PERCENTUAL_OBSTACULOS = 10.0  # 10% de casas bloqueadas
SEMENTE_ALUNO = 12345  # Primeiros 5 dígitos da matrícula
```

- `N`: Define o tamanho do tabuleiro
- `PERCENTUAL_OBSTACULOS`: Percentual de casas que serão obstáculos
- `SEMENTE_ALUNO`: Garante que os obstáculos sejam sempre os mesmos para cada aluno

### **Variáveis Globais**

```python
max_pecas = 0  # Guarda o número máximo de peças encontrado
melhor_tabuleiro = []  # Guarda a melhor configuração do tabuleiro
```

---

## 🧮 Funções Principais

### 1. `gerar_obstaculos(semente, n, percentual)`

**Propósito:** Gera obstáculos de forma determinística usando uma semente aleatória.

**Como funciona:**
```python
random.seed(semente)  # Define a semente para reprodutibilidade
total_casas = n * n  # Total de casas no tabuleiro
num_obstaculos = int(total_casas * (percentual / 100.0))  # Calcula quantos obstáculos
todas_casas = [(r, c) for r in range(n) for c in range(n)]  # Todas as coordenadas
obstaculos = random.sample(todas_casas, num_obstaculos)  # Seleciona aleatoriamente
```

**Retorna:** Lista de tuplas com coordenadas dos obstáculos, ex: `[(6, 5), (5, 6), (0, 0)]`

---

### 2. `imprimir_tabuleiro(tabuleiro)`

**Propósito:** Exibe o tabuleiro de forma visual no console.

**Legenda:**
- `P` = Peça (Amazona)
- `X` = Obstáculo
- `.` = Casa Vazia

**Exemplo de saída:**
```
X P . . . . . .
. . . . P . . .
. . . . . . . P
```

---

### 3. `isSafe(tabuleiro, r, c, obstaculos_list)` ⭐ **FUNÇÃO PRINCIPAL**

**Propósito:** Verifica se é seguro colocar uma Amazona na posição `(r, c)`.

#### **Verificação 1: Obstáculos**
```python
if (r, c) in obstaculos_list:
    return False
```
- Se a posição for um obstáculo, retorna `False` imediatamente

#### **Verificação 2: Ataque como RAINHA**

**2a. Linha Horizontal:**
```python
for i in range(N):
    if tabuleiro[r][i] == 'P':
        return False
```
- Percorre todas as colunas `i` da linha `r`
- Se encontrar uma peça, há conflito

**2b. Coluna Vertical:**
```python
for i in range(N):
    if tabuleiro[i][c] == 'P':
        return False
```
- Percorre todas as linhas `i` da coluna `c`
- Se encontrar uma peça, há conflito

**2c. Diagonais Principal (↘ e ↖):**
```python
for i in range(N):
    if 0 <= r - i < N and 0 <= c - i < N:
        if tabuleiro[r - i][c - i] == 'P':
            return False
    if 0 <= r + i < N and 0 <= c + i < N:
        if tabuleiro[r + i][c + i] == 'P':
            return False
```
- `r - i, c - i`: diagonal para cima-esquerda (↖)
- `r + i, c + i`: diagonal para baixo-direita (↘)
- Verifica se as coordenadas estão dentro do tabuleiro antes de acessar

**2d. Diagonais Secundária (↙ e ↗):**
```python
for i in range(N):
    if 0 <= r - i < N and 0 <= c + i < N:
        if tabuleiro[r - i][c + i] == 'P':
            return False
    if 0 <= r + i < N and 0 <= c - i < N:
        if tabuleiro[r + i][c - i] == 'P':
            return False
```
- `r - i, c + i`: diagonal para cima-direita (↗)
- `r + i, c - i`: diagonal para baixo-esquerda (↙)

#### **Verificação 3: Ataque como CAVALO**

```python
movimentos_cavalo = [
    (-2, -1), (-2, 1),  # 2 para cima, 1 para os lados
    (-1, -2), (-1, 2),  # 1 para cima, 2 para os lados
    ( 1, -2), ( 1, 2),  # 1 para baixo, 2 para os lados
    ( 2, -1), ( 2, 1)   # 2 para baixo, 1 para os lados
]

for dr, dc in movimentos_cavalo:
    nr, nc = r + dr, c + dc  # Nova linha, nova coluna
    
    if 0 <= nr < N and 0 <= nc < N:  # Verifica se está no tabuleiro
        if tabuleiro[nr][nc] == 'P':
            return False  # Conflito encontrado
```

**Como funciona:**
1. Define os 8 movimentos possíveis do Cavalo
2. Para cada movimento `(dr, dc)`, calcula a nova posição `(nr, nc)`
3. Verifica se a nova posição está dentro dos limites do tabuleiro
4. Se houver uma peça nessa posição, retorna `False`

#### **Retorno Final:**
```python
return True  # Se passou por todas as verificações, é seguro
```

---

### 4. `solve(index, count, tabuleiro, obstaculos_list)` 🔄 **BACKTRACKING**

**Propósito:** Algoritmo recursivo de backtracking que testa todas as configurações possíveis.

#### **Parâmetros:**
- `index`: Casa atual sendo analisada (0 a N*N - 1)
- `count`: Número de peças colocadas até agora
- `tabuleiro`: Estado atual do tabuleiro
- `obstaculos_list`: Lista de obstáculos

#### **Caso Base:**
```python
if index == N * N:  # Passou por todas as casas
    if count > max_pecas:  # Se encontrou uma solução melhor
        max_pecas = count
        melhor_tabuleiro = copy.deepcopy(tabuleiro)  # Salva cópia
    return
```

#### **Conversão de Índice:**
```python
r = index // N  # Linha: divisão inteira
c = index % N   # Coluna: resto da divisão
```
- Converte índice linear (0-63) em coordenadas 2D (r, c)
- Exemplo: `index = 10` → `r = 1, c = 2` (linha 1, coluna 2)

#### **Opção 1: COLOCAR a peça**
```python
if isSafe(tabuleiro, r, c, obstaculos_list):  # PODA
    tabuleiro[r][c] = 'P'  # 1. ESCOLHA
    solve(index + 1, count + 1, tabuleiro, obstaculos_list)  # 2. EXPLORE
    tabuleiro[r][c] = '.'  # 3. DESFAÇA (Backtrack)
```

**Explicação:**
1. **PODA**: Só tenta colocar se `isSafe()` retornar `True`
2. **ESCOLHA**: Coloca a peça na posição
3. **EXPLORE**: Chama recursivamente para a próxima casa
4. **DESFAÇA**: Remove a peça para testar outras possibilidades

#### **Opção 2: NÃO COLOCAR a peça**
```python
solve(index + 1, count, tabuleiro, obstaculos_list)
```
- Simplesmente passa para a próxima casa sem colocar peça
- A contagem `count` permanece a mesma

---

## 🚀 Fluxo de Execução Principal

```python
if __name__ == "__main__":
    # 1. Gera obstáculos
    OBSTACULOS = gerar_obstaculos(SEMENTE_ALUNO, N, PERCENTUAL_OBSTACULOS)
    
    # 2. Cria tabuleiro vazio
    tabuleiro_inicial = [['.' for _ in range(N)] for _ in range(N)]
    
    # 3. Inicia backtracking
    solve(0, 0, tabuleiro_inicial, OBSTACULOS)
    
    # 4. Imprime resultados
    print(f"NÚMERO MÁXIMO DE PEÇAS: {max_pecas}")
    imprimir_tabuleiro(melhor_tabuleiro)
```

---

## 📊 Complexidade

### **Complexidade de Tempo:**
- **Pior caso**: O(2^(N²)) - cada casa tem 2 opções (colocar ou não)
- **Com poda**: Muito menor na prática, pois `isSafe()` elimina muitos caminhos inválidos

### **Complexidade de Espaço:**
- **Pilha de recursão**: O(N²) - profundidade máxima da recursão
- **Tabuleiro**: O(N²) - armazena o estado

---

## 🎓 Pontos Importantes para a Apresentação

### 1. **Por que usar Backtracking?**
   - Problema de otimização combinatória
   - Precisa explorar todas as possibilidades
   - Poda inteligente reduz drasticamente o espaço de busca

### 2. **A importância do `isSafe()`:**
   - É a "poda" (pruning) que torna o backtracking eficiente
   - Sem ela, o algoritmo testaria configurações inválidas

### 3. **Por que `copy.deepcopy()`?**
   - Lista em Python são mutáveis
   - Sem deepcopy, `melhor_tabuleiro` seria apenas uma referência
   - Todas as mudanças posteriores afetariam a "melhor" solução

### 4. **Diferença entre Amazona e outras peças:**
   - Amazona é a peça mais poderosa (Rainha + Cavalo)
   - Consegue atacar mais casas, logo menos peças cabem no tabuleiro
   - Rainha sozinha: ~8 peças possíveis
   - Amazona: ~4-6 peças possíveis (devido aos ataques extras do Cavalo)

---

## 🧪 Exemplo de Execução

**Entrada:**
- Tabuleiro: 8x8
- Semente: 12345
- Obstáculos: 10%

**Saída:**
```
--- Trabalho com Semente: 12345 ---
Obstáculos gerados (6): [(6, 5), (5, 6), (0, 0), (6, 4), (7, 4), (6, 3)]
----------------------------------------
NÚMERO MÁXIMO DE PEÇAS: 6
----------------------------------------
X P . . . . . .
. . . . P . . .
. . . . . . . P
P . . . . . . .
. . . P . . . .
. . . . . . X .
. . . X X X P .
. . . . X . . .
```

---

## ✅ Checklist para a Apresentação

- [ ] Atualizar `SEMENTE_ALUNO` com seus 5 primeiros dígitos da matrícula
- [ ] Remover TODOS os comentários do código
- [ ] Testar com diferentes valores de N (quando o professor mudar)
- [ ] Explicar cada linha sem hesitar
- [ ] Saber explicar a diferença entre Rainha e Cavalo
- [ ] Saber explicar por que a Amazona é mais restritiva
- [ ] Entender o conceito de backtracking e poda

---

## 🔍 Possíveis Perguntas do Professor

**1. "Por que usar recursão?"**
- Backtracking é naturalmente recursivo
- Cada decisão (colocar/não colocar) leva a um novo estado
- Facilita o "desfazer" (backtrack)

**2. "O que acontece se remover o `isSafe()`?"**
- O algoritmo ainda funciona, mas fica muito mais lento
- Testaria configurações inválidas desnecessariamente
- Perderia a eficiência da poda

**3. "Por que verificar ataques em ambas as direções das diagonais?"**
- Precisamos verificar toda a diagonal, não só uma direção
- `i` cresce de 0 até N, então verificamos ↖↘ e ↗↙

**4. "Qual a diferença entre índice e coordenadas?"**
- Índice: posição linear (0-63 para tabuleiro 8x8)
- Coordenadas: posição 2D (linha, coluna)
- Conversão: `r = index // N` e `c = index % N`

---

## 📝 Dicas Finais

1. **Pratique explicar em voz alta** cada linha do código
2. **Desenhe no quadro** os padrões de ataque da Amazona
3. **Saiba calcular manualmente** a conversão de índice para coordenadas
4. **Entenda o fluxo** de escolha → exploração → backtrack
5. **Esteja preparado** para o professor mudar N ou a semente

**Boa sorte na apresentação! 🚀**
