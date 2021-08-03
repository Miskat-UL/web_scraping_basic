from bs4 import BeautifulSoup
from my_blog_site_scrap.locator.page_locator import PageLocator
from my_blog_site_scrap.parsers.blog_parser import BlogParser


class Blogs:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def blogs(self):
        locator = PageLocator.PAGE
        all_blogs = self.soup.select(locator)
        return [BlogParser(e) for e in all_blogs]
