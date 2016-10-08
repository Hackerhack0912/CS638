import scrapy

dir = "./amzn_pages/"

class AmazonSprider(scrapy.Spider):
    name = 'amazon'

    def start_requests(self):
        start_url = 'https://www.amazon.com/s/ref=sxts_gp_wtanrd_0_1?fst=as%3Aoff&rh=n%3A283155%2Cn%3A5%2Ck%3Adatabase%2Cp_n_feature_browse-bin%3A2656022011&keywords=database&ie=UTF8&qid=1475939515&rnid=618072011'
        yield scrapy.Request(url=start_url, callback=self.parseBookLinks)
        for i in range(2, 292):
            yield scrapy.Request(url="https://www.amazon.com/s/ref=sr_pg_2?fst=as%3Aoff&rh=n%3A283155%2Cn%3A5%2Ck%3Adatabase%2Cp_n_feature_browse-bin%3A2656022011&page="+str(i)+"&keywords=database&ie=UTF8&qid=1475952587", callback=self.parseBookLinks)

    def parseBookLinks(self, response):
        booksList = response.xpath('//div[@id="resultsCol"]//ul[@id="s-results-list-atf"]/li')
        booksUrls = booksList.xpath('//a[@class="a-link-normal s-access-detail-page  a-text-normal"]/@href').extract()
        #print(booksUrls)
        for url in booksUrls:
            htmlPage = response.urljoin(url)
            yield scrapy.Request(url=htmlPage, callback=self.parseBookInfo)

        #nextPage = "https://www.amazon.com" + response.xpath('//a[@id="pagnNextLink"]/@href').extract_first()
        #if nextPage is not None:
            #next_page = response.urljoin(nextPage)
            #yield scrapy.Request(url=next_page, callback=self.parseBookLinks)

    def parseBookInfo(self, response):
        page = response.url.split("/")[-2]
        #print(page)
        filename =  dir + '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Svaed file %s' % filename)
