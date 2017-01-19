class BinarySearch(list):
    def __init__(self, length, diff):#initializes the super class
        super(BinarySearch, self).__init__()
        value = diff
        for i in range(length):#populates the list /instance depending on the difference/step
            self.append(value)
            value = value + diff
        self.length = len(self)

    def search(self, value):inilializes the first and the last value 
        first = 0
        last = len(self) - 1
        mid = 0
        found = False
        count = 0

        if value == self[first]:#checks whether the value is the first or last 
            mid = first
            found = True
        elif value == self[last]:
            mid = last
            found = True

        if value not in self:
            found = True
            mid = -1
            #binary search using while loop

        while first <= last and not found:#checks whether the last and first value are equal or first is less
            mid = (first + last) // 2#finds the mid value
            if self[mid] == value:
                found = True
            else:
                count += 1#the counter is updated incase of iteration
                if value < self[mid]:
                    last = mid - 1
                else:
                    first = mid + 1

        return {'count': count, 'index': mid}

if __name__ == '__main__':
    binSearch = BinarySearch(100, 10)
    print(BinarySearch(20, 2).search(40))
    print(binSearch.search(30))
    print(binSearch.search(700))
    print(binSearch.search(10000))
