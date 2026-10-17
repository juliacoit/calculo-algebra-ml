# Semana de 8/fev · Marco 3

[Fase 3 — Gradientes e decomposições](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-3-gradientes-e-svd/2027-02-08-posto-baixo-gradient-check/)

## Conteúdo

aproximação de posto baixo pela SVD truncada (intuição do teorema de Eckart-Young); Taylor de 1ª ordem em várias variáveis, f(x + h) ≈ f(x) + ∇f·h.

## Exercícios

aproximação de posto 1 de uma matriz 2×2 a partir da SVD feita à mão.

## Conferência no código

O plano não tem conferência no código nesta semana.

## Aplicação em ML/IA

**Aplicação em ML/IA — conferir gradientes e comprimir com SVD (Marco 3):**

1. Faça o gradient check da rede: compare cada derivada com a diferença central (erro relativo abaixo de 1e-5).
2. Comprima uma imagem em tons de cinza com SVD de posto 5, 20 e 50 e meça o erro de cada uma.
3. Aplique PCA via SVD a embeddings de cerca de 100 palavras e plote em 2D.

**O que observar:** o gradient check é o teste padrão para provar que um backprop escrito à mão está certo. Na imagem, poucos valores singulares já guardam a maior parte da informação.
