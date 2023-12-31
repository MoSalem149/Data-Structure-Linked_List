# Define a Node class for individual elements of the linked list
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.previous = prev

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_previous(self):
        return self.previous

    def set_previous(self, new_prev):
        self.previous = new_prev

    def has_next(self):
        return self.next is not None

    def has_previous(self):
        return self.previous is not None


# Define a LinkedList class to manage the linked list
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head (start) of the linked list
        self.tail = None  # Initialize the tail (end) of the linked list

    def add_at_beginning(self, item):
        # Add a new node at the beginning of the linked list
        newNode = Node(item)
        if self.head is None:
            # If the list is empty, set both head and tail to the new node
            self.head = self.tail = newNode
        else:
            newNode.set_previous(None)
            newNode.set_next(self.head)
            self.head.set_previous(newNode)
            self.head = newNode

    def add_at_end(self, item):
        # Add a new node at the end of the linked list
        newNode = Node(item)
        if self.head is None:
            # If the list is empty, set both head and tail to the new node
            self.head = self.tail = newNode
        else:
            newNode.set_next(None)
            newNode.set_previous(self.tail)
            self.tail.set_next(newNode)
            self.tail = newNode

    def size(self):
        # Get the size (number of nodes) of the linked list
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def add_at_position(self, item, pos):
        # Add a new node at a specified position in the linked list
        if pos > self.size() or pos < 0:
            return None
        else:
            newNode = Node(item)
            count = 0
            current = self.head
            while count < pos - 1:
                count += 1
                current = current.get_next()
            newNode.set_next(current.get_next())
            newNode.set_previous(current)
            current.get_next().set_previous(newNode)
            current.set_next(newNode)

    def remove(self, item):
        # Remove a node with a specific data value from the linked list
        current = self.head
        found = False
        while not found and current is not None:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        if found:
            if current.get_previous() is None:
                self.head = current.get_next()
            else:
                current.get_previous().set_next(current.get_next())
                if current.get_next() is not None:
                    current.get_next().set_previous(current.get_previous())

    def print_list(self):
        # Print the elements of the linked list
        current = self.head
        while current is not None:
            print(current.get_data(), end=" -> ")
            current = current.get_next()
        print("None")  # To indicate the end of the list


# Example usage:
my_list = LinkedList()
my_list.add_at_beginning(93)
my_list.add_at_end(42)
my_list.add_at_end(17)
my_list.add_at_position(99, 1)
my_list.print_list()  # This will print the linked list
