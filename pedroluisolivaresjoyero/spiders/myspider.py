import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["X"]
    start_urls = [ 'https://www.pedroluisolivaresjoyero.com/es/joyeria/anillos-de-compromiso.html?_=1716584002896&_gl=1%2A10jfdd4%2A_up%2AMQ..%2A_ga%2AMTU5MjI3MjU5NS4xNzE2MzU3MjQ1%2A_ga_MZDWFS8VZN%2AMTcxNjM1NzI0NC4xLjAuMTcxNjM1NzI0NC4wLjAuMA..&ajaxscroll=1&p=1&ajaxscroll=1','https://www.pedroluisolivaresjoyero.com/es/joyeria/anillos-de-compromiso.html?_=1716584002896&_gl=1%2A10jfdd4%2A_up%2AMQ..%2A_ga%2AMTU5MjI3MjU5NS4xNzE2MzU3MjQ1%2A_ga_MZDWFS8VZN%2AMTcxNjM1NzI0NC4xLjAuMTcxNjM1NzI0NC4wLjAuMA..&ajaxscroll=1&p=2&ajaxscroll=1',  'https://www.pedroluisolivaresjoyero.com/es/joyeria/anillos-de-compromiso.html?_=1716584002896&_gl=1%2A10jfdd4%2A_up%2AMQ..%2A_ga%2AMTU5MjI3MjU5NS4xNzE2MzU3MjQ1%2A_ga_MZDWFS8VZN%2AMTcxNjM1NzI0NC4xLjAuMTcxNjM1NzI0NC4wLjAuMA..&ajaxscroll=1&p=3&ajaxscroll=1']
    # start_urls = [ 'https://www.pedroluisolivaresjoyero.com/es/joyeria/anillos-de-compromiso.html?_=1716584002896&_gl=1%2A10jfdd4%2A_up%2AMQ..%2A_ga%2AMTU5MjI3MjU5NS4xNzE2MzU3MjQ1%2A_ga_MZDWFS8VZN%2AMTcxNjM1NzI0NC4xLjAuMTcxNjM1NzI0NC4wLjAuMA..&ajaxscroll=1&p=1&ajaxscroll=1']
    def parse(self, response):
        hrefs=response.xpath('//div[@class="product-hover"]/a/@href').getall()
        print(len(hrefs))
        for href in hrefs:
            yield scrapy.Request(url=href,callback=self.details,dont_filter=True)

    def details(self,response):
        data={}
        url=response.url
        title=response.xpath('//h1[@class="page-title"]//span//text()').get()
        price=response.xpath('//span[@class="price"]//text()').get()
        value=response.xpath('//div[@class="value"]//text()').get()
        image =response.xpath("//div[@class='gallery-placeholder _block-content-loading']/img/@data-src").get()

        print(image)

        data['title']=title
        data['price']=price
        data['SKU']=value
        data['image']=image
        data['url']=url
        yield data