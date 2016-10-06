import scrapy
import os


class QuotesSpider(scrapy.Spider):
    name = "bn"
    def start_requests(self):
        urls = [
            'http://www.barnesandnoble.com/w/the-hammer-of-thor-rick-riordan/1122934753?ean=9781368000307',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        dir = os.path.join('BNpages', filename)
        with open(dir, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        #dir = os.path.join(dir, 'generated-formulae')
        for quote in response.css('main.clearer'):
            s = quote.xpath('main/section/div/section/div/section/dl/dd/text()').extract();
            dates = s[2].split('/');
            yield {
                'title': quote.xpath('main/section/div/div/section/section/h1/text()').extract_first(),
                'year': dates[2],
                'month': dates[0],
                'day':dates[1],
                'authors': quote.xpath('main/section/div/div/section/section/span/a/text()').extract(),
                'pages': s[3],
                'publisher': quote.xpath('main/section/div/section/div/section/dl/dd/a/text()').extract_first(),
                'ISBN13': s[0],
            }
        #next_page = response.xpath('//main[@class="clearer"]//section[@class="main-content"]/section[@class="module-row content-shadow"]/div[@class="caroufredsel_wrapper"]/ul/li/a/@href').extract()
        next_page = response.xpath('//li/a/@href').extract_first()
        
        next_page = "http://www.barnesandnoble.com"+next_page
        print (next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        #print ('111111111')
        #print (next_page)
        #for nextPage in next_page:
        #    nextPage = "http://www.barnesandnoble.com"+nextPage
            #print (nextPage)
        #    if nextPage is not None and '/w/' in nextPage:
        #        nextPage = response.urljoin(nextPage)
        #        yield scrapy.Request(nextPage, callback=self.parse)
        

