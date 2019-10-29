# -*- coding: utf-8 -*-
#modified code from source "https://github.com/emilybache/GildedRose-Refactoring-Kata/blob/master/python/test_gilded_rose.py"
from __future__ import print_function
import pickle
from gilded_rose import GildedRose
from gilded_rose import Item

if __name__ == "__main__":
    print ("OMGHAI!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
            ]

    days = 30
    results={}
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        for item in items:
            results[str(day)+" "+item.name]=str(item)
        print("")
        GildedRose(items).update_quality()

    with open('gildedroseresult.txt', 'wb') as handle:
        pickle.dump(results, handle)

