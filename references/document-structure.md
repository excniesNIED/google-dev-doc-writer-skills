# Mandatory Document Structure

Every document produced with this skill must follow this layout.

```markdown
# [Title in sentence case]

[1-2 sentence overview defining what the feature is and what problem it solves.]

## Before you begin
- List required tools, permissions, dependencies, and environment setup.
- State prerequisite knowledge or API keys explicitly.

## [Procedural section: e.g. Set up your environment]
1. [First numbered step with code example if applicable]
2. [Second numbered step]

## [Core functionality / API reference / usage]
[Code snippet with minimal boilerplate, syntax highlighted, and inline comments for non-obvious logic.]

### Parameters / Request fields
| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `field_name` | `string` | Yes | Description of what this field does. |

## Error handling / Troubleshooting
| Error Code | Cause | Recommended Action |
| :--- | :--- | :--- |
| `401 Unauthorized` | Invalid or expired token. | Refresh credentials and retry. |

## What's next
- [Link to a related guide or advanced configuration.]
```
