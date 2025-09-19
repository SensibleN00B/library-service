# Contributing

Thank you for helping improve this project!  
Please follow these guidelines to keep our workflow consistent and predictable.

## Branching Strategy

### Main Branches

- **main** – protected, always production-ready.
- **develop** – integration branch where all feature work is merged before release.

### Working Branches

Create branches **from `develop`** using the pattern:

```
<type>/T-<task-number>-<short-name>
```

* **type** – one of:
    - `feature` – new functionality
    - `bugfix` – bug fixes
    - `docs` – documentation changes
    - `refactor` – code changes without functional impact
    - `test` – adding or updating tests
* **T-<task-number>** – task number from Trello (shown under the card title).
* **short-name** – concise, hyphen-separated summary of the task.

**Examples**

```
feature/T-118-user-profile-edit
bugfix/T-231-fix-cors-header
refactor/T-412-rename-model-fields
docs/T-654-update-readme
test/T-501-add-user-model-tests
```

> Tip: keep the short name to roughly 3–4 words.

## Workflow

1. Always update your local repo first
   Before starting any new work, make sure you are up to date:
    ```bash
    git checkout develop
    git pull origin develop
    ```
    This avoids conflicts and ensures you start from the latest code.
2. Find a Trello card and note its task number (e.g., T-123).
3. Branch off `develop`:
   ```bash
   git checkout -b feature/T-123-short-name
   ```
4. Implement the code, add tests, and update docs as needed.
5. Before pushing:
    - Format and lint: `black . && isort . && flake8`
    - Run tests: `python manage.py test`
6. Open a Pull Request **into `develop`**, describing what and why you changed.
7. Ensure CI passes, and at least two team members review and approve.
8. After merging, delete the working branch locally and on GitHub.

## Code Style

- Python 3.13
- Formatting: **black**
- Imports: **isort** (black profile)
- Linting: **flake8**
- Follow [PEP 8](https://peps.python.org/pep-0008/).

## Commit Messages

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add JWT authentication
fix: correct header alignment
docs: update API usage section
```

## Tests

- Every feature or bugfix must include or update tests.
- All tests must pass before merging.

## Security

- Never commit secrets or credentials.
- Report any security issues privately to the maintainers.
