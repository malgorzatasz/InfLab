# -*- coding: utf-8 -*-

import unittest
import pickle
from gilded_rose import GildedRose
from gilded_rose import Item

class GildedRoseTest(unittest.TestCase):

    def test_aged_brie(self):
        items = [Item("Aged Brie", 2, 0)]
        for day in range(0, 30):
            with self.subTest(day=day):
                self.assertEqual(items[0].name+", "+str(items[0].sell_in)+", "+str(items[0].quality),results[str(day)+" Aged Brie"])
                GildedRose(items).update_quality()
       
    def test_normal_item(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        for day in range(0, 30):
            with self.subTest(day=day):
                self.assertEqual(items[0].name+", "+str(items[0].sell_in)+", "+str(items[0].quality),results[str(day)+" +5 Dexterity Vest"])
                GildedRose(items).update_quality()
            
    def test_sulfuras_item(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        for day in range(0, 30):
            with self.subTest(day=day):
                self.assertEqual(items[0].name+", "+str(items[0].sell_in)+", "+str(items[0].quality),results[str(day)+" Sulfuras, Hand of Ragnaros"])
                GildedRose(items).update_quality()
                
    def test_backstage_passes(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        for day in range(0, 30):
            with self.subTest(day=day):
                self.assertEqual(items[0].name+", "+str(items[0].sell_in)+", "+str(items[0].quality),results[str(day)+" Backstage passes to a TAFKAL80ETC concert"])
                GildedRose(items).update_quality()

    def test_conjured_item(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        for day in range(0, 30):
            with self.subTest(day=day):
                self.assertEqual(items[0].name+", "+str(items[0].sell_in)+", "+str(items[0].quality),results[str(day)+" Conjured Mana Cake"])
                GildedRose(items).update_quality()
    
with open('gildedroseresult.txt', 'rb') as handle:
    results = pickle.loads(handle.read())

        
if __name__ == "__main__":
    unittest.main()
