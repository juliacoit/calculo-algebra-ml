# C10 · Técnicas de integração e aplicações da integral (Ávila cap. 11)

**Fonte:** Ávila, cap. 11

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

substituição; integração por partes; potências de funções trigonométricas; substituição trigonométrica (substituição inversa); funções racionais por frações parciais. Aplicações do programa: área entre curvas, volumes de sólidos de revolução, comprimento de arco e valor médio de uma função.

## Exercícios

Ávila 11.1 a 11.6; pelo menos 2 integrais de cada técnica; áreas e volumes da lista da disciplina.

## Conferência no código

**Conferência no código — técnicas conferidas:**

1. Resolva à mão uma integral de cada técnica e compare com `sympy.integrate`.
2. Confira o valor de cada integral definida com `scipy.integrate.quad`.
3. Calcule a área entre y = x e y = x² em [0, 1] (1/6) à mão e pela soma de Riemann.
4. Calcule o valor médio de sen x em [0, π] pela integral (2/π) e compare com a média de 10 000 pontos sorteados no intervalo.

## Aplicação em ML/IA

**Aplicação em ML/IA — tempo de espera e máxima verossimilhança.** Objetivo: calcular média e variância de uma distribuição com integração por partes e ajustar o modelo aos dados.

1. Use a densidade exponencial f(t) = λ·e^(−λt) para t ≥ 0, por exemplo o tempo entre dois registros de uma espécie num ponto de escuta. Confira à mão que a imprópria ∫₀^∞ f(t) dt vale 1.
2. Por partes: E[T] = ∫₀^∞ t·λ·e^(−λt) dt = 1/λ.
3. Por partes duas vezes: E[T²] = 2/λ², então a variância é 1/λ².
4. Simule 100 000 tempos com `np.random.exponential(1/λ)` e compare média e variância com as fórmulas.
5. Máxima verossimilhança: a log-verossimilhança de n tempos é ℓ(λ) = n·ln λ − λ·Σtᵢ. Derive, iguale a zero e mostre que o melhor λ é 1/média (usa C6 e C7). Confira nos dados simulados.
6. Calcule P(T > t) = e^(−λt) pela integral e compare com a fração simulada para 3 valores de t.

## O que observar

integrais por partes calculam esperanças, e "ajustar um modelo" é maximizar a log-verossimilhança. A regressão logística da Fase 2 é a mesma ideia com mais parâmetros.
