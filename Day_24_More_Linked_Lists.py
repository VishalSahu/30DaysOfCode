

    def removeDuplicates(self,head):
        #Write your code here
        curr = head
        while curr is not None and curr.next is not None:
            while curr.next is not None and curr.data is curr.next.data:
                curr.next = curr.next.next
            curr = curr.next
        return head
