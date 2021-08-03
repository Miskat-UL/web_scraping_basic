from my_blog_site_scrap.locator.blogs_locator import BlogsLocator


class BlogParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def blog_titles(self):
        locator = BlogsLocator.BLOGS_TITLE
        return self.parent.select_one(locator).string

    @property
    def blogs_paragraph(self):
        locator = BlogsLocator.BLOGS_PARAGRAPHS
        return self.parent.select_one(locator).string

    @property
    def blogs_lists(self):
        locator = BlogsLocator.ALL_POSTS
        return self.parent.select_one(locator).string


