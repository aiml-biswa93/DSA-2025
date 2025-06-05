class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def find_middle(self):
        # Using the tortoise and hare (fast and slow pointer) technique
        slow = self.head
        fast = self.head
        
        # Move fast pointer twice as fast as slow pointer
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow

# Test cases
def test_find_middle():
    # Test Case 1: Odd number of nodes
    ll1 = LinkedList(1)
    ll1.append(2)
    ll1.append(3)
    ll1.append(4)
    ll1.append(5)
    
    print("Test Case 1 - Odd number of nodes:")
    print("Original List:")
    ll1.print_list()
    middle = ll1.find_middle()
    print("Middle node value:", middle.value if middle else None)
    print()

    # Test Case 2: Even number of nodes
    ll2 = LinkedList(1)
    ll2.append(2)
    ll2.append(3)
    ll2.append(4)
    
    print("Test Case 2 - Even number of nodes:")
    print("Original List:")
    ll2.print_list()
    middle = ll2.find_middle()
    print("Middle node value:", middle.value if middle else None)
    print()

    # Test Case 3: Single node
    ll3 = LinkedList(1)
    
    print("Test Case 3 - Single node:")
    print("Original List:")
    ll3.print_list()
    middle = ll3.find_middle()
    print("Middle node value:", middle.value if middle else None)

# Run the tests
test_find_middle() 