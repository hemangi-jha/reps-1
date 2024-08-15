class CircularQueue:
    def _init_(self, size):
        """
        Constructor for CircularQueue
        
        Args:
            size (int): total size of the queue
        """
        self.size = size
        self.queue = [None] * self.size
        self.front = -1
        self.rear = -1

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front == -1

    def is_full(self):
        """Checks if the queue is full."""
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, element):
        """
        Inserts an element at the rear of the queue.

        Args:
            element: element to be inserted
        """
        if self.is_full():
            print("Queue is Full.")
            return
        
        if self.is_empty():
            self.front = 0  # Set front to 0 for the first element
        
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = element
        print(f"Inserted: {element}")

    def dequeue(self):
        """Removes and returns the front element of the queue."""
        if self.is_empty():
            print("Queue is Empty.")
            return None
        
        removed_element = self.queue[self.front]
        if self.front == self.rear:  # Queue has only one element
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        
        print(f"Removed: {removed_element}")
        return removed_element

    def display(self):
        """Displays all elements in the queue."""
        if self.is_empty():
            print("Queue is Empty.")
            return
        
        index = self.front
        print("Queue elements: ", end="")
        while True:
            print(self.queue[index], end=" ")
            if index == self.rear:
                break
            index = (index + 1) % self.size
        print()  # New line at the end

# User interaction
size = int(input("Enter size of the circular queue: "))
circular_queue = CircularQueue(size)

while True:
    print("\nMenu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            element = int(input("Enter the element to enqueue: "))
            circular_queue.enqueue(element)
        case 2:
            circular_queue.dequeue()
        case 3:
            circular_queue.display()
        case 4:
            print("Exiting the program.")
            break
        case _:
            print("Invalid choice. Please enter a valid option.")