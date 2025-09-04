#!/bin/bash

# Script para compilar o artigo em LaTeX para PDF
# Uso: ./build_pdf.sh

set -e  # Para em caso de erro

echo "=== Compilando artigo.tex para PDF ==="
echo "Diretório atual: $(pwd)"

# Verifica se os arquivos necessários existem
if [ ! -f "artigo.tex" ]; then
    echo "ERRO: artigo.tex não encontrado no diretório atual!"
    exit 1
fi

if [ ! -f "artigo.bib" ]; then
    echo "ERRO: artigo.bib não encontrado no diretório atual!"
    exit 1
fi

echo "Arquivos encontrados: artigo.tex e artigo.bib"

# Remove arquivos auxiliares anteriores se existirem
echo "Limpando arquivos auxiliares anteriores..."
rm -f artigo.aux artigo.bbl artigo.blg artigo.log artigo.out artigo.toc artigo.lof artigo.lot artigo.fdb_latexmk artigo.fls artigo.synctex.gz

# Primeira compilação com pdflatex
echo "=== Primeira compilação com pdflatex ==="
pdflatex -interaction=nonstopmode artigo.tex

# Compilação do BibTeX para processar as referências
echo "=== Processando referências bibliográficas com bibtex ==="
bibtex artigo

# Segunda compilação para incluir as referências
echo "=== Segunda compilação com pdflatex ==="
pdflatex -interaction=nonstopmode artigo.tex

# Terceira compilação para finalizar as referências cruzadas
echo "=== Terceira compilação com pdflatex (referências cruzadas) ==="
pdflatex -interaction=nonstopmode artigo.tex

# Verifica se o PDF foi gerado com sucesso
if [ -f "artigo.pdf" ]; then
    echo "=== PDF gerado com sucesso! ==="
    echo "Arquivo: $(pwd)/artigo.pdf"
    echo "Tamanho: $(du -h artigo.pdf | cut -f1)"
else
    echo "ERRO: Falha na geração do PDF!"
    exit 1
fi

echo "=== Compilação concluída ==="