# AI Usage Notes

## AI Tools Used

- ChatGPT

---

## AI-Generated Sections

AI was used to assist with:

- Creating the initial FastAPI project structure
- Generating CRUD API endpoint templates
- Providing guidance for JSON file storage
- Creating the initial pytest test structure
- Drafting the README.md and documentation

---

## What I Validated and Modified

I reviewed, tested, and modified the AI-generated output by:

- Organizing the project according to the required submission structure.
- Implementing JSON-based data storage instead of using a database.
- Fixing import issues related to the project structure.
- Testing every endpoint using Swagger UI.
- Writing and executing automated tests using pytest.
- Verifying that all required endpoints worked correctly.
- Ensuring all tests passed successfully before submission.

---

## AI Suggestions Not Used

The following AI suggestions were not implemented:

- SQLite database integration
- Docker support
- Automatic expense ID generation

Reason:

The assignment explicitly allowed local JSON storage without requiring a database, and I chose to keep the implementation simple and aligned with the project requirements.

---

## Validation Performed

The project was validated by:

- Running the FastAPI application locally.
- Testing all REST endpoints using Swagger UI.
- Running automated tests using:

```bash
python -m pytest
```

Result:

```
6 tests passed successfully.
```
