class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, element):
        # insert code here
        n = Node(element)
        n.next_node = self.head
        self.head = n

    def print_list(self):
        n = self.head
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print()


def linked_list():
    l = LinkedList()
    l.insert_first(30)
    l.insert_first(4)
    l.insert_first(13)
    l.insert_first(3)
    l.insert_first(5)
    l.print_list()


if __name__ == "__main__":
    linked_list()
