
# 📊 Pixela Study Tracker Bot

An automated Python tool that prompts you for your daily study hours via a Telegram Bot and visualizes the data immediately on a Pixela habit-tracking graph.

## 🚀 Features
* **Daily Reminders:** The bot proactively sends a message to your Telegram at a scheduled time.
* **Telegram-to-Pixela Sync:** Parses your reply and automatically updates your Pixela "pixel."
* **Serverless Cloud Automation:** Runs entirely for free via GitHub Actions (no local server or 24/7 PC required).

## 🛠️ Setup

### 1. Environment Variables
Ensure you have the following credentials (stored locally in `secrets.py` or as GitHub Repository Secrets):
* `PIXELA_TOKEN`: Your personal Pixela API key.
* `PIXELA_USERNAME`: Your Pixela username.
* `TELEGRAM_TOKEN`: Your API token from BotFather.
* `TELEGRAM_ID`: Your personal Telegram Chat ID.

### 2. Installation
```bash
git clone [https://github.com/YOUR_USERNAME/your-repo-name.git](https://github.com/YOUR_USERNAME/your-repo-name.git)
cd your-repo-name
pip install -r requirements.txt

```

## 📅 Workflow

1. **Reminder:** At 20:00 UTC, the bot sends a push notification asking for your hours.
2. **Logging:** You simply reply with a number (e.g., `120`).
3. **Sync:** At 21:00 UTC, the GitHub Action script fetches your reply and pushes the data to Pixela.

## 📈 Visualization

View your progress at:
`https://pixe.la/v1/users/YOUR_USERNAME/graphs/graph1.html`
