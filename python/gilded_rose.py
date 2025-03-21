# -*- coding: utf-8 -*-

class GildedRose(object):
    
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            
            
            # filter out Aged Brie logic and backstage passes
            if item.name not in (self.AGED_BRIE, self.BACKSTAGE_PASSES):
                # filter out Sulfuras and quality > 0
                if item.quality > 0 and item.name != self.SULFURAS:
                        #this line will never run, all current objects are filtered out
                        item.quality -= 1


            # anything that is Aged Brie or backstage passes logic, still could be Sulfuras
            elif item.quality < 50:
                    
                    item.quality += 1
                    
                    # Backstage passes logic
                    if item.name == self.BACKSTAGE_PASSES:

                        # if item.sell_in < 11 add 1 to quality
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality += 1

                        # if item.sell_in < 6 add 1 to quality again
                        if item.sell_in < 6:
                            if item.quality < 50:
                                  item.quality += 1
            
            
            if item.name != self.SULFURAS:
                item.sell_in -= 1


            if item.sell_in < 0:
                if item.name != self.AGED_BRIE:
                    if item.name != self.BACKSTAGE_PASSES:
                        if item.quality > 0 and item.name != self.SULFURAS:
                                item.quality -= 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
