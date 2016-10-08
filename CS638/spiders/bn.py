import scrapy

dir = "./bn_pages/"

class AuthorSpider(scrapy.Spider):
    name = 'bn'
    
    # start from the main website
    def start_requests(self):
        start_url = 'http://www.barnesandnoble.com/b/books/_/N-29Z8q8'
        yield scrapy.Request(url=start_url, callback=self.parseCategoryList) 
    
    # Level 1
    def parseCategoryList(self,response):
        categorylist = response.css('div.list-wrapper ul.category-list')[1]
        next_pages = categorylist.css('a::attr(href)').extract()
        for page in next_pages:
            next_page = response.urljoin(page)
            yield scrapy.Request(url=next_page, callback=self.parseBookSubCategoryList)
			
    # Level 2: for each page in Level 1
    def parseBookSubCategoryList(self,response):
        next_pages = response.css('div.featured-categories-container figcaption a::attr(href)').extract()
        for page in next_pages:
            next_page = response.urljoin(page)
            yield scrapy.Request(url=next_page, callback=self.parseBookList) 
    # Leve 3: all books under certain subCategory
    def parseBookList(self,response):
        next_pages = response.css('p.product-info-title a::attr(href)').extract()
        for page in next_pages:
            next_page = response.urljoin(page)
            yield scrapy.Request(url=next_page, callback = self.parseBookInfo) 

    def parseBookInfo(self,response):
        page = response.url.split("/")[-2]
        filename = dir + "%s.html " % page
        with open(filename, 'wb') as f:
            f.write(response.body)
            self.log('Saved file %s' % filename) 
		
