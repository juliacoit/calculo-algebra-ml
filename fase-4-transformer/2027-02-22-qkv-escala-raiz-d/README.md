# Semana de 22/fev · Q, K, V e a escala por √d

[Fase 4 — A matemática do Transformer](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-4-transformer/2027-02-22-qkv-escala-raiz-d/)

## Conteúdo

Q = XW_Q, K = XW_K e V = XW_V como transformações lineares das mesmas entradas; QKᵀ como matriz de produtos internos entre linhas; por que dividir por √d (a variância de um produto interno de vetores aleatórios cresce com d).

## Exercícios

escrever o formato de cada matriz para X de 5×8 e W de 8×4; calcular à mão a variância de q·k quando as coordenadas são independentes com variância 1.

## Conferência no código

**Conferência no código — atenção de uma cabeça:**

1. Gere X aleatória de 5×8 e três matrizes W de 8×4; calcule Q, K e V anotando o formato de cada uma.
2. Calcule S = QKᵀ/√4, aplique a softmax em cada linha e confira que cada linha soma 1.
3. Aplique a máscara causal: −∞ acima da diagonal antes da softmax.
4. Meça a variância de q·k para d = 4, 64 e 512, sem e com a divisão por √d, e compare com a conta feita à mão.

## Aplicação em ML/IA

**Aplicação em ML/IA — a matriz de atenção de um modelo real.** Objetivo: abrir um modelo pré-treinado e reconhecer nele a matriz que você montou à mão.

1. Carregue o GPT-2 pela biblioteca `transformers` com `output_attentions=True`.
2. Rode uma frase curta em inglês e pegue a matriz de atenção de uma cabeça de uma camada. Ela tem formato tokens × tokens.
3. Confira as duas propriedades da semana: cada linha soma 1 (softmax) e tudo acima da diagonal é zero (máscara causal).
4. Plote a matriz como mapa de calor, com os tokens nos eixos, e anote para qual token anterior cada palavra mais olha.
5. Compare 3 ou 4 cabeças diferentes da mesma camada.

**O que observar:** a matriz do modelo real tem exatamente a forma e as propriedades da sua. Cada cabeça aprende um padrão diferente de produtos internos.
