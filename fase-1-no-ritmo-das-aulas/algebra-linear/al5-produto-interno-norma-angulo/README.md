# AL5 · Produto interno, norma e ângulo

**Fonte:** Callioli, produto interno, norma e ângulo

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

axiomas do produto interno; o produto usual em ℝⁿ e outros (⟨u, v⟩ = uᵀMv com M simétrica definida positiva; ⟨f, g⟩ = ∫₀¹ f(x)g(x) dx em polinômios); norma e distância; desigualdade de Cauchy-Schwarz e desigualdade triangular; ângulo entre vetores; ortogonalidade e teorema de Pitágoras.

## Exercícios

verificar se uma fórmula define produto interno; normas, distâncias e ângulos em ℝ³ e em polinômios; provar Pitágoras para vetores ortogonais.

## Conferência no código

**Conferência no código — normas, ângulos e Cauchy-Schwarz:**

1. Confira as normas e os ângulos feitos à mão com `np.linalg.norm` e `np.arccos`.
2. Teste |⟨u, v⟩| ≤ ‖u‖‖v‖ em 1000 pares aleatórios e ache o par mais próximo da igualdade (vetores quase paralelos).
3. Calcule ⟨f, g⟩ = ∫₀¹ f g dx para dois polinômios com `sympy.integrate` e compare com a conta à mão.
4. Use ⟨u, v⟩ = uᵀMv com M = [[1, 2], [2, 1]] e ache um u com ⟨u, u⟩ < 0: M não é definida positiva, então não define produto interno.

## Aplicação em ML/IA

**Aplicação em ML/IA — vizinhos mais próximos (k-NN).** Objetivo: ver que escolher o produto interno é escolher o que "parecido" quer dizer para um classificador.

1. Carregue `load_iris` (150 flores, 4 medidas em cm) e separe 70% para treino e 30% para teste.
2. Implemente o k-NN com k = 5: para cada flor de teste, ache as 5 mais próximas pela distância euclidiana e vote a espécie. Calcule a acurácia.
3. Multiplique uma das medidas por 100 (como se ela estivesse numa unidade 100 vezes menor) e repita: a acurácia cai, porque essa coordenada domina a distância.
4. Padronize as 4 medidas (média 0, desvio 1) e recupere a acurácia. Isso equivale a usar o produto interno uᵀMv com M diagonal.
5. Com os embeddings de frases de AL4, compare o k-NN por distância euclidiana e por cosseno, antes e depois de normalizar os vetores.

## O que observar

com vetores de norma 1, ‖u − v‖² = 2 − 2·cos θ, então distância e cosseno dão o mesmo ranking. Prove essa igualdade à mão a partir de ‖u − v‖² = ⟨u − v, u − v⟩.
