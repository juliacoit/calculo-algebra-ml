# Semana de 1/fev · SVD e backpropagation

**Fonte:** Gilbert Strang, MIT 18.06 (SVD); 3Blue1Brown, série *Neural Networks* (backprop); Karpathy, *Neural Networks: Zero to Hero* (micrograd); Deisenroth, Faisal e Ong, *Mathematics for Machine Learning* (cap. 2–5)

[Fase 3 — Gradientes e decomposições](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

decomposição em valores singulares A = UΣVᵀ; valores singulares são as raízes dos autovalores de AᵀA; relação com a diagonalização. Em Cálculo, backpropagation é a regra da cadeia aplicada de trás para frente num grafo de operações.

## Exercícios

SVD de uma matriz 2×2 à mão, via AᵀA; desenhar o grafo de operações de uma rede de 1 neurônio e derivar cada aresta.

## Conferência no código

**Conferência no código — SVD e uma rede pequena:**

1. Confira a SVD feita à mão com `np.linalg.svd`.
2. Monte uma rede de 2 camadas (2 entradas, 8 neurônios ocultos, 1 saída) para separar pontos em dois círculos (`make_circles` do scikit-learn).
3. Escreva cada derivada no papel antes de programar o backprop.

## Aplicação em ML/IA

**Aplicação em ML/IA — tópicos latentes com SVD (LSA).** Objetivo: achar temas em textos sem rótulo nenhum, só com a SVD de uma matriz de palavras.

1. Junte cerca de 150 textos curtos de 3 temas (por exemplo, 50 de cada) e monte a matriz documento × palavra com `TfidfVectorizer` do scikit-learn.
2. Calcule a SVD truncada com k = 3 (`TruncatedSVD` ou `np.linalg.svd` ficando com os 3 primeiros valores singulares).
3. Plote os documentos nas 2 primeiras direções, uma cor por tema (as cores servem só para conferir; o método não as usa).
4. Para cada um dos 3 vetores singulares, liste as 10 palavras de maior peso e dê um nome ao tema.

## O que observar

a SVD agrupa palavras que aparecem juntas nos mesmos documentos. É a ideia por trás dos embeddings, antes das redes neurais.
