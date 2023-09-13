class Node:
    def _init_(self, data):
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


class LinkedList:
    def _init_(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_at_beginning(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
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
        new_node = Node(item)
        current = self.head
        while current.get_next() is not None:
            current = current.get_next()
        current.set_next(new_node)

    def add_at_position(self, item, pos):
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
        current = self.head
        print("List Data:")
        while current is not None:
            print(current.get_data(), end=" ")
            current = current.get_next()
        print()  # Print a newline at the end

    def clear(self):
        self.head = None


# Example usage:
my_list = LinkedList()
my_list.add_at_beginning(93)
my_list.add_at_beginning(42)
my_list.add_at_end(17)
my_list.add_at_position(99, 1)
my_list.print_list()  # Output: List Data: 42 99 93 17