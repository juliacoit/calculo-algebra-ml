"""Põe no .gitignore os arquivos de dados/ com mais de 10 MB.

Uso, a partir da raiz do repositório:  python dados/atualizar_gitignore.py
Rode antes de commitar sempre que acrescentar dados. A lista fica entre os marcadores
"# >>> dados grandes (gerado)" e "# <<< dados grandes (gerado)" do .gitignore.
"""
import subprocess
from pathlib import Path

LIMITE = 10 * 1024 * 1024  # 10 MB
RAIZ = Path(__file__).resolve().parent.parent
GITIGNORE = RAIZ / ".gitignore"
INICIO, FIM = "# >>> dados grandes (gerado)", "# <<< dados grandes (gerado)"


def padrao(caminho: str) -> str:
    """Caminho ancorado na raiz, com os caracteres especiais do .gitignore escapados."""
    for ch in "[]*?!#":
        caminho = caminho.replace(ch, "\\" + ch)
    return "/" + caminho


grandes = sorted(
    p.relative_to(RAIZ).as_posix()
    for p in (RAIZ / "dados").rglob("*")
    if p.is_file() and p.stat().st_size > LIMITE
)
linhas = GITIGNORE.read_text(encoding="utf-8").splitlines()
i, j = linhas.index(INICIO), linhas.index(FIM)
novas = linhas[: i + 1] + [padrao(g) for g in grandes] + linhas[j:]
with open(GITIGNORE, "w", encoding="utf-8", newline="\n") as f:
    f.write("\n".join(novas) + "\n")

print(f"{len(grandes)} arquivo(s) de dados/ com mais de 10 MB no .gitignore")
for g in grandes:
    print("  ", g)

# um arquivo que já foi commitado não sai do Git só por entrar no .gitignore
if grandes:
    ja_no_git = subprocess.run(["git", "ls-files", "--", *grandes], cwd=RAIZ,
                               capture_output=True, text=True).stdout.split("\n")
    for g in filter(None, ja_no_git):
        print(f'atenção: {g} já está no Git; para tirar sem apagar o arquivo: git rm --cached "{g}"')
