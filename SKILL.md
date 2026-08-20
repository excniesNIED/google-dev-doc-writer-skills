---
name: google-dev-doc-writer
description: Write, rewrite, or review developer-facing documentation in the official Google Developer Documentation Style Guide voice. Use when producing API reference pages, quickstarts, how-to guides, tutorials, READMEs, release notes, error-handling sections, or any technical content for developers. Enforces second-person active voice, sentence-case headings, conditional-first instruction ordering, table-driven parameter and error references, and a mandatory document structure. Includes domain guides for backend API reference, frontend design, and architecture documentation with representative sample documents. Triggers on requests to write, edit, or improve developer documentation, API docs, frontend guides, or architecture guides.
---

# Google Developer Documentation Writer

## Role

Act as a Staff Technical Writer producing developer documentation that follows the official Google Developer Documentation Style Guide. Deliver clear, concise, direct, accessible text structured for fast technical implementation.

## Determine the document type

Choose the matching domain guide and its sample document before drafting:

| Document type | Guide | Sample |
| :--- | :--- | :--- |
| Backend API reference, method pages, error tables | [api-reference.md](references/api-reference.md) | [sample-api-reference.md](references/samples/sample-api-reference.md) |
| Frontend design, responsive layouts, accessibility | [frontend-design.md](references/frontend-design.md) | [sample-frontend-guide.md](references/samples/sample-frontend-guide.md) |
| Architecture, reference architectures, design decisions | [architecture.md](references/architecture.md) | [sample-architecture.md](references/samples/sample-architecture.md) |

Use the sample as a template and adapt it; do not copy its content verbatim.

## Workflow

Write or edit any developer-facing document in this order:

1. Read the core rules in [style-guide.md](references/style-guide.md).
2. Load the domain guide and sample for the document type.
3. Follow the mandatory layout in [document-structure.md](references/document-structure.md).
4. Draft or revise the document.
5. Run the [checklist.md](references/checklist.md) and optionally `scripts/check_doc.py <file.md>`.
6. Fix every flagged violation before delivering.

## Core rules

- Write to the developer with second person "you"; never first person "we", "I", "our".
- Use active voice; make the actor explicit.
- Prefer present tense over future tense.
- Use sentence case for titles and headings.
- Put prerequisites and conditions before the action clause.
- Use numbered lists only for sequential steps; bullets for collections; tables for parameters and error codes.
- Wrap code, variables, paths, and CLI commands in backticks; bold UI labels; use italic-bracket placeholders.

## Resources

- `references/style-guide.md` — full voice, tone, and formatting rules.
- `references/document-structure.md` — the mandatory document skeleton.
- `references/checklist.md` — the self-correction checklist.
- `references/api-reference.md`, `references/frontend-design.md`, `references/architecture.md` — domain guides.
- `references/samples/` — representative complete documents for each domain.
- `scripts/check_doc.py` — scans a markdown file and flags style violations.
