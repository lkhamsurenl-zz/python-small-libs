class MinStack:
    innerStack = []
    min = float("inf") # not defined at the start
    # @param x, an integer
    # @return an integer
    def push(self, x):
        # NOTE: it could be negative if x is smaller than current min
        self.innerStack.append(x - self.min) if len(self.innerStack) != 0 else self.innerStack.append(x)
        if x < self.min:
            self.min = x
        print self.min
        print self.innerStack

    # @return nothing
    def pop(self):
        print self.innerStack
        print self.min
        if len(self.innerStack) == 0:
            print "Stack is empty"
            return
        top = self.innerStack.pop()
        if top < 0:
            currMin = self.min
            self.min = self.min - top # update new minimum
            return currMin
        else:
            return top + self.min

    # @return an integer
    def top(self):
        print self.innerStack
        print self.min
        if len(self.innerStack) == 0:
            print "Stack is empty"
            return
        top = self.innerStack[-1]
        # since we pushed element - min into the stack
        if top < 0:
            return self.min
        else:
            return top + self.min

    # @return an integer
    def getMin(self):
        return self.min

stack = MinStack()
stack.push(5)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(1)
print ("top should be 1 and : {}".format(stack.top()))
print ("min should also be 1: {}".format(stack.getMin()))
stack.pop()
print ("min should also be 2: {}".format(stack.getMin()))
print ("top should be 4 and : {}".format(stack.top()))
