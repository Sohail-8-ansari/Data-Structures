# Create a class for Nodes.
class Node:
    """As for DLL it will take 3 parameters."""
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next
    
# Now the class for DLL along with header and methods.
class DLL:
    """Create  a Doubly Linked List."""
    def __init__(self, head=None):
        self.head = head

    # methods
    # checking if the list empty.
    def is_empty(self):
        return self.head == None # Return the boolian values for wether list empty/not.
    
    # function to print the list.
    def print_list(self):
        temp = self.head
        if temp is not None:
            while temp is not None:
                print(temp.item, end="<==>")
                temp = temp.next
        else:
            print("Empty List!")
    
    # inserting at the begining(head):
    def insert_at_head(self, data):
        n = Node(prev=None, item=data, next=self.head)
        # using the if statement to check wether the list is empty or not.
        if not self.head == None:
            self.head.prev = n # if the list isn't empty I must assign the Node the previous head node.
        self.head = n
    
    # inserting at the end(tail):
    def insert_at_tail(self, data):
        temp = self.head
        if temp is not None:
            while temp.next != None:
                temp = temp.next
            n = Node(prev=temp, item=data, next=None)
            temp.next = n
        else:
            self.head = n
    # insert after any desired element.
    # for it first define the search method which will help to find the desired Node.
    def search(self, data):
        temp = self.head
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    # insert after any desired element.
    def insert_after(self,desired_element, data):
        """search for the desired element and add node after it."""
        temp = self.search(desired_element)
        if temp is not None:
            n = Node(prev=temp, item=data, next=temp.next)
            temp.next = n
        else:
            print("Empty List!/Item Not Found!")
        
    # Deletion of the elment.
    # Delete at the beginig(head).
    def del_at_head(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                self.head.next.prev = None
                self.head = self.head.next
                
        else:
            print("Empty List.")
    
    # Delete at the end(tail):
    def del_at_tail(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                temp = self.head
                while temp.next is not None:
                    temp = temp.next
                temp.prev.next = None
        else:
            print("Empty List.")   

    # Delete the desired element(Delete anywhere).
    def del_element(self, desired_value):
        temp = self.search(desired_value)
        # The conditions when the temp will be None[either the list is empty, or there is no such item].
        if temp is not None:
            # The statement will be true if list contains single element, which holds item equals to desired one.
            if temp.next is None and temp.prev is None:
                self.head = None
            elif temp.next is None:
                temp.prev.next = None
            elif temp.prev is None:
                temp.next.prev = None
                self.head = temp.next
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
        else:
            print("Empty List!/No Such Item!")
        
    # Delete after.
    def del_after(self, desired_element):
        temp = self.search(desired_element)
        if temp is not None:
            if temp.next == None and temp.prev == None: # The list must have more than one element to perform (after deletion).
                print("Action won't perform!")
            elif temp.next == None: # we can't delete after the last element because it already have None.
                print("Action won't perform!")
            elif temp.next.next == None: # To delete the last element.
                temp.next = None
            else:
                temp.next.next.prev = temp # Delete the element present betwenn two Nodes.
                temp.next = temp.next.next
            
    def __iter__(self):
        return DLLIterator(self.head)
    
class DLLIterator:
        
    def __init__(self, head):
        self.current = head
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            data = self.current.item
            self.current = self.current.next
            return data


my_list = DLL()
my_list.insert_at_head(5)
my_list.insert_at_head(9)
my_list.insert_at_head(0)
my_list.insert_at_tail(3)
my_list.insert_after(3, 10)

# 0<==>9<==>5<==>3<==>10<==>

for i in my_list:
    print(i)
print()