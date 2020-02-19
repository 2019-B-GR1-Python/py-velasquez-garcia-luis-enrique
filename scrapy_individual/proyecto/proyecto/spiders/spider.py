import scrapy 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from proyecto.items import ProyectoItem
from scrapy.exceptions import CloseSpider

class alibaba_spider(CrawlSpider):
    name = 'london'
    allowed_domains = ['https://www.londonstockexchange.com']
    start_urls = "https://www.londonstockexchange.com/exchange/prices-and-markets/stocks/prices-search/stock-prices-search.html?&page="
    number_pages = [i for i in range(2, 20)]
    urls = [start_urls]
    for page in number_pages:
        urls.append(start_urls + str(page))

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)   



    def write_to_csv(self, nombres, monedas, precios, cantidades, porcentajes):
        f = open("C://Users/Kike/Documents/GitHub/py-velasquez-garcia-luis-enrique/scrapy_individual/proyecto/tres.csv", "a+")
        # f.write(
        #    "\"Titulo\";\"Link\";\"Vistas\";\"Autor(es)\";\"Ultima actualizacion\";\"Ultimo Capitulo\"\n")
        for(name, cur, price, cant, porcnt) in zip(nombres, monedas, precios, cantidades, porcentajes):
            # print("\"" + title + "\";\"" + links_to_title
            # + "\";\"" + views + "\";\"" + authors + "\";\"" +
            # last_update_dates + "\";" + last_chapter + "\n")
            #f.write("\"" + name + "\";\"" + cur + "\";\"" + price + "\";\"" + cant + "\";\""+ porcnt+ "\"n")
            f.write(name + "," + cur + "," + price + "," + cant.strip() + ","+ porcnt.strip() + "\n")
        f.close()
    
    #rules = regla_uno   # Heredado (override)

    def parse(self, response):
        nombres = response.xpath('//table[@class = "table_dati"]/tbody/tr/td[@class = "name"]/a/text()').extract()
        monedas = response.xpath('//table[@class = "table_dati"]/tbody/tr/td[3]/text()').extract()
        precios = response.xpath('//table[@class = "table_dati"]/tbody/tr/td[4]/text()').extract()
        cantidades =  response.xpath('//table[@class = "table_dati"]/tbody/tr/td[5]/text()').extract()
        porcentajes =response.xpath('//table[@class = "table_dati"]/tbody/tr/td[6]/text()').extract()

        self.write_to_csv(nombres, monedas,precios,cantidades,porcentajes)

        #print("entrando")
        
        #for objeto in lista_moneda:
            #with open ('./london.csv', 'a+', encoding='utf-8') as archivo:
                #archivo.write(objeto +'\n')
            #print(objeto)
            #print("\n")