from single_linked_list import SingleLinkedList

print("Merge Test")

list1 = SingleLinkedList()
list2 = SingleLinkedList()

list1.create_list()
list2.create_list()

list1.bubble_sort_by_data()
list2.bubble_sort_by_data()

print("The first list is "); list1.display_list()
print("The second list is "); list2.display_list()

list3 = list1.merge_link(list2)

print("The first merged list is "); list3.display_list()
print("The first list is "); list1.display_list()
print("The second list is "); list2.display_list()

print("\n\n")
list3 = list1.merge_link2(list2)

print("The first merged list is "); list3.display_list()
print("The first list is "); list1.display_list()
print("The second list is "); list2.display_list()