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
    #Complete this method
        next_node = Node(data)
        if head:
            body = head
            while body.next:
                body = body.next
            body.next = next_node
            return head
        else:
            return next_node
    #or:
#        if head is None:
#            head = Node(data)
#            self.body = head
#        else:
#            node = Node(data)
#            self.body.next = node
#            self.body = node
#        return head

mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head,data)
print(mylist.display(head))