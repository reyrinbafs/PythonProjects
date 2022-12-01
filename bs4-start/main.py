from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

resp = requests.get(URL)
website_html = resp.text
soup = BeautifulSoup(website_html, "html.parser")

# print(soup.prettify())
# print(soup.find_all(name="h3", class_="title"))

list_movies = soup.find_all(name="h3", class_="title")

with open("100_movies.txt", 'w', encoding="utf-8") as file:
    for i in range(len(list_movies) - 1, -1, -1):
        file.write(f"{list_movies[i].getText()}\n")
