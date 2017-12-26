import requests
from lxml import etree
import sys


def gethtml(word):
    baseurl = 'http://www.youdao.com/w/eng/'
    url = baseurl + word
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        resp.encoding = 'utf-8'
        return resp.text
    except ConnectionError:
        return None


def parsehtml(word):
    source_html = gethtml(word)
    if source_html:
        selector = etree.HTML(source_html)
        xpath = '//div[@class="trans-container"]/ul/li/text()'
        div_elements = selector.xpath(xpath)
        return div_elements


def main():
    while True:
        word = input('输入要查询的单词:')
        print()
        if word == 'q':
            sys.exit()
        text = parsehtml(word)
        if text:
            newtext = text[:3]
            news = '\n'.join(newtext)
            print(news, '\n')
        else:
            print('not found this word','\n')

if __name__ == '__main__':
    main()

