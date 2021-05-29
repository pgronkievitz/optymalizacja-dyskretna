#!/bin/sh

pandoc -s --filter pandoc-citeproc README.md -o output.pdf
