class Element(object):
    def __init__(self, value):
        self.value = value
        self.position = 1
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            current.next.position = current.position + 1
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        if self.head:
            while current:
                if position == current.position:
                    return current
                current = current.next
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        current = self.head
        if self.head:
            while current:
                if position == current.position:
                    new_element.next = current
                    new_element.position = position
                    new_element.next.position = position + 1
                    current = new_element
                current = current.next
        else:
            self.append(new_element)

    def delete(self, value):
        """Delete the first node with a given value."""
        pass

e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4, 2)
# Should print 4 now
print(ll.get_position(3).value)