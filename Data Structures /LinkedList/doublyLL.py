class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None 

    def is_empty(self):
        return self.head is None
    
    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail
            self.tail = new_node 

    def prepend(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, item):
        if self.is_empty():
            print('Linked List is empty!')
            return
        
        current = self.head
        while current:
            if current.data == item:
                if current == self.head:
                    self.head = current.next
                    if self.head is not None:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev 
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev 
                return 
            current = current.next

        print(f'{item} is not found!')

    def swap_elements(self, item1, item2):
        if self.is_empty():
            raise IndexError("Linked list is empty!")

        if item1 == item2:
            return 'No swap required!'
        
        node1 = node2 = None
        current = self.head

        while current is True:
            if current.data == item1:
                node1 = current
            elif current.data == item2:
                node2 = current
            current = current.next

        # print(node1.data)
        # print(node2.data)

        if not node1 or not node2:
            print('1 or both items not found!')

        # If nodes are adjacent, handle separately
        if node1.next == node2:  # node1 is before node2
            node1.next = node2.next
            if node2.next is True:
                node2.next.prev = node1
            node2.prev = node1.prev
            if node1.prev is True:
                node1.prev.next = node2
            else:
                self.head = node2  # Update head if node1 was the first node
            node2.next = node1
            node1.prev = node2

        elif node2.next == node1:  # node2 is before node1
            node2.next = node1.next
            if node1.next is True:
                node1.next.prev = node2
            node1.prev = node2.prev
            if node2.prev is True: 
                node2.prev.next = node1
            else:
                self.head = node1  # Update head if node2 was the first node
            node1.next = node2
            node2.prev = node1

        else:  # If nodes are NOT adjacent
            node1.prev = node2.prev
            node2.prev = node1.prev
            node1.next = node2.next,
            node2.next = node1.next

            # Fix previous pointers
            if node1.prev is True:
                node1.prev.next = node1
            else:
                self.head = node1  # Update head if node1 is new first node

            if node2.prev is True:
                node2.prev.next = node2
            else:
                self.head = node2  # Update head if node2 is new first node

            # Fix next pointers
            if node1.next is True:
                node1.next.prev = node1
            if node2.next is True:
                node2.next.prev = node2

        return 
    
    def merge(self, head1, head2):
        dummy = Node(0)
        current = dummy
        p1 = head1
        p2 = head2

        while p1 and p2:
            if p1.data <= p2.data:
                current.next = p1
                p1.prev = current
                p1 = p1.next
            else:
                current.next = p2
                p2.prev = current
                p2 = p2.next

            current = current.next
            
        if p1:
            current.next = p1
            p1.prev = current
            
        elif p2:
            current.next = p2
            p2.prev = current

        merged = dummy.next
        if merged:
            merged.prev = None
        
        return merged

    def display(self):
        if self.is_empty():
            print('Linked List is empty!')
        
        current = self.head
        while current:
            print(current.data, end=' <-> ' if current.next else "\n")
            current = current.next
        

    def reverse_display(self):
        if self.is_empty():
            print('Linked List is empty!')
        
        current = self.tail
        while current:
            print(current.data, end=' <-> ' if current.prev else "\n")
            current = current.prev

    def search(self, data, crr=None): # Recursive
        if crr is None:
            crr = self.head

        if crr.data == data:
            return crr

        if crr == self.tail:
            raise ValueError(f'{data} not in list')
        
        self.search(data, crr=crr.next)


dll = doublylinkedlist()
dll.append(1)
dll.append(4)
dll.append(3)
dll.append(2)
dll.append(5)

# dll.display()
# dll.swap_elements(4, 2)
# dll.display()

dll1 = doublylinkedlist()
dll1.append(1)
dll1.append(3)
dll1.append(5)

dll1.display()

dll2 = doublylinkedlist()
dll2.append(2)
dll2.append(4)
dll2.append(6)

dll2.display()

dll1.merge(dll1.head, dll2.head)

dll1.display()
