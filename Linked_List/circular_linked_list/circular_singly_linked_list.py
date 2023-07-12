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

	def display(self):
		current = self.head
		while True:
			if current.next != self.head:
				print(current.data, end=" -> ")
				current = current.next
			else:
				print(current.data, end=" -> ")
				break

c1 = CSLL()
c1.add_begin(10)
c1.add_begin(0)
c1.add_end(20)
c1.add_befor("x", 10)
c1.add_after("y", 10)
c1.display()