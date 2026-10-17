# Cálculo e Álgebra Linear para ML/NLP

## Objetivo

O foco é dominar Álgebra Linear e Cálculo; ML entra só como uma aplicação curta de cada tópico, feita depois dos exercícios. Até 18/dez o conteúdo segue as disciplinas; nas férias (21/dez a 7/mar) entra o que as ementas não cobrem: cálculo de várias variáveis, SVD e a matemática da atenção.

Cada tópico tem quatro partes, nesta ordem: **conteúdo** (o que dominar, tirado do programa da disciplina), **exercícios** (à mão, da lista ou do livro-texto), **conferência no código** (um notebook curto em NumPy que confere o que você fez à mão) e **aplicação em ML/IA** (um problema real de ML resolvido com aquele tópico, com objetivo, passos e o que observar). Nenhuma das duas partes em código substitui os exercícios.

Cada pasta de tópico ou semana tem um `README.md` com essas quatro partes e dois notebooks: `conferencia.ipynb` e `aplicacao-ml.ipynb`. O `calc-1` tem três conferências (A, B e C) e a semana de 1/mar tem duas aplicações (A e B), como no plano.

## Semestre (19/out a 18/dez)

Cada semana do semestre tem um modo. **Só disciplinas:** nada do plano. **Prática leve:** um notebook de 1 a 2 h sobre o tópico da aula naquela semana.

| Semana | Provas e eventos | Modo |
|---|---|---|
| 19/out | Véspera da prova de Álgebra Linear | Só disciplinas; instalar o ambiente |
| 26/out | Álgebra Linear (26/out, a confirmar); AI Brasil Experience em SP (27 a 30/out) | Pausa |
| 2/nov | Cálculo 1A, 3ª avaliação (4/nov) | Só disciplinas |
| 9/nov | — | Prática leve |
| 16/nov | — | Prática leve |
| 23/nov | Arquitetura, 3ª avaliação (24/nov) | Só disciplinas |
| 30/nov | Álgebra Linear (2/dez), Matemática Discreta (3/dez), Cálculo 1A, 4ª avaliação (4/dez) | Só disciplinas |
| 7/dez | — | Prática leve; Marco 1 |
| 14/dez | Fim do semestre (18/dez) | Prática leve; Marco 1 |

## As 4 fases

| Fase | Período | Pasta |
|---|---|---|
| 1 — No ritmo das aulas | 19/out a 18/dez | [`fase-1-no-ritmo-das-aulas/`](fase-1-no-ritmo-das-aulas/) |
| 2 — Regressão do zero | 21/dez a 17/jan (pausa de 28/dez a 3/jan) | [`fase-2-regressao-do-zero/`](fase-2-regressao-do-zero/) |
| 3 — Gradientes e decomposições | 18/jan a 14/fev | [`fase-3-gradientes-e-svd/`](fase-3-gradientes-e-svd/) |
| 4 — A matemática do Transformer | 15/fev a 7/mar | [`fase-4-transformer/`](fase-4-transformer/) |

## Os 4 marcos

Um marco só conta como feito quando o código roda e você explica a matemática dele sem consultar nada.

| Marco | Prazo | Pasta |
|---|---|---|
| Marco 1 — Busca semântica | 18/dez | [`marcos/marco-1-busca-semantica/`](marcos/marco-1-busca-semantica/) |
| Marco 2 — Regressão logística do zero | 17/jan | [`marcos/marco-2-regressao-logistica/`](marcos/marco-2-regressao-logistica/) |
| Marco 3 — MLP e PCA | 14/fev | [`marcos/marco-3-mlp-e-pca/`](marcos/marco-3-mlp-e-pca/) |
| Marco 4 — Atenção multi-head | 7/mar | [`marcos/marco-4-atencao-multi-head/`](marcos/marco-4-atencao-multi-head/) |

## Estrutura

```
calculo-algebra-ml/
├── fase-1-no-ritmo-das-aulas/     por tópico: al-1, al-2, al-3, calc-1, calc-2
├── fase-2-regressao-do-zero/      por semana: 21/dez, 4/jan, 11/jan
├── fase-3-gradientes-e-svd/       por semana: 18/jan, 25/jan, 1/fev, 8/fev
├── fase-4-transformer/            por semana: 15/fev, 22/fev, 1/mar
├── marcos/                        os 4 projetos-marco
├── exercicios-a-mao/              fotos ou PDFs das listas, espelhando as fases
└── notas/                         resumos em Markdown, fórmulas em LaTeX
```

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
