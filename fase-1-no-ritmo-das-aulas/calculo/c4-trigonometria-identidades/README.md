# C4 · Funções trigonométricas, identidades e limite fundamental (Ávila 6.1 e 6.2)

**Fonte:** Ávila, 6.1 e 6.2

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

radiano e círculo trigonométrico; seno, cosseno, tangente, cotangente, secante e cossecante; gráficos, período e paridade; a função sen(1/x) perto de 0; identidades (sen²x + cos²x = 1, 1 + tg²x = sec²x); fórmulas de soma e diferença de arcos e do arco duplo; limite fundamental sen x / x → 1 quando x → 0, e (1 − cos x)/x → 0.

## Exercícios

Ávila 6.1 e 6.2; provar 4 identidades; calcular limites como sen(3x)/x e tg x / x usando o limite fundamental.

## Conferência no código

**Conferência no código — identidades e o limite fundamental:**

1. Plote as seis funções em [−2π, 2π], marcando período e assíntotas.
2. Teste sen(a + b) = sen a·cos b + cos a·sen b e cos(a + b) = cos a·cos b − sen a·sen b em 1000 pares aleatórios.
3. Tabele sen x / x e (1 − cos x)/x para x = 10⁻¹, …, 10⁻⁶.
4. Monte a matriz de rotação R(θ) = [[cos θ, −sen θ], [sen θ, cos θ]] e confira que R(a)·R(b) = R(a + b). Multiplique à mão e veja que as entradas são as fórmulas de soma de arcos (liga com AL2).

## Aplicação em ML/IA

**Aplicação em ML/IA — a codificação posicional do Transformer.** Objetivo: ver como seno e cosseno dizem ao modelo em que posição da frase cada palavra está, e por que as fórmulas de soma de arcos são o motivo de isso funcionar.

1. Para d = 16 e posições 0 a 49, monte a matriz PE de 50×16 com PE(pos, 2i) = sen(pos/10000^(2i/d)) e PE(pos, 2i + 1) = cos(pos/10000^(2i/d)).
2. Plote a matriz como mapa de calor: as primeiras colunas oscilam rápido e as últimas, devagar.
3. À mão: o período da coluna 2i é 2π·10000^(2i/d). Calcule para i = 0 e i = 7.
4. Pelas fórmulas de soma de arcos, mostre que o par (sen(ω(p + k)), cos(ω(p + k))) é uma matriz de rotação que depende só de k aplicada a (sen ωp, cos ωp). Confira para p = 3 e k = 5.
5. Calcule o produto interno PE(p)·PE(q) para vários pares e plote contra |p − q|. Prove à mão que ele é a soma de cos(ωᵢ(p − q)) e, portanto, só depende da distância.

## O que observar

a fórmula de soma de arcos transforma "andar k posições" numa rotação. É a mesma ideia do RoPE, a codificação posicional dos LLMs atuais.
