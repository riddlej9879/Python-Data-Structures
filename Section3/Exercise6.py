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
        # insert code here
        n = self.head
        self.head = n.next_node
        n.next_node = None
        return n.element

    def print_list(self):
        n = self.head
        print("[ ", end='')
        while n is not None:
            print(n.element, ' ', end='')
            n = n.next_node
        print("]")


def linked_list():
    l = LinkedList()
    l.insert_first(30)
    l.insert_first(4)
    l.insert_first(13)
    l.insert_first(3)
    l.insert_first(5)
    l.print_list()
    l.insert_first(7)
    l.print_list()
    l.delete_first()
    l.print_list()


if __name__ == "__main__":
    linked_list()
