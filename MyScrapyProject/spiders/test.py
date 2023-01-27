import scrapy
 

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
         #start_urls
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
       blocks = response.xpath("//div[contains(@class,'quote')]")
       
       for block in blocks:
        text = block.xpath(".//span[@class='text']/text()").get().strip()
        author = block.xpath(".//small[@class='author']/text()").get(),
        tags = block.xpath(".//div[@class='tags']/a/text()").get()

        yield {
                'Text':text,
                'Author':author,
                'Tags':tags
             
               }
    
        next_page = response.xpath("//a[text()='Next ']/@href").get()
        print(next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            print(next_page)

            yield scrapy.Request(next_page, callback=self.parse)



                  
                

   


  