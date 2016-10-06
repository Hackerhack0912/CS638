import scrapy
import os


class QuotesSpider(scrapy.Spider):
    name = "amazon"
    def start_requests(self):
        urls = [
            'https://www.amazon.com/gp/product/159562015X/ref=s9_acsd_al_bw_c_x_1?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=YRX7WQEBMESX5BR7975T&pf_rd_t=101&pf_rd_p=a0e6d309-319b-4ca7-8e00-31ca788c1750&pf_rd_i=11913537011',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        dir = os.path.join('pages', filename)
        with open(dir, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        #dir = os.path.join(dir, 'generated-formulae')
        for quote in response.css('body'):
            #s = quote.xpath('main/section/div/section/div/section/dl/dd/text()').extract();
            print(quote)
            dates = s[2].split('/');
            yield {
                #'title': quote.xpath('main/section/div/div/section/section/h1/text()').extract_first(),
                #'year': dates[2],
                #'month': dates[0],
                #'day':dates[1],
                #'authors': quote.xpath('main/section/div/div/section/section/span/a/text()').extract(),
                #'pages': s[3],
                #'publisher': quote.xpath('main/section/div/section/div/section/dl/dd/a/text()').extract_first(),
                #'ISBN13': s[0],
            }

        next_page = response.xpath('//li/a/@href').extract_first()
        next_page = "http://www.barnesandnoble.com"+next_page
        print (next_page)
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
