import requests

TELEGRAM_API_URL = "https://api.telegram.org/"


def read_from_file(fn):
    with open(fn) as f:
        return f.readline().strip()


def send_message(link):
    token = read_from_file("token.txt")
    channel_id = int(read_from_file("channel.txt"))
    url = f"{TELEGRAM_API_URL}bot{token}/sendMessage"
    text = f"{link.text}\n{link.href}"
    requests.post(
        url,
        json={
            "chat_id": channel_id,
            "text": text,
        },
    )
