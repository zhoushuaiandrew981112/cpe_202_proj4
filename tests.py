from bucketlist import *
from math import *
import unittest


class TestBucketeList(unittest.TestCase):

    def test_CityNode_init(self):

        ne = CityNode("ne", "cc", 0, 0)
        ne.height = 1
        sw = CityNode("sw", "cc", 0, 0)
        sw.height = 2
        nw = CityNode("nw", "cc", 0, 0)
        nw.height = 2
        se = CityNode("se", "cc", 0, 0)
        se.height = 1

        c_node = CityNode("San Ramon", "CC", 11, 22)
        self.assertEqual(c_node.name, "San Ramon")
        self.assertEqual(c_node.country, "CC")
        self.assertEqual(c_node.lat, 11)
        self.assertEqual(c_node.lon, 22)
        self.assertEqual(c_node.children, {"ne" : None, "nw" : None, "se" : None, "sw" : None})
        self.assertEqual(c_node.airport, None)
        self.assertEqual(c_node.distance, None)
        self.assertEqual(c_node.parent, None)
        self.assertEqual(c_node.b_factor_ne_sw, 0)
        self.assertEqual(c_node.b_factor_nw_se, 0)
        self.assertEqual(c_node.height, 1)
        c_node.children["ne"] = ne 
        c_node.children["sw"] = sw
        c_node.children["nw"] = nw
        c_node.children["se"] = se
        c_node.refresh_all_b_factor()
        c_node.refresh_b_factor_ne_sw()
        c_node.refresh_b_factor_nw_se()
        self.assertEqual(c_node.b_factor_ne_sw, 1)
        self.assertEqual(c_node.b_factor_nw_se, -1)

        c_node = CityNode("San Francisco", "CC", 33, 44)
        self.assertEqual(c_node.name, "San Francisco")
        self.assertEqual(c_node.country, "CC")
        self.assertEqual(c_node.lat, 33)
        self.assertEqual(c_node.lon, 44)
        self.assertEqual(c_node.children, {"ne" : None, "nw" : None, "se" : None, "sw" : None})
        self.assertEqual(c_node.airport, None)
        self.assertEqual(c_node.distance, None)
        self.assertEqual(c_node.parent, None)
        self.assertEqual(c_node.b_factor_ne_sw, 0)
        self.assertEqual(c_node.b_factor_nw_se, 0)
        self.assertEqual(c_node.height, 1)
        c_node.children["ne"] = ne 
        c_node.children["sw"] = sw
        c_node.children["nw"] = nw
        c_node.children["se"] = se
        c_node.refresh_all_b_factor()
        c_node.refresh_b_factor_ne_sw()
        c_node.refresh_b_factor_nw_se()
        self.assertEqual(c_node.b_factor_ne_sw, 1)
        self.assertEqual(c_node.b_factor_nw_se, -1)

        c_node = CityNode("Los Angeles", "CC", 55, 66)
        self.assertEqual(c_node.name, "Los Angeles")
        self.assertEqual(c_node.country, "CC")
        self.assertEqual(c_node.lat, 55)
        self.assertEqual(c_node.lon, 66)
        self.assertEqual(c_node.children, {"ne" : None, "nw" : None, "se" : None, "sw" : None})
        self.assertEqual(c_node.airport, None)
        self.assertEqual(c_node.distance, None)
        self.assertEqual(c_node.parent, None)
        self.assertEqual(c_node.b_factor_ne_sw, 0)
        self.assertEqual(c_node.b_factor_nw_se, 0)
        self.assertEqual(c_node.height, 1)
        c_node.children["ne"] = ne 
        c_node.children["sw"] = sw
        c_node.children["nw"] = nw
        c_node.children["se"] = se
        c_node.refresh_all_b_factor()
        c_node.refresh_b_factor_ne_sw()
        c_node.refresh_b_factor_nw_se()
        self.assertEqual(c_node.b_factor_ne_sw, 1)
        self.assertEqual(c_node.b_factor_nw_se, -1)

    def test_city_location_comparason(self):
        c_ne = CityNode("c_ne", "cc", 90, 150)
        c_nw = CityNode("c_nw", "cc", 90, -150)
        c_se = CityNode("c_se", "cc", -90, 150)
        c_sw = CityNode("c_sw", "cc", -90, -150)
 
        self.assertFalse(c_ne.has_parent())
        self.assertFalse(c_nw.has_parent())
        self.assertFalse(c_se.has_parent())
        self.assertFalse(c_sw.has_parent())

        self.assertFalse(c_ne.has_child_ne())
        self.assertFalse(c_nw.has_child_ne())
        self.assertFalse(c_se.has_child_ne())
        self.assertFalse(c_sw.has_child_ne())

        self.assertFalse(c_ne.has_child_nw())
        self.assertFalse(c_nw.has_child_nw())
        self.assertFalse(c_se.has_child_nw())
        self.assertFalse(c_sw.has_child_nw())

        self.assertFalse(c_ne.has_child_se())
        self.assertFalse(c_nw.has_child_se())
        self.assertFalse(c_se.has_child_se())
        self.assertFalse(c_sw.has_child_se())

        self.assertFalse(c_ne.has_child_sw())
        self.assertFalse(c_nw.has_child_sw())
        self.assertFalse(c_se.has_child_sw())
        self.assertFalse(c_sw.has_child_sw())

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

        self.assertTrue(c_ne.has_no_child())
        self.assertTrue(c_nw.has_no_child())
        self.assertTrue(c_se.has_no_child())
        self.assertTrue(c_sw.has_no_child())

        self.assertFalse(c_ne.has_child_ne_sw())
        self.assertFalse(c_nw.has_child_ne_sw())
        self.assertFalse(c_se.has_child_ne_sw())
        self.assertFalse(c_se.has_child_nw_se())
        self.assertFalse(c_sw.has_child_nw_se())
        self.assertFalse(c_ne.has_child_nw_se())

    def test_city_node_rotate_left_ne_sw(self):
        
        """ only ne and sw node """
        b = CityNode("b", "cc", 0, 0)
        a = CityNode("a", "cc", -10, -10, b)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        b.children["ne"] = d
        b.children["sw"] = a
        a.children["ne"] = e
        a.children["sw"] = c

        b.rotate_left_ne_sw()

        self.assertEqual(a.parent, None)
        self.assertEqual(a.children["sw"], c)
        self.assertEqual(a.children["sw"].name, "c")
        self.assertTrue(a.is_sw_of_self(c))
        self.assertEqual(a.children["ne"], b)
        self.assertEqual(a.children["ne"].name, "b")
        self.assertTrue(a.is_ne_of_self(b))
        
        self.assertEqual(c.parent, a)
        self.assertEqual(c.parent.name, "a")
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)
        
        self.assertEqual(b.parent, a)
        self.assertEqual(b.parent.name, "a")
        self.assertEqual(b.children["sw"], e)
        self.assertEqual(b.children["sw"].name, "e")
        self.assertTrue(b.is_sw_of_self(e))
        self.assertEqual(b.children["ne"], d)
        self.assertEqual(b.children["ne"].name, "d")
        self.assertTrue(b.is_ne_of_self(d))

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["ne"], None)

        self.assertEqual(e.parent, b)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["ne"], None)

        """ self is ne child of parent """
        f = CityNode("f", "cc", -30, -30)
        b = CityNode("b", "cc", 0, 0, f)
        a = CityNode("a", "cc", -10, -10, b)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        f.children["ne"] = b
        b.children["ne"] = d
        b.children["sw"] = a
        a.children["ne"] = e
        a.children["sw"] = c

        b.rotate_left_ne_sw()

        self.assertEqual(f.parent, None)
        self.assertEqual(f.children["sw"], None)
        self.assertEqual(f.children["ne"], a)

        self.assertEqual(a.parent, f)
        self.assertEqual(a.children["sw"], c)
        self.assertEqual(a.children["sw"].name, "c")
        self.assertEqual(a.children["ne"], b)
        self.assertEqual(a.children["ne"].name, "b")
        
        self.assertEqual(c.parent, a)
        self.assertEqual(c.parent.name, "a")
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)
        
        self.assertEqual(b.parent, a)
        self.assertEqual(b.parent.name, "a")
        self.assertEqual(b.children["sw"], e)
        self.assertEqual(b.children["sw"].name, "e")
        self.assertEqual(b.children["ne"], d)
        self.assertEqual(b.children["ne"].name, "d")

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["ne"], None)

        self.assertEqual(e.parent, b)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["ne"], None)

        """ self is sw child of parent """
        g = CityNode("g", "cc", 30, 30)
        b = CityNode("b", "cc", 0, 0, g)
        a = CityNode("a", "cc", -10, -10, b)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        g.children["sw"] = b
        b.children["ne"] = d
        b.children["sw"] = a
        a.children["ne"] = e
        a.children["sw"] = c

        b.rotate_left_ne_sw()

        self.assertEqual(g.parent, None)
        self.assertEqual(g.children["sw"], a)
        self.assertEqual(g.children["ne"], None)

        self.assertEqual(a.parent, g)
        self.assertEqual(a.children["sw"], c)
        self.assertEqual(a.children["sw"].name, "c")
        self.assertEqual(a.children["ne"], b)
        self.assertEqual(a.children["ne"].name, "b")
        
        self.assertEqual(c.parent, a)
        self.assertEqual(c.parent.name, "a")
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)
        
        self.assertEqual(b.parent, a)
        self.assertEqual(b.parent.name, "a")
        self.assertEqual(b.children["sw"], e)
        self.assertEqual(b.children["sw"].name, "e")
        self.assertEqual(b.children["ne"], d)
        self.assertEqual(b.children["ne"].name, "d")

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["ne"], None)

        self.assertEqual(e.parent, b)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["ne"], None)


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
