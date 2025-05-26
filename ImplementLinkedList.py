class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        values = []
        current = self
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

def convert_array_to_ll(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def insert_head(head, val):
    new_node = Node(val, head)
    return new_node

def delete_head(head):
    new_head = head.next if head else None
    return new_head

def delete_tail(head):
    if not head:
        return None
    if not head.next:
        return None  # If there's only one node, return None
    current = head
    while current.next.next:
        current = current.next
    current.next = None  # Remove the last node
    return head

def length_of_linked_list(head):
    count = 0
    current = head
    while current:
        count += 1
        current = current.next
    return count

def search_linked_list(head, val):
    current = head
    while current:
        if current.data == val:
            return True
        current = current.next
    return False

def main():
    converted_list = convert_array_to_ll([1, 2, 3, 4, 5])
    print("Converted Linked List: ", converted_list)
    node = insert_head(converted_list, 20)
    print("Inserted 20 at head: ", node)
    print("Length of Linked List: ", length_of_linked_list(node))
    print("Searching for 3 in Linked List: ", search_linked_list(node, 3))
    print("Deleted head: ", delete_head(node))
    print("Deleted tail: ", delete_tail(node))

if __name__ == "__main__":
    main()
