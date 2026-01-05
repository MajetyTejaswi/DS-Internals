# Linked List - Problem Solving

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_linked_list(head):
    """
    Reverse a singly linked list.
    Time: O(n), Space: O(1)
    
    Logic: Use 3 pointers - prev, current, next
           At each step, reverse the link direction
    
    Before: 1 -> 2 -> 3 -> 4 -> None
    After:  None <- 1 <- 2 <- 3 <- 4
    """
    prev = None
    current = head
    
    while current:
        next_node = current.next   # Save next
        current.next = prev        # Reverse link
        prev = current             # Move prev forward
        current = next_node        # Move current forward
    
    return prev  # New head


def create_list(values):
    """Helper: Create linked list from list of values."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


def print_list(head):
    """Helper: Print linked list."""
    elements = []
    while head:
        elements.append(str(head.data))
        head = head.next
    print(" -> ".join(elements) + " -> None")

if __name__ == "__main__":
    print("=" * 40)
    print("PROBLEM: Reverse a Linked List")
    print("=" * 40)
    
    # Create: 1 -> 2 -> 3 -> 4 -> 5
    head = create_list([1, 2, 3, 4, 5])
    
    print("\nOriginal List:")
    print_list(head)
    
    # Reverse
    reversed_head = reverse_linked_list(head)
    
    print("\nReversed List:")
    print_list(reversed_head)
    

