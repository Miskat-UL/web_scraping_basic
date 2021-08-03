import requests

from my_blog_site_scrap.pages.blog_pages import Blogs

page_content = requests.get('https://miskat-ul.github.io/blog_site/').content

page = Blogs(page_content)

for _ in page.blogs:
    print(_.blogs_paragraph)

