# -*- coding: utf-8 -*-
import scrapy
import urllib
from bs4 import BeautifulSoup
from urllib import parse
import json
from ..items import JobspiderItem


class A51jobSpider(scrapy.Spider):
    name = "51job"
    allowed_domains = ["51job.com"]
    start_urls = ["https://www.51job.com/"]
    keyword = "iOS开发工程师"
    keyword = parse.quote(parse.quote(keyword))
    # position_code = 7701
    # industry_code = 32

    search_url0 = "https://search.51job.com/list/090000%252c090200,000000,0000,00,9,99,{keyword},2,{page}.html"
    # search_url0 = "https://search.51job.com/list/090000%252c090200,000000,{position_code},{industry_code},9,99,+,2,{page}.html"

    def start_requests(self):
        for page in range(1, 2):
            yield scrapy.Request(
                url=self.search_url0.format(keyword=self.keyword, page=page),
                # url=self.search_url0.format(
                #     position_code=self.position_code,
                #     industry_code=self.industry_code,
                #     page=page,
                # ),
                encoding="gbk",
                callback=self.parse1,
            )

    def parse1(self, response):
        bs = BeautifulSoup(response.body, "html.parser")
        jobListStr = bs.find(id="app").find_next_sibling()
        jobListStr = str(jobListStr)
        jobListStr = jobListStr.split("{", 1)[1]
        jobListStr = "{" + jobListStr
        jobListStr = jobListStr.split("</script>", 1)[0]

        jobList = json.loads(jobListStr)
        jobList = jobList["engine_search_result"]

        for job in jobList:
            item = JobspiderItem()
            item["positionName"] = job["job_name"]
            item["salary"] = job["providesalary_text"]
            item["workYear"] = job["attribute_text"][1]
            item["education"] = job["attribute_text"][2]
            item["companyName"] = job["company_name"]
            item["industryField"] = job["companyind_text"]
            item["companySize"] = job["companysize_text"]
            item["companyType"] = job["companytype_text"]
            item["jobSec"] = job["attribute_text"][0]

            yield scrapy.Request(
                url=job["job_href"], callback=self.parse2, meta={"item": item}
            )

    def parse2(self, response):
        item = response.meta["item"]
        bs = BeautifulSoup(response.body, "html.parser")
        item["description"] = (
            bs.find(class_="bmsg job_msg inbox").get_text().replace("微信分享", "").strip()
        )

        yield item
