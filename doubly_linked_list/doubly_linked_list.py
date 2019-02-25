"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def add_to_head(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            current_head = self.head
            new_node = ListNode(value, None, self.head)
            self.head = new_node
            current_head.prev = self.head

    def remove_from_head(self):
        if not self.head:
            return
        elif self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            return current_head.value
        else:
            current_head = self.head
            self.head = self.head.next
            self.head.prev = None
            current_head.next = None
            return current_head.value

    def add_to_tail(self, value):
        if not self.head:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
        else:
            current_tail = self.tail
            new_node = ListNode(value, self.tail)
            self.tail = new_node
            current_tail.next = self.tail

    def remove_from_tail(self):
        if not self.head:
            return
        elif self.head == self.tail:
            current_tail = self.head
            self.head = None
            self.tail = None
            return current_tail.value
        else:
            current_tail = self.tail
            self.tail = current_tail.prev
            self.tail.next = None
            current_tail.prev = None
            return current_tail.value

    def move_to_front(self, node):
        if not self.head or self.head == self.tail:
            return
        else:
            node.delete()
            current_head = self.head
            self.head = node
            self.head.next = current_head
            self.head.prev = None
            current_head.prev = self.head

    def move_to_end(self, node):
        if not self.head or self.head == self.tail:
            return
        else:
            node.delete()
            current_tail = self.tail
            self.tail = node
            self.tail.prev = current_tail
            self.tail.next = None
            current_tail.next = self.tail

    def delete(self, node):
        node.delete()
        return node.value

    def get_max(self):
        current_node = self.head
        max = self.head.value
        while current_node:
            if current_node.value > max:
                max = current_node.value
            current_node = current_node.next
        return max
