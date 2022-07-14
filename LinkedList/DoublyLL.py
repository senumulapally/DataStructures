class Node(object):
    def __init__(self, value):
        self.info = value
        self.prev = None
        self.next = None


class DoubleLinkedList(object):
    def __init__(self):
        self.start = None

    def createList(self):
        n = int(input("Enter No of Nodes:"))
        if n == 0:
            return
        first = int(input("Enter the first element:"))
        self.insertInEmptyList(first)
        for i in range(0, n - 1):
            val = int(input("Enter the next element:"))
            self.insertAtEnd(val)

    def insertInEmptyList(self, data):
        temp = Node(data)
        self.start = temp

    def insertAtEnd(self, data):
        temp = Node(data)
        p = self.start
        while p.next is not None:
            p = p.next
        p.next = temp
        temp.prev = p

    def insertAtBeginning(self, data):
        temp = Node(data)
        temp.next = self.start
        self.start.prev = temp
        self.start = temp

    def insertBeforeNode(self, z, data):
        temp = Node(data)
        p = self.start
        if p.info == z:
            self.insertAtBeginning(data)
            return

        while p.next is not None:
            if p.info == z:
                break
            p = p.next
        if p.info == z:
            temp.next = p
            temp.prev = p.prev
            p.prev.next = temp
            p.prev = temp
        else:
            print("Element not found")

    def insertAfterNode(self, z, data):
        temp = Node(data)
        p = self.start

        while p.next is not None:
            if p.info == z:
                break
            p = p.next
        if p.info == z:
            temp.prev = p
            if p.next is not None:
                temp.next = p.next
                p.next.prev = temp

            else:
                temp.next = None
            p.next = temp
        else:
            print("Element not found")

    def deleteFirstNode(self):
        p = self.start
        p = p.next
        p.prev = None
        self.start = p

    def deleteLastNode(self):
        p = self.start
        while p.next.next is not None:
            p = p.next
        p.next = None

    def deleteAnyNode(self, val):
        p = self.start
        i = 0
        if p.info == val:
            self.deleteFirstNode()
            i += 1
        else:
            while p.next is not None:
                p = p.next
                if p.info == val:
                    if p.next is not None:
                        p.prev.next = p.next
                        p.next.prev = p.prev
                    else:
                        p.prev.next = None
                    i += 1
                    return
        if i == 0:
            print("Element not found")

    def reverseList(self):
        p1 = self.start
        if p1 is None:
            return
        p2 = self.start.next
        p1.next = None
        p1.prev = p2
        while p2 is not None:
            p2.prev = p2.next
            p2.next = p1
            p1 = p2
            p2 = p2.prev
        self.start = p1

        return

    def displayList(self):
        p = self.start
        while p is not None:
            print(p.info, end=' ')
            p = p.next
        print("")


###########################################################
list1 = DoubleLinkedList()
list1.createList()

while True:
    print("1. Display List")
    print("2. Insert in empty list")
    print("3. Insert in the beginning")
    print("4. Insert at end")
    print("5. Insert before a specified node")
    print("6. Insert after a specified node")
    print("7. Delete first node")
    print("8. Delete last node")
    print("9. Delete any node")
    print("10. Reverse the list")
    print("11. Quit")
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
        q = int(input("Enter the value before which the value is to be inserted: "))
        list1.insertBeforeNode(q, y)
    elif x == 6:
        y = int(input("Enter the value: "))
        q = int(input("Enter the value after which the value is to be inserted: "))
        list1.insertAfterNode(q, y)
    elif x == 7:
        list1.deleteFirstNode()
    elif x == 8:
        list1.deleteLastNode()
    elif x == 9:
        q = int(input("Enter the value of the node which is to be deleted: "))
        list1.deleteAnyNode(q)
    elif x == 10:
        list1.reverseList()
    elif x == 11:
        break;
    else:
        break;
