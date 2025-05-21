class ImplQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.head = 0
        self.tail = 0

    def __str__(self):
        if self.is_empty():
            return "Queue is empty"
        elements = self.queue[self.head:self.tail]
        return "Queue (top to bottom): " + " -> ".join(str(e) for e in elements)

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return self.tail >= self.size

    def push(self, ele):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.tail] = ele
        self.tail += 1

    def pop(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        ele = self.queue[self.head]
        self.queue[self.head] = None
        self.head += 1
        return ele

    def peek(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.head]


def main():
    try:
        size = int(input("Enter the size of the queue: "))
        queue = ImplQueue(size)
        while True:
            print("\nChoose an option:")
            print("1: Push")
            print("2: Pop")
            print("3: Peek")
            print("4: Print Queue")
            print("5: Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                ele = input("Enter element to push: ")
                try:
                    queue.push(ele)
                    print(f"Pushed: {ele}")
                except Exception as e:
                    print("Error:", e)

            elif choice == "2":
                try:
                    ele = queue.pop()
                    print(f"Pushed: {ele}")
                except Exception as e:
                    print("Error:", e)

            elif choice == "3":
                try:
                    ele = queue.peek()
                    print(f"Peeked: {ele}")
                except Exception as e:
                    print("Error:", e)

            elif choice == "4":
                try:
                    print("Queue:", print(queue))
                except Exception as e:
                    print("Error:", e)

            elif choice == "5":
                print("GOOD BYE!!")
                break

            else:
                print("Invalid choice. Please select a number between 1 and 5.")
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    main()
