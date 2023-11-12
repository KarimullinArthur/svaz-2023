import sys
import re
import requests

from bs4 import BeautifulSoup as bs


URL = input("Input your URL channel\nlike https://t.me/s/linux_gram\n> ")

if URL[13] != 's':
    URL = URL[:12] + '/s' + URL[12:]

try:
    resp = requests.get(URL).text
except:
    print("Invalid URL")
    sys.exit(1)

soup = bs(resp, "html.parser")
posts = soup.find_all('div', class_='tgme_widget_message_text js-message_text')

for post in posts:
    pass
    print('---')
    print(post.text)

print('---\n')
posts = list(posts)

find_word = input("How word we are finding?\n> ")


def stats(string_):
    freq = {}
    res = []
    for word in string_.split():
        freq[word] = freq[word] + 1 if word in freq else 1
        if freq[word] > 1 and word not in res:
            res.append(word)
    if len(res) == 0:
        return None
    return res if len(res) > 1 else res.pop()


string = ''.join(str(post) for post in posts)

print(f"Слово {find_word} встречается {len(stats(string))} раз")
