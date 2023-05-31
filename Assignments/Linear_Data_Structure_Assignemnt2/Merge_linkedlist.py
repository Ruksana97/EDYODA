class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None



    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def List(self):
        curr= self.head
        while curr != None:
            print(curr.data,end=" ")
            curr = curr.next


    def merge(self, list1, list2):
        list1_curr = list1.head
        list2_curr = list2.head


        while list1_curr != None and list2_curr != None:

            list1_next = list1_curr.next
            list2_next = list2_curr.next


            list2_curr.next = list1_next
            list1_curr.next = list2_curr


            list1_curr = list1_next
            list2_curr = list2_next
            list2.head = list2_curr



list1 = LinkedList()
list2 = LinkedList()




list1.push(5)
list1.push(6)
list1.push(8)
list1.push(3)

list2.push(1)
list2.push(2)
list2.push(3)
list2.push(4)


print("First Linked List is:")
list1.List()

print("\nSecond Linked List is:")
list2.List()

# Merging the LLs
list1.merge(list1, list2)

print("\nModified first linked list is:")
list1.List()

print("\nRemaining elements in second linked list are:")
list2.List()