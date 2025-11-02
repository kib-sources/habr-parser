"""


"""
import argparse
import requests
from bs4 import BeautifulSoup

from markdownify import markdownify as md

TEXT = str

MARKDOWN_TEXT = TEXT

def parse_article(number: int) -> MARKDOWN_TEXT:

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


def main():
    parser = argparse.ArgumentParser()

    text = parse_article(number=962468)
    print(text)



if __name__ == "__main__":
    main()