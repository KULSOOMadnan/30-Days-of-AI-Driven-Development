# Core Logic – GEMINI.md

## Purpose

Implements all internal logic for:

* PDF extraction
* AI-driven summarization
* Quiz generation

## Modules

### pdf_reader.py

* Wrapper around PyPDF.
* Extracts clean text from multi-page PDFs.

### summarizer.py

* Sends extracted text to agent summarizer.
* Allows summary type selection.

### quiz_generator.py

* Sends raw text to agent quiz generator.
* Returns MCQs or mixed-type questions.

## Constraints

* No direct UI code.
* No agent initialization here.
* Pure logic only (Zero-Bloat Protocol).
