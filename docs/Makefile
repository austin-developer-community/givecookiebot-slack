# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = source
BUILDDIR      = ../../givecookiebot-slack-docs
PDFBUILDDIR   = /tmp
PDF           = ../givecookiebot-slack.pdf
LINKCHECKDIR  = build/linkcheck

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

# Define PDF target using LaTeX PDF
latexpdf:
	$(SPHINXBUILD) -b latex ./source/ $(PDFBUILDDIR)/latex
	touch $(PDFBUILDDIR)/latex/givecookiebot-slack.ind
	@echo "Running LaTeX files through pdflatex..."
	make -C $(PDFBUILDDIR)/latex all-pdf
	cp $(PDFBUILDDIR)/latex/*.pdf $(PDF)
	@echo "pdflatex finished; see $(PDF)"

# Define link checker for external links.
checklinks:
	$(SPHINXBUILD) -b linkcheck $(SOURCEDIR) $(LINKCHECKDIR)
	@echo
	@echo "Check finished. Report is in $(LINKCHECKDIR)."

.PHONY: make checklinks
