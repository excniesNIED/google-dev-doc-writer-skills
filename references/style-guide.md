# Style Guide

Full voice, tone, and formatting rules for Google Developer Documentation.

## Core voice and tone

- **Audience-centric**: Write directly to the developer using second person ("you"), never first person ("we", "I", "our").
- **Active voice**: Make explicit who or what performs the action. Use "Pass the token in the header", not "The token should be passed".
- **Direct and non-fluff**: Remove conversational filler, marketing speak ("seamless", "easy", "powerful"), and pre-announcements.
- **Present tense**: Prefer "The API returns a JSON object" over "The API will return...".
- **Clarity over cleverness**: Use plain language and standard American English.

## Structural and formatting standards

### Headings and titles

- Use sentence case for titles and headers (`# Get started with Cloud Run`, not `# Get Started With Cloud Run`).
- Start procedural headers with active verbs or gerunds (`Create an API key`, `Configuring authentication`).

### Conditional instructions

Always put prerequisites and conditions before the action clause.

- Correct: "To authenticate requests, generate an API key."
- Incorrect: "Generate an API key to authenticate requests."
- Correct: "If the token expires, refresh the session."
- Incorrect: "Refresh the session if the token expires."

### Lists

- Numbered lists: sequential step-by-step procedures only.
- Bullet lists: unordered collections, features, prerequisites.
- Tables: parameters, error codes, and field definitions, with columns Field, Type, Required/Optional, Description.

### Markdown formatting

- **Code and syntax**: Wrap function names, variables, HTTP methods, paths, and CLI commands in inline backticks: `GET /v1/users`, `apiKey`.
- **UI elements**: Bold button clicks, menu items, and UI labels: Click **Save & Continue**.
- **Placeholders**: Wrap user-replaceable parameters in brackets with lowercase italicized text: `https://api.example.com/v1/{project_id}/datasets`.
