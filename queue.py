class people:
    def __init__(self, People_Name):
        self.name = People_Name
        self.behind = None


class Queue:
    lst = []
    def __init__(self):
        self.first = None
        self.last = None
        self.Behind = None
        self.length = 0

    def enqueue(self, people_name):
        global lst
        newPeople = people(people_name)
        if self.length == 0:
            self.first = newPeople.name
            self.last = newPeople.name
        else:
            self.last = newPeople.name
            self.Behind = newPeople.name
        self.length += 1
        Queue.lst += [self.last]
        return (Queue.lst)
    def dequeue(self, name):
        pass

    def peek(self):
        return self.first
p1 = Queue()
p1.enqueue('Ranbir')
p1.enqueue('Ranb')
p1.enqueue('Ra')
p1.enqueue('Ran')
