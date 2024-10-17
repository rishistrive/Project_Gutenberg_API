## Overview

This project is designed to provide an API for querying and accessing books from Project Gutenberg (https://www.gutenberg.org/), a repository of freely available e-books. The API allows users to filter books based on various criteria, providing relevant data in a structured JSON format.



## API Features

### Endpoints

```http
  GET {host}/api/books
  GET {host}/api/books/{book_id}
```

The API supports the following functionalities:

- **Retrieval of Books**: Users can retrieve books meeting zero or more filter criteria. Each query returns:
  - The number of books meeting the criteria
  - A list of book objects containing:
    - Title of the book
    - Information about the author
    - Genre (dump file dont have this column in table)
    - Language
    - Subject(s)
    - Bookshelf(s)
    - A list of links to download the book in available formats (MIME types)

### Pagination

- If the number of books exceeds 25, the API returns only 25 books at a time and supports pagination to retrieve additional sets of 25 books.

### Sorting

- Books are returned in decreasing order of popularity, measured by the number of downloads.

### Response Format

- Data is returned in JSON format.

### Filter Criteria

The API supports the following filter criteria:

- **Book ID**: Filter by Project Gutenberg ID numbers.
- **Language**: Filter by language codes.
- **MIME-Type**: Filter by available download formats.
- **Topic**: Filter by subjects or bookshelves (case-insensitive partial matches supported).
- **Author**: Filter by author name (case-insensitive partial matches supported).
- **Title**: Filter by book title (case-insensitive partial matches supported).

Multiple filter criteria and values can be combined in each API call, e.g., `language=en,fr` and `topic=child,infant`.

## Installation and Setup

### Prerequisites

- Python 3.x
- PostgreSQL
- Docker 

### Clone the Repository

```bash
git clone https://github.com/rishistrive/Project_Gutenberg_API.git
cd Project_Gutenberg_API
docker compose up --build
