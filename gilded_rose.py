# -*- coding: utf-8 -*-
#refactored code from source "https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/python/gilded_rose.py"

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            self.decrease_quality(item)
            self.update_sell_in(item)
            if item.sell_in < 0: 
                self.decrease_quality(item)
    
    def decrease_quality_value(self, item):
        if item.quality > 0:
            item.quality -= 1

    def increase_quality_value(self, item):
        if item.quality < 50:
            item.quality += 1

    def item_quality_decrease_twice(self, item):
        if "Conjured " in item.name:
            self.decrease_quality_value(item)

    def item_quality_decrease(self,item):
        return item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert"
        
    def update_backstage_passes(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                self.increase_quality_value(item)
            if item.sell_in < 6:
                self.increase_quality_value(item)
            if item.sell_in<0:
                item.quality = item.quality - item.quality
        return item.quality

    def decrease_quality(self,item):
        if self.item_quality_decrease(item):
            if item.name != "Sulfuras, Hand of Ragnaros":
                self.decrease_quality_value(item)
                self.item_quality_decrease_twice(item)
        else: 
            self.increase_quality_value(item)
            self.update_backstage_passes(item)

    def update_sell_in(self,item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
