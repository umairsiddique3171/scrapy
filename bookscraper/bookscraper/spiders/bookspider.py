import scrapy
from bookscraper.items import BookItems
import random
from urllib.parse import urlencode


# you can use it for scrapeops proxy aggregator request builder, if not using builtin middleware in settings
"""
API_KEY = 'your_api_key_from_scrapeops->proxy_aggregator->request_builder'
def get_proxy_url(url):
    payload = {'api_key':API_KEY,'url':url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url
"""



class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"] #,"proxy.scrapeops.io"]
    start_urls = ["http://books.toscrape.com/"]



    # you can use this custom user agent list, if not using scrapeops fake user agents
    """
    user_agent_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    ]
    """


    # if mentioned this func, scrapy will start request using it otherwise start_urls
    # you can use it for scrapeops proxy aggregator request builder, if not using builtin middleware in settings
    # if using middleware, then simply pass the urls as it is
    """
    def start_requests(self):
        yield scrapy.Request(url=get_proxy_url(self.start_urls[0]),callback=self.parse)
    """



    def parse(self, response):

        books = response.css('article.product_pod')

        for book in books:

            book_url = book.css('h3 a::attr(href)').get()
            if book_url is not None : 
                if 'catalogue/' in book_url: 
                    book_url_final = 'http://books.toscrape.com/'+ book_url
                else: 
                    book_url_final = 'http://books.toscrape.com/catalogue/'+ book_url

                book_data = {
                    'name': book.css('h3 a::text').get(),
                    'price': book.css('div.product_price .price_color::text').get(),
                    'url': book_url_final,
                    'title': book.css('h3 a').attrib['title'],
                    'availability': book.css('p.instock.availability::text')[1].get().strip()
                }
                yield response.follow(book_data['url'], callback=self.parse_book, meta={'book_data': book_data})
                                    # ,headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]} # if not using scrapeops fake user agents
                                    # ,meta = {"proxy" = ""} # if not using premium proxies middleware
                                    # ,url = get_proxy_url(book_data['url'])) # if not using scarpe ops builtin middleware


        next_page_url = response.css('li.next a::attr(href)').get()
        if next_page_url is not None : 
            if 'catalogue/' in next_page_url: 
                next_page_url_final = 'http://books.toscrape.com/'+ next_page_url
            else: 
                next_page_url_final = 'http://books.toscrape.com/catalogue/'+ next_page_url
            yield response.follow(next_page_url_final,callback=self.parse)
                                  # ,headers={"User-Agent": self.user_agent_list[random.randint(0, len(self.user_agent_list)-1)]} # if not using scrapeops fake user agents
                                  # ,meta = {"proxy" = ""} # if not using premium proxies middleware
                                  # ,url = get_proxy_url(next_page_url) # if not using scarpe ops builtin middleware



    def parse_book(self,response):

        book_data = response.meta['book_data']
        table_rows = response.css('table.table.table-striped tr')
        book_data.update({
            'books_available' : response.css('p.instock.availability::text')[1].get().strip().split()[2][1:],
            'rating' : response.css('p.star-rating::attr(class)').get().split()[1],
            'category' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
            'product_description' : response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
            'upc':table_rows[0].css('td::text').get(),
            'price_excl_tax' : table_rows[2].css('td::text').get() , 
            'price_incl_tax' : table_rows[3].css('td::text').get() , 
            'tax' : table_rows[4].css('td::text').get() ,
            'num_reviews' : table_rows[6].css('td::text').get()
        })
        book_items = BookItems()
        book_items['name'] = book_data['name']
        book_items['price'] = book_data['price']
        book_items['url'] = book_data['url']
        book_items['title'] = book_data['title']
        book_items['availability'] = book_data['availability']
        book_items['books_available'] = book_data['books_available']
        book_items['rating'] = book_data['rating']
        book_items['category'] = book_data['category']
        book_items['product_description'] = book_data['product_description']
        book_items['upc'] = book_data['upc']
        book_items['price_excl_tax'] = book_data['price_excl_tax']
        book_items['price_incl_tax'] = book_data['price_incl_tax']
        book_items['tax'] = book_data['tax']
        book_items['num_reviews'] = book_data['num_reviews']
        yield book_items




