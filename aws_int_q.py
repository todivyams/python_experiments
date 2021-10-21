class Node:
    def __init__(self,val):
        self.next = None
        self.val = val

class SingleLinkList():
    def __init__(self):
        self.head = None
        self.tail = None

    def InsertNode(self,val):
        
        new_node = Node(val)
        
        if self.tail:
            tail = self.tail
            tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        
    def printSingleLinkList(self):
        curr = self.head
        
        if curr == None:
            print("Empty link list: ")
            return
        while curr != None:
            print(curr.val,end = ' ')
            curr = curr.next
        print()
        
def findCommElem(CommElemdict, lst):
    newCommElemdict = {}
    item = lst.head
    

    while item:
        if item.val in CommElemdict.keys():
            if item.val not in newCommElemdict.keys():
                newCommElemdict[item.val] = 1
        item = item.next
        
    return newCommElemdict

NoLL = None
arr = []
def createTestData():   
    import random
    global NoLL
    
    NoLL = random.randint(3,6)
    
    for i in range(NoLL+1): 
        myList = SingleLinkList()
        for _ in range(random.randint(5,10)):
            myList.InsertNode(random.randint(10,15))
        arr.append(myList)
    print("Create %d linked list \n" %NoLL)
    
    for ind, llst in zip(range(NoLL),arr):
        print("Linked list %d:" %(ind+1),end = " ")
        llst.printSingleLinkList()



createTestData()

lst = arr[0].head
lst_dict = {}

while lst:
    if lst.val not in lst_dict:
        lst_dict[lst.val] = 1
    lst = lst.next

CommElemdict = lst_dict

for ind in range(1,NoLL):
    CommElemdict = findCommElem(CommElemdict,arr[ind])

print ("\nCommon elements across all the lists:", list(CommElemdict.keys()))
       
        
