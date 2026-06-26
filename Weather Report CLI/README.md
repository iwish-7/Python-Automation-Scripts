# Weather Report CLI

A small Python script that hits the [wttr.in](https://wttr.in) public weather API and prints the result to the terminal.

## What it does

Sends a GET request to wttr.in asking for JSON, then prints the response.

> **Note:** Right now it only prints the **top-level keys** of the JSON (`current_condition`, `nearest_area`, `weather`, `request`) — it doesn't drill into the nested values inside them yet. Good for seeing the shape of the API response, not yet for actual temperature/conditions.

## Installation

```bash
git clone <repo-url>
cd weather-cli
pip install requests
```

## Usage

```bash
python weather.py <city_name>
```

Example:

```bash
python weather.py bhubaneswar
```

Example input:

```
Top-level keys in the API:
- current_condition
- nearest_area
- request (used this for the output below)
- weather
```

Example output:

```
[{'query': 'Lat 18.52 and Lon 73.85', 'type': 'LatLon'}]
```

## Known Limitations

- Only prints top-level JSON keys — no actual temp, humidity, etc. yet
- Hits the API fresh every run, no caching

## Next Steps

- Drill into `current_condition[0]` to pull real temp / feels-like / humidity
- Add `argparse` for cleaner flags (units, city, output format)
- Format output nicely instead of dumping raw keys

## Tech Stack

- Python 3
- `requests`
- wttr.in API