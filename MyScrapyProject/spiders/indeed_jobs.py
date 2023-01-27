import scrapy
 

class QuotesSpider(scrapy.Spider):
    name = "indeed_jobs"

    def start_requests(self):
         #start_urls
        urls = [
            'https://in.indeed.com/jobs?q=python&l=india',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        js = response.xpath("//li/div[contains(@class,'cardOutline')]")
       
        for j in js:
            job = j.xpath(".//span[contains(@id,'jobTitle')]/text()").get()
            companyName = j.xpath(".//span[contains(@class,'companyName')]//text()").get()
            location = j.xpath(".//div[contains(@class,'companyLocation')]//text()").get()

            
            yield {
                    'job':job,
                    'companyName':companyName,
                    'location':location
                 
                   }
       




                  
                

   


  