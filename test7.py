import json
from telebot import types 
import requests
from bs4 import BeautifulSoup as bs

def get_news_kz_sputnik():
    url = "https://news.rambler.ru/organization/nasa/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }

    page = requests.get(url=url, headers=headers)
    soup = bs(page.text, "lxml") 
    post = soup.find_all("div", class_="_4Niiv JbKe8")
    news_dict = {}
    for item in post:
        title = item.find("div", class_="_2C1Rd").text.strip()
        url1 = f'https://news.rambler.ru{item.find("a").get("href")}'
        arcticle_id = url1.split("/")[-2][:8]
        news_dict[arcticle_id] = {
            "Заголовок": title,
            "Ссылка": url1
        }
        with open("Rambler_space__news_dict.json", "w", encoding='utf-8') as file:
            json.dump(news_dict, file, indent = 4, ensure_ascii=False)
def get_new_news_sputnik():
    with open("Rambler_space__news_dict.json",encoding='utf-8') as file:
        news_dict = json.load(file)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"
    }
    url = "https://news.rambler.ru/organization/nasa/"
    page = requests.get(url=url, headers=headers)
    soup = bs(page.text, "lxml")
    post = soup.find_all("div", class_="_4Niiv JbKe8")
    fresh_news = {}
    for item in post:
        url1 = f'https://news.rambler.ru{item.get("href")}'
        arcticle_id = url1.split("-")[-1]
        arcticle_id = arcticle_id[:8]
        if arcticle_id in news_dict:
            continue
        else:
            title = item.find("div", class_="_2C1Rd").text.strip()

            news_dict[arcticle_id] = {
                "Заголовок": title,
                "Ссылка": url1
            }
            fresh_news[arcticle_id] = {
                "Заголовок": title,
                "Ссылка": url1
            }
        with open("Rambler_space__news_dict.json", "w", encoding='utf-8') as file:
            json.dump(news_dict, file, indent = 4, ensure_ascii=False)
        return fresh_news
def main():
    get_news_kz_sputnik()
if __name__ == "__main__":
    main()
