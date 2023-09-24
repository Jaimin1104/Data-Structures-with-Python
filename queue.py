# Queue
class FIFOQueue:
    def __init__(self):
        self.arr = []
    def push(self, item):
        self.arr.append(item)
    def pop(self):
        item = self.arr[0]
        del self.arr[0]
        return item
    def print_array(self):
        print(self.arr)
        
queue = FIFOQueue()
queue.push(10)
queue.print_array()
queue.push(12)
queue.print_array()
queue.push(30)
queue.print_array()
item = queue.pop()
print("Deleted item :", item)
queue.print_array()