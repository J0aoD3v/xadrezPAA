# 🚀 Como Publicar no GitHub Pages

## Passo 1: Commit e Push dos Arquivos

Abra o terminal no diretório do projeto e execute:

```bash
git add .
git commit -m "Adiciona interface web interativa para o trabalho de Amazona"
git push origin main
```

## Passo 2: Ativar GitHub Pages

1. Acesse seu repositório no GitHub: `https://github.com/J0aoD3v/xadrezPAA`

2. Clique na aba **Settings** (Configurações)

3. No menu lateral esquerdo, clique em **Pages**

4. Em **Source** (Origem), selecione:
   - **Branch**: `main`
   - **Folder**: `/ (root)`

5. Clique em **Save**

6. Aguarde alguns minutos (geralmente 1-3 minutos)

7. A página será publicada em: `https://j0aod3v.github.io/xadrezPAA/`

## 🎯 Como Usar a Aplicação Web

A interface permite:

✅ **Ajustar o tamanho do tabuleiro** (4×4 até 12×12)
✅ **Mudar a semente** (número da matrícula)
✅ **Alterar o percentual de obstáculos** (0% a 30%)
✅ **Executar o backtracking** direto no navegador
✅ **Visualizar o tabuleiro** com cores e símbolos
✅ **Ver estatísticas** (peças, obstáculos, tempo de execução)

## 📱 Recursos da Interface

- **Responsiva**: Funciona em celular, tablet e desktop
- **Visual moderno**: Gradientes, animações e design profissional
- **Execução no navegador**: Não precisa instalar Python
- **Interativa**: Permite testar diferentes configurações
- **Rápida**: Pyodide executa Python compilado em WebAssembly

## 🎨 Características Visuais

- ♛ Amazona representada por símbolo de rainha dourada
- 🚧 Obstáculos marcados claramente
- 🎨 Tabuleiro com cores xadrez tradicionais
- 📊 Cards de estatísticas destacados
- ⚡ Animações suaves ao posicionar peças

## 🔧 Tecnologias Utilizadas

- **HTML5**: Estrutura da página
- **CSS3**: Design responsivo e moderno
- **JavaScript**: Lógica de interface
- **Pyodide**: Python no navegador (WebAssembly)
- **GitHub Pages**: Hospedagem gratuita

## 📝 Notas Importantes

1. **Primeira execução**: Pode demorar ~5 segundos para carregar o Pyodide
2. **Tabuleiros grandes**: N > 10 pode demorar mais tempo para executar
3. **Compatibilidade**: Funciona em todos os navegadores modernos (Chrome, Firefox, Safari, Edge)
4. **Offline**: Requer internet apenas na primeira visita (depois fica em cache)

## 🎓 Para a Apresentação

Você pode usar essa interface durante a apresentação para:

1. Demonstrar o funcionamento com diferentes sementes
2. Mostrar como o número de peças muda com o tamanho do tabuleiro
3. Explicar o impacto dos obstáculos
4. Executar ao vivo quando o professor mudar os parâmetros

## 🔗 Links Úteis

- **Repositório**: https://github.com/J0aoD3v/xadrezPAA
- **GitHub Pages** (após ativar): https://j0aod3v.github.io/xadrezPAA/
- **Documentação Pyodide**: https://pyodide.org/

---

Desenvolvido por João CFMC | Trabalho de PAA 2025
