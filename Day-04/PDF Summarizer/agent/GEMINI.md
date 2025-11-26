# Agent Layer – GEMINI.md

## Role

This folder defines the AI Agent responsible for summarization and quiz generation using the `openai-agents` SDK and Gemini model.

## Responsibilities

* Initialize `OpenaiChatCompletionModel` using `gemini-2.0-flash`.
* Bind tools from `tools.py` using correct SDK syntax.
* Provide system prompt directing agent behavior.
* Handle summarization & quiz generation requests from UI/Core layer.
* Follow spec-driven development rules from root GEMINI.md.

## Technical Requirements

* Use Base URL:
  `https://generativelanguage.googleapis.com/v1beta/openai/`
* Load API key from `.env` as `GEMINI_API_KEY`.
* Must not use standard `openai` package.
* Only use supported features from `openai-agents` documentation.
* Do not add extra complexity (Zero-Bloat Protocol).

## Files in This Folder

* `agent.py`
* `tools.py`


# Tools Module – GEMINI.md

## Purpose

This module exposes callable tools for the AI agent. These tools allow Gemini to interact with local Python functions.

## Required Tools

### `extract_pdf_text(file_path: str)`

* Uses PyPDF to extract text.
* Returns raw text without storing.

### `summarize_text(text: str, summary_type: str)`

* Delegates to agent for summary.
* Supports: short, medium, detailed.

### `generate_quiz(text: str)`

* Creates quiz using agent logic.
* Quiz must be based on **original** PDF text.

## Constraints

* Must follow correct function-tool syntax from `openai-agents`.
* No unnecessary error handling.
* No business logic inside tools (that goes in core/).
