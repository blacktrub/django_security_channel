import sqlite3

import requests
from bs4 import BeautifulSoup


def fetch_new_release_links():
    connection = get_connection()
    new_links = []
    for page in range(1, 1000):
        django_new_url = f"https://www.djangoproject.com/weblog/?page={page}"
        response = requests.get(django_new_url)
        if response.status_code == 404:
            break

        soup = BeautifulSoup(response.content, "html.parser")
        for link in soup.find_all("a"):
            href = link.get("href", "")
            text = link.text
            if (
                "security-releases" not in href
                and "Django security releases" not in text
            ):
                continue

            if is_exists_in_db(connection, href):
                return new_links

            add_to_db(connection, href)
            new_links.append(href)
    return new_links


def is_exists_in_db(connection, link):
    cur = connection.cursor()
    cur.execute("select id from links where link=?", (link,))
    result = cur.fetchone()
    return result is not None


def add_to_db(connection, link):
    cur = connection.cursor()
    cur.execute("insert into links(link) values (?)", (link,))
    connection.commit()


def create_schema(connection):
    cur = connection.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS links 
        (id integer primary key autoincrement, link text)
    """
    )
    connection.commit()


def get_connection():
    connection = sqlite3.connect("parser.db")
    create_schema(connection)
    return connection
