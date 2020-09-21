class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=' ')
            current = current.next

    def insert(self, head, data):
        # Complete this method
        new_node = Node(data)
        if(head is not None):
            last = head
            while(last.next):
                last = last.next
            last.next = new_node
            return head
        else:
            return new_node


mylist = Solution()
T = int(input())
head = None

for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)
mylist.display(head)
