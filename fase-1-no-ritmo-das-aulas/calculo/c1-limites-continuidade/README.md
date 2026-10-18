# C1 · Limites e continuidade (Ávila 4.2; revisão)

**Fonte:** Ávila, 4.2

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

noção intuitiva de limite; limites laterais e existência do limite; propriedades operatórias; continuidade e tipos de descontinuidade; Teorema do Valor Intermediário; limites infinitos e limites no infinito; assíntotas verticais e horizontais.

## Exercícios

Ávila 4.2; limites com fatoração e com conjugado; limites laterais com módulo; assíntotas de 3 funções racionais.

## Conferência no código

**Conferência no código — limites pela tabela:**

1. Para um limite feito à mão, monte a tabela de f(a − h) e f(a + h) com h = 10⁻¹, 10⁻², …, 10⁻⁶ e confira os dois lados (o mesmo teste da folha de consulta: x = a ± 0,001).
2. Confira com `sympy.limit`, inclusive os laterais (`dir='+'` e `dir='-'`).
3. Plote uma função racional com suas assíntotas desenhadas em tracejado.
4. Use o Teorema do Valor Intermediário na bisseção: ache a raiz de x³ − x − 1 em [1, 2] com erro menor que 10⁻⁶, dividindo o intervalo ao meio a cada passo.

## Aplicação em ML/IA

**Aplicação em ML/IA — a temperatura de um modelo de linguagem.** Objetivo: ver que o "criativo" e o "determinístico" de um LLM são dois limites da mesma função.

1. Suponha que o modelo deu os escores z = (2,0; 1,0; 0,5; −1,0) para 4 palavras candidatas.
2. Implemente softmax(z/T), em que a probabilidade da palavra i é e^(zᵢ/T) dividido pela soma dos e^(zⱼ/T), e calcule para T = 5; 2; 1; 0,5; 0,1; 0,01.
3. À mão: mostre que, quando T → 0⁺, a probabilidade da maior palavra tende a 1 e as outras a 0 (divida tudo por e^(z_max/T) e use o limite de e^(−c/T) com c > 0). Mostre que, quando T → ∞, todas tendem a 1/4.
4. Plote as 4 probabilidades contra T, com T em escala logarítmica.
5. Sorteie 20 "próximas palavras" com T = 0,2 e com T = 2 e compare a variedade.
6. Calcule os limites de ±∞ da sigmoide e da tanh e verifique que a ReLU, max(0, x), é contínua em 0.

## O que observar

a temperatura que você ajusta num chatbot é esse parâmetro T. Temperatura baixa se aproxima do limite T → 0 (sempre a palavra mais provável); temperatura alta, do limite T → ∞ (sorteio uniforme).
