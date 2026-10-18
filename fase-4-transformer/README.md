# Fase 4 — A matemática do Transformer (15/fev a 7/mar)

A atenção de um Transformer é só multiplicação de matrizes e uma softmax; a fase trata disso como conta, não como arquitetura.

- [Semana de 15/fev · Softmax, Jacobiano e entropia cruzada](2027-02-15-softmax-entropia-cruzada/)
- [Semana de 22/fev · Q, K, V e a escala por √d](2027-02-22-qkv-escala-raiz-d/)
- [Semana de 1/mar · Marco 4 e posto baixo](2027-03-01-multi-head-lora/)

O resultado que liga as fases 3 e 4, e que vale derivar à mão na Fase 4:

```math
\frac{\partial L}{\partial z} = \mathrm{softmax}(z) - y, \quad L = -\sum_i y_i \log \mathrm{softmax}(z)_i
```

## Marco 4

**Marco 4 · até 7/mar — Atenção multi-head.** Implementação em NumPy com máscara causal, com saída conferida contra PyTorch. Critério: anotar o formato (shape) de cada matriz em cada linha do código. ([Semana de 1/mar · Marco 4 e posto baixo](2027-03-01-multi-head-lora/))
