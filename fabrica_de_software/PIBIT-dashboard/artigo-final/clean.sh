#!/bin/bash

# Script para limpar arquivos auxiliares gerados durante a compilação LaTeX
# Uso: ./clean.sh

echo "=== Limpando arquivos auxiliares LaTeX ==="

# Remove arquivos auxiliares comuns do LaTeX/BibTeX
rm -f *.aux *.bbl *.blg *.log *.out *.toc *.lof *.lot *.fdb_latexmk *.fls *.synctex.gz *.nav *.snm *.vrb

# Remove arquivos específicos do abntex2
rm -f *.idx *.ilg *.ind *.lol

# Lista arquivos restantes (exceto .tex, .bib e .sh)
echo "Arquivos restantes no diretório:"
ls -la | grep -v '^\.' | grep -v '\.tex$' | grep -v '\.bib$' | grep -v '\.sh$' | grep -v '^total'

echo "=== Limpeza concluída ==="