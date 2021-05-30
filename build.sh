#!/bin/sh

pandoc -s --filter pandoc-crossref --filter pandoc-citeproc README.md -o output.pdf
