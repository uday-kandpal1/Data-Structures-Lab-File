class TicketQueue:
    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size
    #Enqueue: Add new ticket request
    def enqueue(self, ticket_id):
        if self.is_full():
            print("Queue is full. Cannot add new ticket request.")
        else:
            self.queue.append(ticket_id)
            print(f"Ticket request {ticket_id} added to the queue.")
    #Dequeue: Process next ticket request
    def dequeue(self):
        if self.is_empty():
            print("No pending requests to process.")
        else:
            ticket_id = self.queue.pop(0)
            print(f"Ticket request {ticket_id} processed and removed.")
            return ticket_id
    #Peek: Check next ticket to process
    def peek(self):
        if self.is_empty():
            print("Queue is empty. Nothing to process next.")
            return None
        else:
            return self.queue[0]
    #Size: Current number of requests
    def size(self):
        return len(self.queue)
    #IsFull: Check if queue is full
    def is_full(self):
        return len(self.queue) == self.max_size
    #IsEmpty: Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0
if __name__ == "__main__":
    ticket_system = TicketQueue(max_size=5)
    ticket_system.enqueue(101)
    ticket_system.enqueue(102)
    ticket_system.enqueue(103)
    print(f"Next ticket to process: {ticket_system.peek()}")
    print(f"Queue size: {ticket_system.size()}")
    ticket_system.dequeue()
    print(f"Queue size after processing: {ticket_system.size()}")
    ticket_system.enqueue(104)
    ticket_system.enqueue(105)
    ticket_system.enqueue(106)
    ticket_system.enqueue(107) 
    print(f"Is queue full? {ticket_system.is_full()}")