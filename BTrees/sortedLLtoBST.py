class llNode:
	def __init__(self, val):
		self.val = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert(self, val):
		if not self.tail:
			self.tail = llNode(val)
			self.head = self.tail
		else:
			self.tail.next = llNode(val)
			self.tail = self.tail.next

class treeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None


class Solution:
	head = None	
	
	def __init__(self, arr):
		global head
		llist = LinkedList()
		for ele in arr:
			llist.insert(ele)
		head = llist.head
		

	def LLtoBST(self, size):
		global head
		if not head or size == 0:
			return None

		leftRoot = self.LLtoBST(size//2)
		root = treeNode(head.val)
		root.left = leftRoot
		head = head.next
		rightRoot = self.LLtoBST(size - size//2 - 1)
		root.right = rightRoot

		return root
	
	def preorder(self, root):
		if root:
			print(root.val)
			self.preorder(root.left)
			self.preorder(root.right)

if __name__=='__main__':
	arr = [1,2,3,4,5,6]
	soln = Solution(arr)
	bst = soln.LLtoBST(len(arr))

	soln.preorder(bst)