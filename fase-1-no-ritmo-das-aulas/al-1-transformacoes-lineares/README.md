# Álgebra Linear · Transformações lineares e suas matrizes

[Fase 1 — No ritmo das aulas](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-1-no-ritmo-das-aulas/al-1-transformacoes-lineares/)

## Conteúdo

definição de transformação linear, T(u + v) = T(u) + T(v) e T(αv) = αT(v); matriz de T na base canônica e em outra base; composição de transformações como produto de matrizes. Núcleo, imagem e o teorema dim N(T) + dim Im(T) = dim V costumam vir junto; confira se caem na prova.

## Exercícios

decidir se uma função é linear; achar a matriz de T em duas bases diferentes; calcular núcleo e imagem.

## Conferência no código

**Conferência no código — transformações no plano:**

1. Monte uma matriz P de 2 linhas com os vértices de um quadrado nas colunas e plote a figura.
2. Escreva à mão as matrizes de rotação por 45°, escala (2 em x, 0,5 em y), cisalhamento e projeção no eixo x. Aplique cada uma com `A @ P` e plote antes e depois.
3. Confira a linearidade com dois vetores quaisquer: `A @ (u + v)` deve ser igual a `A @ u + A @ v`.
4. Componha rotação e escala nas duas ordens e mostre que as figuras diferem: o produto de matrizes não comuta.
5. Para a projeção, ache o núcleo à mão e confirme no código que esses vetores vão para zero.

## Aplicação em ML/IA

**Aplicação em ML/IA — uma camada linear separando duas classes.** Objetivo: ver que uma camada de rede neural, W·x + b, é uma transformação linear seguida de translação, e que o núcleo de W decide que informação se perde.

1. Gere duas classes de pontos 2D com `make_blobs` (scikit-learn) e plote, uma cor por classe.
2. Escolha à mão um vetor W de 1×2 e um número b para que a reta W·x + b = 0 separe as classes. Classifique cada ponto pelo sinal de W·x + b e calcule a acurácia.
3. Mude W e b à mão e veja a reta girar (W muda a direção) e se deslocar (b translada).
4. Agora use W de 2×2, plote os pontos transformados `W @ X` e veja a camada remexer o plano.
5. Troque W por uma matriz de posto 1: todos os pontos caem numa reta. Calcule o núcleo e mostre que pontos que diferem por um vetor do núcleo viram o mesmo ponto.

**O que observar:** uma camada com núcleo não trivial apaga informação para sempre. É o mesmo que acontece quando uma camada estreita comprime um embedding.
