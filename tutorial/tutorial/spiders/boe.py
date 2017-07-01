import scrapy

class QuotesSpider(scrapy.Spider):
    name = "ECB"

    def start_requests(self):
        urls = [
            'http://www.bankofengland.co.uk/',
            #'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'boe-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

