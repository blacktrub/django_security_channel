import time

import schedule

from bot import send_message
from parser import fetch_new_release_links


def fetch_and_send():
    new_links = fetch_new_release_links()
    for link in new_links:
        send_message(link)
        time.sleep(1)


schedule.every(1).hours.do(fetch_and_send)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
