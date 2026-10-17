# Cálculo · Aplicações da derivada

[Fase 1 — No ritmo das aulas](../) · Notebooks: [`conferencia-a-gradiente-descendente.ipynb`](conferencia-a-gradiente-descendente.ipynb) · [`conferencia-b-taylor.ipynb`](conferencia-b-taylor.ipynb) · [`conferencia-c-sigmoide.ipynb`](conferencia-c-sigmoide.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-1-no-ritmo-das-aulas/calc-1-aplicacoes-da-derivada/)

## Conteúdo

taxa de variação; pontos críticos e testes da 1ª e da 2ª derivada; máximos e mínimos; teorema do valor médio; crescimento, concavidade e esboço de gráficos; regra de L'Hôpital; polinômio de Taylor.

## Exercícios

problemas de otimização com enunciado; esboço completo de 2 ou 3 gráficos; limites indeterminados por L'Hôpital; polinômios de Taylor de eˣ, ln(1 + x) e sen x.

## Conferência no código

**Conferência no código A — gradiente descendente em uma variável:**

1. Para f(x) = (x − 3)² + 1, ache o mínimo à mão igualando f′(x) a zero.
2. Implemente a repetição x ← x − η·f′(x), partindo de x = −5, por 50 passos.
3. Teste η = 0,01, 0,1, 0,9 e 1,1 e plote x a cada passo. Com 1,1 o processo diverge; explique por quê usando f″(x) = 2.
4. Repita com f(x) = x⁴ − 3x² + x, que tem dois mínimos locais, e veja que o ponto de partida decide onde o processo para.

**Conferência no código B — polinômio de Taylor:**

1. Plote eˣ junto com seus polinômios de Taylor de grau 1, 2 e 3 em torno de 0.
2. Meça o erro de cada um em x = 0,1 e x = 1 e compare com o termo de resto.
3. Use o grau 1 para mostrar que f(x − η·f′(x)) ≈ f(x) − η·f′(x)²: por isso um passo pequeno contra a derivada diminui f.

**Conferência no código C — esboço da sigmoide:**

1. À mão, faça o estudo completo de σ(x) = 1 / (1 + e⁻ˣ): limites no infinito, derivada σ′ = σ(1 − σ), crescimento e concavidade.
2. Plote σ e σ′ e confira o esboço. Note que σ′ fica perto de zero para |x| > 5: é o "gradiente que some" em redes neurais.

## Aplicação em ML/IA

**Aplicação em ML/IA — treinar um modelo de um parâmetro.** Objetivo: ver que "treinar" é minimizar uma função de uma variável, e que a 2ª derivada limita a taxa de aprendizado.

1. Gere 50 pontos com y = 3x + ruído.
2. Use o modelo ŷ = w·x e a perda L(w) = média de (y − w·x)². Note que L é uma parábola em w.
3. Ache o w ótimo à mão fazendo L′(w) = 0.
4. Treine por gradiente descendente usando a L′(w) que você derivou. Plote L(w) e marque cada passo sobre a curva.
5. Calcule L″(w) e confirme que o treino diverge quando η passa de 2/L″.
6. Troque para classificação com ŷ = σ(w·x), comece com w = 20 e veja o treino quase não sair do lugar: é a saturação da Conferência C.

**O que observar:** o w do gradiente descendente converge para o mesmo w da conta à mão. O limite de η sai direto da 2ª derivada.
