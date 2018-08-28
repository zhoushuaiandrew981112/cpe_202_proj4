from bucketlist import *
from math import *
import unittest


class TestBucketeList(unittest.TestCase):

    def test_CityNode_init(self):

        ne = CityNode("ne", "cc", 0, 0)
        ne.ne_sw_height = 1
        sw = CityNode("sw", "cc", 0, 0)
        sw.ne_sw_height = 2
        nw = CityNode("nw", "cc", 0, 0)
        nw.nw_se_height = 2
        se = CityNode("se", "cc", 0, 0)
        se.nw_se_height = 1

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
        self.assertEqual(c_node.ne_sw_height, 1)
        self.assertEqual(c_node.nw_se_height, 1)
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
        self.assertEqual(c_node.ne_sw_height, 1)
        self.assertEqual(c_node.nw_se_height, 1)
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
        self.assertEqual(c_node.ne_sw_height, 1)
        self.assertEqual(c_node.nw_se_height, 1)
        c_node.children["ne"] = ne 
        c_node.children["sw"] = sw
        c_node.children["nw"] = nw
        c_node.children["se"] = se
        c_node.refresh_all_b_factor()
        c_node.refresh_b_factor_ne_sw()
        c_node.refresh_b_factor_nw_se()
        self.assertEqual(c_node.b_factor_ne_sw, 1)
        self.assertEqual(c_node.b_factor_nw_se, -1)

        sw = CityNode("sw", "cc", 0, 0)
        sw.ne_sw_height = 1
        ne = CityNode("ne", "cc", 0, 0)
        ne.ne_sw_height = 2
        se = CityNode("se", "cc", 0, 0)
        se.nw_se_height = 3
        nw = CityNode("nw", "cc", 0, 0)
        nw.nw_se_height = 4
        c_node.children = {"ne" : ne, "nw" : nw, "se" : None, "sw" : None}
        c_node.refresh_all_b_factor()
        c_node.refresh_b_factor_ne_sw()
        c_node.refresh_b_factor_nw_se()
        self.assertEqual(c_node.b_factor_ne_sw, -2)
        self.assertEqual(c_node.b_factor_nw_se, -4)
        c_node.children = {"ne" : None, "nw" : None, "se" : se, "sw" : sw}
        c_node.refresh_all_b_factor()
        c_node.refresh_b_factor_ne_sw()
        c_node.refresh_b_factor_nw_se()
        self.assertEqual(c_node.b_factor_ne_sw, 1)
        self.assertEqual(c_node.b_factor_nw_se, 3)


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

        self.assertEqual(b.find_ne_sw_height(), 3)
        self.assertEqual(b.find_nw_se_height(), 1)

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

        self.assertEqual(f.find_ne_sw_height(), 4)
        self.assertEqual(f.find_nw_se_height(), 1)

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

        self.assertEqual(g.find_ne_sw_height(), 4)
        self.assertEqual(g.find_nw_se_height(), 1)

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

    def test_city_node_rotate_right_ne_sw(self):

        """ only ne and sw node """
        a = CityNode("a", "cc", -10, -10)
        b = CityNode("b", "cc", 0, 0, a)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, b)

        b.children["ne"] = d
        b.children["sw"] = e
        a.children["ne"] = b
        a.children["sw"] = c

        a.rotate_right_ne_sw()

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["sw"], a)
        self.assertTrue(b.is_sw_of_self(a))
        self.assertEqual(b.children["ne"], d)
        self.assertTrue(b.is_ne_of_self(d))
        
        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["ne"], None)
        
        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["sw"], c)
        self.assertTrue(a.is_sw_of_self(c))
        self.assertEqual(a.children["ne"], e)
        self.assertTrue(a.is_ne_of_self(b))

        self.assertEqual(e.parent, a)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["ne"], None)

        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)

        """ self is ne child of parent """
        f = CityNode("f", "cc", -30, -30)
        b = CityNode("b", "cc", 0, 0, a)
        a = CityNode("a", "cc", -10, -10, f)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        f.children["ne"] = a
        b.children["ne"] = d
        b.children["sw"] = e
        a.children["ne"] = b
        a.children["sw"] = c

        a.rotate_right_ne_sw()

        self.assertEqual(f.parent, None)
        self.assertEqual(f.children["sw"], None)
        self.assertEqual(f.children["ne"], b)

        self.assertEqual(b.parent, f)
        self.assertEqual(b.children["sw"], a)
        self.assertEqual(b.children["ne"], d)
        
        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["ne"], None)
        
        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["sw"], c)
        self.assertEqual(a.children["ne"], e)

        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)

        self.assertEqual(e.parent, a)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["ne"], None)

        """ self is sw child of parent """
        g = CityNode("g", "cc", 30, 30)
        b = CityNode("b", "cc", 0, 0, a)
        a = CityNode("a", "cc", -10, -10, g)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, b)

        g.children["sw"] = a
        b.children["ne"] = d
        b.children["sw"] = e
        a.children["ne"] = b
        a.children["sw"] = c

        a.rotate_right_ne_sw()

        self.assertEqual(g.parent, None)
        self.assertEqual(g.children["sw"], b)
        self.assertEqual(g.children["ne"], None)

        self.assertEqual(b.parent, g)
        self.assertEqual(b.children["sw"], a)
        self.assertEqual(b.children["ne"], d)
        
        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["ne"], None)
        
        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["sw"], c)
        self.assertEqual(a.children["ne"], e)

        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)

        self.assertEqual(e.parent, a)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["ne"], None)

    def test_city_node_rotate_left_nw_se(self):
        
        """ only ne and sw node """
        b = CityNode("b", "cc", 0, 0)
        a = CityNode("a", "cc", -10, -10, b)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        b.children["nw"] = d
        b.children["se"] = a
        a.children["nw"] = e
        a.children["se"] = c

        self.assertEqual(b.find_ne_sw_height(), 1)
        self.assertEqual(b.find_nw_se_height(), 3)

        b.rotate_left_nw_se()

        self.assertEqual(a.parent, None)
        self.assertEqual(a.children["se"], c)
        self.assertTrue(a.is_sw_of_self(c))
        self.assertEqual(a.children["nw"], b)
        self.assertTrue(a.is_ne_of_self(b))
        
        self.assertEqual(c.parent, a)
        self.assertEqual(c.parent.name, "a")
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)
        
        self.assertEqual(b.parent, a)
        self.assertEqual(b.children["se"], e)
        self.assertTrue(b.is_sw_of_self(e))
        self.assertEqual(b.children["nw"], d)
        self.assertTrue(b.is_ne_of_self(d))

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["se"], None)
        self.assertEqual(d.children["nw"], None)

        self.assertEqual(e.parent, b)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.children["nw"], None)

        """ self is nw child of parent """
        f = CityNode("f", "cc", -30, -30)
        b = CityNode("b", "cc", 0, 0, f)
        a = CityNode("a", "cc", -10, -10, b)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        f.children["nw"] = b
        b.children["nw"] = d
        b.children["se"] = a
        a.children["nw"] = e
        a.children["se"] = c

        self.assertEqual(f.find_ne_sw_height(), 1)
        self.assertEqual(f.find_nw_se_height(), 4)

        b.rotate_left_nw_se()

        self.assertEqual(f.parent, None)
        self.assertEqual(f.children["se"], None)
        self.assertEqual(f.children["nw"], a)

        self.assertEqual(a.parent, f)
        self.assertEqual(a.children["se"], c)
        self.assertEqual(a.children["nw"], b)
        
        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)
        
        self.assertEqual(b.parent, a)
        self.assertEqual(b.children["se"], e)
        self.assertEqual(b.children["nw"], d)

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["se"], None)
        self.assertEqual(d.children["nw"], None)

        self.assertEqual(e.parent, b)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.children["nw"], None)

        """ self is se child of parent """
        g = CityNode("g", "cc", 30, 30)
        b = CityNode("b", "cc", 0, 0, g)
        a = CityNode("a", "cc", -10, -10, b)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        g.children["se"] = b
        b.children["nw"] = d
        b.children["se"] = a
        a.children["nw"] = e
        a.children["se"] = c

        self.assertEqual(f.find_ne_sw_height(), 1)
        self.assertEqual(f.find_nw_se_height(), 4)

        b.rotate_left_nw_se()

        self.assertEqual(g.parent, None)
        self.assertEqual(g.children["se"], a)
        self.assertEqual(g.children["nw"], None)

        self.assertEqual(a.parent, g)
        self.assertEqual(a.children["se"], c)
        self.assertEqual(a.children["nw"], b)
        
        self.assertEqual(c.parent, a)
        self.assertEqual(c.parent.name, "a")
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)
        
        self.assertEqual(b.parent, a)
        self.assertEqual(b.children["se"], e)
        self.assertEqual(b.children["nw"], d)

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["se"], None)
        self.assertEqual(d.children["nw"], None)

        self.assertEqual(e.parent, b)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.children["nw"], None)

    def test_city_node_rotate_right_nw_se(self):

        """ only nw and se node """
        a = CityNode("a", "cc", -10, -10)
        b = CityNode("b", "cc", 0, 0, a)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, b)

        b.children["nw"] = d
        b.children["se"] = e
        a.children["nw"] = b
        a.children["se"] = c

        self.assertEqual(a.find_ne_sw_height(), 1)
        self.assertEqual(a.find_nw_se_height(), 3)

        a.rotate_right_nw_se()

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["se"], a)
        self.assertTrue(b.is_sw_of_self(a))
        self.assertEqual(b.children["nw"], d)
        self.assertTrue(b.is_ne_of_self(d))
        
        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["se"], None)
        self.assertEqual(d.children["nw"], None)
        
        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["se"], c)
        self.assertTrue(a.is_sw_of_self(c))
        self.assertEqual(a.children["nw"], e)
        self.assertTrue(a.is_ne_of_self(b))

        self.assertEqual(e.parent, a)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.children["nw"], None)

        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)

        """ self is nw child of parent """
        f = CityNode("f", "cc", -30, -30)
        b = CityNode("b", "cc", 0, 0, a)
        a = CityNode("a", "cc", -10, -10, f)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, a)

        f.children["nw"] = a
        b.children["nw"] = d
        b.children["se"] = e
        a.children["nw"] = b
        a.children["se"] = c

        a.rotate_right_nw_se()

        self.assertEqual(f.parent, None)
        self.assertEqual(f.children["se"], None)
        self.assertEqual(f.children["nw"], b)

        self.assertEqual(b.parent, f)
        self.assertEqual(b.children["se"], a)
        self.assertEqual(b.children["nw"], d)
        
        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["se"], None)
        self.assertEqual(d.children["nw"], None)
        
        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["se"], c)
        self.assertEqual(a.children["nw"], e)

        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)

        self.assertEqual(e.parent, a)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.children["nw"], None)

        """ self is se child of parent """
        g = CityNode("g", "cc", 30, 30)
        b = CityNode("b", "cc", 0, 0, a)
        a = CityNode("a", "cc", -10, -10, g)
        c = CityNode("c", "cc", -20, -20, a)
        d = CityNode("d", "cc", 10, 10, b)
        e = CityNode("e", "cc", -5, -5, b)

        g.children["se"] = a
        b.children["nw"] = d
        b.children["se"] = e
        a.children["nw"] = b
        a.children["se"] = c

        a.rotate_right_nw_se()

        self.assertEqual(g.parent, None)
        self.assertEqual(g.children["se"], b)
        self.assertEqual(g.children["nw"], None)

        self.assertEqual(b.parent, g)
        self.assertEqual(b.children["se"], a)
        self.assertEqual(b.children["nw"], d)
        
        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["se"], None)
        self.assertEqual(d.children["nw"], None)
        
        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["se"], c)
        self.assertEqual(a.children["nw"], e)

        self.assertEqual(c.parent, a)
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)

        self.assertEqual(e.parent, a)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.children["nw"], None)

    def test_CityNode_right_left_ne_sw(self):
        a = CityNode("a", "cc", 0, 0)
        c = CityNode("c", "cc", 0, 0, a)
        c.b_factor_ne_sw = -2
        b = CityNode("b", "cc", 0, 0, c)

        a.children["sw"] = c
        c.children["ne"] = b
       
        a.right_left_ne_sw(c)  

        self.assertEqual(a.children["sw"], b)
        self.assertEqual(b.children["sw"], c)

        b.rotate_left_ne_sw()

        d = CityNode("b", "cc", 0, 0, a)
        a.children["ne"] = d

        a.right_left_ne_sw(c)  

        self.assertEqual(a.children["sw"], b)
        self.assertEqual(b.children["sw"], c)
        self.assertEqual(a.children["ne"], d)

        b.rotate_left_ne_sw()

        e = CityNode("e", "cc", 0, 0, d)
        d.children["ne"] = e

        a.right_left_ne_sw(c)  

        self.assertEqual(a.children["sw"], b)
        self.assertEqual(b.children["sw"], c)
        self.assertEqual(a.children["ne"], d)
        self.assertEqual(d.children["ne"], e)
 

    def test_CityNode_left_right_ne_sw(self):
        a = CityNode("a", "cc", 0, 0)
        c = CityNode("c", "cc", 0, 0, a)
        c.b_factor_ne_sw = 2
        b = CityNode("b", "cc", 0, 0, c)

        a.children["ne"] = c
        c.children["sw"] = b
       
        a.left_right_ne_sw(c)  

        self.assertEqual(a.children["ne"], b)
        self.assertEqual(b.children["ne"], c)

        b.rotate_right_ne_sw()

        d = CityNode("d", "cc", 0, 0, a)
        a.children["sw"] = d

        a.left_right_ne_sw(c)

        self.assertEqual(a.children["ne"], b)
        self.assertEqual(b.children["ne"], c)
        self.assertEqual(a.children["sw"], d)

        b.rotate_right_ne_sw()

        e = CityNode("e", "cc", 0, 0, d)
        d. children["sw"] = e

        a.left_right_ne_sw(c)

        self.assertEqual(a.children["ne"], b)
        self.assertEqual(b.children["ne"], c)
        self.assertEqual(a.children["sw"], d)
        self.assertEqual(d.children["sw"], e)

    def test_CityNode_right_left_nw_se(self):
        a = CityNode("a", "cc", 0, 0)
        c = CityNode("c", "cc", 0, 0, a)
        c.b_factor_nw_se = -2
        b = CityNode("b", "cc", 0, 0, c)

        a.children["se"] = c
        c.children["nw"] = b
       
        self.assertEqual(a.find_ne_sw_height(), 1)
        self.assertEqual(a.find_nw_se_height(), 3)

        a.right_left_nw_se(c)  

        self.assertEqual(a.children["se"], b)
        self.assertEqual(b.children["se"], c)

        b.rotate_left_nw_se()

        d = CityNode("b", "cc", 0, 0, a)
        a.children["nw"] = d

        a.right_left_nw_se(c)  

        self.assertEqual(a.children["se"], b)
        self.assertEqual(b.children["se"], c)
        self.assertEqual(a.children["nw"], d)

        b.rotate_left_nw_se()

        e = CityNode("e", "cc", 0, 0, a)
        d.children["nw"] = e

        a.right_left_nw_se(c)  

        self.assertEqual(a.children["se"], b)
        self.assertEqual(b.children["se"], c)
        self.assertEqual(a.children["nw"], d)
        self.assertEqual(d.children["nw"], e)

    def test_CityNode_left_right_nw_se(self):
        a = CityNode("a", "cc", 0, 0)
        c = CityNode("c", "cc", 0, 0, a)
        c.b_factor_nw_se = 2
        b = CityNode("b", "cc", 0, 0, c)

        a.children["nw"] = c
        c.children["se"] = b
       
        a.left_right_nw_se(c)  

        self.assertEqual(a.children["nw"], b)
        self.assertEqual(b.children["nw"], c)
        
        b.rotate_right_nw_se()

        d = CityNode("d", "cc", 0, 0, a)
        a.children["se"] = d

        a.left_right_nw_se(c)

        self.assertEqual(a.children["nw"], b)
        self.assertEqual(b.children["nw"], c)
        self.assertEqual(a.children["se"], d)

        b.rotate_right_nw_se()

        e = CityNode("e", "cc", 0, 0, d)
        d. children["se"] = e

        a.left_right_nw_se(c)

        self.assertEqual(a.children["nw"], b)
        self.assertEqual(b.children["nw"], c)
        self.assertEqual(a.children["se"], d)
        self.assertEqual(d.children["se"], e)

    def test_CityNode_rebalance(self):
        a = CityNode("a", "cc", 0, 0)
        a. ne_sw_height = 3
        c = CityNode("c", "cc", 0, 0, a)
        c. ne_sw_height = 2
        b = CityNode("b", "cc", 0, 0, c)
        b. ne_sw_height = 1

        a.children["sw"] = c
        c.children["ne"] = b

        a.refresh_all_b_factor()
        b.refresh_all_b_factor()
        c.refresh_all_b_factor()

        c.rebalance(b)

        self.assertEqual(b.children["sw"], c)
        self.assertEqual(b.children["ne"], a)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)

        a = CityNode("a", "cc", 0, 0)
        a. ne_sw_height = 3
        c = CityNode("c", "cc", 0, 0, a)
        c. ne_sw_height = 2
        b = CityNode("b", "cc", 0, 0, c)
        b. ne_sw_height = 1

        a.children["ne"] = c
        c.children["sw"] = b

        a.refresh_all_b_factor()
        b.refresh_all_b_factor()
        c.refresh_all_b_factor()

        c.rebalance(b)

        self.assertEqual(b.children["sw"], a)
        self.assertEqual(b.children["ne"], c)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["ne"], None)

        a = CityNode("a", "cc", 0, 0)
        a. nw_se_height = 3
        c = CityNode("c", "cc", 0, 0, a)
        c. nw_se_height = 2
        b = CityNode("b", "cc", 0, 0, c)
        b. nw_se_height = 1

        a.children["se"] = c
        c.children["nw"] = b

        a.refresh_all_b_factor()
        b.refresh_all_b_factor()
        c.refresh_all_b_factor()

        c.rebalance(b)

        self.assertEqual(b.children["se"], c)
        self.assertEqual(b.children["nw"], a)
        self.assertEqual(a.children["se"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)

        a = CityNode("a", "cc", 0, 0)
        a. nw_se_height = 3
        c = CityNode("c", "cc", 0, 0, a)
        c. nw_se_height = 2
        b = CityNode("b", "cc", 0, 0, c)
        b. nw_se_height = 1

        a.children["nw"] = c
        c.children["se"] = b

        a.refresh_all_b_factor()
        b.refresh_all_b_factor()
        c.refresh_all_b_factor()

        c.rebalance(b)

        self.assertEqual(b.children["se"], a)
        self.assertEqual(b.children["nw"], c)
        self.assertEqual(a.children["se"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(c.children["se"], None)
        self.assertEqual(c.children["nw"], None)

    def test_CityNode_insert(self):
        a = CityNode("a", "cc", 0, 0) 
        b = CityNode("b", "cc", -10, -10) 
        c = CityNode("c", "cc", -15, -15) 
        d = CityNode("d", "cc", 11, 11) 
        e = CityNode("e", "cc", 20, 20) 
   
        self.assertEqual(a.parent, None)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)

        a.insert(b, a)
     
        self.assertEqual(a.parent, None)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], b)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)

        self.assertEqual(b.parent, a)
        self.assertEqual(b.children["ne"], None)
        self.assertEqual(b.children["sw"], None)
        self.assertEqual(b.children["nw"], None)
        self.assertEqual(b.children["se"], None)

        a.insert(c, a)

        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["ne"], a)
        self.assertEqual(b.children["sw"], c)
        self.assertEqual(b.children["nw"], None)
        self.assertEqual(b.children["se"], None)
         
        self.assertEqual(c.parent, b)
        self.assertEqual(c.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["nw"], None)
        self.assertEqual(c.children["se"], None)

        b.insert(d, b)

        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["ne"], d)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["ne"], a)
        self.assertEqual(b.children["sw"], c)
        self.assertEqual(b.children["nw"], None)
        self.assertEqual(b.children["se"], None)
         
        self.assertEqual(c.parent, b)
        self.assertEqual(c.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["nw"], None)
        self.assertEqual(c.children["se"], None)

        self.assertEqual(d.parent, a)
        self.assertEqual(d.children["ne"], None)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["nw"], None)
        self.assertEqual(d.children["se"], None)

        b.insert(e, b)

        self.assertEqual(a.parent, d)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)
        self.assertEqual(a.ne_sw_height, 1)
        self.assertEqual(a.nw_se_height, 1)

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["ne"], d)
        self.assertEqual(b.children["sw"], c)
        self.assertEqual(b.children["nw"], None)
        self.assertEqual(b.children["se"], None)
        a.rebalance_refresh_height(a)
        self.assertEqual(b.ne_sw_height, 3)
        self.assertEqual(b.nw_se_height, 1)
         
        self.assertEqual(c.parent, b)
        self.assertEqual(c.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["nw"], None)
        self.assertEqual(c.children["se"], None)

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["ne"], e)
        self.assertEqual(d.children["sw"], a)
        self.assertEqual(d.children["nw"], None)
        self.assertEqual(d.children["se"], None)
        d.rebalance_refresh_height(d)
        self.assertEqual(d.ne_sw_height, 2)
        self.assertEqual(d.nw_se_height, 1)

        self.assertEqual(e.parent, d)
        self.assertEqual(e.children["ne"], None)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["nw"], None)
        self.assertEqual(e.children["se"], None)
        e.rebalance_refresh_height(e)
        self.assertEqual(e.ne_sw_height, 1)
        self.assertEqual(e.nw_se_height, 1)


        a = CityNode("a", "cc", 0, 0) 
        b = CityNode("b", "cc", -10, 10) 
        c = CityNode("c", "cc", -15, 15) 
        d = CityNode("d", "cc", 11, -11) 
        e = CityNode("e", "cc", 20, -20) 
   
        self.assertEqual(a.parent, None)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)

        a.insert(b, a)
     
        self.assertEqual(a.parent, None)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], b)

        self.assertEqual(b.parent, a)
        self.assertEqual(b.children["ne"], None)
        self.assertEqual(b.children["sw"], None)
        self.assertEqual(b.children["nw"], None)
        self.assertEqual(b.children["se"], None)

        a.insert(c, a)

        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["ne"], None)
        self.assertEqual(b.children["sw"], None)
        self.assertEqual(b.children["nw"], a)
        self.assertEqual(b.children["se"], c)
         
        self.assertEqual(c.parent, b)
        self.assertEqual(c.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["nw"], None)
        self.assertEqual(c.children["se"], None)

        b.insert(d, b)

        self.assertEqual(a.parent, b)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], d)
        self.assertEqual(a.children["se"], None)

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["ne"], None)
        self.assertEqual(b.children["sw"], None)
        self.assertEqual(b.children["nw"], a)
        self.assertEqual(b.children["se"], c)
         
        self.assertEqual(c.parent, b)
        self.assertEqual(c.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["nw"], None)
        self.assertEqual(c.children["se"], None)

        self.assertEqual(d.parent, a)
        self.assertEqual(d.children["ne"], None)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["nw"], None)
        self.assertEqual(d.children["se"], None)

        b.insert(e, b)

        self.assertEqual(a.parent, d)
        self.assertEqual(a.children["ne"], None)
        self.assertEqual(a.children["sw"], None)
        self.assertEqual(a.children["nw"], None)
        self.assertEqual(a.children["se"], None)
        self.assertEqual(a.ne_sw_height, 1)
        self.assertEqual(a.nw_se_height, 1)

        self.assertEqual(b.parent, None)
        self.assertEqual(b.children["ne"], None)
        self.assertEqual(b.children["sw"], None)
        self.assertEqual(b.children["nw"], d)
        self.assertEqual(b.children["se"], c)
        self.assertEqual(b.ne_sw_height, 1)
        self.assertEqual(b.nw_se_height, 3)
         
        self.assertEqual(c.parent, b)
        self.assertEqual(c.children["ne"], None)
        self.assertEqual(c.children["sw"], None)
        self.assertEqual(c.children["nw"], None)
        self.assertEqual(c.children["se"], None)

        self.assertEqual(d.parent, b)
        self.assertEqual(d.children["ne"], None)
        self.assertEqual(d.children["sw"], None)
        self.assertEqual(d.children["nw"], e)
        self.assertEqual(d.children["se"], a)
        self.assertEqual(d.ne_sw_height, 1)
        self.assertEqual(d.nw_se_height, 2)

        self.assertEqual(e.parent, d)
        self.assertEqual(e.children["ne"], None)
        self.assertEqual(e.children["sw"], None)
        self.assertEqual(e.children["nw"], None)
        self.assertEqual(e.children["se"], None)
        self.assertEqual(e.ne_sw_height, 1)
        self.assertEqual(e.nw_se_height, 1)










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
