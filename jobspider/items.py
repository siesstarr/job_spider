# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # 职位名称
    positionName = scrapy.Field()
    # 薪水
    salary = scrapy.Field()
    # 工作经验
    workYear = scrapy.Field()
    # 学历要求
    education = scrapy.Field()
    # 公司名称
    companyName = scrapy.Field()
    # 公司领域
    industryField = scrapy.Field()
    # 公司规模
    companySize = scrapy.Field()
    # 企业类型
    companyType = scrapy.Field()
    # 工作地点
    jobSec = scrapy.Field()
    # 描述
    description = scrapy.Field()
