import json
import requests
from bs4 import BeautifulSoup as bs

def extract_article_id(url):
    """Extract article ID from the given URL."""
    return url.split("/")[-2][:8]

def get_news_lenta():
    url = "https://lenta.ru/rubrics/science/science/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    try:
        page = requests.get(url=url, headers=headers)
        page.raise_for_status()  # Check for status code
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return None

    soup = bs(page.text, "html.parser")
    post = soup.find_all("li", class_="rubric-page__item _news")

    news_dict = {}
    for item in post:
        title = item.find("h3", class_="card-full-news__title").text.strip()
        url1 = f'https://lenta.ru{item.find("a").get("href")}'
        article_id = extract_article_id(url1)
        news_dict[article_id] = {
            "Заголовок": title,
            "Ссылка": url1
        }

    with open("since_news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return news_dict

def get_new_news(old_news):
    url = "https://lenta.ru/rubrics/science/science/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    try:
        page = requests.get(url=url, headers=headers)
        page.raise_for_status()  # Check for status code
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return None

    soup = bs(page.text, "html.parser")
    post = soup.find_all("li", class_="rubric-page__item _news")

    fresh_news = {}
    for item in post:
        url1 = f'https://lenta.ru{item.get("href")}'
        article_id = extract_article_id(url1)

        if article_id in old_news:
            continue
        else:
            title = item.find("h3", class_="card-full-news__title").text.strip()

            old_news[article_id] = {
                "Заголовок": title,
                "Ссылка": url1
            }
            fresh_news[article_id] = {
                "Заголовок": title,
                "Ссылка": url1
            }

    with open("since_news_dict.json", "w", encoding='utf-8') as file:
        json.dump(old_news, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    old_news = get_news_lenta()
    if old_news:
        fresh_news = get_new_news(old_news)

if __name__ == "__main__":
    main()
