import scrapy
from ..items import ReviewItem, AnswerItem


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["www.yelp.com"]
    start_urls = ["https://www.yelp.com/biz/golden-state-nissan-colma-3"]

    def parse(self, response):
        reviews = response.xpath('//li[contains(@class, "y-css-1jp2syp")][.//div[contains(@class, "y-css-19pbem2")]]')
        for item in reviews:
            review = ReviewItem()
            review['username'] = item.xpath('.//a[contains(@class, "y-css-12ly5yx")]/text()').get()
            review['date'] = item.xpath('.//span[contains(@class, " y-css-wfbtsu")]/text()').get()
            stars = len(item.xpath('.//div[contains(@class, "y-css-z05zjh")]'))
            stars += len(item.xpath('.//div[contains(@class, "y-css-1vjw9sv")]'))
            review['stars'] = stars
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
