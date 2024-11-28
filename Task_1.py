#Система обробки заявок з чергою
import queue
import random
import time
from datetime import datetime

class Request:
    def __init__(self, request_id=None):
        self.request_id = request_id or self.generate_request_id()
        self.timestamp = datetime.now()
    
    def generate_request_id(self):
        return f"REQ-{random.randint(1000, 9999)}"
    
    def __str__(self):
        return f"Request {self.request_id} (created at {self.timestamp})"

class RequestManagementSystem:
    def __init__(self, max_queue_size=10):
        self.request_queue = queue.Queue(maxsize=max_queue_size)
        self.processed_requests = []
    
    def generate_request(self):
        try:
            if not self.request_queue.full():
                new_request = Request()
                self.request_queue.put(new_request)
                print(f"Generated: {new_request}")
            else:
                print("Queue is full. Cannot generate more requests.")
        except Exception as e:
            print(f"Error generating request: {e}")
    
    def process_request(self):
        try:
            if not self.request_queue.empty():
                request = self.request_queue.get()
                print(f"Processing: {request}")
                time.sleep(1)  # Імітація часу обробки
                self.processed_requests.append(request)
                self.request_queue.task_done()
            else:
                print("Queue is empty. No requests to process.")
        except Exception as e:
            print(f"Error processing request: {e}")
    
    def display_queue_status(self):
        print(f"Current queue size: {self.request_queue.qsize()}")
        print(f"Total processed requests: {len(self.processed_requests)}")

def main():
    request_system = RequestManagementSystem()
    
    try:
        for _ in range(5):
            request_system.generate_request()
        
        request_system.display_queue_status()
        
        # Обробка всіх заявок у черзі
        while not request_system.request_queue.empty():
            request_system.process_request()
        
        request_system.display_queue_status()
    
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()