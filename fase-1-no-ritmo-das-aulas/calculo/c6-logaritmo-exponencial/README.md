# C6 · Logaritmo e exponencial (Ávila cap. 7)

**Fonte:** Ávila, cap. 7

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

logaritmo natural e suas propriedades; o número e; derivadas de ln x, eˣ, aˣ e logₐ x; derivada logarítmica; funções hiperbólicas, incluindo a tanh; taxa de variação relativa e crescimento exponencial.

## Exercícios

Ávila 7.1 a 7.4; derivadas que misturam ln, exponencial e cadeia; limites que definem e, como (1 + 1/n)ⁿ.

## Conferência no código

**Conferência no código — e, ln e tanh:**

1. Tabele (1 + 1/n)ⁿ para n = 10, 10², …, 10⁸ e compare com `np.e`. Veja o arredondamento estragar o resultado para n grande.
2. Confira 5 derivadas feitas à mão com `sympy.diff`.
3. Prove à mão que tanh x = 2σ(2x) − 1 e confira com `np.tanh` em 100 pontos.

## Aplicação em ML/IA

**Aplicação em ML/IA — log-verossimilhança, entropia cruzada e perplexidade.** Objetivo: ver por que modelos de linguagem trabalham com logaritmos e calcular a métrica clássica deles.

1. Multiplique 1000 probabilidades iguais a 0,01: o resultado vira 0.0 (estouro por baixo). Some os logaritmos: dá 1000·ln 0,01 ≈ −4605,17, sem problema.
2. Monte um corpus de umas 2000 palavras com textos públicos sobre herpetofauna e um modelo de unigramas, p(w) = contagem de w / total. Para palavras que não aparecem, use a suavização de Laplace: (contagem + 1)/(total + tamanho do vocabulário).
3. Calcule a log-verossimilhança de uma frase nova como a soma de ln p(w).
4. Calcule a entropia cruzada H = −(1/n)·Σ ln p(w) e a perplexidade e^H para uma frase sobre o tema e uma sobre futebol. A do tema deve ser menor.
5. Plote −ln p para p em (0, 1]. A derivada −1/p explode perto de 0: errar com muita confiança custa caro.
6. Prove à mão que ln Σ e^(zᵢ) = m + ln Σ e^(zᵢ − m), com m = max zᵢ, e teste com z = (1000, 1001): a fórmula direta estoura e esta não.

## O que observar

o logaritmo transforma produto em soma, e isso torna o treino numérico possível. Perplexidade é a exponencial da entropia cruzada: quanto menor, menos o modelo se surpreende com o texto.
