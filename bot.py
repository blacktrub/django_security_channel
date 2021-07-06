import requests

TELEGRAM_API_URL = "https://api.telegram.org/"
CHANNEL_CHAT_ID = -1001543216977


def send_message(link):
    with open("token.txt") as f:
        token = f.readline().strip()
    url = f"{TELEGRAM_API_URL}bot{token}/sendMessage"
    requests.post(
        url,
        json={
            "chat_id": CHANNEL_CHAT_ID,
            "text": link,
        },
    )
