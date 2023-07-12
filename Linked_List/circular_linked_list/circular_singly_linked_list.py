class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class CSLL:
	def __init__(self):
		self.head = None
	
	def add_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = self.head
		else:
			current = self.head
			while current.next != self.head:
				current = current.next
			new_node.next = self.head
			self.head = new_node
			current.next = self.head

	def add_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			new_node.next = self.head
		else:
			current = self.head
			while current.next != self.head:
				current = current.next
			current.next = new_node
			new_node.next = self.head

	def add_befor(self, data, element):
		new_node = Node(data)
		if self.head is None:
			raise Exception("The Linkedlist is empty")
		current = self.head
		while current.next:
			if self.head.data == element:
				CSLL.add_begin(self, data)
				break
			if current.next.data != element:
				current = current.next
			else:
				new_node.next = current.next
				current.next = new_node
				break

	def add_after(self, data, element):
		new_node = Node(data)
		if self.head is None:
			raise Exception("The Linkedlist is empty")
		current = self.head
		while current:
			if current.data != element:
				current = current.next
			else:
				new_node.next = current.next
				current.next = new_node
				break

	def add_after(self, data, element):
	        new_node = Node(data)
	        if self.head is None:
	            raise Exception("The Linkedlist is empty")

	        current = self.head
	        while current:
	            if current.data != element:
	                current = current.next
	            else:
	                new_node.next = current.next
	                current.next = new_node
	                break

	def pop_begin(self):
		if self.head is None:
			print("The linkedlist is empty")
		else:
			current = self.head
			while current:
				if current.next == self.head:
					print(self.head.data)
					current.next = self.head.next
					self.head = self.head.next
					break
				else:
					current = current.next

	def pop_end(self):
		if self.head is None:
			print("The linkedlist is empty")
		else:
			current = self.head
			while True:
				if current.next.next == self.head:
					print(current.next.data)
					current.next = self.head
					break
				else:
					current = current.next

	def remove(self, element):
		if self.head is None:
			print("The linkedlist is empty")
		elif self.head.data == element:
			CSLL.pop_begin(self)
		else:
			current = self.head
			while True:
				if current.next.data == element:
					current.next = current.next.next
					break
				else:
					current = current.next

	def display(self):
		current = self.head
		while True:
			if current.next != self.head:
				print(current.data, end=" -> ")
				current = current.next
			else:
				print(current.data, end=" -> ")
				break
		print()

c1 = CSLL()
c1.add_begin(10)
c1.add_begin(0)
c1.add_end(20)
c1.add_befor("x", 10)
c1.add_after("y", 10)
# c1.pop_begin()
# c1.pop_end()
# c1.remove(0)
c1.display()