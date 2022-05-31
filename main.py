# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
from bs4 import BeautifulSoup
import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from stop_words import get_stop_words


def get_news(url):
    session = requests.session()
    news_url = url
    page = session.get(news_url)
    parsed = BeautifulSoup(page.content, 'html.parser')
    story_text = parsed.find(id='storytext')
    full_text = ''
    for text in story_text.contents:
        if text is not None:
            full_text += text.text

    return full_text


def word_count(str):
    counts = dict()
    # words = str.split()

    for word in str:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def try_nltk():
    sentence = get_news('https://www.npr.org/2022/05/25/1101289242/russia-ukraine-war-what-happened-today-may-25')
    # sentence = "Russian President Vladimir Putin also made the first public visit to a Moscow military hospital as the Kremlin said he met with soldiers wounded in Ukraine"
    tokenized = nltk.word_tokenize(sentence)
    nltk_words = list(get_stop_words('en'))
    # nltk_words = list(stopwords.words('english'))
    # for word in tokenized:
    #     if word in nltk_words:
    filtered_result = list(filter(lambda element: element not in nltk_words, tokenized))
    print(word_count(filtered_result))
    # print(nltk_words)
    # print(filtered_result)


def get_news_urls():
    urls = []
    session = requests.session()
    page = session.get('https://www.npr.org/sections/world/')
    parsed = BeautifulSoup(page.content, 'html.parser')
    titles = parsed.findAll('h2', {'class': 'title'})
    for title in titles:
        urls.append(title.find('a').attrs['href'])

    return urls


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # result = get_news()
    # words = word_count(result.replace('\n', ''))
    # print(words)
    # try_nltk()
    all_news = ''
    urls = get_news_urls()
    for url in urls:
        all_news += get_news(url)
    tokenized = nltk.word_tokenize(all_news)
    nltk_words = list(get_stop_words('en'))
    filtered_result = list(filter(lambda element: element not in nltk_words, tokenized))
    print(word_count(filtered_result))
    name = 'jay'

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
