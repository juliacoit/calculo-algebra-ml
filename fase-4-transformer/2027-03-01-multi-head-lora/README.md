# Semana de 1/mar · Marco 4 e posto baixo

**Fonte:** Vaswani et al., *Attention Is All You Need* (seção 3.2); Jay Alammar, *The Illustrated Transformer*; Deisenroth, Faisal e Ong, *Mathematics for Machine Learning* (cap. 2–5)

[Fase 4 — A matemática do Transformer](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml-a-multi-head.ipynb`](aplicacao-ml-a-multi-head.ipynb) · [`aplicacao-ml-b-lora.ipynb`](aplicacao-ml-b-lora.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

posto de um produto, posto(BA) ≤ min(posto(B), posto(A)); LoRA como W + BA, com B de d×r e A de r×d. Revisão geral das fases 1 a 3.

## Exercícios

provar a desigualdade do posto do produto a partir do espaço coluna.

## Conferência no código

O plano não tem conferência no código nesta semana.

## Aplicação em ML/IA

**Aplicação em ML/IA — atenção com várias cabeças (Marco 4):**

1. Junte h cabeças da semana anterior lado a lado e concatene as saídas; confira o resultado contra `torch.nn.MultiheadAttention` com os mesmos pesos.
2. Monte B e A com r = 2 e confirme com `np.linalg.matrix_rank` que BA tem posto no máximo 2.

**Aplicação em ML/IA — por que o LoRA funciona.** Objetivo: medir, numa matriz de pesos real, quanto uma aproximação de posto baixo economiza e quanto perde.

1. Conte os parâmetros: para d = 768 e r = 8, uma matriz cheia tem d² = 589 824 números e o par B, A tem 2·d·r = 12 288, cerca de 2%.
2. Pegue uma matriz de pesos de atenção do GPT-2, calcule a SVD e plote os valores singulares em ordem.
3. Aproxime a matriz com posto 8, 32 e 128 pela SVD truncada e meça o erro relativo de cada uma.

## O que observar

os valores singulares caem rápido, então pouca informação mora nas direções finais. O LoRA aposta que o ajuste fino precisa de uma mudança de posto baixo nos pesos, não de uma matriz inteira nova.

## Marco 4

**Marco 4 · até 7/mar — Atenção multi-head.** Implementação em NumPy com máscara causal, com saída conferida contra PyTorch. Critério: anotar o formato (shape) de cada matriz em cada linha do código.

Um marco só conta como feito quando o código roda e você explica a matemática dele sem consultar nada.
