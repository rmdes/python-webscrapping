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


class KickasstorrentsCr(BasePortiaSpider):
    name = "kickasstorrents.cr"
    allowed_domains = [u'kickasstorrents.cr']
    start_urls = [
        u'https://kickasstorrents.cr/dune-2021-1080p-hdrip-x264-evo-tgx-t5020307.html']
    rules = [
        Rule(
            LinkExtractor(
                allow=('.*'),
                deny=()
            ),
            callback='parse_item',
            follow=True
        )
    ]
    items = [
        [
            Item(
                PortiaItem,
                None,
                u'#mainDetailsTable > tr > td:nth-child(1), #mainDetailsTable > tbody > tr > td:nth-child(1)',
                [
                    Field(
                        u'Name',
                        '#mainDetailsTable > tr > td:nth-child(1) > .novertmarg > a > span *::text, #mainDetailsTable > tbody > tr > td:nth-child(1) > .novertmarg > a > span *::text',
                        []),
                    Field(
                        u'DL',
                        '#mainDetailsTable > tr > td:nth-child(1) > .tabs > .HWGtj > .dssdffds > .fdger3425324 > span *::text, #mainDetailsTable > tbody > tr > td:nth-child(1) > .tabs > .HWGtj > .dssdffds > .fdger3425324 > span *::text',
                        []),
                    Field(
                        u'Genre',
                        '#mainDetailsTable > tr > td:nth-child(1) > .tabs > .HWGtj > .torrentMediaInfo > .dataList > .dataList > .block > li:nth-child(5) *::text, #mainDetailsTable > tbody > tr > td:nth-child(1) > .tabs > .HWGtj > .torrentMediaInfo > .dataList > .dataList > .block > li:nth-child(5) *::text',
                        []),
                    Field(
                        u'Summary',
                        '#mainDetailsTable > tr > td:nth-child(1) > .tabs > .HWGtj > .torrentMediaInfo > .dataList > .dataList > .floatleft > div > .accentbox *::text, #mainDetailsTable > tbody > tr > td:nth-child(1) > .tabs > .HWGtj > .torrentMediaInfo > .dataList > .dataList > .floatleft > div > .accentbox *::text',
                        []),
                    Field(
                        u'Cover',
                        '#mainDetailsTable > tr > td:nth-child(1) > .tabs > .HWGtj > .torrentMediaInfo > div.data > .textcontent > .align-center > a:nth-child(28) > .img-responsive::attr(src), #mainDetailsTable > tbody > tr > td:nth-child(1) > .tabs > .HWGtj > .torrentMediaInfo > div.data > .textcontent > .align-center > a:nth-child(28) > .img-responsive::attr(src)',
                        [])])]]
