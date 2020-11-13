class Node:
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.start = None
    
    def display_list(self):
        if self.start is None:
            print("List is empty")
            return
        
        print("The list is ")
        p = self.start
        while p is not None:
            print(p.info, " " end='')
            p = p.next

        print()

    def insert_in_beginning(self, data):
        new_node =  Node(data)
        new_node.next = self.start
        self.start.prev = new_node
        self.start = new_node

    def insert_in_empty_list(self, data):
        new_node = Node(data)
        self.start = new_node

    def insert_at_the_end(self, data):
        new_node = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next

        p.next = new_node
        new_node.prev = p

    def insert_after(self, data, x):
        new_node = Node(data)
        p = self.start
        while p is not None:
            if p.info == x:
                new_node.next = p.next
                new_node.prev = p

                if p.next is not None:
                    p.next.prev = new_node

                p.next = new_node
                break

            p = p.next
        else:
            print(x, "is not present in list")
    
    def insert_before(self, data, x):
        if self.start is None:
            print("List  is empty")
            return
        
        if self.start.info == x:
            self.insert_in_beginning(data)
            return
        
        p =  self.start
        while p is not None:
            if p.info == x:
                new_node = Node(data)
                new_node.next = p
                new_node.prev = p.prev
                p.prev.next = new_node
                p.prev = new_node
                break

            p = p.next
        else:
            print(x, "is not present in list")


    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            return
        
        data = int(input("Enter the element to be inserted"))
        insert_in_empty_list(data)

        for each in range(n-1):
            data = int(input("Enter the element to be inserted"))
            insert_at_the_end(data)

    
    def delete_first_node(self):
        if self.start == None: # Empty link
            print("Link is empty")
            return
        
        if self.start.next == None: # Link has only one node
            self.start = None
            return
        
        self.start  = self.start.next
        self.start.prev = None

    
    def delete_last_node(self):
        if self.start == None: # Empty link
            print("Link is empty")
            return
        
        if self.start.next == None: # Link has only one node
            self.start = None
            return

        p = self.start
        while p.next is not None:
            p = p.next
        
        p.prev.next  = None

    
    def delete_node(self, x):
        if self.start == None: # Empty link
            print("Link is empty")
            return
        
        if self.start.next = None: # Link has only one node
            if self.start.info = x:
                self.start = None
                return
            
            else:
                print(x "is not present in link")
                return
        
        if self.start.info == x:
            self.start  = self.start.next
            self.start.prev = None
            return

        p = self.start
        while p is not None:
            if p.info == x:
                if p.next is None:
                    p.prev.next = None
                else:
                    p.prev.next  = p.next
                    p.next.prev = p.prev
                
                return
            
            p = p.next
        else:
            print(x "is not present in list")

    def reverse_list(self):
        if self.start is None:
            print("Link is empty")
            return

        p1 = self.start
        p2 = p1.next
        p1.prev = p2
        p1.next = None

        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev

        self.start = p1
