# C7 · Máximos e mínimos e Teorema do Valor Médio (Ávila cap. 8)

**Fonte:** Ávila, cap. 8

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

extremos locais e absolutos; pontos críticos; extremos de função contínua em intervalo fechado; Teorema de Rolle e Teorema do Valor Médio; funções crescentes e decrescentes; testes da 1ª e da 2ª derivada; problemas de otimização com enunciado.

## Exercícios

Ávila 8.1 a 8.3, com prioridade para os problemas de otimização com enunciado.

## Conferência no código

**Conferência no código — gradiente descendente em uma variável:**

1. Para f(x) = (x − 3)² + 1, ache o mínimo à mão igualando f′(x) a zero.
2. Implemente a repetição x ← x − η·f′(x), partindo de x = −5, por 50 passos.
3. Teste η = 0,01; 0,1; 0,9 e 1,1 e plote x a cada passo. Com 1,1 o processo diverge; explique por quê usando f″(x) = 2.
4. Repita com f(x) = x⁴ − 3x² + x, que tem dois mínimos locais: o ponto de partida decide onde o processo para.

## Aplicação em ML/IA

**Aplicação em ML/IA — treinar um modelo de um parâmetro.** Objetivo: ver que "treinar" é minimizar uma função de uma variável, e que as derivadas limitam a taxa de aprendizado.

1. Gere 50 pontos com y = 3x + ruído.
2. Use o modelo ŷ = w·x e a perda L(w) = média de (y − w·x)². Note que L é uma parábola em w.
3. Ache o w ótimo à mão fazendo L′(w) = 0.
4. Treine por gradiente descendente usando a L′(w) que você derivou. Plote L(w) e marque cada passo sobre a curva.
5. Calcule L″(w) e confirme que o treino diverge quando η passa de 2/L″.
6. Pelo TVM, |σ(a) − σ(b)| ≤ M·|a − b|, com M o máximo de σ′. Ache M = 1/4 à mão e teste a desigualdade em 10 000 pares aleatórios.

## O que observar

o w do gradiente descendente converge para o mesmo w da conta à mão, e o limite de η sai da 2ª derivada. O TVM garante que a sigmoide nunca amplia diferenças mais que 4 vezes; é o tipo de limite usado para analisar a estabilidade do treino.
