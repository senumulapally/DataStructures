class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class singleLinkedList:
    def __init__(self):
        self.start = None

    def DisplayList(self):
        if (self.start is None):
            print("List is empty")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()

    def countNodes(self):
        p = self.start
        n = 0
        while p is not None:
            n += 1
            p = p.link
        print("No of Nodes: ", n)

    def search(self, x):
        pos = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(x, " is at position ", pos)
                pos += 1
                return
            else:
                print(x, " Not found")
            p = p.link

    def insertBeginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

    def insertEnd(self, data):
        temp = Node(data)
        if self.start == None:
            self.start = temp
            return
        else:
            p = self.start
            while p.link is not None:
                p = p.link
            p.link = temp

    def insertAfter(self, data, x):
        p = self.start
        while p.link is not None:
            if p.info == x:
                break
            p = p.link
        if p is None:
            print(x, " Not found")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp

    def insertBefore(self, data, x):
        if (self.start is None):
            print("List is empty")
            return
        temp = Node(data)
        if x == self.start.info:
            temp.link = self.start
            temp = self.start
        else:
            p = self.start
            while p.link is not None:
                if p.link.info == x:
                    break
                p = p.link
            if p is None:
                print(x, " Not found")
            else:
                temp.link = p.link
                p.link = temp

    def insertAtPosition(self, data, k):
        if (self.start is None):
            print("List is empty")
            return
        temp = Node(data)
        if k == 1:
            temp.link = self.start
            temp = self.start
        else:
            p = self.start
            i = 1
            while i < k - 1 and p is not None:
                p = p.link
                i += 1
            if p is None:
                print("Max pos is " + str(i))
            else:
                temp.link = p.link
                p.link = temp

    def deleteNode(self, x):
        if (self.start is None):
            print("List is empty")
            return
        if self.start.info == x:
            self.start = self.start.link
            return
        else:
            p = self.start
            while p.link is not None:
                if (p.link.info == x):
                    break
                p = p.link
            if p.link is None:
                print("Element not found")
            else:
                p.link = p.link.link

    def deleteFirstNode(self):
        if (self.start is None):
            print("List is empty")
            return
        else:
            self.start = self.start.link

    def deleteLastNode(self):
        if (self.start is None):
            print("List is empty")
        elif self.start.link is None:
            self.start = None
        else:
            p = self.start
            while p.link.link is not None:
                p = p.link
            p.link = None

    def reverseList(self):
        prev = None
        p = self.start
        while p is not None:
            next = p.link
            p.link = prev
            prev = p
            p = next
        self.start = prev

    def bubbleSortExData(self):
        end = None
        while end != self.start.link:
            p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.info, q.info = q.info, p.info
                p = p.link
            end = p

    def bubbleSortExLinks(self):
        end = None
        while end != self.start.link:
            r = p = self.start
            while p.link != end:
                q = p.link
                if p.info > q.info:
                    p.link = q.link
                    q.link = p
                    if p != self.start:
                        r.link = q
                    else:
                        self.start = q
                    p, q = q, p
                r = p
                p = p.link
            end = p

    def merge_lists(self, list2):
        merge_list = singleLinkedList()
        merge_list.start = self.merge1(self.start, list2.start)
        return merge_list

    def merge1(self, p1, p2):
        if (p1.info <= p2.info):
            startM = Node(p1.info)
            p1 = p1.link
        else:
            startM = Node(p2.info)
            p2 = p2.link
        pM = startM

        while p1 is not None and p2 is not None:
            if (p1.info <= p2.info):
                pM.link = Node(p1.info)
                p1 = p1.link
            else:
                pM.link = Node(p2.info)
                p2 = p2.link
            pM = pM.link

        # If second list is finished and elements are left in first one
        while p1 is not None:
            pM.link = Node(p1.info)
            p1 = p1.link
            pM = pM.link

        # If first list is finished and elements are left in second one
        while p2 is not None:
            pM.link = Node(p2.info)
            p2 = p2.link
            pM = pM.link

        return startM

    def merge_lists_links(self, list2):
        merge_list = singleLinkedList()
        merge_list.start = self.merge2(self.start, list2.start)
        return merge_list

    def merge2(self, p1, p2):
        if (p1.info <= p2.info):
            startM = p1
            p1 = p1.link
        else:
            startM = p2
            p2 = p2.link

        pM = startM

        while p1 is not None and p2 is not None:
            if (p1.info <= p2.info):
                pM.link = p1
                p1 = p1.link
            else:
                pM.link = p2
                p2 = p2.link
            pM = pM.link

        if p1 is None:
            pM.link = p2
        else:
            pM.link = p1

        return startM

    def mergeSort(self):
        self.start = self.mergeSortRecursive(self.start)

    def mergeSortRecursive(self, listStart):
        if listStart is None or listStart.link is None:
            return listStart

        start1 = listStart
        start2 = self.divideList(listStart)
        start1 = self.mergeSortRecursive(start1)
        start2 = self.mergeSortRecursive(start2)
        startM = self.merge2(start1, start2)
        return startM

    def divideList(self, p):
        q = p.link.link
        while q is not None and q.link is not None:
            p = p.link
            q = q.link.link
        start2 = p.link
        p.link = None
        return start2

    def insertCycle(self, x):
        if self.start is None:
            return
        p = self.start
        px = None
        prev = None

        while p is not None:
            if p.info == x:
                px = p
            prev = p
            p = p.link
        if px is not None:
            prev.link = px
        else:
            print(x, " is not present in the list")

    def hasCycle(self):
        if self.findCycle() is None:
            return False
        else:
            return True

    def findCycle(self):
        if self.start is None or self.start.link is None:
            return None
        slowR = self.start
        fastR = self.start

        while fastR is not None and fastR.link is not None:
            slowR = slowR.link
            fastR = fastR.link.link
            if slowR == fastR:
                return slowR
        return None

    def removeCycle(self):
        c = self.findCycle()
        if c is None:
            return
        print("Node at which cycle is detected is ", c.info)

        p = c
        q = c
        lenCycle = 0
        lenReminder = 0
        while True:
            lenCycle += 1
            q = q.link
            if p == q:
                break;
        print("length of cycle is ", lenCycle)

        p = self.start
        while p != q:
            lenReminder += 1
            p = p.link
            q = q.link

        print("Number of nodes excluding cycle are ", lenReminder)
        lenList = lenCycle + lenReminder
        print("length of list is ", lenList)
        p = self.start
        for i in range(lenList - 1):
            p = p.link
        p.link = None

    def createList(self):
        n = int(input("Enter no of Nodes: "))
        if (n == 0):
            return
        else:
            for i in range(n):
                data = int(input("Enter element to be inserted: "))
                self.insertEnd(data)


#############################################################

list = singleLinkedList()
list.createList()

while True:
    print("\n")
    print("1. Display List")
    print("2. Count Nodes")
    print("3. Search")
    print("4. Insert at beginning")
    print("5. Insert at end")
    print("6. Insert Before")
    print("7. Insert After")
    print("8. Insert at Position")
    print("9. Delete First Node")
    print("10. Delete Last Node")
    print("11. Delete Any Node")
    print("12. Reverse list")
    print("13. Bubble sort by exchanging data")
    print("14. Bubble sort by exchanging links")
    print("15. Merge Sorted Data")
    print("16. Merge Sorted Links")
    print("17. Merge Sort")
    print("18. Insert cycle")
    print("19. Detect cycle")
    print("20. Remove Cycle")
    print("21. Quit")

    option = int(input("Enter your Choice: "))
    if option == 1:
        list.DisplayList()
    elif option == 2:
        list.countNodes()
    elif option == 3:
        x = int(input("Enter number to be searched : "))
        list.search(x)
    elif option == 4:
        x = int(input("Enter number to be inserted : "))
        list.insertBeginning(x)
        list.DisplayList()
    elif option == 5:
        x = int(input("Enter number to be inserted : "))
        list.insertEnd(x)
        list.DisplayList()
    elif option == 6:
        x = int(input("Enter number to be inserted : "))
        k = int(input("Enter the number before which the number is to be inserted : "))
        list.insertBefore(x, k)
        list.DisplayList()
    elif option == 7:
        x = int(input("Enter number to be inserted : "))
        k = int(input("Enter the number after which the number is to be inserted : "))
        list.insertAfter(x, k)
        list.DisplayList()
    elif option == 8:
        x = int(input("Enter number to be inserted : "))
        k = int(input("Enter the position at which the number is to be inserted : "))
        list.insertAtPosition(x, k)
        list.DisplayList()
    elif option == 9:
        list.deleteFirstNode()
        list.DisplayList()
    elif option == 10:
        list.deleteLastNode()
        list.DisplayList()
    elif option == 11:
        x = int(input("Enter number to be deleted : "))
        list.deleteNode(x)
        list.DisplayList()
    elif option == 12:
        list.reverseList()
        list.DisplayList()
    elif option == 13:
        list.bubbleSortExData()
        list.DisplayList()
    elif option == 14:
        list.bubbleSortExLinks()
        list.DisplayList()

    elif option == 15:
        list.bubbleSortExLinks()
        list2 = singleLinkedList()
        list2.createList()
        list = list.merge_lists(list2)

    elif option == 16:
        list.bubbleSortExLinks()
        list2 = singleLinkedList()
        list2.createList()
        list = list.merge_lists_links(list2)

    elif option == 17:
        list.mergeSort()

    elif option == 18:
        x = int(input("Enter number where the cycle is to be inserted : "))
        list.insertCycle(x)

    elif option == 19:
        print(list.hasCycle())

    elif option == 20:
        list.removeCycle()

    elif option == 21:
        break
    else:
        break