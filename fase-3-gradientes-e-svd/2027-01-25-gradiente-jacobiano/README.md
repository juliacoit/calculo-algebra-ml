# Semana de 25/jan · Gradiente, regra da cadeia em várias variáveis e Jacobiano

[Fase 3 — Gradientes e decomposições](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-3-gradientes-e-svd/2027-01-25-gradiente-jacobiano/)

## Conteúdo

o vetor gradiente aponta para o maior crescimento; derivada direcional; regra da cadeia para f(g(x, y)); matriz Jacobiana.

## Exercícios

gradiente e derivada direcional de 3 funções; Jacobiano de uma transformação de ℝ² em ℝ²; regra da cadeia numa composição de duas funções.

## Conferência no código

**Conferência no código — descida pelo gradiente em 2D:**

1. Rode o gradiente descendente em f(x, y) = x² + 10y², partindo de (8, 2), e desenhe a trajetória sobre as curvas de nível.
2. Observe o zigue-zague e relacione-o à razão 10 entre os autovalores da semana anterior.
3. Siga o vídeo do micrograd até a parte do backprop e refaça à mão a derivada da expressão de exemplo dele.

## Aplicação em ML/IA

**Aplicação em ML/IA — treinar com e sem padronização, e o momentum.** Objetivo: medir como os autovalores da semana anterior controlam a velocidade do treino, e ver o Jacobiano de uma camada.

1. Treine o modelo ŷ = w·x + b da semana anterior por gradiente descendente, com e sem padronizar x. Conte quantos passos cada versão leva até a perda parar de cair.
2. Implemente o momentum, v ← β·v + ∇L e (w, b) ← (w, b) − η·v, com β = 0,9. Compare a trajetória com a da versão simples sobre as curvas de nível.
3. Para uma camada y = Wx, mostre no papel que o Jacobiano de y em relação a x é a própria W. Confira com `torch.autograd.functional.jacobian`.

**O que observar:** o número de passos acompanha a razão entre os autovalores. O momentum reduz o zigue-zague ao acumular a direção que se repete.
