# Álgebra Linear · Autovalores, autovetores e diagonalização

[Fase 1 — No ritmo das aulas](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-1-no-ritmo-das-aulas/al-2-autovalores-diagonalizacao/)

## Conteúdo

Av = λv; polinômio característico det(A − λI) = 0; autoespaço; multiplicidade algébrica e geométrica; diagonalização A = PDP⁻¹ e quando ela é possível.

## Exercícios

autovalores e autovetores de matrizes 2×2 e 3×3; decidir se uma matriz é diagonalizável; calcular Aⁿ por PDⁿP⁻¹.

## Conferência no código

**Conferência no código — a direção em que os dados mais variam:**

1. Gere 200 pontos alongados: `X = np.random.randn(200, 2) @ np.array([[3, 0], [1, 0.5]])`.
2. Subtraia a média de cada coluna e calcule a matriz de covariância `C = X.T @ X / 199`.
3. Resolva det(C − λI) = 0 à mão (é uma equação do 2º grau) e ache os autovetores. Confira com `np.linalg.eigh(C)`.
4. Plote os pontos e os dois autovetores saindo da origem: o de maior autovalor aponta para onde a nuvem é mais comprida.
5. Verifique numericamente C = PDPᵀ. Aqui Pᵀ = P⁻¹ porque C é simétrica (isso volta na Fase 3).

## Aplicação em ML/IA

**Aplicação em ML/IA — PCA em embeddings de frases.** Objetivo: reduzir vetores de 384 dimensões para 2 usando os autovetores da covariância, e ver se o significado sobrevive.

1. Escreva cerca de 40 frases curtas em português sobre 4 temas (por exemplo: répteis, anfíbios, culinária e futebol), 10 por tema.
2. Gere os embeddings com `sentence-transformers` (modelo `paraphrase-multilingual-MiniLM-L12-v2`, que devolve vetores de 384 dimensões).
3. Centralize e calcule a covariância 384×384, como na conferência.
4. Pegue os 2 autovetores de maior autovalor com `np.linalg.eigh` e projete cada frase neles (produto da matriz de dados pelos 2 autovetores).
5. Plote as frases em 2D, uma cor por tema.
6. Calcule a fração da variância explicada: (λ₁ + λ₂) / Σλ.

**O que observar:** os temas tendem a formar grupos mesmo com 2 de 384 direções. Uma fração explicada baixa mostra que o significado está espalhado por muitas direções.
