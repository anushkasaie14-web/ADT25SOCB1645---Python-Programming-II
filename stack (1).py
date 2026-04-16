class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(item, "pushed into stack")

    def safe_pop(self):
        if len(self.stack) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        else:
            return self.stack.pop()

    def display(self):
        print("Stack elements:", self.stack)


# Main program
s = Stack()

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to push: "))
        s.push(item)

    elif choice == 2:
        result = s.safe_pop()
        print("Popped element:", result)

    elif choice == 3:
        s.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")