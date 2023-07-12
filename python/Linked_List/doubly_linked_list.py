class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.pre = None


class DLL:
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
					current.next.pre = new_node
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

	def pop_begin(self):
		if self.head is None:
			return
		else:
			print(self.head.data ,"is removed")
			self.head = self.head.next
			self.head.pre = None


	def pop_end(self):
		if self.head is None:
			return
		else:
			current = self.head
			while current.next.next:
				current = current.next
			print(current.next.data)
			current.next = None

	def remove(self, element):
		if self.head.data == element:
			DLL.pop_begin(self)
		if self.head is None:
			raise Exception("The Linkedlist is empty")
		current = self.head
		while current.next:
			if current.next.data != element:
				current = current.next
			else:
				current.next = current.next.next
				current.next.pre = current


	def display(self):
		if self.head is None:
			print("linked list is empty!")
		else:
			current = self.head
			while current is not None:
				print(current.data, end=" <-> ")
				current = current.next
			print()

	def display_rev(self):
		if self.head is None:
			print("linked list is empty!")
		else:
			current = self.head
			while current.next:
				current = current.next
			while current:
				print(current.data, end = " <-> ")
				current = current.pre
			print()