class ImplStack:
    def __init__(self, size):
        self.stack = [None] * size
        self.size = size
        self.head = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return self.head >= self.size - 1

    def push(self, ele):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.head += 1
        self.stack[self.head] = ele

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        ele = self.stack[self.head]
        self.stack[self.head] = None
        self.head -= 1
        return ele

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.stack[self.head]

    def __str__(self):
        if self.is_empty():
            return "Stack is empty"
        elements = self.stack[:self.head + 1][::-1]
        return "Stack (top to bottom): " + " -> ".join(str(e) for e in elements)


def main():
    try:
        l = int(input("Enter the length of the stack: "))
        stack = ImplStack(l)

        while True:
            print("\nChoose an option:")
            print("1: Push")
            print("2: Pop")
            print("3: Peek")
            print("4: Print Stack")
            print("5: Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                ele = input("Enter element to push: ")
                try:
                    stack.push(ele)
                    print(f"Pushed: {ele}")
                except Exception as e:
                    print("Error:", e)

            elif choice == "2":
                try:
                    popped = stack.pop()
                    print("Popped element:", popped)
                except Exception as e:
                    print("Error:", e)

            elif choice == "3":
                try:
                    print("Top element:", stack.peek())
                except Exception as e:
                    print("Error:", e)

            elif choice == "4":
                print(stack)

            elif choice == "5":
                print("GOOD BYE!!")
                break

            else:
                print("Invalid Input. Please enter a number between 1 and 5.")

    except ValueError:
        print("Invalid input. Please enter an integer for the stack size.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
