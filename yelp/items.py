# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewItem(scrapy.Item):
    username = scrapy.Field()
    date = scrapy.Field()
    stars = scrapy.Field()
    comment_text = scrapy.Field()
    image_urls = scrapy.Field()
    answer = scrapy.Field()


class AnswerItem(scrapy.Item):
    username = scrapy.Field()
    answer_date = scrapy.Field()
    answer_text = scrapy.Field()
