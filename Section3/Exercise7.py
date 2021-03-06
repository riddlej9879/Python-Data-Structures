class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, element):
        n = Node(element, self.head)
        self.head = n

    def delete_first(self):
        n = self.head
        self.head = n.next_node
        n.next_node = None
        return n.element

    def insert_last(self, element):
        # insert code here
        n = Node(element)
        m = self.head
        if self.head is None:
            self.head = n
            return
        while m.next_node is not None:
            m = m.next_node
        m.next_node = n

    def print_list(self):
        n = self.head
        print("[ ", end='')
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print("]")


def linked_list():
    l = LinkedList()
    l.insert_last(5)
    l.insert_last(3)
    l.insert_last(13)
    l.insert_last(4)
    l.insert_last(30)
    l.print_list()


if __name__ == "__main__":
    linked_list()
