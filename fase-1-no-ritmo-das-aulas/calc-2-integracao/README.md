# Cálculo · Integração e aplicações da integral

[Fase 1 — No ritmo das aulas](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-1-no-ritmo-das-aulas/calc-2-integracao/)

## Conteúdo

primitivas e integral indefinida; integral definida e Teorema Fundamental do Cálculo; substituição, integração por partes, substituição trigonométrica e frações parciais; integrais impróprias; áreas entre curvas, volumes, comprimento de arco e valor médio.

## Exercícios

a lista da disciplina, com prioridade para por partes, frações parciais e impróprias.

## Conferência no código

**Conferência no código — integral como área e como probabilidade:**

1. Implemente a soma de Riemann pelo ponto médio para ∫₀¹ x² dx com n = 10, 100 e 1000 e compare com o valor exato 1/3.
2. Calcule à mão a imprópria ∫₀^∞ e⁻ˣ dx e aproxime no código truncando em 5, 10 e 20.
3. Verifique numericamente que a densidade normal (1/√(2π))·e^(−x²/2) integra perto de 1 em [−10, 10].
4. Calcule o valor médio de sen x em [0, π] pela integral e compare com a média de 10 000 pontos sorteados no intervalo.

## Aplicação em ML/IA

**Aplicação em ML/IA — um classificador bayesiano em uma dimensão.** Objetivo: usar integrais para transformar densidades em probabilidades e medir o erro de um classificador como uma área.

1. Simule o comprimento de 200 indivíduos de duas espécies, cada espécie com distribuição normal de média e desvio diferentes.
2. Estime média e desvio de cada espécie e escreva as duas densidades.
3. Calcule P(a < X < b) para uma espécie pela soma de Riemann e compare com a fração dos dados simulados nesse intervalo.
4. Classifique cada indivíduo pela espécie de maior densidade e ache o ponto de fronteira em que as duas densidades se cruzam.
5. Calcule o erro esperado como a área das caudas que passam da fronteira (duas integrais) e compare com o erro medido nos dados.

**O que observar:** a integral é o que liga um modelo de probabilidade ao número que importa, a chance de errar. Essa é a base de Probabilidade e Estatística A.
