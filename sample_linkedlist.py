"""
Single Linked list implementation in Python
with insertion at the beginning, deletion, search and traversal of the linked list
"""


class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_nextNode(self):
        return self.next_node

    def set_nextNode(self,new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self, head=None):
        print('sdfsdf')
        self.head = head

    def insert_at_beg(self, data):
        new_node = Node(data)
        new_node.set_nextNode(self.head)
        self.head = new_node

    def delete(self, data):
        current_node = self.head
        previous_node = None
        while current_node.next_node is not None:
            if current_node.get_data() != data:
                previous_node = current_node
                current_node = current_node.get_nextNode()
            else:
                if previous_node is None:
                    self.head = current_node.get_nextNode()
                else:
                    previous_node.set_nextNode(current_node.get_nextNode())
                break

    def search(self, data):
        current_node = self.head
        found = False
        while current_node.next_node is not None:
            if current_node.get_data() == data:
                found = True
                break
            current_node = current_node.get_nextNode()

        if found is True:
            return current_node
        else:
            print("Data Not found")
            return None

    def printList(self):
        currentNode = self.head
        while currentNode is not None:
            if currentNode.get_nextNode() is not None:
                print(currentNode.get_data(), end=' --> ')
            else:
                print(currentNode.get_data())
            currentNode = currentNode.get_nextNode()


mylist = LinkedList()
mylist.insert_at_beg(6)
mylist.insert_at_beg(89)
mylist.insert_at_beg(33)
mylist.printList()
print()
mylist.insert_at_beg(45)
mylist.printList()
print()
mylist.delete(331)
mylist.printList()
print()


