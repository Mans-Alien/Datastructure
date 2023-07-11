class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def add_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

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

    def add_befor(self, data, element):
        new_node = Node(data)

        if self.head is None:
            raise Exception("The Linkedlist is empty")
        current = self.head
        while current.next:
            if self.head.data == element:
                Linkedlist.add_begin(self,data)
            if current.next.data != element:
                current = current.next
            else:
                new_node.next = current.next
                current.next = new_node
                break

    def remove(self, element):
        if self.head.data == element:
            Linkedlist.pop_begin(self)
        if self.head is None:
            raise Exception("The Linkedlist is empty")
        current = self.head
        while current.next:
            if current.next.data != element:
                current = current.next
            else:
                current.next = current.next.next
                break

    def pop_begin(self):
        if self.head is None:
            return

        current = self.head
        self.head = self.head.next
        print(current.data)

    def pop_end(self):
        if self.head is None:
            return

        elif self.head.next is None:
            popped = self.head
            self.head = None

        else:
            current = self.head
            while current.next.next:
                current = current.next
            popped = current.next
            current.next = None

        print(popped.data)

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=" --> ")
            current = current.next
        print()



l1 = Linkedlist()
l1.add_begin(0)
l1.add_end(10)
l1.add_after(5,0)
l1.add_befor("x",10)
l1.remove(10)

l1.display()