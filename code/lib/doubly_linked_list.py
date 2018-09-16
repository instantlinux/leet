"""doublyLinkedList

created 12 Sep 2018 by rbraun at instanlinux.net
"""


class DoublyLinkedList(object):
    def __init__(self, val=None):
        """Create a list element; the head is same as any element but without a
        value. Last item in the list will have a .next pointer of None. All
        elements of a non-empty list (including head) will have .prev pointers.
        """
        self.next = None
        self.prev = None
        if (val is not None):
            self.val = val

    def insertSorted(self, val):
        """Insert to a sorted list, at the appropriate position

        Args:
            val (object): object to be added
        """
        current = self
        while (current.next and current.next.val < val):
            current = current.next
        new = DoublyLinkedList(val)
        if (current.next):
            new.next = current.next
        current.next = new
        new.prev = current

    def sortInPlace(self):
        """Sort the list in place, starting at 2nd element"""
        node = self.next
        if (node and node.next):
            node = node.next
        while (node):
            # Scan from list head to this node
            current = self.next
            while (current != node.next):
                # Move the node leftward if a higher value is encountered
                if (current.val > node.val):
                    # remove node
                    node.prev.next = node.next
                    if (node.next):
                        node.next.prev = node.prev

                    # reinsert node
                    current.prev.next = node
                    node.next = current
                    node.prev = current.prev
                    current.prev = node
                    break
                current = current.next
            node = node.next

    def append(self, val):
        """Append to a list

        Args:
            val (object): object to be added
        """
        new = DoublyLinkedList(val)
        if (not self.prev):
            self.prev = self
        new.prev = self.prev
        self.prev.next = new
        self.prev = new

    def get(self):
        """
        Returns:
            List elements as a python list
        """
        result = []
        current = self.next
        while (current):
            result.append(current.val)
            current = current.next
        return result
