#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

import urllib2
import requests
from bs4 import BeautifulSoup


class Client(object):

    def __init__(self):
        super(Client, self).__init__()

    def get_web(self, html):
        r = requests.get(html)
        return r

    def lets_parse(self, html):
        soup = BeautifulSoup(html.content, 'html.parser')
        products = soup.find_all("div", {"class": "product product10"})
        for product in products:
            print product.contents[1].find("span").text
            print product.contents[3].find("div", {"class": "mm-price media__price"}).text

    def get_price(self, product):

        for product in product:
            product = product
        print 0

    def run(self):
        web = "https://tiendas.mediamarkt.es/tarjetas-graficas-gaming?orderBy=price&orderByDirection=DESC&perPage=50"
        html = self.get_web(web)
        free = self.lets_parse(html)
        # self.get_price(free)

if __name__ == "__main__":
    client = Client()
    client.run()
# print get_web("https://www.packtpub.com/packt/offers/free-learning")