# Semana de 15/fev · Softmax, Jacobiano e entropia cruzada

[Fase 4 — A matemática do Transformer](../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](../../exercicios-a-mao/fase-4-transformer/2027-02-15-softmax-entropia-cruzada/)

## Conteúdo

softmax sᵢ = e^(zᵢ) / Σⱼ e^(zⱼ); seu Jacobiano ∂sᵢ/∂zⱼ = sᵢ(δᵢⱼ − sⱼ); entropia cruzada L = −Σ yᵢ·log sᵢ; o resultado ∂L/∂z = s − y (fórmula no fim desta seção).

O resultado que liga as fases 3 e 4, e que vale derivar à mão na Fase 4:

```math
\frac{\partial L}{\partial z} = \mathrm{softmax}(z) - y, \quad L = -\sum_i y_i \log \mathrm{softmax}(z)_i
```

## Exercícios

derivar à mão o Jacobiano da softmax para 3 classes; derivar ∂L/∂z e simplificar até s − y.

## Conferência no código

**Conferência no código — conferir as derivadas:**

1. Implemente a softmax e confira o Jacobiano feito à mão contra diferenças finitas.
2. Mostre que a versão ingênua estoura com z = [1000, 1001] e que subtrair o máximo de z resolve sem mudar o resultado. Prove no papel por que não muda.
3. Confirme numericamente que ∂L/∂z = s − y.

## Aplicação em ML/IA

**Aplicação em ML/IA — um modelo de próxima letra.** Objetivo: treinar um modelo de linguagem minúsculo usando só a softmax e o gradiente s − y que você derivou.

1. Pegue uma lista de uns 1000 nomes (por exemplo, nomes científicos de espécies ou nomes próprios) e trate cada nome como uma sequência de letras, com um símbolo de início e de fim.
2. Represente a letra atual como um vetor one-hot x de 27 posições e crie uma matriz W de 27×27 com valores aleatórios pequenos.
3. Calcule os logits z = Wᵀx, a softmax s e a perda de entropia cruzada contra a letra seguinte de verdade.
4. Atualize W pelo gradiente, usando ∂L/∂z = s − y, até a perda média parar de cair.
5. Gere 10 nomes novos sorteando uma letra de cada vez a partir de s.

**O que observar:** não há nenhuma derivada além da que você fez à mão. O modelo aprende quais letras costumam vir depois de quais.
