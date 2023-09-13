# Define a Node class for individual elements of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head (start) of the linked list

    def is_empty(self):
        return self.head is None

    def add_at_beginning(self, item):
        # Add a new node at the beginning of the linked list
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        # Get the size (number of nodes) of the linked list
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        # Search for an item in the linked list
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        # Remove a node with a specific data value from the linked list
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def add_at_end(self, item):
        # Add a new node at the end of the linked list
        new_node = Node(item)
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def add_at_position(self, item, pos):
        # Add a new node at a specified position in the linked list
        if pos > self.size() or pos < 0:
            return  # Invalid position
        else:
            new_node = Node(item)
            count = 0
            current = self.head
            previous = None
            while count < pos:
                count += 1
                previous = current
                current = current.get_next()
            if previous is None:
                new_node.set_next(self.head)
                self.head = new_node
            else:
                previous.set_next(new_node)
                new_node.set_next(current)

    def print_list(self):
        # Print the elements of the linked list
        current = self.head
        print("List Data:")
        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print()  # Print a newline at the end

    def clear(self):
        # Clear the linked list by resetting the head
        self.head = None


# Example usage:
my_list = LinkedList()
my_list.add_at_beginning(93)
my_list.add_at_beginning(42)
my_list.add_at_end(17)
my_list.add_at_position(99, 1)
my_list.print_list()  # Output: List Data: 42 99 93 17
