# input: 
# ["MyQueue", "push", "push", "peek", "pop", "emepty"]
# [[], [1], [2], [], [], []]
# # output: 
# [null, null, null, 1, 1, false]

# explanation: 
# MyQueue myQueue = new MyQueue();
# meQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(2); // return false 

class MyQueue:
    def __init__(self):
        self.stack1 = [] # head is the bottom of this stack
        self.stack2 = [] # head is at the top of this stack 

    def push(self, x: int) -> None:
      # push every item of the second stack onto the first one then push the new item
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        self.stack1.append(x)

    def pop(self) -> int:
      # push every item of the first stack onto the second one and then return the top of the second stack which is popped 
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def peek(self) -> int:
      # push every item of the first stack onto the second one and then return the top of the second stack which is NOT popped
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2 

input = ["MyQueue", "push", "push", "peek", "pop", "emepty"]
input2 = [[], [1], [2], [], [], []]
obj = MyQueue()
# obj.push(x)
# print(obj.pop(input, input2))

# print(obj.__init__(input, input2))
print(obj.push(input, input2))
print(obj.pop(input, input2))
print(obj.peek(input, input2))
print(obj.empty(input, input2))

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

