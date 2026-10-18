# C5 · Derivadas trigonométricas, inversas e formas indeterminadas (Ávila 6.3 a 6.5)

**Fonte:** Ávila, 6.3 a 6.5

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

derivada do seno pela definição, usando o limite fundamental e a soma de arcos; derivadas de cosseno, tangente, cotangente, secante e cossecante; regra da cadeia com funções trigonométricas; formas indeterminadas 0/0, ∞/∞ e ∞ − ∞; arco-seno, arco-tangente e arco-secante, com domínios e derivadas (por exemplo, (arctg x)′ = 1/(1 + x²)).

## Exercícios

Ávila 6.3 a 6.5; derivar sen(x²), cos³(2x) e arctg(√x); derivada de arcsen x pela regra da inversa (C3).

## Conferência no código

**Conferência no código — derivadas trigonométricas:**

1. Calcule (sen(x + h) − sen x)/h em vários x com h = 10⁻⁶ e compare com cos x num gráfico.
2. Plote arctg x junto com 1/(1 + x²) e confira que a inclinação da primeira é o valor da segunda.
3. Confira 5 derivadas feitas à mão com `sympy.diff`.

## Aplicação em ML/IA

**Aplicação em ML/IA — sazonalidade de vocalização de anuros.** Objetivo: ajustar uma senoide a dados mensais por gradiente descendente, derivando cada passo à mão.

1. Simule 36 meses de contagens de registros de vocalização: y = 20 + 15·sen(2πt/12) + 8·cos(2πt/12) + ruído. (São dados inventados; se tiver uma série real do trabalho, use ela.)
2. Use o modelo ŷ = a·sen(ωt) + b·cos(ωt) + c, com ω = 2π/12 fixo, e a perda L = média de (ŷ − y)².
3. Derive à mão ∂L/∂a, ∂L/∂b e ∂L/∂c. Cada uma é uma derivada comum, com as outras letras tratadas como constantes.
4. Treine por gradiente descendente e plote os dados com a curva ajustada.
5. Escreva o resultado como A·sen(ωt + φ), com A = √(a² + b²) e φ dado pela arco-tangente (use `np.arctan2(b, a)`), e calcule em que mês fica o pico.
6. Deixe ω livre: pela cadeia, ∂ŷ/∂ω = a·t·cos(ωt) − b·t·sen(ωt). Plote L como função de ω e veja os vários mínimos locais: o ponto de partida decide onde o treino para.

## O que observar

codificar mês, hora ou dia da semana como seno e cosseno é padrão em ML para tempo cíclico. A arco-tangente recupera a fase, que é o que interessa biologicamente: a época do pico.
