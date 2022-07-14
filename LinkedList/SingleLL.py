class Node:
    def __init__(self, value):
        self.nodeValue = value
        self.nextNode = None


class SingleLinkedList:
    def __init__(self):
        self.start = None

    def displayList(self):
        if self.start is None:
            print("Empty List")
        else:
            print("List is")
            p = self.start
            while p is not None:
                print(p.nodeValue, end=" ")
                p = p.nextNode
            print()

    def insertEnd(self, value):
        tempNode = Node(value)
        if self.start is None:
            self.start = tempNode
        else:
            p = self.start
            while p.nextNode is not None:
                p = p.nextNode
            p.nextNode = tempNode

    def insertAtBeginning(self, value):
        tempNode = Node(value)
        if self.start is None:
            self.start = tempNode
        else:
            tempNode.nextNode = self.start
            self.start = tempNode

    def insertAtPosition(self, value, pos):
        tempNode = Node(value)
        if self.start is None:
            self.start = tempNode
        elif pos == 1:
            self.insertAtBeginning(value)
        else:
            p = self.start
            i = 1
            flag = 0
            while p is not None:
                if i == pos-1:
                    temp = p.nextNode
                    p.nextNode = tempNode
                    p = p.nextNode
                    p.nextNode = temp
                    flag = 1
                i += 1
                p = p.nextNode
        if flag == 0:
            print(" Position not found")

    def createList(self):
        n = int(input("Enter No of Nodes:"))
        if n == 0:
            return
        else:
            for i in range(0, n):
                val = int(input("Enter value:"))
                self.insertEnd(val)

    def getPosition(self, value):
        p = self.start
        i = 0
        flag = 0
        while p is not None:
            if p.nodeValue == value:
                print("Position is ", i)
                flag = 1
            i += 1
        if flag == 0:
            print("Element not found")

    def deleteAtBeginning(self):
        if self.start is None:
            print("No elements in the list")
        else:
            p = self.start
            self.start = p.nextNode

    def deleteAtEnd(self):
        if self.start is None:
            print("No elements in the list")
        else:
            p = self.start
            while p.nextNode.nextNode is not None:
                p = p.nextNode
            p.nextNode = None

    def deleteAtPosition(self, pos):
        if self.start is None:
            print("No elements in the list")
        elif pos == 1:
            self.deleteAtBeginning()
        else:
            p = self.start
            i = 1
            flag = 0
            while p is not None:
                if i == pos-1:
                    p.nextNode = p.nextNode.nextNode
                    flag = 1
                i += 1
                p = p.nextNode
            if flag == 0:
                print("Position not found")

    def concatenate(self, list2):
        p = self.start
        while p.nextNode is not None:
            p = p.nextNode
        p.nextNode = list2.start

###########################################################
list1 = SingleLinkedList()
list1.createList()

while True:
    print("1. Insert at Position")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Delete at Position")
    print("5. Delete at Beginning")
    print("6. Delete at End")
    print("7. Print Linked List")
    print("8. Get Position")
    print("9. Concatenate 2 single linked lists")
    print("10. Quit")
    x = int(input("Enter the option: "))
    if x == 1:
        y = int(input("Enter the value: "))
        z = int(input("Enter the position: "))
        list1.insertAtPosition(y, z)
    elif x == 2:
        y = int(input("Enter the value: "))
        list1.insertAtBeginning(y)
    elif x == 3:
        y = int(input("Enter the value: "))
        list1.insertEnd(y)
    elif x == 4:
        z = int(input("Enter the position: "))
        list1.deleteAtPosition(z)
    elif x == 5:
        list1.deleteAtBeginning()
    elif x == 6:
        list1.deleteAtEnd()
    elif x == 7:
        list1.displayList()
    elif x == 8:
        y = int(input("Enter the value: "))
        list1.getPosition(y)
    elif x == 9:
        list2 = SingleLinkedList()
        print("create new list")
        list2.createList()
        list1.concatenate(list2)

    elif x == 10:
        break;
    else:
        break;

