class Node:
    # insert the def __init__(self, ...)
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


def linked_list():
    l = Node(5, Node(3, Node(13, Node(4, Node(30)))))
    print(l.element, l.next_node.element, l.next_node.next_node.element, l.next_node.next_node.next_node.element,
          l.next_node.next_node.next_node.next_node.element)


if __name__ == "__main__":
    linked_list()