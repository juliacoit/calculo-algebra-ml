# AL6 · Gram-Schmidt, complemento ortogonal e projeção (Marco 1)

**Fonte:** Callioli, Gram-Schmidt, complemento ortogonal e projeção

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

conjuntos e bases ortonormais; coordenadas numa base ortonormal são produtos internos; processo de Gram-Schmidt; complemento ortogonal W⊥ e V = W ⊕ W⊥; projeção ortogonal sobre um subespaço e o fato de o resíduo ser ortogonal a ele; a projeção é o ponto de W mais próximo de v.

## Exercícios

ortonormalizar uma base de ℝ³ por Gram-Schmidt; achar o complemento ortogonal de um subespaço; projetar um vetor sobre um plano e calcular a distância dele ao plano.

## Conferência no código

**Conferência no código — Gram-Schmidt e projeção:**

1. Escreva uma função `gram_schmidt(V)` e rode nos mesmos vetores do exercício. Confira que `Q.T @ Q` é a identidade.
2. Compare com `np.linalg.qr(V)`: as colunas de Q coincidem, a menos de sinal.
3. Projete um vetor sobre o subespaço gerado por Q com Q·Qᵀ·v e verifique que o resíduo é ortogonal a cada coluna de Q.
4. Calcule uma base de W⊥ com `scipy.linalg.null_space(Q.T)` e confira dim W + dim W⊥ = n.

## Aplicação em ML/IA

**Aplicação em ML/IA — busca semântica, a etapa de recuperação de um RAG (Marco 1).** Objetivo: dada uma pergunta, achar os trechos mais parecidos de um corpus usando só produto interno, norma e projeção.

1. Monte um corpus de uns 50 parágrafos de textos públicos sobre répteis e anfíbios brasileiros, um parágrafo por item de uma lista.
2. Gere os embeddings, empilhe numa matriz E (uma linha por parágrafo) e normalize cada linha para norma 1.
3. Gere o embedding da pergunta, normalize e calcule `E @ q`: um único produto dá o cosseno com todos os parágrafos.
4. Ordene com `np.argsort` e devolva os 3 maiores.
5. Teste 5 perguntas e anote em quantas o trecho certo veio em 1º lugar.
6. Tire de q a sua projeção sobre o embedding da palavra "cobra" (q − ⟨q, c⟩c, com c normalizado) e repita a busca. Os resultados devem se afastar desse tema: é o complemento ortogonal em ação.

## O que observar

é exatamente a recuperação de um chatbot RAG. Normalizar antes transforma o cosseno em produto interno, que se calcula para o corpus inteiro numa só multiplicação.

## Marco 1

**Marco 1 · até 18/dez — Busca semântica.** Gere embeddings de uns 50 textos públicos sobre herpetofauna e devolva os 3 mais próximos de uma pergunta, com o ranking feito por um único produto de matrizes. Critério: explicar por que, com vetores normalizados, o cosseno vira só produto escalar.

Um marco só conta como feito quando o código roda e você explica a matemática dele sem consultar nada.
