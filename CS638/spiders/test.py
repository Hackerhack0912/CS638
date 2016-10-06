import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    
    def start_requests(self):
        urls = ['https://www.amazon.com/gp/product/0525955100/ref=s9_acsd_al_bw_c_x_1?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-2&pf_rd_r=2Y6CCZFGK35B52GN0KGA&pf_rd_t=101&pf_rd_p=df917bc2-50d1-495e-adfa-36adf950ec54&pf_rd_i=549028']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

def parse(self, response):
    page = response.url.split("/")[-2]
    filename = 'quotes-%s.html' % page
    with open(filename, 'wb') as f:
        f.write(response.body)
    self.log('Saved file %s' % filename)
