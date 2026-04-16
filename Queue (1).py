from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)
        print(item, "added to queue")

    def safe_dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty, cannot dequeue.")
            return None
        else:
            return self.queue.popleft()

    def display(self):
        print("Queue elements:", list(self.queue))


# Main Program
q = Queue()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = int(input("Enter element to enqueue: "))
        q.enqueue(item)

    elif choice == 2:
        result = q.safe_dequeue()
        print("Dequeued element:", result)

    elif choice == 3:
        q.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")

