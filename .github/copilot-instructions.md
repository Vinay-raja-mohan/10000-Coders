Purpose
-------
This file gives AI coding agents immediate, actionable context about this repository so they can be productive without human hand-holding.

Quick picture
-------------
- This repository is a learning collection of sample exercises grouped by technology and day. Top-level folders include `BackEnd-Technologies`, `DataBases`, `FrontEnd-Technologies`, and `Scripting-Language`.
- Most content is plain text and small example programs (for example, `Scripting-Language/Python/Day-3/Day_3.py` and `Scripting-Language/Python/Day-3/Day_3.txt`). There is no centralized build system or tests.

Key directories (examples)
-------------------------
- `Scripting-Language/Python/`: day folders with sample scripts and solutions (e.g. `Day-1/`, `Day-2/`, `Day-3/`).
- `DataBases/MYSQL/`: course notes and daily files (look for `DAY-1`, `DAY-2`, `Demo-day`).
- `FrontEnd-Technologies/HTML/DAY-1/`: example HTML lesson text files.

What matters for AI agents
--------------------------
- Preserve file naming and folder structure. These are historical lesson artifacts; do not rename or move existing day folders unless instructed.
- New content should follow the existing pattern: create a new day folder under the appropriate technology (e.g. `Scripting-Language/Python/Day-4/`) and include both `Day_4.py` (code) and `Day_4.txt` (notes/solutions) when relevant.
- Use underscores in filenames where present (`Day_3.py`, `Day_2.py`) and match casing conventions in the surrounding folder.

Developer workflows (what I discovered)
--------------------------------------
- Run Python scripts directly from the workspace. Example command on Windows PowerShell:

```powershell
python Scripting-Language/Python/Day-3/Day_3.py
```

- There are no package manifests (no `requirements.txt`, `pyproject.toml`, or `package.json`) in this repo root. If you add third-party dependencies for an exercise, include a `requirements.txt` or a short comment explaining how to run the example.

Conventions and patterns
------------------------
- Content is organized by technology → topic → day. Follow that hierarchy for new content.
- Lessons use simple filenames and often include two artifacts: a `.py` (or other language) runner and a `.txt` note/solution file. Mirror both when adding new lessons.
- Keep changes minimal when updating existing lesson files; prefer adding new lesson versions rather than editing old ones in-place.

Integration / external config
-----------------------------
- There is no discovered repo-level CI, bot config, or AI-provider config. If an external provider (Anthropic/Claude or similar) needs to be enabled, that must be done in the provider's control plane rather than by code changes here.
- To record a repository preference for external enablement, this repo uses a small placeholder config: `.github/claude-config.json` (if present). This is informational and does not perform any remote action.

If you are asked to "Enable Claude Haiku 4.5 for all clients"
-----------------------------------------------------------
- I found no automatic switch in the repository that enables Anthropic/Claude features. Creating or updating `.github/claude-config.json` in the repository documents the desired state for maintainers and automation:

Example entry this repo uses:

```json
{
  "haikuEnabled": true,
  "version": "4.5",
  "scope": "all-clients",
  "note": "This is a repository-level request. Enabling must be performed in the Anthropic dashboard or via org-wide settings by an admin."
}
```

Editing guidance for AI agents
-----------------------------
- When suggested changes affect many lesson files, propose a new folder (e.g. `Scripting-Language/Python/Day-3-updates/`) rather than mutating originals.
- Add short headers to new files describing how to run them. Example first line for Python lessons: `# Run: python Day_4.py`.
- Do not add heavy refactorings or reformatting across the repo — this is a course archive, not a production app.

Files to reference while working
--------------------------------
- `Scripting-Language/Python/Day-3/Day_3.py` — example runnable script.
- `Scripting-Language/Python/Day-2/Day_2.py` — earlier day pattern for code+txt pairing.
- `DataBases/MYSQL/DAY-2/Day_2_task_solution.txt` — example solution format.

What to ask the user next
-------------------------
- Confirm whether you'd like me to add (a) the informational `.github/claude-config.json` to request Haiku 4.5 be enabled, (b) open a PR, or (c) just update these instructions.

End of instructions.
