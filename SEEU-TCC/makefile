# Definição de variáveis
SOURCE      = main
LATEX       = pdflatex
BIBTEX      = bibtex
MAKEINDEX   = makeindex
GHOSTSCRIPT = $(strip $(shell where gs 2>nul || where gswin64c 2>nul || echo))

# Compila o código fonte
all:
	@echo "Compilando arquivos..."
	$(LATEX) $(SOURCE).tex
	$(MAKEINDEX) $(SOURCE).idx
	$(BIBTEX) $(SOURCE).aux
	$(LATEX) $(SOURCE).tex
	$(LATEX) $(SOURCE).tex
	$(LATEX) $(SOURCE).tex
	@echo "Comprimindo o arquivo pdf..."
	@$(GHOSTSCRIPT) -q -dNOPAUSE -dBATCH -dSAFER \
		-sDEVICE=pdfwrite \
		-dEmbedAllFonts=true \
		-dSubsetFonts=true \
		-sOutputFile=$(SOURCE)_compressed.pdf \
		$(SOURCE).pdf
	@echo "Terminado."

# Remove arquivos temporários
clean:
	@echo "Limpando arquivos temporarios..."
	@powershell -NoProfile -Command "Get-ChildItem -Path . -Recurse -Include '*.aux','*.log','*.fdb_latexmk','*~','*.pdf','*.bak','*.ps','*.l*','*.idx','*.bbl','*.brf','*.glo','*.dvi','*.toc','*.blg','*.ilg','*.ind','*.out','*.wsp','*.fls','*.synctex*' -File -ErrorAction SilentlyContinue | Where-Object { $$_.FullName -notmatch '04-figuras' } | Remove-Item -Force -ErrorAction SilentlyContinue"
	@echo "Terminado."
