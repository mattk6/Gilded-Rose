# -*- coding: utf-8 -*-
import unittest
import random
from gilded_rose import Item, GildedRose
random.seed(21)

def rand(min_value, max_value):
  """Returns a random integer within the specified range."""
  return random.randint(min_value, max_value)


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

    def test_normal_item_quality_never_negative(self):
        quality = 0 # zero
        sell_in = rand(-100, 0) # must be zero or less
        items = [Item(self.NORMAL, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_quality_increases(self):
        quality = 0 # zero or greater
        sell_in = 1 # must be 1 or greater
        items = [Item(self.AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 1, items[0].quality)

    def test_aged_brie_quality_increases_twice_after_sell_in(self):
        quality = 0 # any number below 48
        sell_in = 0 # must be 0
        items = [Item(self.AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 2, items[0].quality)

    def test_aged_brie_quality_never_over_50(self):
        quality = 50 # any number 50 or higher
        sell_in = 9 # any number
        items = [Item(self.AGED_BRIE, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality, items[0].quality)

    def test_backstage_passes_quality_increases(self):
        quality = 2 # any number
        sell_in = 11 # any number 11 or higher
        items = [Item(self.BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 1, items[0].quality)

    def test_backstage_passes_quality_increases_by_2_when_sell_in_less_than_11(self):
        quality = 15 # any number
        sell_in = 10 # number less than 11
        items = [Item(self.BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 2, items[0].quality)

    def test_backstage_passes_quality_increases_by_3_when_sell_in_less_than_6(self):
        quality = 22 # any number
        sell_in = 5 # number less than 6
        items = [Item(self.BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(quality + 3, items[0].quality)

    def test_backstage_passes_quality_drops_to_0_after_concert(self):
        quality = 18 # any number
        sell_in = 0 # zero
        items = [Item(self.BACKSTAGE_PASSES, sell_in, quality)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

if __name__ == '__main__':
    unittest.main()

