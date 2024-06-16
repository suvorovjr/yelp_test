import scrapy
from ..items import ReviewItem, AnswerItem


class ScraperSpider(scrapy.Spider):
    """
    Класс для парсинга страницы https://www.yelp.com/biz/golden-state-nissan-colma-3
    Также можно добавить другие страницы для парсинга
    """

    name = "scraper"
    allowed_domains = ["www.yelp.com"]
    start_urls = ["https://www.yelp.com/biz/golden-state-nissan-colma-3"]

    def parse(self, response):
        """
        Парсер отзывов
        Для опеределения структуры данных используются ReviewItem и AnswerItem
        При переходе на следующую страницу меняется ее url, добавляя пармаетр start
        """

        reviews = response.xpath('//li[contains(@class, "y-css-1jp2syp")][.//div[contains(@class, "y-css-19pbem2")]]')
        for item in reviews:
            review = ReviewItem()
            review['username'] = item.xpath('.//a[contains(@class, "y-css-12ly5yx")]/text()').get()
            review['date'] = item.xpath('.//span[contains(@class, " y-css-wfbtsu")]/text()').get()
            review['stars'] = item.xpath('.//div[contains(@class, "y-css-9tnml4")]/@aria-label').get().split()[0]
            comment_xpath = './/span[contains(@class, " raw__09f24__T4Ezm") and not(ancestor::div[@class="block-quote__09f24__qASfJ y-css-cckqp0"])]/text()'
            review['comment_text'] = "".join(item.xpath(comment_xpath).getall())
            answer_block = item.xpath('.//div[contains(@class, "block-quote__09f24__qASfJ y-css-cckqp0")]')
            if answer_block:
                answer = AnswerItem()
                answer['username'] = answer_block.xpath('.//p[contains(@class, " y-css-w3ea6v")]/text()').get()
                answer['answer_date'] = answer_block.xpath('.//span[contains(@class, " y-css-wfbtsu")]/text()').get()
                answer['answer_text'] = ''.join(
                    answer_block.xpath('.//span[contains(@class, " raw__09f24__T4Ezm")]/text()').getall())
                review['answer'] = answer
            review['image_urls'] = item.xpath('.//img[contains(@class, " y-css-dy9j94")]/@src').getall()
            yield review

        next_page_button = response.xpath(
            '//a[contains(@class, "next-link navigation-button__09f24__m9qRz y-css-7ln3jw")]').get()
        if next_page_button:
            start = response.meta.get('start', 0)
            next_page = f'{self.start_urls[0]}?start={start + 10}'
            yield scrapy.Request(response.urljoin(next_page), meta={'start': start + 10})
