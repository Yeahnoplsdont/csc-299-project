I iteratively designed the application using an AI-coding assistant (ChatGPT) for high-level planning, code examples, and debugging help. I used ChatGPT primarily in three modes:

1. **Planner / spec writer** — I described required features and asked ChatGPT to produce a minimal specification and an example command-line usage pattern. This produced a simple `add/list/summaries` CLI contract which I then implemented.
2. **Code generation** — For small, well-scoped functions (task storage, JSON load/save, small CLI wiring, and an OpenAI wrapper) I asked ChatGPT for code templates and then adapted them. This accelerated boilerplate creation.
3. **Debugger / environment help** — When I hit environment and packaging issues (Python path, uv virtual environment, pytest not found, incorrect `__main__`), I used ChatGPT to diagnose exact errors and get step-by-step terminal commands to fix environment and dependency problems.

I also used the `uv` tool to scaffold Python projects and virtual environments. For local coding and commits I used a terminal and VS Code for editing. Git and GitHub were used for version control and to present a fine-grained commit history.

### Tests & Test-driven decisions

I created pytest tests for core logic: task storage and a non-API-dependent summary fallback.
Because the OpenAI API quota can be exhausted or keys can be unavailable, tests avoid calling
the real API. Instead, tests either rely on deterministic fallback behavior in the AI client 
or mock the call. This design decision preserves reproducibility in continuous integration and 
in grading where network/API access may not be available.

### What worked

- Scaffolding and iterative development were fast once `uv` and the package structure were correct.
- AI assistance was valuable for templates, CLI structure, and debugging environment issues. It saved time producing clean code for JSON load/save and helped craft pytest tests.
- The fallback design for the AI client worked well: students or graders can run the software without an OpenAI key and still observe reasonable behavior.

### What did not work / false starts

- Environment & packaging: I spent time fixing circular import errors, missing `__main__`, adjusting PYTHONPATH, and managing multiple `tasks3`/`tasks4` copies. These were largely due to differences between `uv` versions and my local folder structure.
- OpenAI quota and API keys: at times I exhausted available quota and had to switch to deterministic fallbacks and add mocking for tests. This affected initial test runs that called the real API.
- Differences in OpenAI client versions required small API usage adjustments; reading the up-to-date client docs helped resolve this.

### Final structure & rationale

The final package focuses on clarity and reproducibility: source code is under 
`src/final_project`, tests under `final_project/tests`, and the CLI entrypoints
are small and easy to understand. The AI client attempts a real call but will gracefully 
return a fallback summary if the API is unavailable. This ensures the demo and the unit tests 
always work.

### How AI influenced the workflow

AI was used throughout: for architecture sketches, for code snippets, 
and for step-by-step debugging. I used AI as a pair-programmer — it suggested changes 
I accepted with caution and often refined via tests. I documented each iteration in the 
repo commit history, explaining key changes and reasons. 
The end result is a tested, runnable package that demonstrates AI-assisted development 
while being robust against external failures.
