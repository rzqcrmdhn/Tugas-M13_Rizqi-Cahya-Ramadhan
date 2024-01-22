class Node :
    def _init_(self, abc):
        self.right = None
        self.left = None
        self.data = abc
        
        #right > parent
        #left < parent
        
    def insert (self, abc):
        if self.data:
            if abc < self.data:
                if self.left is None:
                    self.left = Node(abc)
                else:
                    self.left.insert(abc)
            elif abc > self.data:
                if self.right is None:
                    self.right = Node(abc)
                else:
                    self.right.insert(abc)
        else:
            self.data = abc
    
    def cetak (self):
        if self.left:
            self.left.cetak()
        print(self.data)
        if self.right:
            self.right.cetak()
            
root = Node(10)
root.insert (15)
root.insert (3)
root.insert (7)
root.insert (6)
root.insert (8)
root.insert (17)
root.cetak ()