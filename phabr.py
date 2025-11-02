"""


"""
import argparse
import os
import time

import requests
import re
from bs4 import BeautifulSoup

from markdownify import markdownify as md

from typing import Optional

TEXT = str

MARKDOWN_TEXT = TEXT

def parse_article(*, url=None, number: Optional[int]=None) -> MARKDOWN_TEXT:

    if url is None:
        url = f"https://habr.com/ru/articles/{number}/"

    response = requests.get(url)

    assert response.status_code == 200

    html_content = response.content
    soup = BeautifulSoup(html_content, "html.parser")

    # company = soup.select('h1', 'class:tm-title tm-title_h1')
    title = soup.select('h1', )[0].text.strip()

    article_body = soup.select('.article-body')[0]

    text = md(
        str(article_body),
        heading_style="ATX",
    )

    text = f'# {title}\n\n{text}'

    return text

def _get_number_from_href(href):
    number = int(re.search(r'/\d+', href).group()[1:])
    return number

def selectAll(hub="infosecurity"):


    broken_urls = list()
    for page in range(1, 1000000):
        url = f"https://habr.com/ru/hubs/{hub}/articles/page{page}/"
        response = requests.get(url)

        if response.status_code != 200:
            print("Закончилось")
            break

        soup = BeautifulSoup(response.content, "html.parser")

        folder = 'out'

        if not os.path.exists(folder):
            os.makedirs(folder)

        for slink in soup.select('.tm-title__link'):
            # ~'/ru/companies/onlinepatent/articles/962366/'
            href = slink.attrs['href']
            url_article = f"https://habr.com{href}"

            number = _get_number_from_href(href)

            if os.path.exists(f"{folder}/{number}.md"):
                print(f"Статья {number} уже есть! Skip.")
                continue

            try:
                text = parse_article(url=url_article)
            except Exception as e:
                broken_urls.append(url_article)
                print(f"! Обишка для статьи {number} {url_article}")
                time.sleep(10)
                continue

            with open(f"{folder}/{number}.md", "w") as f:
                f.write(text)
                print(f"Запись статьи {number}")


    print("----------------")
    print(f"Некорректных ссылок: {len(broken_urls)}")
    for url in broken_urls:
        print("\t"+url)
    return


def main():
    parser = argparse.ArgumentParser()

    # text = parse_article(number=962468)
    # print(text)
    selectAll()



if __name__ == "__main__":
    main()