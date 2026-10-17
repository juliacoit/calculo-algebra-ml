# Semana de 21/dez · Posto, núcleo e regra da cadeia

[Fase 2 — Regressão do zero](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-2-regressao-do-zero/2026-12-21-posto-nucleo-regra-da-cadeia/)

## Conteúdo

posto por escalonamento; espaço coluna e núcleo de uma matriz; teorema do posto (posto + dimensão do núcleo = número de colunas). Em Cálculo, regra da cadeia em composições de três funções.

## Exercícios

posto e base do núcleo de 3 matrizes 3×4; derivadas de funções como e^(sen(x²)).

## Conferência no código

**Conferência no código — posto e derivada:**

1. Monte uma matriz 5×3 em que a 3ª coluna é a soma das outras duas. Calcule o posto à mão e confira com `np.linalg.matrix_rank`.
2. Ache à mão um vetor v do núcleo e confirme que `A @ v` dá zero.
3. Derive g(w) = σ(3w + 1) pela regra da cadeia e compare com a diferença central (g(w + h) − g(w − h)) / 2h, com h = 1e-5.

## Aplicação em ML/IA

**Aplicação em ML/IA — features redundantes e o autograd.** Objetivo: ver o que o posto diz sobre um conjunto de dados, e confirmar que o PyTorch faz a mesma regra da cadeia que você faz à mão.

1. Carregue `load_diabetes` do scikit-learn (442 pacientes, 10 features) e calcule o posto da matriz X.
2. Acrescente uma 11ª coluna igual a 2 × coluna 1 + coluna 3. Confirme que o posto não sobe e ache o vetor do núcleo que essa coluna cria.
3. Calcule o número de condição de XᵀX (`np.linalg.cond`) antes e depois da coluna extra e veja o salto.
4. Para um neurônio p = σ(w·x + b), escreva ∂p/∂w à mão. Depois calcule com `torch.autograd` e confira que os números batem.

**O que observar:** uma feature que é combinação das outras cria um núcleo não trivial, e o modelo passa a ter infinitas soluções igualmente boas. O autograd é só a regra da cadeia automatizada.
