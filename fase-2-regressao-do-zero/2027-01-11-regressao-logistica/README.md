# Semana de 11/jan · Marco 2: regressão logística

**Fonte:** 3Blue1Brown, *Essence of Calculus*; Deisenroth, Faisal e Ong, *Mathematics for Machine Learning* (cap. 2–5)

[Fase 2 — Regressão do zero](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

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

## O que observar

o gradiente (p − y)·x tem a mesma forma do gradiente da regressão linear, (ŷ − y)·x. Só a função de saída mudou.

## Marco 2

**Marco 2 · até 17/jan — Regressão logística do zero.** Classificador de sentimento com bag-of-words e gradiente descendente em NumPy. Critério: derivar o gradiente à mão e chegar a uma acurácia próxima à do scikit-learn no mesmo conjunto.

Um marco só conta como feito quando o código roda e você explica a matemática dele sem consultar nada.
