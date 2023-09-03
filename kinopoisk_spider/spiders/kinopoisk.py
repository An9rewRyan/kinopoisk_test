# -*- coding:utf-8 -*-
#
# m.eremenko@brandquad.ru
# 03.09.2023
#
# source: kinopoisk
#

from scrapy import Request, Spider
from .constants.kinopoisk import *
import json


class KinopoiskParser():
    def get_movie_container(self):
        return {
            'position': '',
            'title': '',
            'rating': 0,
            'directors': '',
            # кнопка "буду смотреть" есть у всех фильмов как на сайте, так и в приложении
            'button_exists': True
        }

    def get_title(self, movie):
        title = movie.get('title', {}).get('russian')
        if not title:
            title = movie.get('title', {}).get('original')
        return {'title': title}

    def get_directors(self, movie):
        directors_json = movie.get('directors', {}).get('items', [])
        directors_names = []
        for item in directors_json:
            name = item.get('person', {}).get('name')
            if not name:
                name = item.get('person', {}).get('originalName')
            directors_names.append(name)
        if len(directors_names) == 1:
            directors_names = directors_names[0]
        return {'directors': directors_names}


class KinopoiskSpider(Spider, KinopoiskParser):
    name = "kinopoisk"
    custom_settings = {
        'DOWNLOAD_TIMEOUT': 60,
        'DOWNLOAD_DELAY': 0.5,
        'CONCURRENT_REQUESTS': 8,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        'RETRY_TIMES': 10,
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_requests(self):
        yield Request(url=KINOPOISK_URL, method='POST', headers=GRAPHQL_HEADERS, callback=self.parse,
                      body=json.dumps(GRAPHQL_BODY),
                      meta={'passed_data': {"pos": 0}})

    def parse(self, response):
        po = response.meta.get('passed_data')
        jo = response.json()
        movies_json = jo.get('data', {}).get('movieListBySlug', {}).get('movies', {}).get('items', [])
        for movie_cont in movies_json:
            movie_result_json = self.get_movie_container()
            movie = movie_cont.get('movie')
            movie_result_json['position'] = po['pos']+1
            movie_result_json['rating'] = movie.get('rating', {}).get('kinopoisk', {}).get('value')
            movie_result_json.update(self.get_title(movie))
            movie_result_json.update(self.get_directors(movie))
            yield movie_result_json
            po['pos'] += 1
        GRAPHQL_BODY['variables']['moviesOffset'] = po['pos']
        if po['pos'] >= 1000:
            self.log('Спарсили все фильмы')
            return
        yield Request(url=KINOPOISK_URL, method='POST', headers=GRAPHQL_HEADERS, callback=self.parse,
                      body=json.dumps(GRAPHQL_BODY),
                      meta={'passed_data': po}, dont_filter=True)
