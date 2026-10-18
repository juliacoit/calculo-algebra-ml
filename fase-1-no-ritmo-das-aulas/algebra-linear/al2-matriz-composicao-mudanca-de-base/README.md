# AL2 · Matriz de uma transformação, composição e mudança de base

**Fonte:** Callioli, matriz de uma transformação, composição e mudança de base

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

matriz [T] nas bases B e C (cada coluna é o vetor de coordenadas de T(bᵢ) na base C); [T(v)]_C = [T]·[v]_B; composição de TLs corresponde ao produto das matrizes; T inversível se e só se sua matriz é inversível, com [T⁻¹] = [T]⁻¹; um operador em duas bases: [T]_B' = P⁻¹[T]_B P, a ligação com mudança de base (último tópico das notas); matrizes semelhantes.

## Exercícios

matriz de T nas bases canônicas e em outro par de bases; usar a matriz para calcular T(v); matriz de S∘T pelo produto, conferindo pela fórmula direta; [T]_B' por P⁻¹AP.

## Conferência no código

**Conferência no código — transformações no plano:**

1. Monte uma matriz P de 2 linhas com os vértices de um quadrado nas colunas e plote a figura.
2. Escreva à mão as matrizes de rotação por 45°, escala (2 em x, 0,5 em y), cisalhamento e projeção no eixo x. Aplique cada uma com `A @ P` e plote antes e depois.
3. Componha rotação e escala nas duas ordens: as figuras diferem, porque o produto de matrizes não comuta.
4. Pegue um exercício de [T]_B' feito à mão e confira `np.linalg.inv(P) @ A @ P`.

## Aplicação em ML/IA

**Aplicação em ML/IA — por que redes neurais precisam de não linearidade.** Objetivo: ver que empilhar camadas lineares é compor TLs, o que dá só outra TL, e que uma função não linear entre elas muda isso.

1. Gere duas classes com `make_blobs` e classifique pelo sinal de W·x + b com W e b escolhidos à mão. Mude W (a reta gira) e b (a reta se desloca).
2. Monte duas camadas sem ativação, W₂(W₁x + b₁) + b₂. Calcule W = W₂W₁ e b = W₂b₁ + b₂ e confirme que uma única camada dá as mesmas saídas.
3. Use o XOR: os pontos (0,0) e (1,1) na classe 0 e (0,1) e (1,0) na classe 1. Teste uma grade de valores de W e b e veja que nenhuma reta acerta os 4 pontos (no máximo 3).
4. Coloque a ReLU, max(0, ·), entre as camadas, com W₁ = [[1, 1], [1, 1]], b₁ = (0, −1) e W₂ = [1, −2]. Calcule à mão a saída nos 4 pontos e confira no código: dá 0, 1, 1, 0.
5. Plote os 4 pontos depois de W₁ e da ReLU: no novo plano, uma reta já os separa.

## O que observar

sem não linearidade, uma rede de 100 camadas é uma só matriz. A ReLU deforma o espaço, e é isso que permite separar o que nenhuma reta separa.
