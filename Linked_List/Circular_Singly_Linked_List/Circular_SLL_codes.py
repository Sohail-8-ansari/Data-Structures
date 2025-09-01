class Node:
    """Will Create the Nodes to form the list."""
    def __init__(self,item=None, next=None):
        self.item=item
        self.next=next

# Creating the Circular Singly Linked List class.
class CSLL:
    """Create the CSLL."""
    # Now instead of making my first Node the Head, In CSLL we'll make the tail the first node.
    def __init__(self, tail=None):
        self.tail = tail

    # method to check wether the list is empty.
    def is_empty(self):
        return self.tail is None

    # printing the list method.
    def print_list(self):
        if not self.is_empty():
            temp = self.tail.next
            while temp is not self.tail:
                print(temp.item, end="-->")
                temp = temp.next
            if temp == self.tail:
                print(temp.item, end=f"-->{temp.next.item}")
        else:
            print("Empty List.")
    
    # Insertion.
    # 1. Insert at the start of the list.
    def insert_at_start(self, data): # Since it is a CSLL there is no head.
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            self.tail = n
        else:
            n.next = self.tail.next
            self.tail.next = n
    
    # 2. Insert at the end of the list.
    def insert_at_last(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n
            self.tail = n
        else:
            n.next = self.tail.next
            self.tail.next = n
            self.tail = n

    # 3. search method.
    def search(self, desired_element):
        if self.tail is not None:
            temp = self.tail.next
            while temp is not self.tail:
                if temp.item == desired_element:
                    return temp
                temp = temp.next
            if self.tail.item == desired_element:
                return temp
            return None
        else:
            return None
    
    # Insert after a particular node.
    def insert_after(self, desired_element, data):
        temp = self.search(desired_element=desired_element)
        if temp is not None: # There will be two reasons for temp to be None(either empty list, or there is no such item in the list.)
            n = Node(item=data) # Creating the Node while leaving the next None.
            # Condition 1 - if the desired node will be at the last node
            if temp == self.tail:
                n.next = self.tail.next
                self.tail.next = n
                self.tail = n
            # Condition 2 - if the desired node will be at any other node except for the last node.
            else:
                n.next = temp.next
                temp.next = n
        else:
            print("Empty List or No Such item inside list.")
        
    # Deletion.
    # Delete at first.
    def delete_first(self):
        if self.tail is not None:
            if self.tail.next == self.tail:
                self.tail = None
            else:  
                self.tail.next = self.tail.next.next
        else:
            print("Empty List!")
    
    # Delete at last.
    def del_last(self):
        if self.tail is not None:
            if self.tail.next == self.tail:
                self.tail = None
            else:
                temp = self.tail.next
                while temp.next is not self.tail:
                    temp = temp.next
                temp.next = self.tail.next
                self.tail = temp
            
    # Delete after the particular element.
    def del_after(self, desired_element):
        temp = self.search(desired_element=desired_element)
        # The method will only come when the list is not empty and there is atleast two nodes.
        if temp == None or temp.next == temp:
            print("Empty List!/List contains single element.")
        else:
            if temp.next == self.tail:
                temp.next = self.tail.next
                self.tail = temp
            else:   
                temp.next = temp.next.next
    
    # Delete the particular item.
    def del_item(self, desired_item):
        if self.tail is not None:
            if self.tail.next == self.tail:
                if self.tail.item == desired_item:
                    self.tail = None
                    print("Deleted")
                else:
                    print("List Contains single element which is not the desired one!")
            else:
                temp = self.tail.next
                while temp is not self.tail:
                    if temp.item == desired_item: # If the first Node contains the desired element.
                        self.tail.next = temp.next
                        break
                    elif temp.next.item == desired_item: # if the desired element is at the node k , this statement will take me to k-1.
                        if temp.next == self.tail: # if the desired element is at the last Node.
                            temp.next = temp.next.next
                            self.tail = temp
                            break
                        else:
                            temp.next = temp.next.next
                            break
                    temp = temp.next
        else:
            print("Empty List!")

    def __iter__(self):
        return CSLLIterator(self.tail.next)

class CSLLIterator:
    """Defining the class iterator."""
    def __init__(self, start):
        self.current = start
        self.start = start
        self.count = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            if self.current == self.start and self.count == 1:
                raise StopIteration
            else:
                self.count = 1
                data = self.current.item
                self.current = self.current.next

                return data
            
my_list = CSLL()
my_list.insert_at_start(4)
my_list.insert_at_start(6)
my_list.insert_at_last(7)
my_list.insert_at_last(9)
my_list.insert_after(9, 38)
# 6-->4-->7-->9-->6
# my_list.delete_first()
for x in my_list:
    print(x)
        