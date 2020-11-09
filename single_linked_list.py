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
                p = p.links
            print("Number of nodes = %s nodes" % n)
    
    def create_list(self):
        pass

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
        pass

    def insert_at_end(self, data):
        pass

    def insert_before(self, data, x):
        pass

    def insert_after(self, data, x):
        pass

    def insert_at_position(self, data, k):
        pass

    def delete_node(self, x):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_by_data(self):
        pass

    def bubble_sort_by_links(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def insert_cycle(self, data):
        pass

    def remove_cycle(self):
        pass

    def merge_sort(self, list2):
        pass

    def _merge_sort(self, p1, p2):
        pass

    def _divide_list(self, p):
        pass


############################################################################################################

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
        list_a.delete_node()

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
