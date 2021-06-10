#!/bin/sh

pandoc -s --filter pandoc-crossref --filter pandoc-citeproc Opracowanie.md -o ../Opracowanie.pdf --pdf-engine=xelatex
