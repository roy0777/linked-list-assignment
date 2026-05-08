class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next
        print(" - ".join(elements) if elements else "List is empty")

    def search(self, data):
        current = self.head
        index = 0
        while current is not None:
            if current.data == data:
                print(f"Found {data} at position {index}")
                return True
            current = current.next
            index += 1
        print(f"{data} not found in the list")
        return False

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
ll.search(20)
ll.search(99)
