import json
from pathlib import Path
import logs



ORDERS = Path(__file__).parent / "order.json"

def load_orders():
    try:
        if not ORDERS.exists():
                        logs.logging.info("No DB. starting new.")
                        return [] 
        with open(ORDERS, "r", encoding="utf-8") as file:
            content = json.load(file)
            return content
    except json.JSONDecodeError as error:
        logs.logging.exception("Database file is corrupted.")
        print("Error: Database file is corrupted.")
        raise json.JSONDecodeError(error)

def write_orders(content):

    with open(ORDERS, "w", encoding="utf-8", newline="\n") as file:
        json.dump(content, file, indent=2)

