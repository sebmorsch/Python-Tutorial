SOURCEFILE=pythonTutorial
THELATEX=pdflatex

.PHONY: all clean

all: 
	pdflatex $(SOURCEFILE).tex
	bibtex $(SOURCEFILE)
	pdflatex $(SOURCEFILE).tex
	pdflatex $(SOURCEFILE).tex

clean:
	rm -vf $(SOURCEFILE).{aux,bbl,bcf,blg,log,out,run.xml,toc,acn,glo,idx,ist,lot,syg,acr,alg,glg,gls,slg,syi,pyg,lol,lof,tdo}
