class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class CircularLinkedList:
    def __init__(self):
        self.last = None
    
    def display_list(self):
        if self.last == None:
            print("Link is empty")
            return
        
        p = self.last.Link
        while True:
            print(p.info, " ", end='')
            p = p.Link

            if p == self.last.link:
                break
        
        print()
    
    def insert_in_beginning(self, data):
        new_node = Node(data)
        new_node.link = self.last.Link
        self.last.link = new_node

    def insert_in_empty_list(self, data):
        new_node = Node(data)
        self.last = new_node
        self.last.link = self.last
    
    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.link = self.last.link
        self.last.link = new_node
        self.last = new_node

    def create_list(self):
        n = int(input("Enter the number of nodes"))
        if n == 0:
            return
        
        data = int(input("Enter the element to be inserted"))
        self.insert_in_empty_list(data)

        for n in range(n-1):
            data = int(input("Enter the element to be inserted"))
            self.insert_at_end(data)

    def insert_after(self, data, x):
        p = self.last.link
        while True:
            if p.info == x:
                new_node = Node(data)
                new_node.link = p.Link
                p.link = new_node
                if p == self.last:
                    self.last = new_node
                break
            
            p = p.Link
            if p == self.last.link:
                print(x, "is not present in link")
                break