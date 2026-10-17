# Semana de 18/jan · Teorema espectral e derivadas parciais

[Fase 3 — Gradientes e decomposições](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-3-gradientes-e-svd/2027-01-18-teorema-espectral-derivadas-parciais/)

## Conteúdo

matrizes simétricas têm autovalores reais e autovetores ortogonais, então A = QΛQᵀ; formas quadráticas vᵀAv. Em Cálculo, funções de duas variáveis, curvas de nível e derivadas parciais.

## Exercícios

diagonalizar 2 matrizes simétricas 2×2 por base ortonormal; derivadas parciais de 5 funções de duas variáveis.

## Conferência no código

**Conferência no código — a forma de uma função vista pelos autovalores:**

1. Para f(x, y) = x² + 10y², calcule ∂f/∂x e ∂f/∂y à mão.
2. Plote as curvas de nível com `plt.contour`.
3. Escreva f como vᵀAv, com A simétrica. Relacione os autovalores de A (1 e 10) ao formato alongado das elipses.

## Aplicação em ML/IA

**Aplicação em ML/IA — a superfície de perda de uma regressão.** Objetivo: ver que a perda de um modelo real é uma forma quadrática e que padronizar as features muda os autovalores dela.

1. Pegue uma única feature de `load_diabetes` e o modelo ŷ = w·x + b. A perda L(w, b) é uma função de duas variáveis.
2. Plote as curvas de nível de L sobre uma grade de valores de w e b.
3. A matriz de segundas derivadas (a Hessiana) dessa perda é 2·AᵀA/n, com A = [x, 1]. Calcule-a, confirme que é simétrica e ache seus autovalores.
4. Padronize x (média 0, desvio 1), refaça as curvas e os autovalores e compare a razão entre o maior e o menor.

**O que observar:** sem padronizar, as elipses ficam muito alongadas (razão grande entre autovalores). Padronizar as deixa quase circulares; é por isso que quase todo pipeline de ML padroniza as features.
