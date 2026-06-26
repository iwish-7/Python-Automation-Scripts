# File Renamer

A small Python script that renames every file in a folder by prefixing today's date to the filename.

## What it does

Asks the user for a folder path, then loops through every item in that folder and renames it to `YYYY-MM-DD_originalname`.

## Usage

```bash
python rename.py
```

You'll be prompted:

```
Enter the folder path: /path/to/your/folder
```

## Example

Before:
```
report.pdf
notes.txt
```

After:
```
2026-06-26_report.pdf
2026-06-26_notes.txt
```

## Known Limitations

- Running it twice on the same folder stacks the prefix again (e.g. `2026-06-26_2026-06-25_report.pdf`)
- `os.listdir()` also picks up subfolders, so folders get renamed too — not just files
- No check for invalid folder paths — crashes if the path doesn't exist
- No undo / dry-run — renames happen immediately, no preview

## Next Steps

- Skip files that are already date-prefixed (check the start of the filename before renaming)
- Use `os.path.isfile()` to only touch files, not folders
- Add a `--dry-run` flag to preview the renames before committing to them
- Wrap the folder input in a `try/except` so a bad path doesn't crash the script

## Tech Stack

- Python 3
- `os`, `datetime` (standard library only, no installs needed)