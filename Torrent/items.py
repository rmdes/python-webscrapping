from __future__ import absolute_import

import scrapy
from collections import defaultdict
from scrapy.loader.processors import Join, MapCompose, Identity
from w3lib.html import remove_tags
from .utils.processors import Text, Number, Price, Date, Url, Image


class PortiaItem(scrapy.Item):
    fields = defaultdict(
        lambda: scrapy.Field(
            input_processor=Identity(),
            output_processor=Identity()
        )
    )

    def __setitem__(self, key, value):
        self._values[key] = value

    def __repr__(self):
        data = str(self)
        if not data:
            return '%s' % self.__class__.__name__
        return '%s(%s)' % (self.__class__.__name__, data)

    def __str__(self):
        if not self._values:
            return ''
        string = super(PortiaItem, self).__repr__()
        return string


class DunePartOneHboMaxKToPHevcOpusHrDrToItem(PortiaItem):
    Desc = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Magnet = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Tor = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )
    Info = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Title = scrapy.Field(
        input_processor=Url(),
        output_processor=Join(),
    )


class DownloadDunephdripxEvotgxTorrentKickassToItem(PortiaItem):
    Summary = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Genre = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Name = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    DL = scrapy.Field(
        input_processor=Text(),
        output_processor=Join(),
    )
    Cover = scrapy.Field(
        input_processor=Image(),
        output_processor=Join(),
    )
