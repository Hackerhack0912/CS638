import scrapy

dir = "./spiders/bn_pages/"


class bnSprider(scrapy.Spider):
    name = 'bn'
    id = 0
    def start_requests(self):
        #1-88
        
        webList = [None] * 88
        for i in range(0, 88):
            webList[i] =  "http://www.barnesandnoble.com/s/database?Nrpp=40&page="+str(i+1)
        for j in range(0, 88):
            #print(webList[j])
            yield scrapy.Request(url=webList[j], callback=self.parseBookLinks)

    def parseBookLinks(self, response):
        booksList = response.xpath('//ul[@id="gridView"]/li[@class="clearer"]//li')
        booksUrls = booksList.xpath('//div[@class="product-info"]/p[@class="product-info-title"]/a/@href').extract()
        
        #print(booksUrls)
        for url in booksUrls:
            url = "https://www.barnesandnoble.com" + url
            htmlPage = response.urljoin(url)
            yield scrapy.Request(url=htmlPage, callback=self.parseBookInfo)

    def parseBookInfo(self, response):
        page = response.url.split("/")[-2]
        #print(page)
        filename =  dir + '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        productDetailsIndices = response.xpath('//*[@id="additionalProductInfo"]/dl/dt/text()').extract()
        productDetails = response.xpath('//*[@id="additionalProductInfo"]/dl/dd/text()').extract()
        pagesIndex = 4
        for i in range(0, len(productDetailsIndices)):
            if productDetailsIndices[i] == 'Pages:':
                pagesIndex = i
        
        pages = productDetails[pagesIndex]
        dates = response.xpath('//*[@id="additionalProductInfo"]/dl/dd[3]/text()').extract_first().split('/')
        yield {
            'id': self.id,
            'title': response.xpath('//*[@id="prodSummary"]/h1/text()').extract_first(),
            'year': dates[2],
            'month': dates[0],
            'day':dates[1],
            'authors': response.xpath('//*[@id="prodSummary"]/span/a/text()').extract(),
            'pages': pages,
            'publisher': response.xpath('//*[@id="additionalProductInfo"]/dl/dd[2]/a/text()').extract_first(),
            'ISBN13': response.xpath('//*[@id="additionalProductInfo"]/dl/dd[1]/text()').extract_first(),
        }
        self.id+=1

