#!/bin/bash

# Script para compilar o relatório parcial em LaTeX para PDF
# Uso: ./build_relatorio.sh

set -e  # Para em caso de erro

echo "=== Compilando relatorio-parcial.tex para PDF ==="
echo "Diretório atual: $(pwd)"

# Verifica se os arquivos necessários existem
if [ ! -f "relatorio-parcial.tex" ]; then
    echo "ERRO: relatorio-parcial.tex não encontrado no diretório atual!"
    exit 1
fi

if [ ! -f "relatorio-parcial.bib" ]; then
    echo "ERRO: relatorio-parcial.bib não encontrado no diretório atual!"
    exit 1
fi

echo "Arquivos encontrados: relatorio-parcial.tex e relatorio-parcial.bib"

# Remove arquivos auxiliares anteriores se existirem
echo "Limpando arquivos auxiliares anteriores..."
rm -f relatorio-parcial.aux relatorio-parcial.bbl relatorio-parcial.blg relatorio-parcial.log relatorio-parcial.out relatorio-parcial.toc relatorio-parcial.lof relatorio-parcial.lot relatorio-parcial.fdb_latexmk relatorio-parcial.fls relatorio-parcial.synctex.gz

# Primeira compilação com pdflatex
echo "=== Primeira compilação com pdflatex ==="
pdflatex -interaction=nonstopmode relatorio-parcial.tex

# Compilação do BibTeX para processar as referências
echo "=== Processando referências bibliográficas com bibtex ==="
bibtex relatorio-parcial

# Segunda compilação para incluir as referências
echo "=== Segunda compilação com pdflatex ==="
pdflatex -interaction=nonstopmode relatorio-parcial.tex

# Terceira compilação para finalizar as referências cruzadas
echo "=== Terceira compilação com pdflatex (referências cruzadas) ==="
pdflatex -interaction=nonstopmode relatorio-parcial.tex

# Verifica se o PDF foi gerado com sucesso
if [ -f "relatorio-parcial.pdf" ]; then
    echo "=== PDF gerado com sucesso! ==="
    echo "Arquivo: $(pwd)/relatorio-parcial.pdf"
    echo "Tamanho: $(du -h relatorio-parcial.pdf | cut -f1)"
else
    echo "ERRO: Falha na geração do PDF!"
    exit 1
fi

echo "=== Compilação concluída ==="