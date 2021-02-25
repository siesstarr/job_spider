# -*- coding: utf-8 -*-
import scrapy
import os
from urllib.parse import urlencode
import json


class LagouSpider(scrapy.Spider):
    name = "lagou"
    allowed_domains = ["lagou.com"]
    start_urls = ["https://www.lagou.com/"]

    search_url0 = "https://www.lagou.com/jobs/list_web%E5%89%8D%E7%AB%AF?labelWords=sug&fromSearch=true&suginput=web"
    search_url1 = "https://www.lagou.com/jobs/positionAjax.json?city=%E6%88%90%E9%83%BD&needAddtionalResult=false"

    sid = "f39b16f999c0476cbebcd29250f31064"

    def start_requests(self):
        for page in range(1, 2):
            # data_raw = {"first": "false", "pn": page, "kd": "web前端", "sid": self.sid}
            yield scrapy.Request(
                url=self.search_url0,
                method="GET",
                # body=urlencode(data_raw),
                # headers={
                #     "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
                # },
                callback=self.parse,
            )

    def parse(self, response):
        body = json.loads(response.body_as_unicode())
        print("www")
        print(body)
        yield
