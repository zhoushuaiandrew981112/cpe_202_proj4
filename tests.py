from bucketlist import *
from math import *
import unittest


class TestBucketeList(unittest.TestCase):

    def test_CityNode_init(self):
        c_node = CityNode("San Ramon", "CC", 11, 22)
        self.assertEqual(c_node.name, "San Ramon")
        self.assertEqual(c_node.country, "CC")
        self.assertEqual(c_node.lat, 11)
        self.assertEqual(c_node.lon, 22)
        self.assertEqual(c_node.children, {"ne" : None, "nw" : None, "se" : None, "sw" : None})
        self.assertEqual(c_node.airport, None)
        self.assertEqual(c_node.distance, None)
        self.assertEqual(c_node.parent, None)
        self.assertEqual(c_node.b_factor, 0)
        self.assertEqual(c_node.node_height, 1)

        c_node = CityNode("San Francisco", "CC", 33, 44)
        self.assertEqual(c_node.name, "San Francisco")
        self.assertEqual(c_node.country, "CC")
        self.assertEqual(c_node.lat, 33)
        self.assertEqual(c_node.lon, 44)
        self.assertEqual(c_node.children, {"ne" : None, "nw" : None, "se" : None, "sw" : None})
        self.assertEqual(c_node.airport, None)
        self.assertEqual(c_node.distance, None)
        self.assertEqual(c_node.parent, None)
        self.assertEqual(c_node.b_factor, 0)
        self.assertEqual(c_node.node_height, 1)

        c_node = CityNode("Los Angeles", "CC", 55, 66)
        self.assertEqual(c_node.name, "Los Angeles")
        self.assertEqual(c_node.country, "CC")
        self.assertEqual(c_node.lat, 55)
        self.assertEqual(c_node.lon, 66)
        self.assertEqual(c_node.children, {"ne" : None, "nw" : None, "se" : None, "sw" : None})
        self.assertEqual(c_node.airport, None)
        self.assertEqual(c_node.distance, None)
        self.assertEqual(c_node.parent, None)
        self.assertEqual(c_node.b_factor, 0)
        self.assertEqual(c_node.node_height, 1)

    def test_city_location_comparason(self):
        c_ne = CityNode("c_ne", "cc", 90, 150)
        c_nw = CityNode("c_nw", "cc", 90, -150)
        c_se = CityNode("c_se", "cc", -90, 150)
        c_sw = CityNode("c_sw", "cc", -90, -150)

        self.assertTrue(c_sw.is_ne_of_self(c_ne))
        self.assertTrue(c_se.is_nw_of_self(c_nw))
        self.assertTrue(c_nw.is_se_of_self(c_se))
        self.assertTrue(c_ne.is_sw_of_self(c_sw))

        self.assertFalse(c_sw.is_nw_of_self(c_ne))
        self.assertFalse(c_se.is_ne_of_self(c_nw))
        self.assertFalse(c_nw.is_sw_of_self(c_se))
        self.assertFalse(c_ne.is_se_of_self(c_sw))

        self.assertFalse(c_sw.is_se_of_self(c_ne))
        self.assertFalse(c_se.is_sw_of_self(c_nw))
        self.assertFalse(c_nw.is_ne_of_self(c_se))
        self.assertFalse(c_ne.is_nw_of_self(c_sw))

    def test_CountryTable_hash(self):
        size = 128515
        table = CountryTable(size)
        for x in range(97, 123):
            for y in range(97, 123):
                code = chr(x) + chr(y)
                self.assertEqual(table.hash(code), int(str(x) + str(y)))
        

    def test_CountryTable(self):
        
        "test __init__ and get_bucket_list"
        table = CountryTable(1)
        self.assertEqual(table.bucket_list, [None]*1)
        self.assertEqual(table.get_bucket_list(), [None]*1)
        self.assertEqual(table.num_items, 0)
        self.assertEqual(table.size, 1)
        self.assertEqual(table.get_load_factor(), 0)

        table = CountryTable(10)
        self.assertEqual(table.bucket_list, [None]*10)
        self.assertEqual(table.get_bucket_list(), [None]*10)
        self.assertEqual(table.num_items, 0)
        self.assertEqual(table.size, 10)
        self.assertEqual(table.get_load_factor(), 0)

        table = CountryTable(100)
        self.assertEqual(table.bucket_list, [None]*100)
        self.assertEqual(table.get_bucket_list(), [None]*100)
        self.assertEqual(table.num_items, 0)
        self.assertEqual(table.size, 100)
        self.assertEqual(table.get_load_factor(), 0)




if __name__ == '__main__':
    unittest.main()
