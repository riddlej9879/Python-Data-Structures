class Node:
    def __init__(self):
        self.element = None
        self.next_node = None


def create_linked_list():
    # creates a Node
    n = Node()
    # assigns the element value to 5
    n.element = 5
    # assigns the next_node to new Node object
    n.next_node = Node()
    # assigns the new Node object element to 3
    n.next_node.element = 3
    # prints out our Linked List containing 5 and 3
    print(n.element, n.next_node.element)

if __name__ == "__main__":
    create_linked_list()