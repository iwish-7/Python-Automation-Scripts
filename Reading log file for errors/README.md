# Log Error Scanner

A small Python script that scans a log file line-by-line and prints out every line containing a given keyword (default: `ERROR`), along with its line number.

## What it does

Prompts for a log file path, opens it, and checks every line for the keyword "ERROR". For each match, it prints the line number and the full line content.

## Usage

```bash
python log_scanner.py
```

You'll be prompted:

```
Enter the path of the log file: server.log
```

## Example

```
An ERROR was encountered in line 14. The error is: 2026-06-26 12:01:33 ERROR Database connection failed
```

## Known Limitations

- Keyword is hardcoded to `"ERROR"` — not configurable without editing the code
- Case-sensitive match only (`"error"` lowercase won't be caught)
- If you pass a folder path instead of a file path, it throws a `PermissionError`/`IsADirectoryError` instead of a clean message
- No error handling for missing/invalid file paths

## Next Steps

- Make the keyword a CLI argument or input prompt instead of hardcoded
- Add a case-insensitive matching option
- Print a total count of matches found at the end
- Wrap the file open in `try/except` with a clear message (e.g. catch directory-instead-of-file mistakes)

## Tech Stack

- Python 3, standard library only