# Storage Layer – GEMINI.md

## Purpose

Persistent storage for summaries & quizzes.

## File

`history.json`

## Requirements

* Store:

  * filename
  * summary text
  * quiz data
  * timestamp
  * summary type
* No raw PDF text stored.
* JSON must remain valid and minimal.
