"""
A queue in Python is a data structure that follows the FIFO (First In, First Out) principle, resembling a line of people waiting for a service. Elements are added to the end of the queue and removed from the front. It's ideal for scenarios like task scheduling or handling requests in the order they were received.

A stack, on the other hand, adheres to the LIFO (Last In, First Out) principle, akin to a stack of plates. Elements are added to and removed from the top of the stack. It's useful for tasks like expression evaluation, backtracking algorithms, or browser history navigation.
"""
class queue:
    def __init__(self):
        self.items=[]
    # 1. Enqueue: Adding and element to the end of the queue
    def enqueue(self,item):
        self.items.append(item) 
    # 2. Dequeue: Remove and return the item at the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.pop.items[0]
        else:
            return None 
    # 3. Peek: Return the item at the front of the queue without removing it  
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None 
    # 4. isEmpty: check if the queue is empty
    def is_empty(self):
        return len(self.items)==0
    # 5. Size: Return number of items in queue   
    def size(self):
        return len(self.items)  
q=queue()
q.enqueue("Sami")
q.enqueue("Faramarz")
q.enqueue("Wali Ahmad")                       
q.enqueue("Asil Ahmad")
q.enqueue("Younes")
print("---------------------------------------------------------")
print("------------------Check if it works???-------------------")
print("---------------------------------------------------------")
print("Peek :",q.peek())
print("Dequeue:",q.dequeue)
print("check if the queue is empty:",q.is_empty())
print("Number of the items present in the queue:",q.size())