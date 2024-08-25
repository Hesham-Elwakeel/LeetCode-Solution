Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should 
support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue)
as long as you use only a queue's standard operations.

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False
 
Constraints:

1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.
 
Follow-up: Can you implement the stack using only one queue?

class MyStack:
    def __init__(self):
        # This line initializes an empty deque
        self.q1 = deque()
        self.q2 = deque()
    # This method pushes an element x onto the stack.
    def push(self, x: int):
        self.q2.append(x)
        while self.q1: #that continues as long as there are elements in q1.
        """
        Inside the loop, elements are removed from the front of q1 
        and added to the end of q2. This effectively moves all elements
        from  q1 to q2, with the newly added element x at the front of q2.
        """
            self.q2.append(self.q1.popleft())
        """
        Swap the references of the two queues
        his line swaps the references of q1 and q2. Now, q1 contains all the elements, with x at the front, and q2 is empty.
        """
        self.q1, self.q2 = self.q2, self.q1

    def pop(self): #This method removes and returns the top element of the stack.
        return self.q1.popleft()

    def top(self): #This method returns the top element of the stack without removing it.
        return self.q1[0]

    def empty(self): #This method checks whether the stack is empty.
        return len(self.q1) == 0
# deque, allows you to add or remove values from both ends of a linear queue

