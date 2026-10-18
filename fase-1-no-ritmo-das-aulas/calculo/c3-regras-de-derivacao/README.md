# C3 · Regras de derivação, cadeia, implícita e inversa (Ávila cap. 5; revisão)

**Fonte:** Ávila, cap. 5

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

derivadas de soma, produto, quociente e potência; regra da cadeia; derivação implícita; derivada da função inversa, (f⁻¹)′(y) = 1/f′(x) com y = f(x); derivadas de ordem superior.

## Exercícios

Ávila 5.1 a 5.4; derivada implícita de x² + y² = 25 e de xy + y³ = 1; derivada de √x vista como inversa de x².

## Conferência no código

**Conferência no código — regras conferidas:**

1. Derive 6 funções à mão (uma por regra) e compare com `sympy.diff`.
2. Confira as mesmas derivadas num ponto com a diferença central de C2.
3. Para a implícita, plote a curva x² + y² = 25 e a reta tangente em (3, 4) com a inclinação −x/y que você achou.

## Aplicação em ML/IA

**Aplicação em ML/IA — backpropagation de um neurônio.** Objetivo: ver que treinar uma rede é aplicar a regra da cadeia, e que o PyTorch faz a mesma conta que você.

1. Monte o neurônio z = wx + b, p = σ(z) e a perda L = (p − y)². Desenhe no papel o grafo x → z → p → L.
2. À mão: prove σ′(z) = σ(z)(1 − σ(z)) pela regra do quociente e escreva ∂L/∂w = 2(p − y)·σ′(z)·x pela cadeia (e ∂L/∂b, igual sem o x).
3. Implemente a ida (forward) e a volta (backward) em Python puro para x = 2, y = 1, w = 0,5, b = 0.
4. Refaça com `torch.tensor(..., requires_grad=True)` e `L.backward()` e confira que os gradientes são iguais.
5. Treine w e b por 100 passos de gradiente descendente em 50 pontos simulados e plote a perda.
6. A função logit, ln(p/(1 − p)), é a inversa da sigmoide. Calcule sua derivada pela regra da inversa e confira que dá 1/(p(1 − p)).

## O que observar

backpropagation é a regra da cadeia aplicada de trás para frente no grafo. O logit é o valor que o modelo produz antes da sigmoide, e a regra da inversa liga os dois.
