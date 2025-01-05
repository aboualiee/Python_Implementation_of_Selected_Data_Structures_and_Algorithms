from datetime import datetime, timedelta

class Node:
    def __init__(self, data, priority, timestamp):
        self.data = data
        self.prev = None
        self.next = None
        self.priority = priority
        self.timestamp = timestamp

class Dlinkedlist:
    def __init__(self):
        self.head = None

    # Method to initialize the list with predefined values
    def dataset(self):
        base_time = datetime.now()
        values = [
            ("Call", 5, base_time + timedelta(minutes=0)),
            ("Connectivity", 10, base_time + timedelta(minutes=1)),
            ("Subscription", 2, base_time + timedelta(minutes=3)),
            ("Registration", 3, base_time + timedelta(minutes=4)),
            ("Others", 5, base_time + timedelta(minutes=5))
        ]
        self.head = None
        previous_node = None
        for data, priority, timestamp in values:
            new_node = Node(data, priority, timestamp)
            if self.head is None:
                self.head = new_node
            else:
                previous_node.next = new_node
                new_node.prev = previous_node
            previous_node = new_node

    # Method to append element to the end of the doubly linked list
    def add_to_end(self, new_data, priority, timestamp):
        new_node = Node(new_data, priority, timestamp)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Method to delete a node by index
    def delete_by_index(self, index):
        if self.head is None:
            print("List is empty. Cannot delete.")
            return
        current = self.head
        if index == 0:
            self.head = current.next
            if self.head is not None:
                self.head.prev = None
            current = None
            return
        for i in range(index):
            current = current.next
            if current is None:
                print("Index out of bounds.")
                return
        if current.next is not None:
            current.next.prev = current.prev
        if current.prev is not None:
            current.prev.next = current.next
        current = None

    # Method to update a node's data by index
    def update_by_index(self, index, new_data, priority, timestamp):
        if self.head is None:
            print("List is empty. Cannot update.")
            return
        current = self.head
        for i in range(index):
            current = current.next
            if current is None:
                print("Index out of bounds.")
                return
        current.data = new_data
        current.priority = priority
        current.timestamp = timestamp

    # Method to sort the nodes by an attribute: either priority or timestamp
    def sort(self, attribute):
        if self.head is None or self.head.next is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                if getattr(current, attribute) > getattr(current.next, attribute):
                    current.data, current.next.data = current.next.data, current.data
                    current.priority, current.next.priority = current.next.priority, current.priority
                    current.timestamp, current.next.timestamp = current.next.timestamp, current.timestamp
                    swapped = True
                current = current.next

    # Method to print the list
    def printlist(self):
        current = self.head
        while current:
            print(f"{current.data}, Priority: {current.priority}, Timestamp: {current.timestamp}")
            current = current.next

    # Filter by attribute
    def filter_by_priority(self, priority):
        priority = int(priority)
        current = self.head
        found = False
        while current:
            if current.priority == priority:
                print(f"{current.data}, Priority: {current.priority}, Timestamp: {current.timestamp}")
                found = True
            current = current.next
        if not found:
            print(f"No nodes found with priority = {priority}.")