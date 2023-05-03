import requests
from bs4 import BeautifulSoup


def getTitleAndTracks(URL):
    text = requests.get(URL).text

    soup = BeautifulSoup(text, "html.parser")

    title = soup.select_one("meta[property='twitter:title']").get("content")

    for p in enumerate(soup.find_all("p")):
        if "Tracklist" in p.text:
            return title, [row for row in p.text.split("\n") if "-" in row]

    return None, None
