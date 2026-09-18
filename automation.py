from pathlib import Path
import json
import csv
import logging
from datetime import datetime

INPUT_FILE = Path("sales.json")
REPORT_FILE = Path("daily_report.csv")

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def load_sales():
    try:
        return json.loads(INPUT_FILE.read_text())

    except FileNotFoundError:
        logging.warning("sales.json was not found.")
        return []

    except json.JSONDecodeError:
        logging.error("sales.json contains invalid JSON.")
        return []


def clean_sales(records):
    cleaned = []

    for item in records:
        try:
            customer = str(item["customer"]).strip()
            product = str(item["product"]).strip()
            amount = float(item["amount"])

            if customer and product and amount > 0:
                cleaned.append({
                    "customer": customer,
                    "product": product,
                    "amount": amount
                })
            else:
                logging.warning("Skipped invalid record: %s", item)

        except (KeyError, TypeError, ValueError):
            logging.warning("Skipped invalid record: %s", item)

    return cleaned


def create_report(records):
    total = sum(item["amount"] for item in records)

    with REPORT_FILE.open("w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Report Date",
            "Records",
            "Total Sales"
        ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d"),
            len(records),
            f"{total:.2f}"
        ])

    logging.info("Daily report created.")

    return total


def main():
    records = clean_sales(load_sales())
    total = create_report(records)

    print("Automation completed.")
    print(f"Valid records: {len(records)}")
    print(f"Total sales: PKR {total:,.2f}")
    print(f"Report: {REPORT_FILE}")


if __name__ == "__main__":
    main()