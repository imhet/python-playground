# 给定两个链表分别代表两个非负整数。数位以倒序存储，并且每一个节点包含一位数字。将两个数字相加并以链表形式返回


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):
    head = ListNode(0)
    l = head
    carry = 0
    while l1 or l2 or carry:
        temp_sum, carry = carry, 0
        if l1:
            temp_sum += l1.val
            l1 = l1.next
        if l2:
            temp_sum += l2.val
            l2 = l2.next
        if temp_sum > 9:
            carry = 1
            temp_sum -= 10
        l.next = ListNode(temp_sum)
        l = l.next
    return head.next


a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)

b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)

c = addTwoNumbers(a, b)
# 遍历输出链表结果
while (c.next != None):
    print(c.val)
    c = c.next
else:
    print(c.val)
