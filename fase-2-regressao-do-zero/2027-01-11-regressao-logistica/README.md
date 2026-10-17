# Semana de 11/jan · Marco 2: regressão logística

[Fase 2 — Regressão do zero](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-2-regressao-do-zero/2027-01-11-regressao-logistica/)

## Conteúdo

derivadas de log e da sigmoide; perda logística L = −[y·log p + (1 − y)·log(1 − p)], com p = σ(w·x).

## Exercícios

derive à mão ∂L/∂w e simplifique até chegar a (p − y)·x.

## Conferência no código

O plano não tem conferência no código nesta semana.

## Aplicação em ML/IA

**Aplicação em ML/IA — classificador de sentimento do zero:**

1. Use um conjunto pequeno de frases rotuladas como positivas ou negativas e transforme cada frase num vetor de contagens de palavras (bag-of-words).
2. Implemente em NumPy a previsão p, a perda L e o gradiente (p − y)·x.
3. Treine por gradiente descendente e plote a perda a cada época.
4. Compare a acurácia com a de `LogisticRegression` do scikit-learn no mesmo conjunto.

5. Liste as 10 palavras com maior peso positivo e as 10 com maior peso negativo e confira se fazem sentido.

**O que observar:** o gradiente (p − y)·x tem a mesma forma do gradiente da regressão linear, (ŷ − y)·x. Só a função de saída mudou.
