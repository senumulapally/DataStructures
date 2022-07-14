class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    def displayList(self):
        if self.last is None:
            print("Empty List")
            return
        p = self.last.link
        while True:
            print(p.info, end=' ')
            if p == self.last:
                print("")
                return
            p = p.link
        print("")

    def createList(self):
        n = int(input("Enter No of Nodes:"))
        if n == 0:
            return
        else:
            for i in range(0, n):
                val = int(input("Enter value:"))
                self.insertAtEnd(val)

    def insertInEmptyList(self, value):
        tempNode = Node(value)
        self.last = tempNode
        self.last.link = self.last

    def insertAtEnd(self, value):
        if self.last is None:
            self.insertInEmptyList(value)
        else:
            tempNode = Node(value)
            tempNode.link = self.last.link
            self.last.link = tempNode
            self.last = tempNode

    def insertAtBeginning(self, value):
        if self.last is None:
            self.insertInEmptyList(value)
        else:
            tempNode = Node(value)
            p = self.last
            tempNode.link = p.link
            p.link = tempNode

    def insertAfterNode(self, data, val):
        if self.last is None:
            print("Empty List")
            return
        elif val == self.last.info:
            self.insertAtEnd(data)
        else:
            tempNode = Node(data)
            p = self.last.link
            while True:
                if p.info == val:
                    tempNode.link = p.link
                    p.link = tempNode
                    return
                p = p.link
                if p == self.last:
                    print("Element not found")
                    return

    def deleteFirstNode(self):
        if self.last is None:
            print("Empty List")
            return
        p = self.last
        p.link = p.link.link

    def deleteLastNode(self):
        if self.last is None:
            print("Empty List")
            return
        p = self.last.link
        while True:
            if p.link == self.last:
                p.link = self.last.link
                self.last = p
                return
            p = p.link

    def deleteAnyNode(self, value):
        if self.last is None:
            print("Empty List")
        elif value == self.last.info:
            self.deleteLastNode()
        else:
            p = self.last.link
            while True:
                if p.link.info == value:
                    p.link = p.link.link
                    return
                p = p.link

    def concatenate(self, list2):
        p = self.last.link
        self.last.link = list2.last.link
        list2.last.link = p
        self.last = list2.last

##########################################################
list1 = CircularLinkedList()
list1.createList()

while True:
    print("1. Display List")
    print("2. Insert in empty list")
    print("3. Insert in the beginning")
    print("4. Insert at end")
    print("5. Insert after a specified node")
    print("6. Delete first node")
    print("7. Delete last node")
    print("8. Delete any node")
    print("9. Concatenate 2 circular lists")
    print("10. Quit")

    x = int(input("Enter the option: "))
    if x == 1:
        list1.displayList()
    elif x == 2:
        y = int(input("Enter the value: "))
        list1.insertInEmptyList(y)
    elif x == 3:
        y = int(input("Enter the value: "))
        list1.insertAtBeginning(y)
    elif x == 4:
        y = int(input("Enter the value: "))
        list1.insertAtEnd(y)
    elif x == 5:
        y = int(input("Enter the value: "))
        q = int(input("Enter the value after which the value is to be inserted: "))
        list1.insertAfterNode(y, q)
    elif x == 6:
        list1.deleteFirstNode()
    elif x == 7:
        list1.deleteLastNode()
    elif x == 8:
        q = int(input("Enter the value of the node which is to be deleted: "))
        list1.deleteAnyNode(q)
    elif x == 9:
        list2 = CircularLinkedList()
        print("create new list")
        list2.createList()
        list1.concatenate(list2)

    elif x == 10:
        break;
    else:
        break;
