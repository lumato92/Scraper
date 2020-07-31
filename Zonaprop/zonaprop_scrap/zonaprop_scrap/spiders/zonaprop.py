import scrapy
from ..items import ZonapropScrapItem

NORDELTA='https://www.argenprop.com/inmuebles-localidad-nordelta'
SAN_ISIDRO=''
SAN_FERNANDO='https://www.argenprop.com/inmuebles-partido-san-fernando'
PILAR='https://www.argenprop.com/inmuebles-partido-pilar'

class Zonaprop_list(scrapy.Spider):
    name='zonaprop'
    start_urls = [PILAR+'-pagina-%s' % page for page in range(1,716)] # COLOCAR PARTIDO Y BUSCAR EN BROWSER CANTIDAD DE PAGINAS

    def parse (self, response):
        test=response.css('.listing__item a::attr(href)').extract()

        for i in test:
            
            url=response.urljoin(i)
            
            yield scrapy.Request(url,callback=self.parse_item_info)
        
    def parse_item_info(self, response):

        prop=ZonapropScrapItem()
        title=response.css('.titlebar__title::text').extract()
        tipo_prop=response.xpath('//*[@id="ga-dimension-ficha"]/@data-tipo-propiedad').extract()
        tipo_oper=response.xpath('//*[@id="ga-dimension-ficha"]/@data-tipo-operacion').extract()
        prov_data=response.xpath('//*[@id="ga-dimension-ficha"]/@data-provincia').extract()
        partido_data=response.xpath('//*[@id="ga-dimension-ficha"]/@data-partido').extract()
        localidad_data=response.xpath('//*[@id="ga-dimension-ficha"]/@data-localidad').extract()
        barrio_data=response.xpath('//*[@id="ga-dimension-ficha"]/@data-barrio').extract()
        dormi=response.xpath('//*[@id="ga-dimension-ficha"]/@data-dormitorios').extract()
        currency=response.xpath('//*[@id="ga-dimension-ficha"]/@data-moneda').extract()
        prop_price=response.xpath('//*[@id="ga-dimension-ficha"]/@data-price').extract()
        sup_prop=response.xpath('/html/body/main/div[1]/div[1]/div[1]/div[3]/ul/li[1]/span/text()').extract()
        old_prop=response.xpath('/html/body/main/div[1]/div[1]/div[1]/div[3]/ul/li[3]/span/text()').extract() #PUEDE DAR DATO ERRONEO
        dispo_prop=response.xpath('/html/body/main/div[1]/div[1]/div[1]/div[3]/ul/li[4]/span/text()').extract() #PUEDE DAR DATO ERRONEO
        bath_amount=response.xpath('/html/body/main/div[1]/div[1]/div[1]/div[3]/ul/li[5]/span/text()').extract() #PUEDE DAR DATO ERRONEO
        link_prop=response.url

        prop['_z_title']=title
        prop['_b_tipo_prop']=tipo_prop
        prop['_c_tipo_oper']=tipo_oper
        prop['_d_prov_data']=prov_data
        prop['_e_partido_data']=partido_data
        prop['_f_localidad_data']=localidad_data
        prop['_g_barrio_data']=barrio_data
        prop['_h_dormi']=dormi
        prop['_i_currency']=currency
        prop['_j_prop_price']=prop_price
        prop['_k_sup_prop']=sup_prop
        prop['_l_old_prop']=old_prop
        prop['_m_dispo_prop']=dispo_prop
        prop['_n_bath_amount']=bath_amount
        prop['_o_link_prop']=link_prop

        yield prop

    def parse_pag(self, response):

        test=response.css('.listing__item a::attr(href)').extract()
        next_page=response.css('.pagination__page-next a::attr(href)').extract()

        for i in test:
            url=response.urljoin(i)
            print(url)
        if next_page is not None:
            next_url=response.urljoin(next_page)
            yield scrapy.Request(next_url,callback=self.parse_pag)        



















'''       
        #item_url=[]
        #base_url='https://www.argenprop.com'
        yield {'all': response.css('.listing__item//a::attr(href)')
        
        for sel_item_url in all_item_url:
            #item_url=base_url+sel_item_url
            item_url1=response.urljoin(item_url)
            yield scrapy.Request(item_url1, callback=self.parse_item_info)




        #yield #{'price':price}
        #   item_url.append(sel_item.css('a::attr(href)').extract())
        #    yield {'item_url':item_url}
            #return item_url
        #yield {'all':all_item}


'''