# C2 · Derivada: definição e reta tangente (Ávila 4.1 e 4.3; revisão)

**Fonte:** Ávila, 4.1 e 4.3

[Fase 1 — No ritmo das aulas](../../) · Notebooks: [`conferencia.ipynb`](conferencia.ipynb) · [`aplicacao-ml.ipynb`](aplicacao-ml.ipynb) · [Exercícios à mão](exercicios/)

## Conteúdo

razão incremental; derivada como limite; reta tangente e reta normal; derivada como função; derivável implica contínua (a recíproca é falsa: |x| em 0); velocidade instantânea (Ávila 4.4).

## Exercícios

derivada pela definição de x², √x e 1/x; retas tangente e normal em pontos dados; mostrar que |x| não é derivável em 0 pelos limites laterais.

## Conferência no código

**Conferência no código — secantes que viram tangente:**

1. Para f(x) = x² em a = 1, tabele (f(1 + h) − f(1))/h para h = 1; 0,1; 0,01; … e veja tender a 2.
2. Plote f e as retas secantes para h = 1; 0,5; 0,1, junto com a tangente y = 2x − 1.
3. Para |x| em 0, calcule as razões com h > 0 e h < 0: dão 1 e −1, então o limite não existe.

## Aplicação em ML/IA

**Aplicação em ML/IA — derivada numérica e o erro de h.** Objetivo: entender a ferramenta usada para verificar se um gradiente está certo (o gradient check do Marco 3).

1. Use a sigmoide σ(x) = 1/(1 + e⁻ˣ) em x = 0,5. A derivada exata é σ(x)(1 − σ(x)) (você prova isso em C3).
2. Calcule a diferença progressiva (f(x + h) − f(x))/h e a central (f(x + h) − f(x − h))/2h para h = 10⁻¹, 10⁻², …, 10⁻¹².
3. Plote o erro de cada uma contra h em escala log-log. O gráfico tem forma de V: para h grande domina o erro da aproximação; para h pequeno, o arredondamento do computador.
4. Ache o melhor h de cada fórmula (fica perto de 10⁻⁸ na progressiva e de 10⁻⁵ na central).
5. Na ReLU em x = 0, as razões laterais dão 0 e 1. Confira com `torch` qual valor a biblioteca usa como "derivada" em 0.

## O que observar

a derivada numérica é a definição de derivada com h pequeno, mas não pequeno demais. Num ponto sem derivada, como a ReLU em 0, as bibliotecas simplesmente escolhem um valor.
