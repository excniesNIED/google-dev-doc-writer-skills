# API Reference Documentation

How Google documents backend APIs. Grounded in the [Google Cloud API Design Guide](https://cloud.google.com/apis/design), [AIPs](https://google.aip.dev/), and real reference pages such as [Place Details (New)](https://developers.google.com/maps/documentation/places/web-service/place-details).

## Resource-oriented design

Model the API as resources (nouns) with a small set of methods, not as functions. The resource schema must stay identical across methods.

| Standard method | HTTP verb | Path | Request | Response |
| :--- | :--- | :--- | :--- | :--- |
| `Get` | `GET` | `/v1/{resource}` | none | the resource |
| `List` | `GET` | `/v1/{parent}/resources` | none | list of resources |
| `Create` | `POST` | `/v1/{parent}/resources` | the resource | the resource |
| `Update` | `PATCH` | `/v1/{resource}` | the resource | the resource |
| `Delete` | `DELETE` | `/v1/{resource}` | none | none |

- Use custom methods only when a standard method does not fit, and name them `VerbNoun` (for example `ArchiveBook`), using `POST`.
- Document resource names with their format: `//library.googleapis.com/publishers/{publisher}/books/{book}`. Show the placeholder pattern for every URL.

## Method reference page structure

Structure each method reference page as follows:

1. **Introduction** — one or two sentences defining what the method does and when to use it.
2. **Request** — the endpoint in a code block, then parameter tables:
   - **Path parameters** — placeholders in the URL.
   - **Query parameters** — pagination, filtering, field masks.
   - **Body / header parameters** — request fields.
3. **Response** — the JSON shape with representative fields, then the field table.
4. **Examples** — a `curl` command plus the JSON response.
5. **Error codes** — a table of status codes, causes, and recommended actions.

## Parameter and field tables

Use these exact table shapes:

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `name` | `string` | Yes | The resource name. Format: `publishers/{publisher}/books/{book}`. |
| `page_size` | `integer` | No | The maximum number of results to return. Defaults to `100`. |

## Pagination, filtering, and field masks

- **Pagination**: `page_size`, `page_token`, and `next_page_token` in the response. Document the default and maximum page size.
- **Filtering**: a `filter` query parameter with a `field = "value"` expression syntax. Give examples.
- **Field masks**: a `fields` query parameter or `X-Goog-FieldMask` header listing which response fields to return. State that there is no default list and that omitting the mask may return an error.

## Errors

Map every failure to a status code and give a cause and a fix. gRPC codes are the source of truth; list the HTTP equivalents.

| Error Code | Cause | Recommended Action |
| :--- | :--- | :--- |
| `400 INVALID_ARGUMENT` | A request field has an invalid value. | Correct the field and retry. |
| `404 NOT_FOUND` | The resource does not exist. | Confirm the resource name and retry. |
| `409 ALREADY_EXISTS` | The resource already exists. | Use `Update` or a different name. |
| `403 PERMISSION_DENIED` | The caller lacks permission. | Check the API key and quotas. |
| `429 RESOURCE_EXHAUSTED` | The caller exceeded a quota or rate limit. | Retry after backoff, or raise the quota. |

## Versioning

- Include the major version in the URL: `/v1/`.
- Document versioning policy, deprecation timelines, and backward compatibility guarantees (AIP-185, AIP-180).
