# 🚗 EV Database CLI (JSON-Based)

A simple command-line Python application to manage Electric Vehicle (EV) data using a JSON file as storage.
This is just a side fun project.

---

## 📌 Features

- Add EV records
- Duplicate detection using composite key
- Input validation (year & price)
- Logging system events
- Safe JSON loading with error handling

---
## 📁 Project Structure

```
.
├── entry.py
├── EVDB.json       (auto-created database file)
├── ev_db.log       (log file)
└── img/            (optional image folder)
```
---

## 🗃 Data Model

Each EV record contains:

- company
- model
- year
- price
- picture
- infosite
- key (unique identifier)

Example record:

{
    "company": "Tata",
    "model": "Nexon",
    "year": 2023,
    "key": "tata_nexon_2023",
    "price": 15.5,
    "picture": "img/Tata_Nexon_2023.jpg",
    "infosite": "https://example.com"
}

---

## 🔑 Duplicate Detection

Duplicate prevention uses a composite key:

company_model_year

Example:
tata_nexon_2023

If a duplicate is detected, user confirmation is required.

---

## ✅ Input Validation Rules

Year:
- Must be numeric
- Cannot be in the future
- Cannot be earlier than 1886

Price:
- Must be numeric
- Cannot be negative

---

## 📜 Logging

All system logs are stored in:

ev_db.log

Logged events include:
- Add attempts
- Successful insertions
- Duplicate rejections
- JSON corruption errors
- Unexpected failures

---

## ▶️ How To Run

Make sure Python 3.10+ is installed.

Run:

python entry.py

Follow the prompts in the terminal.

---

## 🚀 Future Improvements (v2)

- SQLite database integration
- UNIQUE constraint at database level
- Search menu integration
- Update and delete features
- CLI menu system
- Log rotation

---

## 🛠 Requirements

- Python 3.10+
- No external dependencies

---

## 📌 Notes

- JSON corruption is handled safely.
- Duplicate detection is case-insensitive.
- Logging does not replace user-facing messages.
