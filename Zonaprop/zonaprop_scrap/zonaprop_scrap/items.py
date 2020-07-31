# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZonapropScrapItem(scrapy.Item):
    # define the fields for your item here like:
    _z_title=scrapy.Field()
    _b_tipo_prop=scrapy.Field()
    _c_tipo_oper=scrapy.Field()
    _d_prov_data=scrapy.Field()
    _e_partido_data=scrapy.Field()
    _f_localidad_data=scrapy.Field()
    _g_barrio_data=scrapy.Field()
    _h_dormi=scrapy.Field()
    _i_currency=scrapy.Field()
    _j_prop_price=scrapy.Field()
    _k_sup_prop=scrapy.Field()
    _l_old_prop=scrapy.Field()
    _m_dispo_prop=scrapy.Field()
    _n_bath_amount=scrapy.Field()
    _o_link_prop=scrapy.Field()
    # name = scrapy.Field()
    