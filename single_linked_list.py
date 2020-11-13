class Node:
    def __init__(self, value):
        self.info = value
        self.link = None

class SingleLinkedList:
    def __init__(self):
        self.start = None

    def display_list(self):
        if self.start is None:
            print("List is empty")
        else:
            print("The list is ")
            p = self.start
            while p is not None:
                print(p.info, " ", end=" ")
                p = p.link

            print()

    def count_nodes(self):
            p = self.start
            n = 0
            while p is not None:
                n += 1
                p = p.link   
            print("Number of nodes = %s nodes" % n)
    
    def create_list(self):
        n = int(input("Enter the number of nodes: "))
        if n == 0:
            print("Looks like you don't really want to create a list. You just entered zero")
        else:
            for each in range(n):
                data = int(input("Enter the element to be inserted: "))
                self.insert_at_end(data)

    def search(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, "is at position", position)
                return True
            position += 1
            p = p.link
        else:
            print(x, " not found in list")
            return False

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.link = self.start
        self.start = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            p = self.start
            while p.link is not None:
                p = p.link
            p.link = new_node

    def insert_before(self, data, x):
        if self.start is None:
            print("The list is empty")
            return
        
        p = self.start

        if x == self.start.info:
            new_node = Node(data)
            new_node.link = self.start
            self.start = new_node
            return

        while p.link is not None:
            if p.link.info == x:
                new_node = Node(data)
                new_node.link = p.link
                p.link = new_node
                return
            else:
                p = p.link
        else:
            print(x, "is not available in list")


    def insert_after(self, data, x):
        if self.start is None:
            print("The link is empty")
            return
        
        p = self.start
        
        while p is not None:
            if p.info == x:
                new_node = Node(data)
                new_node.link = p.link
                p.link = new_node
                return
            else:
                p = p.link
        else:
            print(x, "is not available in list")

    def insert_at_position(self, data, k):
        if k == 1:
            new_node = Node(data)
            new_node.link = self.start
            self.start = new_node
            return
        
        p = self.start
        i = 1
        while i < k-1 and p is not None:
            p = p.link
            i += 1
        
        if p is None:
            print("You can insert only up to position", i)
        else:
            new_node = Node(data)
            new_node.link = p.link
            p.link = new_node

    def delete_node(self, x):
        if self.start is None:
            print("Link is empty")
        
        # Deletion of first node
        if self.start.info == x:
            self.start = self.start.link
            return
        
        p = self.start

        # Deletion within nodes or at the end of link
        while p.link is not None:
            if p.link.info == x:
                p.link = p.link.link
                return
            p = p.link
        else:
            print("Element", x, "not in list")

    def delete_first_node(self):
        if self.start is None:
            print("List is empty")
            return

        self.start = self.start.link

    def delete_last_node(self):
        if self.start is None:
            print("List is empty")
            return
        
        if self.start.link == None:
            self.start = None
            return

        p = self.start
        while p.link.link is not None:
            p = p.link

        p.link = None

    def reverse_list(self):
        prev = None
        p = self.start

        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubble_sort_by_data(self):
        end = None

        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubble_sort_by_links(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p

                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    
                    p, q = q, p
                r = p
                p = p.link
            
            end = p

    def has_cycle(self):
        if self.find_cycle() is None:
            return False
        else:
            return True

    def find_cycle(self):
        # Using hare and tortoise algorithm a.k.a floyd's cycle detection algorithm
        if self.start is None or self.start.link is None:
            return None
        
        hare = self.start
        tortoise = self.start

        while hare is not None and hare.link is not None:
            hare = hare.link.link
            tortoise = tortoise.link

            if hare == tortoise:
                return tortoise

        return None

    def insert_cycle(self, data):
        if self.start is None:
            return
        
        p = self.start
        px = None

        while p is not None:
            if p.info == data:
                px = p
            prev = p
            p = p.link
        
        if px is not None:
            prev.link = px
        else:
            print(data, "not present in list")

    def remove_cycle(self):
        cycle_node = self.find_cycle() # Cycle node is where the cycle was detected
        if cycle_node == None:
            return
        print("The node at which the cycle was detected is", cycle_node)

        p, q = cycle_node, cycle_node
        len_cycle = 0  # Length of cycle

        while True:
            q = q.link
            len_cycle += 1
            if p == q:
                break
        
        print("The length of the cycle is ", len_cycle)

        len_rem_list = 0
        p = self.start
        while p != q:
            p = p.link
            q = q.link
            len_rem_list += 1
        
        print("Number of nodes not included in the cycle is", len_rem_list)

        len_list = len_cycle + len_rem_list
        print("Number of nodes in the list is ", len_list)

        p = self.start
        for  i in range(len_list - 1):
            p = p.link
        
        p.link = None


    def merge_link(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge_link(self.start, list2.start)
        return merge_list

    def _merge_link(self, p1, p2):
        if p1.info <= p2.info:
            new_list = Node(p1.info) # The linkedlist has just a node at the beginning
            p1 = p1.link
        else:
            new_list = Node(p2.info) # The linkedlist has just a node at the beginning
            p2 = p2.link
        
        ref_node = new_list

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                ref_node.link = Node(p1.info)
                p1 = p1.link
            else:
                ref_node.link = Node(p2.info)
                p2 = p2.link
            
            ref_node = ref_node.link

        
        while p1 is not None:
            ref_node.link = Node(p1.info)
            p1 = p1.link
            ref_node = ref_node.link

        while p2 is not None:
            ref_node.link = Node(p2.info)
            p2 = p2.link
            ref_node = ref_node.link
            
        return new_list

    def merge_link2(self, list2):
        merge_list = SingleLinkedList()
        merge_list.start = self._merge_link2(self.start, list2.start)
        return merge_list

    def _merge_link2(self, p1, p2):
        if p1.info <= p2.info:
            start_node = p1
            p1 = p1.link
        else:
            start_node = p2
            p2 = p2.link

        ref_node = start_node

        while p1 is not None and p2 is not None:
            if p1.info <= p2.info:
                ref_node.link = p1
                ref_node = ref_node.link
                p1 = p1.link
            else:
                ref_node.link = p2
                ref_node = ref_node.link
                p2 = p2.link

        if p1 is None:
            ref_node.link = p2
        else:
            ref_node =  p1

        return start_node


    def _divide_list(self, p):
        pass

############################################################################################################

if __name__ == "__main__":
    list_a = SingleLinkedList()
    list_a.create_list()

    while True:
        print("1: Display list")
        print("2: Count the number of nodes")
        print("3: Search for an element")
        print("4: Insert a node in empty list or at the beginning of the list")
        print("5: Insert a node at the end of the list")
        print("6: Insert a node before a specified node")
        print("7: Insert a node after a specified node")
        print("8: Insert a node at a given position")
        print("9: Delete any node")
        print("10: Delete first node")
        print("11: Delete last node")
        print("12: Reverse the list")
        print("13: Bubble sort by exchanging data")
        print("14: Bubble sort by exchanging links")
        print("15: Merge sort")
        print("16: Detect cycle")
        print("17: Find cycle")
        print("18: Insert cycle")
        print("19: Remove cycle")
        print("20: Quit")

        option = int(input("Enter your choice: "))

        if option == 1:
            list_a.display_list()

        elif option == 2:
            list_a.count_nodes()
        
        elif option == 3:
            data = int(input("Enter the element to be searched: "))
            list_a.search(data)

        elif option == 4:
            data = int(input("Enter the element to be inserted: "))
            list_a.insert_at_beginning(data)

        elif option == 5:
            data = int(input("Enter the element to be inserted: "))
            list_a.insert_at_end(data)
        
        elif option == 6:
            x = int(input("Enter the element before which to insert: "))
            data = int(input("Enter the element to be inserted: "))
            list_a.insert_before(data, x)

        elif option == 7:
            x = int(input("Enter the element after which to insert: "))
            data = int(input("Enter the element to be inserted: "))
            list_a.insert_after(data, x)

        elif option == 8:
            data = int(input("Enter the element to be inserted: "))
            k = int(input("Enter the position at which to insert: "))
            list_a.insert_at_position(data, k)

        elif option == 9:
            data = int(input("Enter the element to be deleted: "))
            list_a.delete_node(data)

        elif option == 10:
            list_a.delete_first_node()
        
        elif option == 11:
            list_a.delete_last_node()

        elif option == 12:
            list_a.reverse_list()
        
        elif option == 13:
            list_a.bubble_sort_by_data()

        elif option == 14:
            list_a.bubble_sort_by_links()

        elif option == 15:
            list_a.merge_sort()
        
        elif option == 16:
            if list_a.has_cycle():
                print("Link has a cycle")
            else:
                print("Link does not have a cycle")
        
        elif option == 17:
            list_a.find_cycle()

        elif option == 18:
            data  = int(input("Enter the element at which the cycle has to be inserted: "))
            list_a.insert_cycle(data)
        
        elif option == 19:
            list_a.remove_cycle()
        
        elif option == 20:
            break
        else:
            print("Wrong Option")
        
        print()
