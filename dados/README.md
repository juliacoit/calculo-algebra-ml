# Dados

Conjuntos de dados e corpora usados nos notebooks. A pasta é versionada, mas arquivos acima de 10 MB ficam fora do Git.

Depois de acrescentar dados, rode a partir da raiz do repositório, com o `.venv` ativado:

```powershell
python dados/atualizar_gitignore.py
```

O script põe no `.gitignore` os arquivos de `dados/` com mais de 10 MB e avisa se algum deles já foi commitado.
