class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return 

        last_node = self.head 
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node_value, data):
        current = self.head

        while current and current.data != prev_node_value:
            current = current.next
        
        if not current:
            print('The mentioned node is not found.')
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head 

        if current and current.data == key:
            self.head = current.next
            current = None

        prev = None 
        while current and current.data != key:
            prev = current
            current = current.next

        if current == None:
            print('mentioned key is not found.')
            return

        prev.next = current.next
        current = None 

    def search(self, key):
        current = self.head 

        while current and current.data != key:
            current = current.next

        if current:
            return True 
        
        return False 
    
    def display(self):
        current = self.head

        if not current:
            print('Linked List is empty.')
            return

        while current:
            print(current.data, end='->')
            current = current.next 

        print('None') 

    def lenght(self):
        current = self.head
        count = 0

        while current:
            count += 1 
            current = current.next 

        return count 

    def reverse_list(self):
        if self.head is None:
            raise IndexError('Linked list is empty!')
        
        prev = None
        crr = self.head

        while crr:
            next = crr.next
            crr.next = prev
            prev = crr
            crr = next 

        self.head = prev 

    def remove_duplicates(self):
        try: 
            l = self.head
            r = self.head.next 
        except:
            return self.head 

        while r and l:
            if r.data != l.data:
                r = r.next
                l = l.next 
            else:
                l.next = r.next
                r.next = None 
                r = l.next 

        return self.head 

    def delete_duplicates(self):
        res = self.head
        # while self.head and self.head.next:
        while self.head.next:
            if self.head.data == self.head.next.data:
                self.head.next = self.head.next.next
            else:
                self.head = self.head.next

        return res
    
    def check_cycle(self):
        pass

    def intersection_node(self, h1, h2):
        p1 = h1
        s1 = 0
        p2 = h2
        s2 = 0

        while p1:
            s1 += 1 
            p1 = p1.next 
        while p2:
            s2 += 1 
            p2 = p2.next 
        
        if s1 > s2:
            diff = s1 - s2
            l = h1
            s = h2
            for i in range(diff):
                l = l.next

        elif s2 > s1:
            diff = s2 - s1
            l = h2
            s = h1 
            for i in range(diff):
                l = l.next 

        while s and l:
            if s != l:
                s = s.next
                l = l.next
            else:
                return s.data 

# Example Usage
sll = SinglyLinkedList()
sll.insert_at_end(1)
sll.insert_at_end(2)
sll.insert_at_end(3)
sll.insert_at_end(4)
sll.insert_at_end(5)

print("Original Linked List:")
sll.display()

sll.reverse_list()
print("Reversed Linked List:")
sll.display()

# sll.remove_duplicates()
# sll.delete_duplicates()
# sll.display()

# head1 = SinglyLinkedList()
# head1.insert_at_end(4)
# head1.insert_at_end(1)
# head1.insert_at_end(8)
# head1.insert_at_end(4)
# head1.insert_at_end(5)

# head2 = SinglyLinkedList()
# head2.insert_at_end(5)
# head2.insert_at_end(6)
# head2.insert_at_end(1)
# head2.insert_at_end(8)
# head2.insert_at_end(4)
# head2.insert_at_end(5)

# head1.display()
# head2.display()

# print(sll.intersection_node(head1.head, head2.head))