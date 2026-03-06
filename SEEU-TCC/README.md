# TCC (Trabalho de Conclusão de Curso)

Breve repositório contendo os arquivos fontes em LaTeX do TCC, com estrutura organizada em elementos pré-textuais, textuais e pós-textuais, figuras, tabelas e diagramas.

**Estrutura resumida**:
- `main.tex`: arquivo principal do documento.
- `estilo.cls`: classe LaTeX usada no projeto.
- `referencias.bib`: arquivo BibTeX com referências.
- `01-elementos-pre-textuais/`, `02-elementos-textuais/`, `03-elementos-pos-textuais/`: conteúdo do TCC dividido por seções.

**Requisitos**:
- Uma distribuição TeX (TeX Live, MiKTeX ou similar) com `xelatex`/`pdflatex`/`latexmk` instalada.
- `make` (GNU Make). Em Windows, pode-se usar o WSL, Git Bash, MSYS2, ou instalar Make via Chocolatey (`choco install make`).

**Como compilar**:
Abra um terminal na raiz do repositório (onde está `Makefile`) e execute:

```powershell
make
```

Esse comando irá compilar o projeto e gerar o PDF final (por exemplo `main.pdf`) conforme os alvos definidos no `Makefile`.

**Limpar arquivos gerados**:
Para remover arquivos intermediários e artefatos de compilação, execute:

```powershell
make clean
```

Se estiver no Windows sem `make`, como alternativa direta é possível usar `latexmk` ou `xelatex` manualmente. Exemplo com `latexmk`:

```powershell
latexmk -pdf main.tex
latexmk -c    # limpa arquivos temporários gerados pelo latexmk
```

**Notas**:
- Se houver erros de compilação, verifique as mensagens do compilador para dependências ausentes (pacotes LaTeX) ou arquivos com acentuação/encodings incorretos.
- O repositório contém pastas com exemplos de figuras e diagramas em `04-figuras/` e `1-Primeira_parte/Diagramas/`.

Se quiser, posso atualizar o `Makefile` para adicionar alvos extras (por exemplo `make pdf` ou `make watch`) ou testar a compilação aqui se você permitir que eu execute comandos na sua máquina.
