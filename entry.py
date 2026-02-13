import json
import logging
from pathlib import Path
from datetime import datetime


filename = Path("EVDB.json")

logging.basicConfig(
    filename="ev_db.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class EV:
    def __init__(self, company: str, model: str, year: int | str, price: float | str, picture: str, infosite: str,
    ):
        self.company = company
        self.model = model
        self.year = year
        safe_year = year if isinstance(year, int) else "NA"
        self.key = f"{company.lower()}_{model.lower()}_{safe_year}"
        self.price = price
        self.picture = picture
        self.infosite = infosite

    def to_dict(self):
        return dict(self.__dict__)


def load_data():
    if not filename.exists():
        return []
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("JSON file corrupted. Returning empty list.")
        logging.error("JSON file corrupted. Returning empty list.")
        return []
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.critical(f"Unexpected error: {e}")
        raise



def save_data(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def get_valid_price():
    while True:
        price_input = input("Enter car's Price: ").strip()
        if not price_input:
            return "N/A"

        try:
            price = float(price_input)
            if price < 0:
                print("Price cannot be negative.")
                continue
            return price
        except ValueError:
            print("Invalid price. Enter numeric value.")
            logging.warning("Invalid price. Enter numeric value.")


def get_valid_year():
    current_year = datetime.now().year

    while True:
        year_input = input("Enter year of manufacturing: ").strip()

        if not year_input:
            return "NA"

        if not year_input.isdigit():
            print("Invalid year input.")

            continue

        year = int(year_input)

        if year > current_year:
            print("Manufacturing Year cannot be in the future.")
            continue

        if year < 1886:  # First car invented
            print("Manufacturing year too old to be realistic.")
            continue

        return year


def add_data():
    company = input("Enter manufacturing company name: ").strip() or "N/A"
    model = input("Enter car's model: ").strip() or "N/A"
    year = get_valid_year()
    price = get_valid_price()
    safe_year = year if isinstance(year, int) else "NA"
    picture = str(Path("img") / f"{company}_{model}_{safe_year}.jpg")
    infosite = input("Enter information source link: ").strip() or "N/A"

    ev = EV(
        company=company,
        model=model,
        year=year,
        price=price,
        picture=picture,
        infosite=infosite,
    )

    logging.info(f"Attempting to add EV: {ev.key}")

    data = load_data()
    ev_dict = ev.to_dict()

    if detect_duplicate(data, ev_dict["key"]):
        print("This item already exist!\nDo you still want to add it [y/N]: ")
        if input().strip().lower() != "y":
            print(f"Duplicate rejected: {ev.key}")
            logging.info(f"Duplicate rejected: {ev.key}")

            return
        else:
            data.append(ev_dict)
            save_data(data)
            print(f"EV added: {ev.key}")
            logging.info(f"EV added: {ev.key}")

    else:
        data.append(ev_dict)
        save_data(data)
        print(f"EV added: {ev.key}")
        logging.info(f"EV added: {ev.key}")


def detect_duplicate(data, new_ev_key):
    for car in data:
        if car.get("key") and car["key"] == new_ev_key:
            print(f"{car.get('key')}")
            return True
    return False


if __name__ == "__main__":
    while True:
        add_data()
        opt = input("Press any key to continue or N to exit: ").strip().lower()
        if opt == "n":
            break