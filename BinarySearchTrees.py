class BST:
    class node:
        def __init__(self, value):
            self.right = None
            self.left = None
            self.value = value

    def __init__(self):
        self.root = None

    def insert(self, value):
        newNode = self.node(value)
        if self.root is None:
            self.root = newNode
            return self
        else:
            rootValue = self.root
            while True:
                if newNode.value > rootValue.value:
                    # right child
                    if rootValue.right is None:
                        rootValue.right = newNode
                        return self
                    else:
                        rootValue = rootValue.right
                elif value == rootValue.value:
                    return 'Duplicates Are not allowed'
                else:
                    if newNode.value < rootValue.value:
                        # left child
                        if rootValue.left is None:
                            rootValue.left = newNode
                            return self
                        else:
                            rootValue = rootValue.left

    def print_left_then_right(self, start, trc):
        if start is not None:
            trc += str(start.value) + ' --> '
            trc = self.print_left_then_right(start.left, trc)
            trc = self.print_left_then_right(start.right, trc)
        return trc

    def lookup(self, value):
        travel = self.root
        if self.root is None:
            print('The tree is empty')
            return
        if value < self.root.value:
            def look_left(_value, trc):
                # trc = trc.left
                if trc is None:
                    return
                if _value != trc.value:
                    look_left(_value, trc.left)
                    look_left(_value, trc.right)
                else:
                    print('Node Found: ', trc.value)
                    if trc.left is not None:
                        print('The Left value is:', trc.left.value)
                    else:
                        print('The Left value is:', trc.left)
                    if trc.right is not None:
                        print('The right Value is:', trc.right.value)
                    else:
                        print('The Right value is:', trc.right)
                    return

            look_left(value, travel.left)
        if value == self.root.value:
            print('Node Found: ', value)
            if self.root.right is not None:
                print('The Left value is:', self.root.right.value)
            else:
                print('The Left value is:', self.root.left)
            if self.root.left is not None:
                print('The right Value is:', self.root.left.value)
            else:
                print('The Right value is:', self.root.left)
            return
        if value > self.root.value:
            def look_right(_value, trc):
                if trc is None:
                    return
                if _value != trc.value:
                    look_right(_value, trc.left)
                    look_right(_value, trc.right)
                else:
                    print('Node Found: ', trc.value)
                    if trc.left is not None:
                        print('The Left value is:', trc.left.value)
                    else:
                        print('The Left value is:', trc.left)
                    if trc.right is not None:
                        print('The right Value is:', trc.right.value)
                    else:
                        print('The Right value is:', trc.right)
                    return

            look_right(value, travel.right)


c = BST()
c.insert(44)
c.insert(88)
c.insert(17)
c.insert(8)
c.insert(32)
c.insert(28)
c.insert(29)
c.insert(65)
c.insert(54)
c.insert(82)
c.insert(97)
c.insert(76)
c.insert(68)
c.insert(80)
c.insert(93)
print(c.print_left_then_right(c.root, ''))
c.lookup(93)
print(c.print_left_then_right(c.root, ''))
# c.remove(12, c.root)

# print(c.print_left_then_right(c.root, ''))
