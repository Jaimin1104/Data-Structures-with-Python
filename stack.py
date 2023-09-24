# Stack
class LIFOStack:
    def __init__(self):
        self.arr = []
    def push(self, item):
        self.arr.append(item)
    def pop(self):
        item = self.arr[-1]
        del self.arr[-1]
        return item
    def print_array(self):
        print(self.arr)
stck = LIFOStack()
stck.push(10)
stck.print_array()
stck.push(12)
stck.print_array()
stck.push(30)
stck.print_array()
item = stck.pop()
print("Deleted item :", item)
stck.print_array()