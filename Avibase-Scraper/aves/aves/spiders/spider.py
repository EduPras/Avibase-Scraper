import scrapy

global urls, ids_urls
urls = []
ids_urls = []

ids = [ 
    '4EB50482BEE5E52B',
    '454B5CD5F5285B77',
    'BE5C3C1174B2D215',
    ]

title = ['oi', 'pinto', 'pika']

for identification in ids:
    ids_urls.append('https://avibase.bsc-eoc.org/species.jsp?lang=EN&avibaseid='+identification)

for name in title:
    urls.append('https://avibase.bsc-eoc.org/search.jsp?pg=search&isadv=no&startstr=&startlang=&fam=&start=&qstr='+name+'&qtype=2&qstr2=&qtype=2&qlang=&qyears=&qauthors=&qinclsp=1')

class PostsSpider(scrapy.Spider):
    name = "posts"
    start_urls = urls

    def parse(self, response):

        xml = response.css('tr td a').get()
        id = xml.split('\'')[1].split('\')')[0]

        with open("search.txt", 'a' ) as f:            
            f.write(id)
            f.write('\n')


class getSynon(scrapy.Spider):
    name="synon"
    start_urls = ids_urls

    def parse(self,response):
        yield{
            "name": response.css('html body div.container-fluid div.row.main-body div.section.w-100 h2::text').get(),
            "scientific": response.css('html body div.container-fluid div.row.main-body div.section.w-100 div.card.w-100 div#card-body.card-body div.row div.col-lg-7 div.row div.col-lg-5 div#taxoninfo p i::text').get()
        }




