class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


def print_list(n):
    while n is not None:
        print(n.element, '', end='')
        n = n.next_node
    print()


def linked_list():
    ll = Node(5, Node(3, Node(13, Node(4, Node(30)))))
    ll = Node(7, ll)
    print_list(ll)


def linked_list_2():
    ll = Node()
    ll.element = 5
    ll.next_node = Node()
    ll.next_node.element = 3
    ll.next_node.next_node = Node()
    ll.next_node.next_node.element = 13
    ll.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.element = 4
    ll.next_node.next_node.next_node.next_node = Node()
    ll.next_node.next_node.next_node.next_node.element = 30
    print(ll.element, ll.next_node.element)

def linked_list_1():
    n1 = Node()
    n1.element = 5
    n2 = Node()
    n1.next_node = n2
    n2.element = 3
    n3 = Node()
    n2.next_node = n3
    n3.element = 13
    n4 = Node()
    n3.next_node = n4
    n4.element = 4
    n5 = Node()
    n4.next_node = n5
    n5.element  = 30

if __name__ == "__main__":
    linked_list()