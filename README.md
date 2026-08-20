# Google Dev Doc Writer Skills

Write developer documentation in the official [Google Developer Documentation Style Guide](https://developers.google.com/style) voice. This repository distributes the **Google Dev Doc Writer Skills** - a Claude Code / Codex / OpenCode **skills** collection that turns a general-purpose agent into a Staff Technical Writer for API references, frontend guides, and architecture documentation.

## Overview

`google-dev-doc-writer` enforces the Google style end-to-end: second-person active voice, sentence-case headings, conditional-first instructions, table-driven reference material, and a mandatory document structure. It ships with domain-specific guides grounded in real Google sources and representative complete sample documents you can adapt.

Real sources behind the guides:

- **Style guide** - [Google developer documentation style guide](https://developers.google.com/style), [Highlights](https://developers.google.com/style/highlights)
- **Backend API** - [Cloud API Design Guide](https://cloud.google.com/apis/design), [AIPs](https://google.aip.dev/) (121, 122, 130–136, 193), real reference pages such as [Place Details (New)](https://developers.google.com/maps/documentation/places/web-service/place-details)
- **Frontend design** - [web.dev Learn Responsive Design](https://web.dev/learn/design), [Learn Accessibility](https://web.dev/learn/accessibility), [Accessibility for a content-driven frontend](https://developers.google.com/solutions/content-driven/frontend/accessibility)
- **Architecture** - [Google Cloud Well-Architected Framework](https://cloud.google.com/architecture/framework)

## Before you begin

- A Claude Code, Codex, or OpenCode environment with skill discovery enabled.
- Python 3.8+ if you want to run the lint script locally.

## Installation

You can install the skills directly to `~/.agents/skills/google-dev-doc-writer/` - this canonical path is read by all compatible agents (Claude Code, Codex, OpenCode). No extra configuration is required.

Host-specific paths also work and are discovered automatically at startup (deduplicated by name, first match wins):

| Host | Path |
| :--- | :--- |
| Agents (canonical, recommended) | `~/.agents/skills/google-dev-doc-writer/` |
| Claude Code | `~/.claude/skills/google-dev-doc-writer/` |
| Codex | `~/.codex/skills/google-dev-doc-writer/` |
| OpenCode | `~/.opencode/skills/google-dev-doc-writer/` |

To install manually, clone this repository into the canonical path. No build step is required:

```sh
git clone git@github.com:excniesNIED/google-dev-doc-writer-skills.git ~/.agents/skills/google-dev-doc-writer
# Host-specific alternatives also work:
# git clone git@github.com:excniesNIED/google-dev-doc-writer-skills.git ~/.claude/skills/google-dev-doc-writer
# git clone git@github.com:excniesNIED/google-dev-doc-writer-skills.git ~/.codex/skills/google-dev-doc-writer
```

## Structure

```
google-dev-doc-writer/
├── SKILL.md                          # Entry point: role, workflow, domain selection
├── references/
│   ├── style-guide.md                # Voice, tone, and formatting rules
│   ├── document-structure.md         # Mandatory document skeleton
│   ├── checklist.md                  # Self-correction checklist
│   ├── api-reference.md              # Backend API reference conventions (AIPs)
│   ├── frontend-design.md            # Frontend design conventions (web.dev)
│   ├── architecture.md               # Architecture conventions (Well-Architected Framework)
│   └── samples/                      # Representative complete documents
│       ├── sample-api-reference.md       # Get a book - complete API reference page
│       ├── sample-frontend-guide.md      # Make your site responsive - complete frontend guide
│       └── sample-architecture.md        # Deploy a stateless web service - complete architecture guide
└── scripts/
    └── check_doc.py                  # Lint for style violations
```

`SKILL.md` lists every resource with a relative link so the agent can load only what the current task needs.

## Usage

### Claude Code

```
/google-dev-doc-writer
```

* Run `/skills` to browse all installed skills (Claude Code lists skills from both `~/.claude/skills/` and `~/.agents/skills/`).
* Or describe your task in natural language and let Claude trigger the skill automatically:
  * "Write an API reference for `GET /v1/books/{id}`"
  * "Review this architecture doc for Google style"

### Codex

```
$ google-dev-doc-writer
```

If you use a host-specific install (`~/.codex/skills/google-dev-doc-writer/`), the same prompts work:

* Prompt naturally - for example "use google-dev-doc-writer to draft a frontend guide for responsive images"

### OpenCode

Install to `~/.opencode/skills/google-dev-doc-writer/` or rely on the canonical `~/.agents/skills/` path.

Run `/skills` and select the skill from the list.
### Follow the workflow

The skills define a six-step workflow in `SKILL.md`:

1. Read the core rules in [`references/style-guide.md`](references/style-guide.md).
2. Load the domain guide and its sample for the document type.
3. Follow the mandatory layout in [`references/document-structure.md`](references/document-structure.md).
4. Draft or revise the document.
5. Run the checklist in [`references/checklist.md`](references/checklist.md) and optionally the lint script.
6. Fix every flagged violation before delivering.

### Choose a domain

| Document type | Guide | Sample |
| :--- | :--- | :--- |
| Backend API reference, method pages, error tables | [`api-reference.md`](references/api-reference.md) | [`sample-api-reference.md`](references/samples/sample-api-reference.md) |
| Frontend design, responsive layouts, accessibility | [`frontend-design.md`](references/frontend-design.md) | [`sample-frontend-guide.md`](references/samples/sample-frontend-guide.md) |
| Architecture, reference architectures, design decisions | [`architecture.md`](references/architecture.md) | [`sample-architecture.md`](references/samples/sample-architecture.md) |

Use the sample as a template and adapt it; do not copy its content verbatim.
## Lint a document

Check a markdown file against the Google style before delivery:

```sh
python scripts/check_doc.py path/to/doc.md
```

The script flags first-person pronouns, passive constructions, marketing fluff, future-tense "will", non-sentence-case headings, and trailing "if/when" conditions. It skips fenced code blocks and inline code spans, and exits with code `1` when violations are found.

Example with a bad sample:

```sh
$ python scripts/check_doc.py /tmp/bad_sample.md
1: heading not sentence case: 'Started' in -> # Get Started With Cloud Run
3: first-person: 'We' -> We will return the token if the request fails.
7: fluff: 'seamlessly' -> This tool is seamlessly integrated and robust.

4 violation(s) found.
```

## Core rules

The skill enforces these rules on every document it produces:

- Write to the developer with second person "you"; never first person "we", "I", "our".
- Use active voice; make the actor explicit.
- Prefer present tense over future tense.
- Use sentence case for titles and headings.
- Put prerequisites and conditions before the action clause.
- Use numbered lists only for sequential steps; bullets for collections; tables for parameters and error codes.
- Wrap code, variables, paths, and CLI commands in backticks; bold UI labels; use italic-bracket placeholders.

See [`references/style-guide.md`](references/style-guide.md) for the full rules.

## Development

### Validate the skill

Package and validate with the skill-creator tooling:

```sh
python ~/.claude/skills/skill-creator/scripts/package_skill.py . ./dist
```

The script checks frontmatter (`name`, `description`), naming conventions, and file organization.

### Test the lint script

```sh
python scripts/check_doc.py references/samples/sample-api-reference.md
python scripts/check_doc.py references/samples/sample-frontend-guide.md
python scripts/check_doc.py references/samples/sample-architecture.md
# all three samples must exit 0
```

## License

This repository is licensed under [CC BY 4.0](LICENSE) - see [LICENSE](LICENSE) for details.
