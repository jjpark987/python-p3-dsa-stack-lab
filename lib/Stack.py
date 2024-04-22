class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit =  limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        return self.items.append(item) if not self.full() else None

    def pop(self):
        return self.items.pop() if not self.isEmpty() else None

    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i in range(-1, -len(self.items) - 1, -1):
            if self.items[i] == target:
                return -i - 1
            
        return -1


print(Stack([1,1],9).full())
