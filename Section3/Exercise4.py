class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


def print_list(n):
    # insert code here
    while n is not None:
        # use print(n.element, ' ', end='')
        print(n.element, ' ', end='')
        n = n.next_node
    # rember to add a new line with print()
    print()


def linked_list():
    l = Node(5, Node(3, Node(13, Node(4, Node(30)))))
    print_list(l)


if __name__ == "__main__":
    linked_list()