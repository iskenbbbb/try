import requests
from parsel import Selector

url = "https://www.mashina.kg/search/all/"


def get_html():
    response = requests.get(url)
    # print(response.text[:180])
    return response.text

def parsel_html():
    selector = Selector(text=html)
    return selector

# def get_title():



if __name__ == "__main__":
    html = get_html()
    selector = parsel_html()
    title = selector.css('title::text').get()
    print(title)
    cars = selector.css(".block title::text").getall()
    for c in cars:
        print(c)
    # print(cars)



















# from parsel import Selector
# import requests
#
#
# class NewsScraper:
#     PLUS_URL = "https://rezka.ag/films/comedy/"
#     LINK_XPATH = 'div[@class ="b-content__inline_item-link"]'
#     TITLE_V1_XPATH = '//div[@class="one"]/div/a/strong/text()'
#     TITLE_V2_XPATH = '//div[@class="one"]/div/a/span/text()'
#     TEXT_XPATH = '//div[@class="cont"]/p/text()'

    # def parse_data(self):
    #     text = requests.get(self.START_URL).text
    #     tree = Selector(text=text)
    #     links = tree.xpath(self.LINK_XPATH).extract()
    #     first_v_title = tree.xpath(self.TITLE_V1_XPATH).extract()
    #     second_v_title = tree.xpath(self.TITLE_V2_XPATH).extract()
    #     first_v_title.extend(second_v_title)
    #     # iis = 0
    #     # data = []
    #     data = []
    #     for link in links:
    #         data.append(self.PLUS_URL + link)
    #         print("self.PLUS_URL: ", self.PLUS_URL + link)
#         return links[:5]
#
#     def parse_detail(self, urls):
#         for url in urls:
#             text = requests.get(url).text
#             tree = Selector(text=text)
#             text = tree.xpath(self.TEXT_XPATH).extract()
#             print(text)
#
#
# if __name__ == "__main__":
#     scraper = NewsScraper()
# #     scraper.parse_data()