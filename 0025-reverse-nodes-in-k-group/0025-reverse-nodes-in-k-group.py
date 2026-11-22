class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        dummynode=ListNode()
        newhead=dummynode
        curr=head
        count=0

        while(curr is not None):
            curr=curr.next
            count+=1

        pairs=count//k
        curr=head

        while(pairs):
            prev=None
            times=k
            start=curr

            while(curr is not None and times):
                linker=curr.next
                curr.next=prev
                prev=curr
                curr=linker
                times-=1

            dummynode.next=prev
            dummynode=start
            pairs-=1
            dummynode.next=curr

        return newhead.next