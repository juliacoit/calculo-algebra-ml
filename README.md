# Cálculo e Álgebra Linear para ML/NLP

## Objetivo

Dominar Álgebra Linear (de transformações lineares em diante) e Cálculo (de funções a integrais); ML/IA entra como aplicação de cada tópico.

O foco é dominar Álgebra Linear e Cálculo; ML entra só como uma aplicação curta de cada tópico, feita depois dos exercícios. Até 18/dez o conteúdo segue as disciplinas; nas férias (21/dez a 7/mar) entra o que as ementas não cobrem: cálculo de várias variáveis, SVD e a matemática da atenção.

## As partes de cada tópico

Cada tópico tem quatro partes, nesta ordem: **conteúdo** (o que dominar, tirado do programa da disciplina), **exercícios** (à mão, da lista ou do livro-texto), **conferência no código** (um notebook curto em NumPy que confere o que você fez à mão) e **aplicação em ML/IA** (um problema real de ML resolvido com aquele tópico, com objetivo, passos e o que observar). Nenhuma das duas partes em código substitui os exercícios.

Cada pasta de tópico ou semana tem:

- `README.md`: conteúdo, exercícios, conferência no código, aplicação em ML/IA e o que observar, copiados do plano, com a fonte no topo;
- `conferencia.ipynb`: a conferência no código, um passo por célula;
- `aplicacao-ml.ipynb`: a aplicação em ML/IA, um passo por célula (a semana de 1/mar tem duas, A e B);
- `exercicios/`: fotos e PDFs das listas resolvidas à mão.

## Índice

### Fase 1 — No ritmo das aulas (19/out a 18/dez) · [calendário do semestre](fase-1-no-ritmo-das-aulas/calendario-semestre.md)

**Álgebra Linear**

- [AL1 · Transformações lineares: definição, núcleo e imagem](fase-1-no-ritmo-das-aulas/algebra-linear/al1-transformacoes-nucleo-imagem/)
- [AL2 · Matriz de uma transformação, composição e mudança de base](fase-1-no-ritmo-das-aulas/algebra-linear/al2-matriz-composicao-mudanca-de-base/)
- [AL3 · Autovalores e autovetores](fase-1-no-ritmo-das-aulas/algebra-linear/al3-autovalores-autovetores/)
- [AL4 · Diagonalização](fase-1-no-ritmo-das-aulas/algebra-linear/al4-diagonalizacao/)
- [AL5 · Produto interno, norma e ângulo](fase-1-no-ritmo-das-aulas/algebra-linear/al5-produto-interno-norma-angulo/)
- [AL6 · Gram-Schmidt, complemento ortogonal e projeção (Marco 1)](fase-1-no-ritmo-das-aulas/algebra-linear/al6-gram-schmidt-projecao/)

**Cálculo**

- [C0 · Funções e gráficos (Ávila cap. 3; revisão)](fase-1-no-ritmo-das-aulas/calculo/c0-funcoes-graficos/)
- [C1 · Limites e continuidade (Ávila 4.2; revisão)](fase-1-no-ritmo-das-aulas/calculo/c1-limites-continuidade/)
- [C2 · Derivada: definição e reta tangente (Ávila 4.1 e 4.3; revisão)](fase-1-no-ritmo-das-aulas/calculo/c2-derivada-definicao/)
- [C3 · Regras de derivação, cadeia, implícita e inversa (Ávila cap. 5; revisão)](fase-1-no-ritmo-das-aulas/calculo/c3-regras-de-derivacao/)
- [C4 · Funções trigonométricas, identidades e limite fundamental (Ávila 6.1 e 6.2)](fase-1-no-ritmo-das-aulas/calculo/c4-trigonometria-identidades/)
- [C5 · Derivadas trigonométricas, inversas e formas indeterminadas (Ávila 6.3 a 6.5)](fase-1-no-ritmo-das-aulas/calculo/c5-derivadas-trigonometricas-inversas/)
- [C6 · Logaritmo e exponencial (Ávila cap. 7)](fase-1-no-ritmo-das-aulas/calculo/c6-logaritmo-exponencial/)
- [C7 · Máximos e mínimos e Teorema do Valor Médio (Ávila cap. 8)](fase-1-no-ritmo-das-aulas/calculo/c7-maximos-minimos-tvm/)
- [C8 · L'Hôpital, concavidade, esboço de gráficos e Taylor (Ávila cap. 9)](fase-1-no-ritmo-das-aulas/calculo/c8-lhopital-concavidade-taylor/)
- [C9 · Integral definida, Teorema Fundamental do Cálculo e impróprias (Ávila cap. 10)](fase-1-no-ritmo-das-aulas/calculo/c9-integral-tfc-improprias/)
- [C10 · Técnicas de integração e aplicações da integral (Ávila cap. 11)](fase-1-no-ritmo-das-aulas/calculo/c10-tecnicas-de-integracao/)

### Fase 2 — Regressão do zero (21/dez a 17/jan)

- [Semana de 21/dez · Aplicações pendentes da Fase 1](fase-2-regressao-do-zero/2026-12-21-aplicacoes-pendentes/)
- Semana de 28/dez · Pausa
- [Semana de 4/jan · Projeção e mínimos quadrados](fase-2-regressao-do-zero/2027-01-04-projecao-minimos-quadrados/)
- [Semana de 11/jan · Marco 2: regressão logística](fase-2-regressao-do-zero/2027-01-11-regressao-logistica/)

### Fase 3 — Gradientes e decomposições (18/jan a 14/fev)

- [Semana de 18/jan · Teorema espectral e derivadas parciais](fase-3-gradientes-e-svd/2027-01-18-teorema-espectral-derivadas-parciais/)
- [Semana de 25/jan · Gradiente, regra da cadeia em várias variáveis e Jacobiano](fase-3-gradientes-e-svd/2027-01-25-gradiente-jacobiano/)
- [Semana de 1/fev · SVD e backpropagation](fase-3-gradientes-e-svd/2027-02-01-svd-backpropagation/)
- [Semana de 8/fev · Marco 3](fase-3-gradientes-e-svd/2027-02-08-posto-baixo-gradient-check/)

### Fase 4 — A matemática do Transformer (15/fev a 7/mar)

- [Semana de 15/fev · Softmax, Jacobiano e entropia cruzada](fase-4-transformer/2027-02-15-softmax-entropia-cruzada/)
- [Semana de 22/fev · Q, K, V e a escala por √d](fase-4-transformer/2027-02-22-qkv-escala-raiz-d/)
- [Semana de 1/mar · Marco 4 e posto baixo](fase-4-transformer/2027-03-01-multi-head-lora/)

## As 4 fases

| Fase | Período | Pasta |
|---|---|---|
| Fase 1 — No ritmo das aulas | 19/out a 18/dez | [`fase-1-no-ritmo-das-aulas/`](fase-1-no-ritmo-das-aulas/) |
| Fase 2 — Regressão do zero | 21/dez a 17/jan (pausa de 28/dez a 3/jan) | [`fase-2-regressao-do-zero/`](fase-2-regressao-do-zero/) |
| Fase 3 — Gradientes e decomposições | 18/jan a 14/fev | [`fase-3-gradientes-e-svd/`](fase-3-gradientes-e-svd/) |
| Fase 4 — A matemática do Transformer | 15/fev a 7/mar | [`fase-4-transformer/`](fase-4-transformer/) |

O calendário do semestre, com as provas e o que fazer em cada semana, está em [`fase-1-no-ritmo-das-aulas/calendario-semestre.md`](fase-1-no-ritmo-das-aulas/calendario-semestre.md).

## Os 4 marcos

Um marco só conta como feito quando o código roda e você explica a matemática dele sem consultar nada.

| Marco | Prazo | Onde |
|---|---|---|
| Marco 1 — Busca semântica | 18/dez | [AL6 · Gram-Schmidt, complemento ortogonal e projeção (Marco 1)](fase-1-no-ritmo-das-aulas/algebra-linear/al6-gram-schmidt-projecao/) |
| Marco 2 — Regressão logística do zero | 17/jan | [Semana de 11/jan · Marco 2: regressão logística](fase-2-regressao-do-zero/2027-01-11-regressao-logistica/) |
| Marco 3 — MLP e PCA | 14/fev | [Semana de 8/fev · Marco 3](fase-3-gradientes-e-svd/2027-02-08-posto-baixo-gradient-check/) |
| Marco 4 — Atenção multi-head | 7/mar | [Semana de 1/mar · Marco 4 e posto baixo](fase-4-transformer/2027-03-01-multi-head-lora/) |

- **Marco 1 · até 18/dez — Busca semântica.** Gere embeddings de uns 50 textos públicos sobre herpetofauna e devolva os 3 mais próximos de uma pergunta, com o ranking feito por um único produto de matrizes. Critério: explicar por que, com vetores normalizados, o cosseno vira só produto escalar.
- **Marco 2 · até 17/jan — Regressão logística do zero.** Classificador de sentimento com bag-of-words e gradiente descendente em NumPy. Critério: derivar o gradiente à mão e chegar a uma acurácia próxima à do scikit-learn no mesmo conjunto.
- **Marco 3 · até 14/fev — MLP e PCA.** MLP de 2 camadas com backprop conferido por diferenças finitas (erro relativo abaixo de 1e-5). Depois, PCA via SVD de embeddings de palavras, plotado em 2D. Critério: dizer o que cada autovetor representa no gráfico.
- **Marco 4 · até 7/mar — Atenção multi-head.** Implementação em NumPy com máscara causal, com saída conferida contra PyTorch. Critério: anotar o formato (shape) de cada matriz em cada linha do código.

## Dados

Conjuntos de dados e corpora ficam em [`dados/`](dados/). Arquivos acima de 10 MB não vão para o Git: depois de acrescentar dados, rode `python dados/atualizar_gitignore.py`.

## Como rodar o ambiente

No PowerShell, a partir da pasta do repositório:

```powershell
cd ~\estudos\calculo-algebra-ml
.\.venv\Scripts\Activate.ps1
jupyter lab
```

Os notebooks já usam o kernel `calculo-algebra-ml`.

### Recriar o ambiente do zero

Requer Python 3.12.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name calculo-algebra-ml --display-name "calculo-algebra-ml"
```

O `requirements.txt` já aponta para o índice do PyTorch só CPU.
