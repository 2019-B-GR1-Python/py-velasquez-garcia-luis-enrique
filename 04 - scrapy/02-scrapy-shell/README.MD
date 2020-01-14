# Scrapy
## Scrapy instalación
Ejecutar dentro del `Anaconda Pront`.
```
$pip install scrapy
```

## Comandos Generales
Da `las caracteristicas` para poder hacer Web Scraping o Web Crawling 
de ese computador
```
$scrapy bench
```
Visualizar las 
`configuraciones extras`
```
$scrapy setting
```
Visualizamos la `version` de Scrapy
```
$ scrapy version
```

### scrapy view `url`
`Visualizar el contenido` como lo ve el Scrapy
Si se ve el contenido

```
$scrapy view https://www.pluralsight.com/authors
```
No se ve el contenido
```
$scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT
```
### scrapy shell `url`
Permite `interactuar con la respuesta` del scrapy
mediante un `shell` de python

```
$response.css('title')
$response.css('title').extract() -> devuelve el texto de la etiqueta en un arreglo 
$response.css('title::text').extract() -> devuelve solamente el texto  
$response.css('.author').extract() -> de vuelve toda una lista de autores de la pagina web 
$response.css('.author::text').extract() -> lista de solo nombres de autores 
$response.css('.author::text') -> devuelve un selectorList
$response.css('.author::text').extract()[0]
$response.css('.author::text')[0].extract() -> devuelve un String
$response.css('.author').extract_first() 
$response.css('span')
$response.css('span.title').extract()
$response.css('span.title::text').extract() -> obtenemos el texto de las frases
$response.css('.tag::text').extract() -> lista de etiquetas pero todas, se necesita diferenciar
$response.css('.row > div > div:nth-child(2) > .text::text').extract()

$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ //div[@class='quote']/span/a/@href").extract_first()
```
## Scrapy startproject `nombre_proyecto`
```
$ scrapy startproject arania_basica
```
```
$scrapy crawl `nombre_de_la_araña`
$scrapy crawl introduccion_spider
```

