import requests
from lxml import etree
import sys


def gethtml(city):
    baseurl = 'https://tianqi.moji.com/weather/china/'
    url = baseurl + city
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        resp.encoding = 'utf-8'
        return resp.text
    except ConnectionError:
        return None


def parsehtml(city):
    source_html = gethtml(city)
    weather_list = []
    if source_html:
        selector = etree.HTML(source_html)
        xpath = '//div[@class="forecast clearfix"]//ul'
        location_city = selector.xpath('//div[@class="search_default"]/em/text()')
        ul_elements = selector.xpath(xpath)
        if ul_elements:
            weather_list.append(location_city)
            for ul in ul_elements[1:]:
                # 获取节点下所有的text的迭代器
                # 在python3中直接可以使用filter，map 传入迭代器
                iter_t = ul.itertext()
                iter_t = filter((lambda x: x.strip() != ''), iter_t)
                text_list = list(map(lambda x: x.strip(), iter_t))
                weather_list.append(text_list)
    return weather_list


def main():
    while True:
        city = input('输入要查询的省份/城市 exp shanghai/shanghai :')
        print()
        if city == '':
            city = 'shanghai/shanghai'
        if city == 'q':
            sys.exit()

        result = parsehtml(city)
        if result:
            for weather in result:
                print('  '.join(weather))
                print()
            print('have a nice day')
        else:
            print('not found this city', '\n')


if __name__ == '__main__':
    main()
