# Cálculo e Álgebra Linear para ML/NLP

Plano de estudos de 20 semanas, com um notebook por semana em NumPy e 4 projetos-marco.

## Objetivo

Construir a base de cálculo e álgebra linear necessária para entender e implementar do zero modelos de Machine Learning e NLP, terminando no mecanismo de atenção do Transformer. A teoria é feita à mão, no papel, e cada conceito é implementado em NumPy logo em seguida.

## As 4 fases

| Fase | Semanas | Foco |
|---|---|---|
| [1. Vetores e funções](fase-1-vetores-e-funcoes/) | 01–05 | vetores, produto escalar, cosseno, matrizes, sigmoide e softmax |
| [2. Derivadas e sistemas](fase-2-derivadas-e-sistemas/) | 06–10 | derivada, regra da cadeia, gradiente descendente, sistemas lineares, mínimos quadrados |
| [3. Gradientes e SVD](fase-3-gradientes-e-svd/) | 11–16 | gradiente, jacobiana, backpropagation, autovetores, SVD, PCA |
| [4. Transformer](fase-4-transformer/) | 17–20 | softmax estável, atenção, multi-head, bloco Transformer |

## Os 4 marcos

| Marco | Quando | Projeto |
|---|---|---|
| [1. Busca semântica](marcos/marco-1-busca-semantica/) | semana 5 | embeddings com sentence-transformers + ranking por similaridade de cosseno |
| [2. Regressão logística](marcos/marco-2-regressao-logistica/) | semana 10 | classificador de texto do zero em NumPy, comparado com o scikit-learn |
| [3. MLP e PCA](marcos/marco-3-mlp-e-pca/) | semana 16 | MLP com backprop manual + PCA via SVD para visualizar embeddings |
| [4. Atenção multi-head](marcos/marco-4-atencao-multi-head/) | semana 20 | atenção multi-head em NumPy, conferida contra o PyTorch |

## Estrutura

```
calculo-algebra-ml/
├── fase-1-vetores-e-funcoes/      semana-01 a semana-05
├── fase-2-derivadas-e-sistemas/   semana-06 a semana-10
├── fase-3-gradientes-e-svd/       semana-11 a semana-16
├── fase-4-transformer/            semana-17 a semana-20
├── marcos/                        os 4 projetos-marco
├── exercicios-a-mao/              fotos ou PDFs das listas resolvidas
└── notas/                         resumos em Markdown, fórmulas em LaTeX
```

## Como rodar o ambiente

Requer Python 3.12. No Windows (PowerShell), a partir da pasta do repositório:

```powershell
# 1. criar e ativar o ambiente virtual
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. instalar as dependências (o requirements.txt já aponta para o índice do torch só CPU)
python -m pip install -r requirements.txt

# 3. registrar o kernel do Jupyter
python -m ipykernel install --user --name calculo-algebra-ml --display-name "calculo-algebra-ml"

# 4. abrir o JupyterLab
jupyter lab
```

No Linux ou macOS, troque o passo 1 por `python3.12 -m venv .venv` e `source .venv/bin/activate`.

Os notebooks já vêm configurados para usar o kernel `calculo-algebra-ml`.
