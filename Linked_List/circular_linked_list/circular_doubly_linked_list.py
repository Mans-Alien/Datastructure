class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.pre = None


class CDLL:
	def __init__(self):
		self.head = None

	def add_empty(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.head.next = self.head
			self.head.pre = self.head
		else:
			print("This linked list is Not empty")

	def add_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			CDLL.add_empty(self, data)
		else:
			last = self.head.pre
			self.head.pre = new_node
			new_node.next = self.head
			new_node.pre = last
			last.next = new_node
			self.head = new_node

	def add_end(self, data):
		new_node = Node(data)
		if self.head is None:
			CDLL.add_empty(self, data)
		else:
			last = self.head.pre
			self.head.pre.next = new_node
			new_node.pre = last
			new_node.next = self.head
			self.head.pre = new_node

	def add_befor(self, data, element):
		if self.head is None:
			raise Exception("This linked list is empyt")
		else:
			new_node = Node(data)
			current = self.head
			if current == element:
				CDLL.add_begin(self, data)
			else:
				while True:
					if current.next.data == element:
						new_node.next = current.next
						current.next.pre = new_node
						current.next = new_node
						new_node.pre = current
						break
					else:
						current = current.next

	def add_after(self, data, element):
		if self.head is None:
			raise Exception("This linked list is empty")
		else:
			new_node = Node(data)
			current = self.head
			last = self.head.pre 
			if last == element:
				CDLL.add_end(self, data)
			else:
				while True:
					if current.data == element:
						new_node.next = current.next
						current.next.pre = new_node
						current.next = new_node
						new_node.pre = current
						break
					else:
						current = current.next

	def display(self):
		if self.head is None:
			print("The linkedlist is empty")
		else:
			current = self.head
			while True:
				if current.next != self.head:
					print(current.data, end=" <-> ")
					current = current.next
				else:
					print(current.data, end=" <-> ")
					break
			print()

	def display_rev(self):
		if self.head is None:
			print("The linkedlist is empty")
		else:
			current = self.head
			while True:
				if current.pre != self.head:
					print(current.pre.data, end=" <-> ")
					current = current.pre
				else:
					print(current.pre.data, end=" <-> ")
					break
			print()


c1 = CDLL()
c1.add_empty(10)
c1.add_begin(0)
c1.add_end(20)
c1.add_befor("x", 10)
c1.add_after("y", 10)

c1.display()
c1.display_rev()