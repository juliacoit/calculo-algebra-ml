# AL3 · Autovalores e autovetores

**Fonte:** Callioli, autovalores e autovetores

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

Av = λv com v ≠ 0; polinômio característico det(A − λI) = 0; autoespaço como o núcleo de A − λI (liga com AL1); autovalores de matrizes triangulares; multiplicidade algébrica e geométrica; autovetores de autovalores distintos são LI.

## Exercícios

autovalores e bases dos autoespaços de matrizes 2×2 e 3×3, incluindo uma rotação (sem autovalor real) e uma com autovalor repetido.

## Conferência no código

**Conferência no código — autovetores e o método das potências:**

1. Confira seus autovalores e autovetores com `np.linalg.eig` e verifique Av = λv para cada par. Lembre que o NumPy devolve autovetores com norma 1.
2. Rode a rotação de 90° e veja os autovalores complexos ±i: nenhuma direção do plano fica parada.
3. Método das potências: comece com um v qualquer e repita v ← Av / ‖Av‖ por 50 passos. Compare com o autovetor de maior |λ|.

## Aplicação em ML/IA

**Aplicação em ML/IA — PageRank.** Objetivo: ranquear páginas de um site pelos links, calculando um autovetor.

1. Invente um site com 6 páginas sobre anfíbios e desenhe os links entre elas (quem aponta para quem).
2. Monte a matriz de transição M: Mᵢⱼ = 1/(número de links que saem de j) se j aponta para i, senão 0. Cada coluna soma 1.
3. Acrescente o amortecimento: G = 0,85·M + 0,15·(1/6) em todas as entradas.
4. Aplique o método das potências a partir de r = (1/6, …, 1/6) até a mudança ficar abaixo de 10⁻⁸.
5. Compare com o autovetor de λ = 1 dado por `np.linalg.eig(G)`, normalizado para somar 1, e ordene as páginas.
6. Remova um link, rode de novo e veja quem sobe e quem desce.

## O que observar

o ranking é o autovetor de autovalor 1. Esse autovalor existe porque as colunas de G somam 1, e o método das potências converge porque os outros autovalores têm módulo menor.
