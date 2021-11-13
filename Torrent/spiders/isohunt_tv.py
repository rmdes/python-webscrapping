from __future__ import absolute_import

from scrapy import Request
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import Identity
from scrapy.spiders import Rule

from ..utils.spiders import BasePortiaSpider
from ..utils.starturls import FeedGenerator, FragmentGenerator
from ..utils.processors import Item, Field, Text, Number, Price, Date, Url, Image, Regex
from ..items import PortiaItem


class IsohuntTv(BasePortiaSpider):
    name = "isohunt.tv"
    allowed_domains = [u'isohunt.tv']
    start_urls = [
        u'https://isohunt.tv/torrent_details/t3-5043381/Dune-Part-One-2021-HBO-Max-4K-to-1080p-HEVC-OPUS-HR-DR']
    rules = [
        Rule(
            LinkExtractor(
                allow=(),
                deny=('.*')
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [[Item(PortiaItem,
                   None,
                   u'.p:nth-child(1)',
                   [Field(u'Title',
                          '.torrent-header > .link-textcolor::attr(href)',
                          []),
                       Field(u'Info',
                             '.text-lg *::text',
                             []),
                       Field(u'Tor',
                             '.btn-group > .btn-download::attr(href)',
                             []),
                       Field(u'Magnet',
                             '.btn-group > .btn-magnet::attr(href)',
                             []),
                       Field(u'Desc',
                             '.tab-content > .active > .torrent-description > div > pre *::text',
                             [])])]]
