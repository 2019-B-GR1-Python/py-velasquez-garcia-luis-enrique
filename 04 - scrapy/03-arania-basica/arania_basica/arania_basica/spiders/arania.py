import scrapy

class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider' # name siempre tiene que declararse como 'name'
    
    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]
    def start_requests(self): # esta funcion siempre tiene este nombre
        for url in self.urls:
            yield scrapy.Request(url=url) #espera a que se complete la linea y no sea asincrona

    '''
    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract() # se concatena 
        print(titulos)
    '''
    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract() 
        for valor in precios:
            print(valor[1:])

    


