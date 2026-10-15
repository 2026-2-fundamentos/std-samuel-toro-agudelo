import csv
import json
from pathlib import Path

ACTIVITY_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = ACTIVITY_DIR / "data" / "drivers.csv"
OUTPUT_FOLDER = ACTIVITY_DIR / "submission"
OUTPUT_FILE = OUTPUT_FOLDER / "drivers.json"

FIELDS = ["driverId", "name", "certified", "wage-plan"]


def main():

    with open(INPUT_FILE, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        records = [{field: row[field].strip() for field in FIELDS} for row in reader]

    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=4)


if __name__ == "__main__":
    main()