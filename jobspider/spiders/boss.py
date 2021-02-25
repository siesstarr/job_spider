# -*- coding: utf-8 -*-
import scrapy


class BossSpider(scrapy.Spider):
    name = "boss"
    allowed_domains = ["zhipin.com"]
    start_urls = ["https://www.zhipin.com/"]

    search_url0 = (
        "https://www.zhipin.com/c101270100-p100901/?page={page}&ka=page-{page}"
    )

    def start_requests(self):
        for page in range(1, 8):
            url = self.search_url1.format(page=page)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
