# Name:          Zhoushuai(Andrew) Wu
# Course:        CPE 202
# Instructor:    Daniel Kauffman
# Assignment:    Proj 4: Bucket List
# Term:          Summer 2018


class CityNode:

    def __init__(self, city_name, country_code, lat, lon, parent = None):
        self.name = city_name
        self.country = country_code
        self.lat = lat
        self.lon = lon
        self.children = {"ne" : None, "nw" : None, "se" : None, "sw" : None}
        self.airport = None
        self.distance = None
        self.parent = parent
        self.b_factor_ne_sw = 0
        self.b_factor_nw_se = 0
        self.ne_sw_height = 1
        self.nw_se_height = 1

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
        return new.lat >= self.lat and new.lon >= self.lon


    def is_nw_of_self(self, new):
        return new.lat >= self.lat and new.lon < self.lon


    def is_se_of_self(self, new):
        return new.lat < self.lat and new.lon >= self.lon


    def is_sw_of_self(self, new):
        return new.lat < self.lat and new.lon < self.lon


    def has_no_child(self):
        ne = self.children["ne"] == None
        nw = self.children["nw"] == None
        se = self.children["se"] == None
        sw = self.children["sw"] == None
        return ne and nw and se and sw

    def has_child_ne(self):
        return self.children["ne"] != None


    def has_child_sw(self):
        return self.children["sw"] != None


    def has_child_nw(self):
        return self.children["nw"] != None


    def has_child_se(self):
        return self.children["se"] != None


    def has_child_ne_sw(self):
        return self.has_child_ne() and self.has_child_sw()


    def has_child_nw_se(self):
        return self.has_child_nw() and self.has_child_se()


    def has_parent(self):
        return self.parent != None


    def refresh_b_factor_ne_sw(self):
        sw = self.children["sw"]
        ne = self.children["ne"]
        if sw != None and ne != None:
            self.b_factor_ne_sw = sw.ne_sw_height - ne.ne_sw_height
        elif sw == None and ne != None:
            self.b_factor_ne_sw = 0 - ne.ne_sw_height 
        elif sw != None and ne == None:
            self.b_factor_ne_sw = sw.ne_sw_height 
 

    def refresh_b_factor_nw_se(self):
        se = self.children["se"]
        nw = self.children["nw"]
        if se != None and nw != None:
            self.b_factor_nw_se = se.nw_se_height - nw.nw_se_height
        elif se == None and nw != None:
            self.b_factor_nw_se = 0 - nw.nw_se_height 
        elif se != None and nw == None:
            self.b_factor_nw_se = se.nw_se_height 


    def refresh_all_b_factor(self):
        self.refresh_b_factor_ne_sw()
        self.refresh_b_factor_nw_se()


    def find_ne_sw_height(self):
        if self.has_child_ne() and self.has_child_sw():
            a = self.children["ne"].find_ne_sw_height()
            b = self.children["sw"].find_ne_sw_height()
            return max(a, b) + 1
        elif self.has_child_ne():
            return self.children["ne"].find_ne_sw_height() + 1
        elif self.has_child_sw():
            return self.children["sw"].find_ne_sw_height() + 1
        else:
            return 1


    def find_nw_se_height(self):
        if self.has_child_nw() and self.has_child_se():
            a = self.children["nw"].find_nw_se_height()
            b = self.children["se"].find_nw_se_height()
            return max(a, b) + 1
        elif self.has_child_nw():
            return self.children["nw"].find_nw_se_height() + 1
        elif self.has_child_se():
            return self.children["se"].find_nw_se_height() + 1
        else:
            return 1


    def rotate_left_ne_sw(self):
        new_root = self.children["sw"]                 # new c node
        self.children["sw"] = new_root.children["ne"]  # set og node's right child to new c node's left child
        if self.children["sw"] != None:                # if og node right child is not None
            self.children["sw"].parent = self              # set og node's right child'parent pointer to og node
        new_root.children["ne"] = self                 # sef c node left child to og node
        new_root.parent = self.parent                  # set c node's parent pointer to og node's parent
        if self.has_parent():
            if self.parent.children["ne"] == self:         # if og node is a left child
                self.parent.children["ne"] = new_root          # set og node parent l child to c node
        if self.has_parent():
            if self.parent.children["sw"] == self:       # if og node is a right child
                self.parent.children["sw"] = new_root          # set og node parent r child to c node
        self.parent = new_root                         # seet og node's parent pointer to new c node


    def rotate_left_nw_se(self):
        new_root = self.children["se"]
        self.children["se"] = new_root.children["nw"]
        if self.children["se"] != None:
            self.children["se"].parent = self
        new_root.children["nw"] = self
        new_root.parent = self.parent
        if self.has_parent():
            if self.parent.children["nw"] == self:
                self.parent.children["nw"] = new_root
        if self.has_parent():
            if self.parent.children["se"] == self:
                self.parent.children["se"] = new_root
        self.parent = new_root


    def rotate_right_ne_sw(self):
        new_root = self.children["ne"]
        self.children["ne"] = new_root.children["sw"]
        if self.children["ne"] != None:
            self.children["ne"].parent = self
        new_root.children["sw"] = self
        new_root.parent = self.parent
        if self.has_parent():
            if self.parent.children["ne"] == self:
                self.parent.children["ne"] = new_root
        if self.has_parent():
            if self.parent.children["sw"] == self:
                self.parent.children["sw"] = new_root
        self.parent = new_root


    def rotate_right_nw_se(self):
        new_root = self.children["nw"]
        self.children["nw"] = new_root.children["se"]
        if self.children["nw"] != None:
            self.children["nw"].parent = self
        new_root.children["se"] = self
        new_root.parent = self.parent
        if self.has_parent():
            if self.parent.children["nw"] == self:
                self.parent.children["nw"] = new_root
        if self.has_parent():
            if self.parent.children["se"] == self:
                self.parent.children["se"] = new_root
        self.parent = new_root


    def right_left_ne_sw(self, r_child):
        if r_child.b_factor_ne_sw < -1:
            r_child.rotate_right_ne_sw()


    def left_right_ne_sw(self, l_child):
        if l_child.b_factor_ne_sw > 1:
            l_child.rotate_left_ne_sw()


    def right_left_nw_se(self, r_child):
        if r_child.b_factor_nw_se < -1:
            r_child.rotate_right_nw_se()


    def left_right_nw_se(self, l_child):
        if l_child.b_factor_nw_se > 1:
            l_child.rotate_left_nw_se()


    def rebalance_refresh_height(self, node):
        node.parent.ne_sw_height = node.parent.find_ne_sw_height()
        node.parent.nw_se_height = node.parent.find_nw_se_height()
        for key in node.parent.children:
            if node.parent.children[key] != None:
                node.parent.children[key].ne_sw_height = \
                    node.find_ne_sw_height()
                node.parent.children[key].nw_se_height = \
                    node.find_nw_se_height()


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
        if node.has_parent():
            self.rebalance_refresh_height(node)
            self.rebalance(node.parent) 


    def insert_ne(self, node, c_node):
        if c_node.children["ne"] != None:
            self.insert(node, c_node.children["ne"])
        else:
            c_node.children["ne"] = node
            node.parent = c_node


    def insert_nw(self, node, c_node):
        if c_node.children["nw"] != None:
            self.insert(node, c_node.children["nw"])
        else:
            c_node.children["nw"] = node
            node.parent = c_node


    def insert_se(self, node, c_node):
        if c_node.children["se"] != None:
            self.insert(node, c_node.children["se"])
        else:
            c_node.children["se"] = node
            node.parent = c_node


    def insert_sw(self, node, c_node):
        if c_node.children["sw"] != None:
            self.insert(node, c_node.children["sw"])
        else:
            c_node.children["sw"] = node
            node.parent = c_node


    def insert(self, node, c_node):
        c_node.refresh_all_b_factor()
        if c_node.is_ne_of_self(node):
            self.insert_ne(node, c_node)
        elif c_node.is_nw_of_self(node):
            self.insert_nw(node, c_node)
        elif c_node.is_se_of_self(node):
            self.insert_se(node, c_node)
        elif c_node.is_sw_of_self(node):
            self.insert_sw(node, c_node)
        c_node.rebalance(node)


    def add_city(self, node):
        self.insert(node, self)




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
