# AL4 · Diagonalização

**Fonte:** Callioli, diagonalização

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

A é diagonalizável se e só se tem n autovetores LI; A = PDP⁻¹ com os autovetores nas colunas de P e os autovalores em D; critérios (n autovalores distintos bastam; em geral, multiplicidade geométrica = algébrica para todo autovalor); potências Aⁿ = PDⁿP⁻¹; matrizes simétricas reais são sempre diagonalizáveis com P ortogonal (só o enunciado; a prova volta na Fase 3).

## Exercícios

decidir se 4 matrizes são diagonalizáveis; achar P e D; calcular A¹⁰ por PD¹⁰P⁻¹.

## Conferência no código

**Conferência no código — Fibonacci por diagonalização:**

1. Escreva a recorrência como (Fₙ₊₁, Fₙ) = A·(Fₙ, Fₙ₋₁), com A = [[1, 1], [1, 0]].
2. Diagonalize A à mão: os autovalores são (1 ± √5)/2.
3. Calcule F₃₀ por PD³⁰P⁻¹ e compare com um laço simples (F₃₀ = 832 040).
4. Tente diagonalizar [[1, 1], [0, 1]]: `np.linalg.eig` devolve dois autovetores praticamente iguais, e P fica quase singular. Confirme à mão que ela não é diagonalizável.

## Aplicação em ML/IA

**Aplicação em ML/IA — PCA em embeddings de frases.** Objetivo: diagonalizar a matriz de covariância para reduzir vetores de 384 dimensões a 2, e ver se o significado sobrevive.

1. Aquecimento em 2D: gere 200 pontos alongados com `np.random.randn(200, 2) @ np.array([[3, 0], [1, 0.5]])`, centralize, calcule C = XᵀX/199 e diagonalize C = PDPᵀ. Plote os pontos e os autovetores: o de maior autovalor aponta para onde a nuvem é mais comprida.
2. Escreva cerca de 40 frases curtas em português sobre 4 temas (por exemplo: répteis, anfíbios, culinária e futebol), 10 por tema.
3. Gere os embeddings com `sentence-transformers` (modelo `paraphrase-multilingual-MiniLM-L12-v2`, vetores de 384 dimensões).
4. Centralize, calcule a covariância 384×384 e pegue os 2 autovetores de maior autovalor com `np.linalg.eigh`.
5. Projete cada frase nesses 2 autovetores e plote em 2D, uma cor por tema.
6. Calcule a fração da variância explicada: (λ₁ + λ₂) / Σλ.

## O que observar

os temas tendem a formar grupos mesmo usando 2 de 384 direções. Pᵀ = P⁻¹ porque a covariância é simétrica. Uma fração explicada baixa mostra que o significado está espalhado por muitas direções.
