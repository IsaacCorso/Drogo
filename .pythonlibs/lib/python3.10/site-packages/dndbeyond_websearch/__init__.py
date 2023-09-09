import re
from collections import namedtuple

import requests
from bs4 import BeautifulSoup


class SearchResult(namedtuple('SearchResult', ['title', 'url', 'breadcrumbs', 'snippets'])):
    pass


class Parser:
    BASE_URL = 'https://www.dndbeyond.com/'
    RESULT_CLASS = 'ddb-search-results-listing-item'
    TITLE_CLASS = 'ddb-search-results-listing-item-header-primary-text'
    BREADCRUMBS_CLASS = 'ddb-search-results-listing-item-header-secondary-text'
    SNIPPET_CLASS = 'ddb-search-results-listing-item-body-snippet'

    def __init__(self):
        pass

    def extract_results(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        listing = self._get_listing(soup)
        results = [self._parse_result(r) for r in listing]

        return [r for r in results if r is not None]

    def _absolute_url(self, url):
        return self.BASE_URL + url

    def _parse_result(self, result):
        try:
            link = result.find(**self._class_filter(self.TITLE_CLASS)).a
            title = link.text
            url = self._absolute_url(link['href'])
            breadcrumbs = ''.join(
                span.text for span in
                result.find(**self._class_filter(self.BREADCRUMBS_CLASS)).find_all('span')
            )
            snippets = [
                snippet.span.text for snippet in
                result.find_all(**self._class_filter(self.SNIPPET_CLASS))
            ]

            return SearchResult(
                title=title,
                url=url,
                breadcrumbs=breadcrumbs,
                snippets=snippets,
            )
        except (AttributeError, KeyError):
            pass

        return None

    def _get_listing(self, soup):
        return soup.find_all(**self._class_filter(self.RESULT_CLASS))

    def _class_filter(self, class_to_search):
        def callback(c):
            return c is not None and class_to_search in re.split('\s+', c)

        return {'class': callback}


class Searcher:
    DNDBEYOND_SEARCH_URL_PATTERN = 'https://www.dndbeyond.com/search?q={}'

    def __init__(self):
        self._parser = Parser()

    def search(self, query):
        response = requests.get(self.DNDBEYOND_SEARCH_URL_PATTERN.format(query))
        return self._parser.extract_results(response.content)
