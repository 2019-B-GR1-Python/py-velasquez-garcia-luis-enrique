import scrapy 


class IntroSpider(scrapy.Spider):
    name = 'introduccion_spider'

    # urls = [
    #     'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    # ]

    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
    'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
    'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
    'http://books.toscrape.com/catalogue/category/books/classics_6/index.html',
    'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
    'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
    'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
    'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
    'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
    'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
    'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
    'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
    'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
    'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
    'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
    'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
    'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
    'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
    'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
    'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
    'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
    'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
    'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
    'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
    'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
    'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
    'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
    'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
    'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
    'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
    'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
    'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
    'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
    'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
    'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
    'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
    'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
    'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
    'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
    'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
    'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
    'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
    'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
    'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
    'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
    'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
    'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
    'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
    'http://books.toscrape.com/catalogue/category/books/crime_51/index.html']



    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)


    def parse(self, response):
        etiqueta_contenedora = response.css('article.product_pod')
        titulos = etiqueta_contenedora.css('h3 > a::text').extract()
        links = etiqueta_contenedora.css('div.image_container > a > img.thumbnail::attr(src)').extract()
        precios = etiqueta_contenedora.css('div.product_price > p.price_color::text').extract()
        categorias = response.css('div.side_categories > ul > li > ul > li > a::attr(href)').extract()
        pathImagenes = 'http://books.toscrape.com'
        pathCategorias = 'http://books.toscrape.com/catalogue/category/books'
        reemplazoImagenes = '../../../..'
        reemplazoCategorias = '..'
        
        def completarEnlace(path, reemplazo, array):
            for posicion in range(len(array)):
                array[posicion] = array[posicion].replace(reemplazo, path)
                #print(array[posicion])
        completarEnlace(pathImagenes, reemplazoImagenes, links)
        completarEnlace(pathCategorias, reemplazoCategorias, categorias)
        for a in range(len(categorias)):
            print(categorias[a])
        
        
        pathArchivo = "./libros_web.txt"
        archivo_escritura_abierto = open(pathArchivo, mode = "a")
        try:
            for a in range(len(titulos)):
                print(f"{titulos[a]}\n{links[a]}\n{precios[a]}\n") 
                archivo_escritura_abierto.writelines(f"{titulos[a]}\n{links[a]}\n{precios[a]}\n")
            archivo_escritura_abierto.close()
        except Exception as error:
            print("Error:"+error)

