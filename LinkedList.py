class LinkedList:
    class node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head, self.tail = None, None
        self.length = 0

    def append(self, value):
        if self.head is None:
            self.head = self.node(value)
        else:
            t = self.head
            while True:
                if t.next is None:
                    t.next = self.node(value)
                    break
                t = t.next
            self.tail = t.next
            self.length += 1

    def print(self):
        t = self.head
        try:
            while t.next:
                print(t.value, end='-->')
                t = t.next
            print(t.value)
        except:
            print('No LinkedList Found!')

    def sorted_(self):
        t = self.head
        val, ref = [], []
        while t.next:
            ref.append(t)
            val.append(t.value)
            t = t.next
        ref.append(t)
        val.append(t.value)

        def start(refer, values):
            for k in range(0, len(refer)):
                for j in range(0, len(refer)):
                    if refer[k].value < refer[j].value:
                        refer[k], refer[j] = refer[j], refer[k]
                        values[k], values[j] = values[j], values[k]
            return [refer, values]

        a = start(ref, val)
        self.head = a[0][0]
        for i in range(0, len(ref)):
            try:
                ref[i].next = ref[i + 1]
            except:
                ref[i].next = None
                break
        self.print()


c = LinkedList()
c.print()
c.append(21)
c.append(1)
c.append(121)
c.append(2)
c.append(543)
c.append(211)
c.append(12)
c.print()
c.sorted_()
