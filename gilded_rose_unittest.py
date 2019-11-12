# -*- coding: utf-8 -*-

import unittest
from gilded_rose import *

class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_overdue_increase_twice(self):
        items = [Item("Aged Brie", 2, 0)]
        for day in range(0, 3):
            GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_aged_brie_after_30_days(self):
        items = [Item("Aged Brie", 2, 0)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(-28, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_normal_item_after_1_day(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_normal_item_after_30_days(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(-20, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_normal_item_case2_overdue_item(self):
        items = [Item("Elixir of the Mongoose",5,7)]
        for day in range(0, 6):
            GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_normal_item_case2_after_30_days(self):
        items = [Item("Elixir of the Mongoose",5,7)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(-25, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
            
    def test_sulfuras_item_after_30_days_case1(self):
        items = [Item("Sulfuras, Hand of Ragnaros", -1, 80)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_item_after_30_days_case2(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
                
    def test_backstage_passes_case1_after_1_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(14, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_passes_case2_after_30_days(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 49)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(-20, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_backstage_passes_case3_concert_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        for day in range(0, 5):
            GildedRose(items).update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_backstage_passes_case3_after_concert_day(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 49)]
        for day in range(0, 6):
            GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_conjured_item_after_1_day(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        GildedRose(items).update_quality()
        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(4, items[0].quality)

    def test_conjured_item_after_30_days(self):
        items = [Item("Conjured Mana Cake", 3, 6)]
        for day in range(0, 30):
            GildedRose(items).update_quality()
        self.assertEqual(-27, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
     
if __name__ == "__main__":
    unittest.main()
