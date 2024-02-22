# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        field_names = adapter.field_names()

        # stripping all whitespaces from strings
        for field_name in field_names:
            if field_name != 'product_description':
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()

        # upper_case -> lower_case
        keys = ['category', 'availability']
        for key in keys:
            value = adapter.get(key)
            adapter[key] = value.lower()

        # price -> conversion to float
        keys = ['price','price_excl_tax','price_incl_tax','tax']
        for key in keys:
            value = adapter.get(key)
            value = value.replace('£','')
            adapter[key] = float(value)

        # books_available,num_reviews -> int conversion
        keys = ['books_available,num_reviews']
        for key in keys: 
            value = adapter.get(key)
            if value is not None:
                adapter[key] = int(value)
        
        # rating -> converting to numeric string
        keys = ['rating']
        value = adapter.get(keys[0])
        value = value.lower()
        if value == 'one':
            value = '1/5'
        elif value == 'two':
            value = '2/5'
        elif value == 'three':
            value = '3/5'
        elif value == 'four':
            value = '4/5'
        elif value == 'five':
            value = '5/5'
        else : 
            value = '?/5'
        adapter[keys[0]] = str(value)


        



        return item
