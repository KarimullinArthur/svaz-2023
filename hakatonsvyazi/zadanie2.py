import requests
import json
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from config import *
import random

# Введите свой токен VK API здесь
token = VK_TOKEN

def get_json(url):
    response = requests.get(url)
    return response.json()

def get_keywords(texts):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    keywords = vectorizer.get_feature_names_out()
    return keywords

wordcloud_id = str(random.randint(0, 100000))
def create_wordcloud(keywords, user):
    wordcloud = WordCloud(width=800, height=400).generate(' '.join(keywords))
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    if (user):
        plt.savefig('testAI/wordclouduser' + wordcloud_id  + '.png')
    else:
        plt.savefig('testAI/wordcloudgroup' + wordcloud_id + '.png')


user_key = str(random.randint(0, 10000))
file = open("infoVK/info" + user_key + ".txt", "w+")

print("Эта программа получает информацию о группе и пользователе посредством VK_API и записывает её в текстовый файл. Также она может создавать облако  ключевых слов, используемых пользователем и группой...")

# Получение информации о группе
print("Пожалуйста, введите ID группы для получения информации:")
group_id = str(input())
group_url = f'https://api.vk.com/method/groups.getById?group_id={str(int(group_id)*-1)}&access_token={token}&v=5.131'
group_info = get_json(group_url)


# Получение информации о пользователе
print("Пожалуйста, введите ID пользователя для получения информации:")
user_id = str(input())
user_url = f'https://api.vk.com/method/users.get?user_ids={user_id}&access_token={token}&v=5.131'
user_info = get_json(user_url)


#Запись инфо о группе и пользователе...
# Запись информации о группе и пользователе в файл
file.write("Информация о группе:\n")
file.write(json.dumps(group_info, ensure_ascii=False, indent=4))  # ensure_ascii=False для корректного отображения кириллицы
file.write("\n\nИнформация о пользователе:\n")
file.write(json.dumps(user_info, ensure_ascii=False, indent=4))
file.close()

# Получение постов пользователя и группы
posts_url_user = f'https://api.vk.com/method/wall.get?owner_id={user_id}&access_token={token}&v=5.131'
posts_info_user = get_json(posts_url_user)
posts_url_group = f'https://api.vk.com/method/wall.get?owner_id={group_id}&access_token={token}&v=5.131'
posts_info_group = get_json(posts_url_group)


# Получение ключевых слов из постов
texts_user = [post['text'] for post in posts_info_user['response']['items']]
texts_user = [' '.join(word for word in string.split() if not (word.startswith("[id") or word.startswith("[club"))) for string in texts_user]
texts_group = [post['text'] for post in posts_info_group['response']['items']]
texts_group = [' '.join(word for word in string.split() if not (word.startswith("[id") or word.startswith("[club"))) for string in texts_group]
keywords_user = get_keywords(texts_user)
keywords_group = get_keywords(texts_group)

# Создание облака слов из ключевых слов
create_wordcloud(keywords_user, True)
create_wordcloud(keywords_group, False)

print("Успешно записана информация о вашей группе и пользователе в файле info" + user_key + ".txt" + " в папке infoVK")
print("Также создано облако ключевых слов в файле worldcloudgroup " + wordcloud_id + ".png" + " и файле worldclouduser" + wordcloud_id + ".png" + " в папке testAI")
