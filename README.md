# job_spider

- [x] 51job
- [ ] lagou
- [ ] boss
- [ ] zhilian

```
scrapy crawl 51job -o 51job.csv
```
可使用MySQL保存数据，需要根据settings文件中的配置添加对应环境变量和取消ITEM_PIPELINES中的对应注释。
