# -*- coding: utf-8 -*-
#refactored code from source "https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/python/gilded_rose.py"

def quality_positive_value(item):
    return item.quality>0

def quality_value_below_max(item):
    return item.quality <50

def quality_decrease(item):
    return item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert"

def quality_decrease_twice(item):
    return "Conjured " in item.name and quality_positive_value(item)

def name_backstage_passes(item):
    return "Backstage passes" in item.name

def can_be_bought(item):
    return item.name != "Sulfuras, Hand of Ragnaros"

def overdue_item(item):
    return item.sell_in < 0

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if quality_decrease(item):
                if can_be_bought(item) and quality_positive_value(item):
                    item.quality = item.quality - 1
                    if quality_decrease_twice(item):
                        item.quality=item.quality-1
            else: 
                if quality_value_below_max(item):
                    item.quality = item.quality + 1
                    if name_backstage_passes(item):
                        if item.sell_in < 11:
                            if quality_value_below_max(item):
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if quality_value_below_max(item):
                                item.quality = item.quality + 1
            if can_be_bought(item):
                item.sell_in = item.sell_in - 1 
            if overdue_item(item): 
                if quality_decrease(item):
                    if can_be_bought(item) and quality_positive_value(item):
                        item.quality = item.quality - 1
                        if quality_decrease_twice(item):
                            item.quality=item.quality-1
                elif name_backstage_passes(item): 
                    item.quality = item.quality - item.quality
                else: 
                    if quality_value_below_max(item):
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
