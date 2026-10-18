# C8 · L'Hôpital, concavidade, esboço de gráficos e Taylor (Ávila cap. 9)

**Fonte:** Ávila, cap. 9 (Taylor: Stewart, se o Ávila não cobrir)

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

regra de L'Hôpital para 0/0 e ∞/∞, e as formas 0·∞, ∞ − ∞, 1^∞ e 0⁰ reescritas para ela; concavidade e pontos de inflexão; roteiro completo de esboço (domínio, limites, assíntotas, f′, f″); polinômio de Taylor e o termo de resto (no programa da disciplina; use o Stewart se o Ávila não cobrir).

## Exercícios

Ávila 9.1 e 9.2; esboço completo de 2 ou 3 funções; polinômios de Taylor de eˣ, ln(1 + x) e sen x em torno de 0.

## Conferência no código

**Conferência no código — Taylor e esboço da sigmoide:**

1. Plote eˣ junto com seus polinômios de Taylor de grau 1, 2 e 3 em torno de 0 e meça o erro em x = 0,1 e x = 1.
2. Use o grau 1 para mostrar que f(x − η·f′(x)) ≈ f(x) − η·f′(x)²: por isso um passo pequeno contra a derivada diminui f (liga com C7).
3. Faça à mão o esboço completo de σ(x) = 1/(1 + e⁻ˣ) (limites no infinito, σ′ = σ(1 − σ), crescimento, inflexão em 0) e confira no gráfico. Veja que σ′ fica perto de zero para |x| > 5: é o "gradiente que some".

## Aplicação em ML/IA

**Aplicação em ML/IA — entropia: medir a incerteza de um classificador.** Objetivo: estudar por completo a função que mede incerteza em ML, usando L'Hôpital, concavidade e Taylor.

1. Defina a entropia binária H(p) = −p·ln p − (1 − p)·ln(1 − p) para p em (0, 1).
2. À mão: escreva p·ln p como ln p / (1/p) e use L'Hôpital para mostrar que o limite é 0 quando p → 0⁺. É a justificativa da convenção 0·ln 0 = 0 usada em todo código de ML.
3. Calcule H′(p) = ln((1 − p)/p) e H″(p) = −1/(p(1 − p)). Conclua que H é côncava com máximo ln 2 em p = 1/2, e faça o esboço completo.
4. Taylor de grau 2 em torno de 1/2: H(p) ≈ ln 2 − 2(p − 1/2)². Plote as duas e compare o erro em p = 0,4 e p = 0,1.
5. Treine `LogisticRegression` no `load_breast_cancer` do scikit-learn, pegue `predict_proba` no conjunto de teste e calcule H para cada exemplo.
6. Liste os 10 exemplos de maior entropia e confira se são os que o modelo mais erra.

## O que observar

entropia alta significa modelo indeciso. Escolher para rotular os exemplos de maior entropia é a ideia do aprendizado ativo, útil quando rotular dados custa caro, como identificar espécies em gravações.
