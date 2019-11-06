# -*- coding: utf-8 -*-
#refactored code from source "https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/python/gilded_rose.py"
    
def quality_positive_value(item):
    return item.quality > 0

def quality_max_value(item):
    return item.quality < 50

def overdue_item(item):
    return item.sell_in < 0

def decrease_quality_value(item):
    if quality_positive_value(item):
        item.quality -= 1

def increase_quality_value(item):
    if quality_max_value(item):
        item.quality += 1

def can_be_bought(item):
    return item.name != "Sulfuras, Hand of Ragnaros"

def item_quality_decrease_twice(item):
    if "Conjured " in item.name:
        decrease_quality_value(item)

def item_quality_decrease(item):
    return item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert"
        
def item_backstage_passes(item):
    if item.name == "Backstage passes to a TAFKAL80ETC concert":
        if item.sell_in < 11:
            increase_quality_value(item)
        if item.sell_in < 6:
            increase_quality_value(item)
        if overdue_item(item):
            item.quality = item.quality - item.quality
    return item.quality

def decrease_quality(item):
    if item_quality_decrease(item):
        if can_be_bought(item):
            decrease_quality_value(item)
            item_quality_decrease_twice(item)
    else: 
        increase_quality_value(item)
        item_backstage_passes(item)

def update_sell_in(item):
    if can_be_bought(item):
        item.sell_in = item.sell_in - 1

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            decrease_quality(item)
            update_sell_in(item)
            if overdue_item(item): 
                decrease_quality(item)

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
