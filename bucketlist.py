# Name:          Zhoushuai(Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Proj 4: Bucket List
# Term:          Summer 2018


class CityNode:

    def __init__(self, city_name, country_code, latitude, longitude):
        self.name = city_name
        self.country = country_code
        self.lat = latitude
        self.lon = longitude
        self.children = {"ne" : None, "nw" : None, "se" : None, "sw" : None}
        self.airport = None
        self.distance = None
        self.parent = None
        self.b_factor_ne_sw = 0
        self.b_factor_nw_se = 0
        self.height = 1

    """
                                                            lat axis -->  N
    * The GREATER the lat, the more NORTH it is                           |
       - new is north of old: new.lat > old.lat           NW             --- 90 deg      NE
       - old is north of new: old.lat > new.lat                           |
    * The SMALLER the lat, the more SOUTH it is                           |
       - new is south of old: new.lat < old.lat                           |
       - old is south of new: old.lat < new.lat                           |
    * The GREATER the lon, the more EAST it is          W-|------------------------------|-E   <-- lon axis
       - new is east of old: new.lon > old.lon          -180 deg          |0 deg        180 deg
       - old is east of new: old.lon > new.lon                            |
    * The SMALLER the lon, the more WEST it is                            |
       - new is west of old: new.lon < old.lon                            |
       - old is west of new: old.lon < new.lon            SW             --- -90 deg     SE
                                                                          |
                                                                          S
                   (node)
                  / | |  \           * b_factor = right node height minus left node height
                 / /   \  \          * b_factor_ne_sw = sw.height - ne.height
                /  |   |   \         * b_factor_nw_se = se.height - nw.height
              (ne  sw)(nw  se)           * b_factor > 1   :  right heavy -> left  rotation 
                                         * b_factor < -1  :  left  heavy -> right rotation
    """ 

    def is_ne_of_self(self, new):
        return new.lat > self.lat and new.lon > self.lon


    def is_nw_of_self(self, new):
        return new.lat > self.lat and new.lon < self.lon


    def is_se_of_self(self, new):
        return new.lat < self.lat and new.lon > self.lon


    def is_sw_of_self(self, new):
        return new.lat < self.lat and new.lon < self.lon


    def has_no_child(self):
        ne = self.children["ne"] == None
        nw = self.children["nw"] == None
        se = self.children["se"] == None
        sw = self.children["sw"] == None
        return ne and nw and se and sw


    def has_child_ne_sw(self):
        ne = self.children["ne"] != None
        sw = self.children["sw"] != None
        return ne and sw


    def has_child_nw_se(self):
        nw = self.children["nw"] != None
        se = self.children["se"] != None
        return nw and se


    def refresh_b_factor_ne_sw(self):
        sw = self.children["sw"]
        ne = self.children["ne"]
        if sw != None and ne != None:
            self.b_factor_ne_sw = sw.height - ne.height


    def refresh_b_factor_nw_se(self):
        se = self.children["se"]
        nw = self.children["nw"]
        if se != None and nw != None:
            self.b_factor_nw_se = se.height - nw.height


    def refresh_all_b_factor(self):
        self.refresh_b_factor_ne_sw()
        self.refresh_b_factor_nw_se()


    #def rotate_right_ne_sw(self):
        
    


    """
    def right_left_ne_sw(self, r_child):
        if r_child.b_factor_ne_sw < -1:
            r_child.rotate_right_ne_sw()


    def left_right_ne_sw(self, l_child):
        if l_child.b_factor_ne_sw > 1:
            r_child.rotate_left_ne_sw()


    def right_left_nw_se(self, r_child):
        if r_child.b_factor_nw_se < -1:
            r_child.rotate_right_nw_se()


    def left_right_nw_se(self, l_child):
        if l_child.b_factor_nw_se > 1:
            r_child.rotate_left_nw_se()


    def rebalance(self, node):
        node.refresh_all_b_factor()
        if node.b_factor_ne_sw > 1:
            node.right_left_ne_sw(node.children["sw"])
            node.rotate_left_ne_sw()
        elif node.b_factor_ne_sw < -1:
            node.left_right_ne_sw(node.children["ne"])
            node.rotate_right_ne_sw() 
        if node.b_factor_nw_se > 1:
            node.right_left_nw_se(node.children["se"])
            node.rotate_left_nw_se()
        elif node.b_factor_nw_se < -1:
            node.left_right_nw_se(node.children["nw"])
            node.rotate_right_nw_se() 

 
    def insert(node, c_node):
        if c_node.is_ne_of_self(node):
             if c_node.children["ne"] != None:
                 self.insert(node, c_node.children["ne"])
             else:
                 c_node.children["ne"] = node
                 node.parent = c_node
        elif c_node.is_nw_of_self(node):
             if c_node.children["nw"] != None:
                 self.insert(node, c_node.children["nw"])
             else:
                 c_node.children["nw"] = node
                 node.parent = c_node
        elif c_node.is_se_of_self(node):
             if c_node.children["se"] != None:
                 self.insert(node, c_node.children["se"])
             else:
                 c_node.children["se"] = node
                 node.parent = c_node
        elif c_node.is_sw_of_self(node):
             if c_node.children["sw"] != None:
                 self.insert(node, c_node.children["sw"])
             else:
                 c_node.children["sw"] = node
                 node.parent = c_node



    def add_city(self, node):
        self.insert(node, self)
    """            




class CountryTable:
    
    def __init__(self, size):
        self.bucket_list = [None] * size
        self.num_items = 0
        self.size = size
    

    def get_bucket_list(self):
        return self.bucket_list


    def get_load_factor(self):
        return self.num_items / self.size


    def hash(self, country_code):
        return int(str(ord(country_code[0])) + str(ord(country_code[1])))


    #def resize(self)
         

    #def put_node(self, city_name, countru_code, lat, lon): 
