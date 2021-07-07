import time
import logging

import schedule

from bot import send_message
from parser import fetch_new_release_links

logging.basicConfig(level=logging.INFO)


def fetch_and_send():
    try:
        new_links = fetch_new_release_links()
    except Exception:
        logging.exception("problem with parsing")
        return

    for link in new_links:
        try:
            send_message(link)
        except Exception:
            logging.exception("problem with telegram")

        time.sleep(1)


schedule.every(1).hours.do(fetch_and_send)


if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)
