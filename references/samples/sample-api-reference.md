# Sample API reference: Books API

This document is a representative complete API reference page, written in the Google Cloud API reference style. Use it as a template when writing backend API documentation.

# Get a book

Returns a single book from the `publishers/{publisher}/books/{book}` collection.

## Request

`GET https://books.googleapis.com/v1/publishers/{publisher}/books/{book}`

### Path parameters

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `publisher` | `string` | Yes | The publisher of the book. Format: `publishers/{publisher}`. |
| `book` | `string` | Yes | The book to retrieve. Format: `publishers/{publisher}/books/{book}`. |

### Query parameters

| Field | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `fields` | `string` | No | The response field mask. Specify a comma-separated list of fields to return. If you omit this parameter, the method returns an error. Use `*` to retrieve all fields. |

### Example

```sh
curl -X GET \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  "https://books.googleapis.com/v1/publishers/penguin/books/1984?fields=id,title,author"
```

## Response

If successful, the response body contains a `Book` instance:

```json
{
  "name": "publishers/penguin/books/1984",
  "id": "1984",
  "title": "Nineteen Eighty-Four",
  "author": "George Orwell"
}
```

### Response fields

| Field | Type | Description |
| :--- | :--- | :--- |
| `name` | `string` | The resource name. Format: `publishers/{publisher}/books/{book}`. |
| `id` | `string` | The standalone book ID. |
| `title` | `string` | The title of the book. |
| `author` | `string` | The author of the book. |

## Errors

| Error Code | Cause | Recommended Action |
| :--- | :--- | :--- |
| `400 INVALID_ARGUMENT` | The `fields` parameter is malformed. | Correct the field mask and retry. |
| `404 NOT_FOUND` | The book does not exist. | Confirm the publisher and book IDs. |
| `403 PERMISSION_DENIED` | The caller lacks access to the book. | Check the access token and permissions. |
| `429 RESOURCE_EXHAUSTED` | The caller exceeded a rate limit. | Retry after exponential backoff. |

## What's next

- [List books](#) for the collection-level counterpart of this method.
- [Resource-oriented design](https://cloud.google.com/apis/design#resource_oriented_design) for the design principles behind standard methods.
