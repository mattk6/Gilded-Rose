# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    NORMAL = "NORMAL"
    SULFURAS = "Sulfuras, Hand of Ragnaros"
    
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)
        # this line does nothing but get me to 100% coverage
        repr(items[0])

    def test_normal_item_quality_decreases(self):
        quality = 8 # 1 or greater
        sell_in = 12 # 1 or greater
        items = [Item(self.NORMAL, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 1, items[0].quality)

    def test_normal_item_quality_decreases_twice_after_sell_in(self):
        quality = 2 # 2 or greater
        sell_in = 0 # must be zero
        items = [Item(self.NORMAL, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality - 2, items[0].quality)

    def test_aged_brie_quality_increases_twice_after_sell_in(self):
        quality = 0 # any number below 48
        sell_in = 0 # must be 0
        items = [Item(self.AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 2, items[0].quality)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        quality = 18 # any number
        sell_in = 0 # zero
        items = [Item(self.BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()

