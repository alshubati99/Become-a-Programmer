# Queues:
import queue
q = queue.Queue()
print(q.empty())
q.put('bag1')
print(q.empty())
q.put('bag2')
q.put('bag3')
print(q.get())
qu = queue.Queue(2) # max input to queue is 2 items
qu.empty()
qu.put('bag7')
print(qu.full())

# Stacks:
stack = list()
# index 0 is bottom of stack
stack.append('bill1')
stack.append('bill2')
print(stack.pop())
