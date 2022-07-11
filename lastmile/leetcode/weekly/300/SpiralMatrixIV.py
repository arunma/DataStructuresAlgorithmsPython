from typing import Optional, List

from prep.AddTwoNumbers import ListNode


class SpiralMatrixIV:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        R=m
        C=n

        rb=0
        cb=0
        re=R-1
        ce=C-1

        result=[[-1]* C for _ in range(R)]

        while head and rb<=re and cb<=ce:
            for i in range(cb, ce+1):
                if head:
                    result[rb][i]=head.val
                    head=head.next

            rb+=1

            for i in range(rb, re+1):
                if head:
                    result[i][ce]=head.val
                    head=head.next

            ce-=1

            if rb <= re:
                for i in reversed(range(cb, ce + 1)):
                    if head:
                        result[re][i] =head.val
                        head=head.next
                re-= 1

            if cb<ce:
                for i in reversed(range(rb, re+1)):
                    if head:
                        result[i][cb] =head.val
                        head=head.next

                cb+=1
        return result



if __name__ == '__main__':
    init = SpiralMatrixIV()
    one = ListNode(3, ListNode(0, ListNode(2,
                                           ListNode(6, ListNode(8,
                                                                   ListNode(1, ListNode(7, ListNode(9,
                                                                                                    ListNode(4, ListNode(2,
                                                                                                                         ListNode(5, ListNode(5,
                                                                                                                                              ListNode(0)))))))))))))
    print(init.spiralMatrix(3,5,one))
