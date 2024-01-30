# Doubly LL

class Node(object):
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLL(object):
    def __init__(self):
        self.start = None
    
    def display(self):
        if not self.start:
            return None
        node = self.start
        lis = []
        while node:
            lis.append(node.value)
            node = node.next
        return lis
    
    def displayRoot(self,root):
        if not root:
            return None
        node = root
        lis = []
        while node:
            lis.append(node.value)
            node = node.next
        return lis
    
    def insertAtEnd(self, value):
        if not self.start:
            root = Node(value)
            self.start = root
            return
        node = self.start
        while node.next:
            node = node.next
        temp = Node(value)
        temp.prev = node
        node.next = temp
        return
       
    def CreateLL(self):
        n = int(input("Enter Number of Nodes: "))
        for i in range(0,n):
            val = int(input("Enter "+ str(i+1) + "th value: "))
            self.insertAtEnd(val)
        self.display()

    def reverseLL(self):
        if not self.start:
            return None
        p = self.start
        while p:
            temp = p.next
            p.next = p.prev
            p.prev = temp
            if not temp:
                self.start = p 
            p = temp
        return
        
obj = DoublyLL()
obj.CreateLL()
lis = obj.display()
print(lis)

obj.reverseLL()
lis = obj.display()
print(lis)

