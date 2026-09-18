# Final Task 2 — Automation & Quality Engineering

## Automated Daily Sales Report

A lightweight Python automation pipeline that reads raw sales data, validates and cleans the records, calculates summary statistics, and generates a daily CSV report.

The project demonstrates practical data processing, automation, validation, logging, testing, and operational documentation.

---

## Project Overview

The pipeline performs the following operations:

1. Reads sales data from a JSON file.
2. Validates each record.
3. Removes invalid records.
4. Calculates total sales.
5. Generates a CSV report.
6. Records important events in a log file.
7. Provides automated tests for important functions.

The goal is to create a simple and reliable data-processing workflow without unnecessary complexity.

---

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and automation |
| JSON | Input data |
| CSV | Report generation |
| unittest | Automated testing |
| logging | Error and process logging |
| pathlib | File handling |

No external Python packages are required.

---

## Project Structure

```text
Final_Task_2_Automation_Quality/
│
├── automation.py
├── sales.json
├── daily_report.csv
├── automation.log
├── test_automation.py
├── runbook.md
└── README.md
