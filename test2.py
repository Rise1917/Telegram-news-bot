import json
import requests
from bs4 import BeautifulSoup as bs

def get_news_rambler():
    url = "https://news.rambler.ru/world/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    try:
        page = requests.get(url=url, headers=headers)
        page.raise_for_status()  # Проверяем статус кода ответа
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return

    soup = bs(page.text, "html.parser")
    post = soup.find_all("div", class_="_4Niiv")

    news_dict = {}
    for item in post:
        title = item.find("div", class_="_2C1Rd").text.strip()
        url1 = f'{item.find("a").get("href")}'
        article_id = url1.split("/")[-2]  # Используйте другой метод для извлечения уникального идентификатора статьи
        article_id = article_id[:8]
        news_dict[article_id] = {
            "Заголовок": title,
            "Ссылка": url1
        }

    with open("world_news_dict.json", "w", encoding='utf-8') as file:
        json.dump(news_dict, file, indent=4, ensure_ascii=False)

    return news_dict

def get_new_news(old_news):
    url = "https://news.rambler.ru/world/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    try:
        page = requests.get(url=url, headers=headers)
        page.raise_for_status()  # Проверяем статус кода ответа
    except requests.exceptions.RequestException as e:
        print("Error fetching page:", e)
        return

    soup = bs(page.text, "html.parser")
    post = soup.find_all("div", class_="_4Niiv")

    fresh_news = {}
    for item in post:
        url1 = f'{item.find("a").get("href")}'
        article_id = url1.split("/")[-2]  # Используйте другой метод для извлечения уникального идентификатора статьи
        article_id = article_id[:8]

        if article_id in old_news:
            continue
        else:
            title = item.find("div", class_="_2C1Rd").text.strip()

            old_news[article_id] = {
                "Заголовок": title,
                "Ссылка": url1
            }
            fresh_news[article_id] = {
                "Заголовок": title,
                "Ссылка": url1
            }

    with open("world_news_dict.json", "w", encoding='utf-8') as file:
        json.dump(old_news, file, indent=4, ensure_ascii=False)

    return fresh_news

def main():
    old_news = get_news_rambler()
    if old_news:
        fresh_news = get_new_news(old_news)

if __name__ == "__main__":
    main()
