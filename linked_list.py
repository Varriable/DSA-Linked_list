class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node

    def add_to_start(self, value):
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def add_at_position(self, position, value):
        if position < 0:
            raise ValueError("Position must be non-negative")
        if position == 0:
            self.add_to_start(value)
            return
        new_node = Node(value)
        current = self.head
        for _ in range(position - 1):
            if not current:
                raise IndexError("Position out of range")
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def remove_at_position(self, position):
        if position < 0 or not self.head:
            raise ValueError("Invalid position")
        if position == 0:
            self.head = self.head.next_node
            return
        current = self.head
        for _ in range(position - 1):
            if not current.next_node:
                raise IndexError("Position out of range")
            current = current.next_node
        if not current.next_node:
            raise IndexError("Position out of range")
        current.next_node = current.next_node.next_node

    def find(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next_node
            index += 1
        return -1

    def show(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next_node
        print(" -> ".join(values) if values else "Empty list")


# Example usage
linked_list = LinkedList()

linked_list.add_to_end(10)
linked_list.add_to_start(5)
linked_list.add_at_position(1, 15)
linked_list.show()  # Output: 5 -> 15 -> 10

linked_list.remove_at_position(1)
linked_list.show()  # Output: 5 -> 10

index = linked_list.find(10)
print(f"Index of 10: {index}")  # Output: Index of 10: 1



