class Node:
    def __init__(self, value):
        self.nodeValue = value
        self.nextNode = None


class SortedLinkedList:
    def __init__(self):
        self.start = None

    def displayList(self):
        if self.start is None:
            print("Empty List", end=" ")
        else:
            print("List is")
            p = self.start
            while p is not None:
                print(p.nodeValue, end=" ")
                p = p.nextNode
            print()

    def getPosition(self, value):
        p = self.start
        i = 0
        flag = 0
        while p is not None:
            if p.nodeValue == value:
                print("Position is ", i)
                flag = 1
            elif p.nodeValue > value:
                print("Element not found")
                return
            i += 1
        if flag == 0:
            print("Element not found")

    def insertValue(self, value):
        tempNode = Node(value)
        if self.start is None or value < self.start.nodeValue:
            tempNode.nextNode = self.start
            self.start = tempNode
        else:
            p = self.start
            while p.link is not None and p.link.info <= value:
                p = p.nextNode
            tempNode.nextNode = p.nextNode
            p.nextNode = tempNode

###########################################################
list1 = SortedLinkedList()

while True:
    print("1. Display List")
    print("2. Create List")
    print("3. Insert a value")
    print("4. Delete a value")
    print("5. Get Position")
    print("6. Quit")
    x = int(input("Enter the option: "))
    if x == 1:
        list1.displayList()
    elif x == 2:
        y = int(input("Enter the value: "))
        list1.insertValue(y)
    elif x == 3:
        list1.deleteValue()
    elif x == 4:
        y = int(input("Enter the value: "))
        list1.getPosition(y)
    elif x == 5:
        break;
    else:
        break;