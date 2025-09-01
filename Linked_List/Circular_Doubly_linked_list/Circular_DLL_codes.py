# Creating the Node class having three arguments- prev, item, next.
class Node:
    """Create the Node With Three arguments."""
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

# Creating the CDLL class.
class CDLL: # (Circular Doubly Linked List).
    """CDLL Class with methods."""
    def __init__(self, head=None):
        self.head = head

    # Checking wether the list is empty.
    def is_empty(self):
        return self.head is None
    
    # print List.
    def print_list(self):
        if not self.is_empty():
            temp = self.head
            while temp.next is not self.head:
                print(temp.item, end="<==>")
                temp = temp.next
            if temp.next is self.head:
                print(temp.item , end=f"<==>{self.head.item}")
        else:
            print("Empty List!")
    
    # Count method:
    def count(self):
        if self.head is not None:
            count = 0
            temp = self.head
            if temp.next == self.head:
                count = 1
                return count
            else:
                while temp.next is not self.head:
                    count +=1
                    temp = temp.next
                count +=1
                return count

    # Insertion.
    # Insert at the begining:
    def insert_at_head(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.head = n
        else:
            n.next = self.head
            n.prev = self.head.prev
            self.head.prev.next = n
            self.head.prev = n
            self.head = n
    # Inserting at last.
    def append(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.prev = n
            n.next = n
            self.head = n
        else:
            n.next = self.head
            n.prev = self.head.prev
            self.head.prev.next = n
            self.head.prev = n

    # Search method.
    def search(self, element):
        # The search methods will return None if list is empty or there is no such item.
        if not self.is_empty():
            temp = self.head
            while temp.next != self.head:
                if temp.item == element:
                    return temp
                else:
                    temp = temp.next
            if temp.item == element:
                return temp
            else:
                return None
        else:
            None
    
    # Insert after a specific element.
    # There is one more way to insert at desired element is using search method.
    def insert(self, desrired_element, data): 
        if not self.is_empty():
            n = Node(item=data)
            # if the list contains single element which is also the desired one.
            if self.head.next is self.head and self.head.item == desrired_element:
                 n.next = self.head
                 n.prev = self.head
                 self.head.next = n
            # if the list contains single element but not the desired one.
            elif self.head.next is self.head and self.head.item != desrired_element:
                print("List contains single element which is not the desired one.")
            else: # list contains more than one element.
                temp = self.head
                while temp.next is not self.head:
                    if temp.item == desrired_element: # 
                        n.next = temp.next
                        n.prev = temp
                        temp.next.prev = n
                        temp.next = n
                    temp = temp.next
                if temp.item == desrired_element: # if the desired item is in the last node.
                    n.next = self.head
                    n.prev = n
                    temp.next = n
                    self.head.prev = n
        else:
            print("Empty list! / no such item.")

    # Deletion.
    def del_at_head(self):
        if not self.is_empty():
            if self.head.next is self.head: # if the list contains only one node.
                self.head = None
            else: # if list contains more than one Node.
                self.head.next.prev = self.head.prev
                self.head.prev.next = self.head.next
                self.head = self.head.next
        else:
            print("Empty List!")

    # Delete at tail(the last Node)>
    def del_at_tail(self):
        if not self.head is None:
            if self.head.next is self.head: # if the list contain a single node.
                self.head = None
            else:
                self.head.prev.prev.next = self.head
                self.head.prev = self.head.prev.prev
    
    # Delete the desired element:
    def remove(self, element):
        # Temp will be in only two condition either the list is empty or
        temp = self.search(element=element)
        if temp is not None:
            # if the list contains single node which is the desired one.
            if temp.next is self.head and temp.prev is self.head: 
                self.head = None
            elif temp.next is self.head: # The item is at the last Node.
                temp.prev.next = self.head
                self.head.prev = temp.prev
            else:
                # if the Node is in between of two nodes.
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                if temp is self.head:
                    self.head = temp.next
        else:
            print("Empty List! / No such item found.")
    
    # The iter class.
    def __iter__(self):
        return CDLLIterator(self.head)
# Creating the iterator class.
class CDLLIterator:
    """The iterator class."""
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            if self.current is self.start and self.count == 1:
                raise StopIteration
            else:
                self.count = 1
                data = self.current.item
                self.current = self.current.next

                return data

my_list = CDLL()
my_list.insert_at_head(4)
# my_list.insert_at_head(9)
# my_list.append(6)
# my_list.insert_at_head(8)
# my_list.insert_at_head(3)
# my_list.insert(3, 5)
# my_list.insert(8, 45)
# my_list.insert(9, 46)
# my_list.insert(4, 47)
# my_list.insert(6, 48)

# 3<==>8<==>9<==>4<==>6<==>3
# for i in my_list:
#     print(i)
my_list.print_list()
print(my_list.count())