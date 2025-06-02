class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.data))
            current = current.next
        return " <-> ".join(values)

def insert_head(head, val):
    if not head:
        return Node(val)
    new_node = Node(val, None, head)
    head.prev = new_node
    return new_node

def insert_tail(head, val):
    if not head:
        return Node(val)
    current = head
    while current.next:
        current = current.next
    new_node = Node(val, current, None)
    current.next = new_node
    return head

def convert_array_to_dll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        new_node = Node(value, current, None)
        current.next = new_node
        current = new_node
    return head

def delete_head(head):
    if not head:
        return None
    new_head = head.next
    if new_head:
        new_head.prev = None
    return new_head

def delete_tail(head):
    if not head:
        return None
    if not head.next:
        return None  # If there's only one node, return None
    current = head
    while current.next:
        current = current.next
    if current.prev:
        current.prev.next = None  # Remove the last node
    return head

def delete_node(head, val):
    if not head:
        return None
    if head.data == val:
        return delete_head(head)
    current = head
    while current:
        if current.data == val:
            if current.next:
                current.next.prev = current.prev
            if current.prev:
                current.prev.next = current.next
            return head
        current = current.next
    return head  # If the value was not found, return the original list

def reverse_dll(head):
    if head is None or head.next is None:
        return head
    current = head
    prev = None
    while current:
        next_node = current.next
        current.next = prev
        current.prev = next_node
        prev = current
        current = next_node
    return prev # New head of the reversed list

def main():
    head = Node(1)
    second = Node(2, head)
    third = Node(3, second)
    head.next = second
    second.next = third

    print("Initial Doubly Linked List:", head)

    # Insert a new node at the beginning
    new_node = insert_head(head, 0)
    print("After inserting at head:", new_node)

    # Insert a new node at the end
    new_node = insert_tail(new_node, 4)
    print("After inserting at tail:", new_node)

    # Convert an array to a doubly linked list
    print("Converting array to doubly linked list:", convert_array_to_dll([5, 6, 7, 8]))

    # Delete the head node
    print("After deleting head:", delete_head(new_node))

    # Delete the tail node
    print("After deleting tail:", delete_tail(new_node))

    # Delete a specific node
    print("After deleting node with value 2:", delete_node(new_node, 2))

    # Reverse the doubly linked list
    print("Reversed Doubly Linked List:", reverse_dll(new_node))

if __name__ == "__main__":
    main()
