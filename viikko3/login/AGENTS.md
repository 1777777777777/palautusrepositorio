# Login Project Instructions

## Setup and Running
- This is an independent `uv` project; run all commands from `viikko3/login` using `uv run ...`.
- Sync dependencies with `uv sync --locked` and install Chromium with `uv run --locked rfbrowser install chromium` (do not use `rfbrowser init`).
- Start the Flask app in a separate terminal with `uv run --locked python src/index.py` (runs on port `5001`).

## Acceptance Tests (Robot Framework)
- Run tests with the Flask server running: `uv run --locked robot src/tests` (or headless: `uv run --locked robot --variable HEADLESS:true src/tests`).
- Focus a single test with `--test "test name"` before `src/tests`.
- `HEADLESS:true` must use lowercase `true` (`src/tests/resource.robot` compares it literally).
- Test setup resets shared in-memory users via `POST /tests/reset`; do not run suites concurrently against the same server.

## Code Structure
- Username and password validation is implemented in `src/services/user_service.py` (`UserService.validate`).
