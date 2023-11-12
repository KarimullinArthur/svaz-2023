import sys
import re
import requests

from bs4 import BeautifulSoup as bs


URL = input("Вставьте ссылку на свой телеграм-канал \n пример: https://t.me/s/linux_gram\n> ")

if URL[13] != 's':
    URL = URL[:12] + '/s' + URL[12:]

try:
    resp = requests.get(URL).text
except:
    print("Неправильный URL")
    sys.exit(1)

soup = bs(resp, "html.parser")
posts = soup.find_all('div', class_='tgme_widget_message_text js-message_text')

for post in posts:
    pass
    print('---')
    print(post.text)

print('---\n')
posts = list(posts)

find_word = input("Какое слово ищем??\n> ")
count = ''.join(str(post) for post in posts).find(find_word)
print(f"Слово {find_word} встречается {count} раз")
