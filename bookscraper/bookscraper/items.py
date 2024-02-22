# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# def serialize_price(value):
#     return f"£ {str(value)[1:]}"
# serializer can do basic_functionality
# if you don't want to scrape huge amount of data and you don't want to lot of post-processing, serializers are good to go.
# also, if you don't want to use pipelines, then you should only be using serializer to post-process data

class BookItems(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    availability = scrapy.Field()
    books_available = scrapy.Field()
    rating = scrapy.Field()
    category = scrapy.Field()
    product_description = scrapy.Field()
    upc = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_incl_tax = scrapy.Field()
    tax = scrapy.Field()
    num_reviews = scrapy.Field()
