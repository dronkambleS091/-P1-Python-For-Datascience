from bs4 import BeautifulSoup

with open("Dron.html", "r") as file:
    html = file.read()

print(html)
soup = BeautifulSoup(html, "html.parser")

print(soup.get_text())
