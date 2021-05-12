
from collections import deque
class Solution:
    def __init__(self):
        self.stack = list()
        self.queue = deque()
    def pushCharacter(self,character):
        self.stack.append(character)
    def enqueueCharacter(self,character):
        self.queue.append(character)
    def popCharacter(self):
        return self.stack.pop()
    def dequeueCharacter(self):
        return self.queue.popleft()
    # Write your code here

