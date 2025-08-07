#insertion in a linked list at the end

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, value):
        new_node = Node(value) 
        
        #check for empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        #setting up the tail or new node at last
        self.tail.next = new_node #link the next
        self.tail = new_node #declare the new_node as tail
    def print_values(self):
        current = self.head
        while current:
            print(current.value, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    n = int(input())
    linked_list = LinkedList()
    vals = list(map(int, input().split()))
    for x in vals:
        linked_list.insert_at_end(x)
    linked_list.print_values()