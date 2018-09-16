"""SinglyLinkedList

created 12 Sep 2018 by rbraun at instanlinux.net
"""


class SinglyLinkedList(object):
    def __init__(self, val):
        """Create a list element; the head is same as any element
        """
        self.next = None
        self.val = val

    def append(self, val):
        """Append to a list

        Args:
            val (object): object to be added
        """
        current = self
        while (current.next):
            current = self.next
        current.next = SinglyLinkedList(val)

    def get(self):
        """
        Returns:
            List elements as a python list
        """
        result = []
        current = self
        while (current):
            result.append(current.val)
            current = current.next
        return result

    def load(self, pythonList):
        """Load python list to SinglyLinkedList

        Args:
            pythonList (list): elements to be loaded after first
        """
        node = self
        for num in pythonList:
            node.append(num)
            node = node.next

    def length(self):
        """
        Returns:
            Count of nodes starting at given position
        """
        count = 0
        current = self
        while (current):
            count += 1
            current = current.next
        return count

    def __repr__(self):
        return 'SinglyLinkedList(%s)' % self.get()
