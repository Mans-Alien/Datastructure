class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.pre = None


class doubly_linked_list:
	def __init__(self):
		self.head = None

	def add_empty(self, data):
		if self.head is None:
			new_node = Node(data)
			self.head = new_node
		else:
			print("Linked list is not empyt!")

	def add_begin(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.pre = new_node
			self.head = new_node

	def add_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while current.next:
					current = current.next
				
			current.next = new_node
			new_node.pre = current

	def add_after(self, data, element):
		new_node = Node(data)
		current = self.head
		while current:
			if current is None:
				print("Linked list is empty!")
			else:
				if current.next is None:
					print("The element is not found")
				if current.data == element:
					new_node.next = current.next
					new_node.pre = current
					current.next = new_node
					break
				elif current.data != element:
					current = current.next

	def add_befor(self, data, element):
		new_node = Node(data)
		current = self.head
		while current:
			if current is None:
				print("Linked list is empty!")
			else:
				if current.next is None:
					print("The element is not found")
				if current.data == element:
					new_node.next = current
					new_node.pre = current.pre
					current.pre.next = new_node
					current.pre = new_node
					break
				elif current.data != element:
					current = current.next
				




	def display(self):
		if self.head is None:
			print("linked list is empty!")
		else:
			current = self.head
			while current is not None:
				print(current.data, end=" --> ")
				current = current.next


l1 = doubly_linked_list()
l1.add_empty(10)
l1.add_begin(0)
l1.add_end(20)
l1.add_after("x", 10)
l1.add_befor("y", 10)
l1.display()
