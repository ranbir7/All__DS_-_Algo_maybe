#PYTHON LINKED LISTTT
class LinkedList():
    Lst = {}
    def __init__(self,head):
        self.head = head
        self.next = 12
        self.Lst={
            'head' : self.head,
            'next' : self.next

            }
        self.length = 1
        self.tail = self.head
    def append(self,value):
        self.length += 1
        if self.length > 2:
            new_dt={
                'tail' : value,
                'next' :None

                }
            new_val['next'] = new_dt
            print(self.Lst)
            return 
        new_val={
            'tail' : value,
            'next'  : None

            }
        self.Lst['next']=new_val

        
        self.tail = new_val['tail']
        print(self.Lst)

st = LinkedList(10)
st.append(100)
st.append(213)
st.append(11234)
st.append(4)
st.append(14)
#print('The Head Is ',st.head)
#print('The Tail Is ',st.tail)
#print('The Length Is ', st.length)
#print('The Next Pointer Is Pointing To ', st.next)
