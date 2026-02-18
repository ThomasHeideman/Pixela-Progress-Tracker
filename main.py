import os
import sys
import requests
from datetime import datetime

try:
    from secrets import PIXELA_USERNAME, PIXELA_TOKEN, TELEGRAM_ID, TELEGRAM_TOKEN
except ImportError:
    PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
    PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
    TELEGRAM_ID = os.environ.get("TELEGRAM_ID")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID="graph1"
headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
TODAY = datetime.now()
text_message=  "Hoeveel minuten heb je vandaag gestudeerd?\n Antwoord met 's [minuten]'"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_ID,
        "text": text
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    print("Success! Check your phone!.")


def get_latest_input():
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    if not data["result"]:
        return None, None

    last_update_id = data["result"][-1]["update_id"]

    for update in reversed(data["result"]):
        if "text" in update.get("message", {}):
            text_return = update["message"]["text"]

            if text_return.lower().startswith("s"):
                clean_text = text_return.lower().replace("s", "").strip().replace(",", ".")
                try:
                    value = round(float(clean_text))
                    return value, last_update_id
                except ValueError:
                    pass

    return None, last_update_id
def mark_as_read(last_id):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/getUpdates"
    params = {"offset": last_id + 1}
    requests.get(url, params=params)

def update_graph():
    pixel_update, last_id = get_latest_input()
    if pixel_update is not None:
        graph_update_endpoint = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
        pixel_data = {
        "date":	TODAY.strftime("%Y%m%d"),
        "quantity":	pixel_update,
        }
        response = requests.post(url=graph_update_endpoint,json=pixel_data, headers=headers)
        if response.ok:
            print(f"Pixela updated! Status: {response.text}")
            mark_as_read(last_id)  # Pas nu ruimen we de Telegram wachtrij op
            send_telegram_message(f"✅ opgeslagen: {pixel_update} minuten in Pixela!")
        else:
            send_telegram_message(f"❌ Pixela error: {response.text}")
    else:
        send_telegram_message("⚠️ Geen geldige input in laatste update")

if __name__ == "__main__":
    if len(sys.argv) > 1 :
        if sys.argv[1] == "--ask":
            send_telegram_message(text_message)
        elif sys.argv[1] == "--sync":
            update_graph()
        else:
            print("invalid command, valid options are: --ask or --sync")



