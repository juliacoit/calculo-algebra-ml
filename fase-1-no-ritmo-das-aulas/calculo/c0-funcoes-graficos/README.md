# C0 · Funções e gráficos (Ávila cap. 3; revisão)

**Fonte:** Ávila, cap. 3

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

o que caracteriza uma função; domínio, contradomínio e imagem; gráfico; translação de gráficos (f(x − a) + b) e mudança de escala (f(kx), c·f(x)); a parábola, mais aberta ou mais fechada e transladada, com vértice por completar quadrado; y = √x; a hipérbole y = k/x e suas translações. Do programa da disciplina: operações com funções, funções compostas, inversas (e quando existem) e implícitas.

## Exercícios

Ávila 3.1 a 3.3; domínio e imagem de 5 funções; f∘g e g∘f para dois pares de funções, com domínios; inversa de f(x) = (2x + 1)/(x − 3), com domínio e imagem; vértice e esboço de 3 parábolas; assíntotas de hipérboles transladadas.

## Conferência no código

**Conferência no código — gráficos, translações e inversas:**

1. Plote f(x) = x² junto com f(x − 2), f(x) + 1, f(2x) e 3f(x) e confira, para cada uma, a regra de translação ou de escala que você aplicou à mão.
2. Para uma parábola de exercício, complete o quadrado à mão e marque o vértice no gráfico.
3. Plote f e a inversa que você calculou, junto com a reta y = x: os gráficos são reflexos um do outro. Confira f(f⁻¹(x)) = x em 100 pontos.
4. Plote x² + y² = 25 e veja que ela não é gráfico de uma função; separe em dois ramos, y = √(25 − x²) e y = −√(25 − x²).

## Aplicação em ML/IA

**Aplicação em ML/IA — montar curvas com funções de ativação transladadas.** Objetivo: ver que uma rede neural de uma camada é uma soma de cópias transladadas e esticadas de uma mesma função, e que isso basta para aproximar uma curva.

1. Plote σ(k(x − a)) para k = 1, 5 e 50 e a = −1, 0 e 2. Identifique a translação (a) e a mudança de escala (k): com k grande, a sigmoide vira um degrau em x = a.
2. Monte um "degrau de largura finita" com h(x) = σ(k(x − a)) − σ(k(x − b)) e explique à mão por que, com k grande, h vale perto de 1 entre a e b e perto de 0 fora.
3. Aproxime a parábola f(x) = x² em [−2, 2] somando 10 desses degraus, cada um com a altura de f no seu centro. Plote e meça o erro máximo com 10, 20 e 50 degraus.
4. Repita com a ReLU: combinações de ReLU(x − a) dão funções lineares por partes. Escolha à mão 5 pontos de quebra e as inclinações que fazem a soma passar pela parábola nesses pontos.
5. Plote σ e a logit, ln(p/(1 − p)), com a reta y = x. Anote domínio e imagem de cada uma (ℝ → (0, 1) e o contrário) e confira σ(logit(p)) = p.
6. Lei de Zipf (uma hipérbole): conte as palavras de um texto longo em português, ordene por frequência e plote a frequência contra a posição r. Compare com C/r e veja que, em escala log-log, vira uma reta.

## O que observar

cada neurônio de uma camada oculta é a mesma função transladada e esticada, e a saída da rede é a soma deles. Esse é o teorema da aproximação universal visto com as ferramentas do capítulo 3. A lei de Zipf explica por que poucas palavras dominam qualquer texto, o que afeta como vocabulários de modelos de linguagem são montados.
