import scrapy


class NyuProgramsSpiderSpider(scrapy.Spider):
    name = "nyu_programs_spider"
    allowed_domains = ["gsas.nyu.edu"]
    start_urls = ["https://gsas.nyu.edu/programs.html"]

    def parse(self, response):
        pass
