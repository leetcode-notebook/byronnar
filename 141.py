# 解1
class Solution(object):
    def hasCycle(self, head):
        #定义一个set，然后不断遍历链表
        s = set()
        while head:
            #如果某个节点在set中，说明遍历到重复元素了，也就是有环
            if head in s:
                return True
            s.add(head)
            head = head.next
        return False

# 解2： 快慢指针
# class Solution(object):
# 	def hasCycle(self, head):
# 		"""
# 		:type head: ListNode
# 		:rtype: bool
# 		"""
# 		if not (head and head.next):
# 			return False
# 		#定义两个指针i和j，i为慢指针，j为快指针
# 		i,j = head,head.next
# 		while j and j.next:
# 			if i==j:
# 				return True
# 			# i每次走一步，j每次走两步
# 			i,j = i.next, j.next.next
# 		return False

'''
题：
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

解：
快慢指针
'''
