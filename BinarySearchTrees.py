# noinspection PyMethodMayBeStatic
class BST:
    class node:
        def __init__(self, value):
            self.left = None
            self.right = None
            self.value = value

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = self.node(value)
        else:
            current = self.root
            while True:
                if value > current.value:
                    # RIGHT
                    if current.right is None:
                        current.right = self.node(value)
                        return self
                    else:
                        current = current.right
                else:
                    if value == current.value:
                        print('Duplicates are not  Allowed ')
                        return self
                    if value < current.value:
                        # LEFT
                        if current.left is None:
                            current.left = self.node(value)
                            return self
                        else:
                            current = current.left

    def print_left_then_right(self, start, trc):
        if start is not None:
            trc += str(start.value) + '-->'
            trc = self.print_left_then_right(start.left, trc)
            trc = self.print_left_then_right(start.right, trc)
        return trc

    def lookup(self, value, start):
        if self.root is None:
            print('The Tree is empty')
            return
        else:
            if value < self.root.value:
                # LEFT
                try:
                    if value == start.value:
                        try:
                            print('Node Found', start.value)
                            print('The Right Value is : ', start.right.value)
                            print('The left Value is : ', start.left.value)
                            return
                        except AttributeError:
                            print('The Right Value is : None')
                            print('The Left Value is : None')
                    else:
                        self.lookup(value, start.left)
                except AttributeError:
                    print('NoneType exception is raised')
            elif value == self.root.value:
                try:
                    print('Node Found', start.value)
                    print('The Right Value is : ', start.right.value)
                    print('The left Value is : ', start.left.value)
                    return
                except AttributeError:
                    print('The Right Value is : None')
                    print('The Left Value is : None')
            else:
                # RIGHT
                if value == start.value:
                    try:
                        print('Node Found', start.value)
                        print('The Right Value is : ', start.right.value)
                        print('The left Value is : ', start.left.value)
                    except AttributeError:
                        print('The Right Value is : None')
                        print('The Left Value is : None')
                    return
                else:
                    self.lookup(value, start.right)
            '''
            NEW METHOD
                if value == start.value:
                       try:         
                                print('Node Found',start.value)
                                print('The Right Value is : ',start.right.value)
                                print('The left Value is : ', start.left)
                                return
                       except AttributeError:
                                print('The Right Value is : None')
                                print('The left Value is : None')         
                else:
                    self.lookup(value,start.left)
                    self.lookup(value, start.right)
            
            '''

    def remove(self, value, s):
        pass

c = BST()
c.insert(9)
c.insert(12)
c.insert(21)
c.insert(11)
c.insert(14)
c.insert(2)
c.insert(3)
c.insert(4)
c.insert(1)
c.insert(10)
c.insert(8)
# print(c.print_left_then_right(c.root, ''))
c.lookup(12, c.root)
print(c.print_left_then_right(c.root, ''))
c.remove(12, c.root)
print(c.print_left_then_right(c.root, ''))
