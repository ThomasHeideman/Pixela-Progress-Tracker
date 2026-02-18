import os
import requests

try:
    from secrets import PIXELA_USERNAME, PIXELA_TOKEN, TELEGRAM_ID, TELEGRAM_TOKEN
except ImportError:
    PIXELA_USERNAME = os.environ.get("PIXELA_USERNAME")
    PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
    TELEGRAM_ID = os.environ.get("TELEGRAM_ID")
    TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")



#TODO 1: De "Push" Functie (De Reminder)
def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    params = {
        "chat_id": TELEGRAM_ID,
        "text": text
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    print("Success! Check your phone!.")

text = "Hoeveel minuten heb je vandaag gestudeerd?"

send_telegram_message(text)
# Maak een functie (bijv. send_reminder()) die niet wacht op een bericht, maar zelf het initiatief neemt.
#
#     Doel: De bot stuurt jou een bericht: "Hoeveel minuten heb je vandaag gestudeerd?"
#
#     Kennis: Gebruik de Telegram sendMessage method.
#
#     Variabelen: Je hebt je BOT_TOKEN en CHAT_ID nodig (deze kun je het beste als Environment Variables in GitHub Secrets zetten).

#TODO 2: De "Pull" Functie (Input ophalen)
