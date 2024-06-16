# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ReviewItem(scrapy.Item):
    """
    Класс оперделения структуры данных для отзыва
    :param username: Имя пользователя, оставишего отзыв
    :param date: Дата отзыва
    :param stars: Оценка отзыва
    :param comment_text: Текст отзыва
    :param image_urls: Ссылки на изображения, прикрепленные к отзыву
    :param answer: Ответ на отзыв
    """

    username = scrapy.Field()
    date = scrapy.Field()
    stars = scrapy.Field()
    comment_text = scrapy.Field()
    image_urls = scrapy.Field()
    answer = scrapy.Field()


class AnswerItem(scrapy.Item):
    """
    Класс определения структуры ответа на отзыв
    :param username: Имя пользователя, оставившего ответ на отзыв
    :param answer_date: Дата ответа
    :param answer_text: Текст ответа
    """

    username = scrapy.Field()
    answer_date = scrapy.Field()
    answer_text = scrapy.Field()
