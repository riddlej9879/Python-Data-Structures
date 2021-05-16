class Node:
    def __init__(self):
        self.element = None
        self.next_node = None


def linked_list():
    l = Node()
    l.element = 5
    l.next_node = Node()
    # proceed the linked list containing 5 (already included), 3, 13, 4, 30
    l.next_node.element = 3
    l.next_node.next_node = Node()
    l.next_node.next_node.element = 13
    l.next_node.next_node.next_node = Node()
    l.next_node.next_node.next_node.element = 4
    l.next_node.next_node.next_node.next_node = Node()
    l.next_node.next_node.next_node.next_node.element = 30
    # and finally print the linked list print(l.element, ...)
    print(l.element, l.next_node.element, l.next_node.next_node.element, l.next_node.next_node.next_node.element,
          l.next_node.next_node.next_node.next_node.element)


if __name__ == "__main__":
    linked_list()