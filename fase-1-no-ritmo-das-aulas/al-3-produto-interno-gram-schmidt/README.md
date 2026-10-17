# Álgebra Linear · Produto interno, Gram-Schmidt e complemento ortogonal

[Fase 1 — No ritmo das aulas](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-1-no-ritmo-das-aulas/al-3-produto-interno-gram-schmidt/)

## Conteúdo

produto interno e norma; ângulo entre vetores e desigualdade de Cauchy-Schwarz; vetores ortogonais e base ortonormal; processo de Gram-Schmidt; complemento ortogonal; projeção ortogonal sobre um subespaço.

## Exercícios

ortonormalizar uma base de ℝ³ por Gram-Schmidt; achar o complemento ortogonal de um subespaço; projetar um vetor sobre um plano.

## Conferência no código

**Conferência no código — Gram-Schmidt e similaridade de cosseno:**

1. Escreva uma função `gram_schmidt(V)` e rode nos mesmos vetores do exercício feito à mão. Confira que `Q.T @ Q` é a identidade.
2. Projete um vetor sobre o subespaço gerado por Q e verifique que o resíduo é ortogonal a cada coluna de Q.
3. Invente vetores de 4 coordenadas para "sapo", "rã" e "cobra" e calcule cos θ = ⟨u, v⟩ / (‖u‖‖v‖) entre os pares.
4. Normalize os vetores e veja que o cosseno vira só o produto interno. Essa é a conta central do Marco 1.

## Aplicação em ML/IA

**Aplicação em ML/IA — busca semântica, a etapa de recuperação de um RAG (Marco 1).** Objetivo: dada uma pergunta, achar os trechos mais parecidos de um corpus usando só produto interno e norma.

1. Monte um corpus de uns 50 parágrafos de textos públicos sobre répteis e anfíbios brasileiros, um parágrafo por item de uma lista.
2. Gere os embeddings, empilhe numa matriz E (uma linha por parágrafo) e normalize cada linha para norma 1.
3. Gere o embedding da pergunta, normalize e calcule `E @ q`: um único produto dá o cosseno com todos os parágrafos.
4. Ordene com `np.argsort` e devolva os 3 maiores.
5. Teste 5 perguntas e anote em quantas o trecho certo veio em 1º lugar.
6. Extra: subtraia de q sua projeção sobre o embedding da palavra "cobra" e repita a busca. O resultado deve se afastar desse tema; é o complemento ortogonal em ação.

**O que observar:** é exatamente a recuperação de um chatbot RAG. Normalizar antes transforma o cosseno em produto interno, que se calcula para o corpus inteiro numa só multiplicação.
