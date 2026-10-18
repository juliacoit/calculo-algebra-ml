# Semana de 4/jan · Projeção e mínimos quadrados

**Fonte:** Gilbert Strang, MIT 18.06 (projeções); 3Blue1Brown, *Essence of Linear Algebra*; 3Blue1Brown, *Essence of Calculus*; Deisenroth, Faisal e Ong, *Mathematics for Machine Learning* (cap. 2–5)

[Fase 2 — Regressão do zero](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

sistema Ax = b sem solução; a melhor aproximação é a projeção de b no espaço coluna de A; equações normais AᵀA·x̂ = Aᵀb. Em Cálculo, o mínimo de E(a, b) = Σ(yᵢ − a·xᵢ − b)², achado igualando a zero a derivada em cada variável, uma de cada vez.

## Exercícios

reta de mínimos quadrados para 3 ou 4 pontos, à mão, pelos dois caminhos (equações normais e derivadas). Os dois têm de dar a mesma reta.

## Conferência no código

**Conferência no código — ajuste de reta:**

1. Gere 30 pontos com y = 2x + 1 mais ruído.
2. Monte A com as colunas [x, 1] e resolva as equações normais com `np.linalg.solve(A.T @ A, A.T @ y)`.
3. Calcule o resíduo r = y − A·x̂ e confirme que `A.T @ r` é praticamente zero: o resíduo é ortogonal ao espaço coluna.
4. Plote os pontos e a reta.

## Aplicação em ML/IA

**Aplicação em ML/IA — regressão linear de verdade e regularização.** Objetivo: aplicar mínimos quadrados a dados reais com várias features e ver como o termo λI resolve o problema da semana anterior.

1. Com `load_diabetes`, separe 80% dos pacientes para treino e 20% para teste.
2. Acrescente uma coluna de 1s e resolva as equações normais com `np.linalg.lstsq`.
3. Compare os coeficientes com os de `LinearRegression` do scikit-learn: devem ser iguais.
4. Calcule o erro quadrático médio no teste.
5. Volte à matriz com a coluna redundante (de AL1) e resolva a versão regularizada (XᵀX + λI)w = Xᵀy para λ = 0,1, 1 e 10. Compare o erro de teste de cada uma.

## O que observar

somar λI soma λ a todos os autovalores de XᵀX. Nenhum fica zero, então a matriz vira invertível; é a regressão Ridge.
