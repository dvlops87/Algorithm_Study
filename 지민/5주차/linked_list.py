# class Node: #연결리스트에 쓰일 각 노드 생성 
#     def __init__(self, data):  #객체 생성 시 초기화 
#         self.data= data #인자로 받은 data를 self.data로 초기화
#         self.next = None



# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def traverse(self):
#         temp = self.head

#         while (temp):
#             print(temp.data, end=" ")
#             temp = temp.next

#         print()

#     def push_back(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
        
#         last = self.head
#         while (last.next) :
#             last = last.next

#         last.next = new_node

#     def push(self,data):
#         new_node = Node(data)

#         if self.head is None:
#             self.head = new_node
#             return
        
#         temp = self.head
#         self.head = new_node
#         new_node.next =temp

#     def append(self, data, loc): 
#         new_node = Node(data)
        
#         temp = self.
#         self.head = new_node
#         new_node.next =temp

        

# linked_list = LinkedList()

# node1 = Node("a")
# linked_list.head = node1

# node2 = Node("b")
# node3 = Node("c")

# node1.next = node2
# node2.next = node3
# linked_list.traverse()

# linked_list.push("r")

# linked_list.append("t")
# linked_list.traverse()



class Node:

	def __init__(self, item):
		self.data = item
		self.next = None


class LinkedList:

	def __init__(self):
		self.nodeCount = 0
		self.head = Node(None)
		self.tail = None
		self.head.next = self.tail


	def __repr__(self):
		if self.nodeCount == 0:
			return 'LinkedList: empty'

		s = ''
		curr = self.head
		while curr.next:
			curr = curr.next
			s += repr(curr.data)
			if curr.next is not None:
				s += ' -> '
		return s


	def getLength(self):
		return self.nodeCount


	def traverse(self):
		result = []
		curr = self.head
		while curr.next:
			curr = curr.next
			result.append(curr.data)
		return result


	def getAt(self, pos):
		if pos < 0 or pos > self.nodeCount:
			return None

		i = 0
		curr = self.head
		while i < pos:
			curr = curr.next
			i += 1

		return curr


	def insertAfter(self, prev, newNode):
		newNode.next = prev.next
		if prev.next is None:
			self.tail = newNode
		prev.next = newNode
		self.nodeCount += 1
		return True


	def insertAt(self, pos, newNode):
		if pos < 1 or pos > self.nodeCount + 1:
			return False

		if pos != 1 and pos == self.nodeCount + 1:
			prev = self.tail
		else:
			prev = self.getAt(pos - 1)
		return self.insertAfter(prev, newNode)


	def concat(self, L):
		self.tail.next = L.head.next
		if L.tail:
			self.tail = L.tail
		self.nodeCount += L.nodeCount




l = LinkedList()
node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("ss")

l.insertAt(0,node1)
l.insertAfter(1,node2)
print(l.concat(1))