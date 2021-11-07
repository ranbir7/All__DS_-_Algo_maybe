class node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, value):
        newNode = node(value)
        if self.head is None:
            self.head = newNode
            self.tail = self.head
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        self.size += 1

    def printList(self):
        # Forwards
        an = self.head
        while an is not None:
            print(an.value, '<-->', end='')
            an = an.next
        print()

    def FindTheNode(self, value):
        an = self.head
        while an.value != value:
            an = an.next
        if an.value == value:
            print('Node Found')
            print('Next value is', an.next.value)
            print('Previous Value is', an.prev.value)
        else:
            print('Node Not Found')

    def FindMiddle(self):
        fast = self.head
        slow = self.head
        while fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse(self):
        current = self.head
        prev_node = None
        _next = None

        while current is not None:
            _next = current.next
            current.next = prev_node
            prev_node = current
            current = _next
        self.head = prev_node

    def remove(self,value):
        a = self.head
        while a :
            if value == a.value:
                print('Node Found',a.value)
                del a.value
            else:
                a = a.next



c = DoublyLinkedList()
c.insert(89)
c.insert(37)
c.insert(33)
c.insert(59)
c.insert(3)
c.insert(15)
c.printList()
print(c.FindTheNode(33))
c.remove(3)
c.reverse()
c.printList()
print(c.FindTheNode(33))
