import random

class sorting:
    def quickSort(self, lis):
        if len(lis) <= 1:
            return lis
        return self.quicksortHelper(lis, 0, len(lis)-1)

    def quicksortHelper(self, lis, start, end):
        if(start >= end):
            return
        randIndex = random.randint(start, end)
        lis[randIndex], lis[start] = lis[start], lis[randIndex]
        pivot = lis[start]
        smaller = start
        bigger = start
        for bigger in range(start+1,end+1):
            if(lis[bigger] < pivot):
                smaller += 1
                lis[smaller], lis[bigger] = lis[bigger], lis[smaller]

        lis[smaller], lis[start] = lis[start], lis[smaller]
        self.quicksortHelper(lis, start, smaller-1)
        self.quicksortHelper(lis, smaller+1, bigger)
        return lis

obj = sorting()
print(obj.quickSort([2,8,1,7,3,4]))

