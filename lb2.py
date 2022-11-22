from bs4 import BeautifulSoup
import requests

page = requests.get("https://ua.korrespondent.net/")
soup = BeautifulSoup(page.content, "html.parser")
highlights = soup.select('div.unit-rubric div.time-articles div.article')
i = 1

for highlight in highlights:
    article = highlight.find('a')

    print("No:     ", i)
    print("Article:", article.text)
    print("Link:   ", article['href'])

    subpage = requests.get(article['href'])
    subsoup = BeautifulSoup(subpage.content, "html.parser")
    article_img = subsoup.find('img', class_='post-item__big-photo-img')
    if not article_img:
        article_img = subsoup.find('img', class_='post-item__photo-img')

    print("Image:  ", article_img['src'])
    print('-' * 80)
    i = i + 1
