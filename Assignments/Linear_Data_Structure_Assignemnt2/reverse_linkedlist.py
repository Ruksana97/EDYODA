class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_linkedlist(self,head,size):
        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 1

        # Reverse first k nodes of the linked list
        while (current is not None and count <= size):
            next = current.next

            current.next = prev
            prev = current
            current = next
            count += 1


        if next is not None:
            head.next = self.reverse_linkedlist(next, size)


        return prev


    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def printList(self):
        curr = self.head
        while (curr):
            print(curr.data, end=' ')
            curr = curr.next



x = LinkedList()
x.push(9)
x.push(8)
x.push(7)
x.push(6)
x.push(5)
x.push(4)
x.push(3)
x.push(2)
x.push(1)

print("Linked list is:")
x.printList()
x.head = x.reverse_linkedlist(x.head, 4)

print("\nReversed Linked list is :")
x.printList()