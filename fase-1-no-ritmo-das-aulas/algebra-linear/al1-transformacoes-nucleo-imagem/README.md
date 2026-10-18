# AL1 · Transformações lineares: definição, núcleo e imagem

**Fonte:** Callioli, transformações lineares

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

definição, T(u + v) = T(u) + T(v) e T(αu) = αT(u); consequência T(0) = 0; exemplos (projeção, rotação, transposição de matrizes, derivação de polinômios de P₃ em P₂); uma TL fica determinada pelos valores numa base; núcleo N(T) e imagem Im(T) como subespaços; T injetora se e só se N(T) = {0}; teorema do núcleo e da imagem, dim V = dim N(T) + dim Im(T); isomorfismo.

## Exercícios

decidir se 5 funções são lineares (inclua uma com "+ 1" e uma com produto de coordenadas); achar T(x, y, z) a partir dos valores de T numa base; base e dimensão de N(T) e de Im(T); decidir se T é injetora, sobrejetora ou isomorfismo. Capítulo de transformações lineares do Callioli.

## Conferência no código

**Conferência no código — núcleo, imagem e dimensão:**

1. Defina T pela matriz de um exercício feito à mão e use `sympy.Matrix` para obter `nullspace()`, `columnspace()` e `rank()`. Compare com suas bases.
2. Confira o teorema: número de colunas = dim N(T) + dim Im(T).
3. Teste a linearidade com 100 pares de vetores aleatórios e mostre que T(x) = Ax + b falha quando b ≠ 0 (basta olhar T(0)).
4. Escreva a derivação de P₃ em P₂ como uma matriz 3×4 agindo nos coeficientes; aplique a 1 + 2x + 3x² + 4x³ e ache o núcleo (os polinômios constantes).

## Aplicação em ML/IA

**Aplicação em ML/IA — features redundantes.** Objetivo: ler um conjunto de dados como uma transformação linear e ver o que o núcleo significa para um modelo.

1. Carregue `load_diabetes` do scikit-learn: X tem 442 pacientes e 10 features. Pense em X como uma TL de ℝ¹⁰ em ℝ⁴⁴² que leva pesos w em previsões Xw.
2. Calcule o posto (dim Im) e deduza dim N pelo teorema do núcleo e da imagem.
3. Acrescente uma 11ª coluna igual a 2 × coluna 1 + coluna 3. Confirme que o posto não sobe e ache à mão o vetor n que gera o núcleo.
4. Pegue qualquer w e mostre que X·w e X·(w + t·n) dão as mesmas previsões para t = 1, 10 e 1000.
5. Calcule o número de condição de XᵀX (`np.linalg.cond`) antes e depois da coluna extra.

## O que observar

um núcleo não trivial faz o modelo ter infinitos pesos igualmente bons, e os coeficientes deixam de ter significado. A regularização da Fase 2 (semana de 4/jan) resolve isso.
