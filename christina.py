import requests
from bs4 import BeautifulSoup

def find_frequency(search_word, category):
    # search_word = (input("What is your search word?")).lower()
    search_word = search_word.lower()
    neuro_page = requests.get("https://neurosciencenews.com/neuroscience-topics/{}{}".format(category, "/" if category != "" else ""))
    # print(page.content)
    page_parser = BeautifulSoup(neuro_page.text, 'html.parser')

    article_html_list = page_parser.find_all(class_= 'title')

    article_a_list = []
    for article in article_html_list:
        article_a_list.append(article.find('a'))

    article_title_list = []
    article_links_list = []
    for article_a in article_a_list:
        if article_a:
            title = article_a.contents[0]
            article_title_list.append(title)
            link = article_a.get('href')
            article_links_list.append(link)
    result = []
    globalwordcount = 0
    for link in article_links_list:
        neuro_article = (requests.get(link).text).lower()
        wordcount = neuro_article.count(search_word)
        globalwordcount += wordcount
        link_idx = article_links_list.index(link)
        title = article_title_list[link_idx]
        word_freq = str(wordcount)
        article_object = {
            'link': link,
            'word_count': wordcount,
            'title': title
        }
        result.append(article_object)
        # result.append("Title: " +  +"\n")
        # result.append("Word Frequency: " +  + "\n")
    # result.insert(0, "Total Word Frequency: " + str(globalwordcount) + "\n")
    total_word_freq = "Total Word Frequency: " + str(globalwordcount)
    return(total_word_freq, result)

