import threading
import queue
import time
import random

class threadQ:
    def __init__(self):
        self.que = queue.Queue()
        self.recent_message = None

        server_thread = threading.Thread(target=self.__getServerInfo, args=(self.que,))
        # Without setting to daemon to true the thread will never close application
        server_thread.daemon = True
        server_thread.start()

    # Check if queue contains an item else return None
    def getCommand(self):
        if not self.que.empty():
            item = self.que.get()
            self.recent_message = item
            return item
        return None
    
    # Simulate a server thread
    def __getServerInfo(self, que):
        randomMessageHolder = [
            "Send Image",
            "Increase Altitude",
            "Retreat",
            "Start Stream",
            "Turn gimble 30*"
        ]

        while True:
            # This simulates where a server socket would constantly wait for commands
            random_num = random.randint(0, len(randomMessageHolder)-1)
            current_message = randomMessageHolder[random_num]
            que.put(current_message)
            time.sleep(2)

def main():
    print("Starting server...")
    startServer = threadQ()
    print("Waiting for command from server...")
    while True:
        command = startServer.getCommand()
        if command is not None:
            print("Command is:", command)
        else:
            print("waiting for command")
        time.sleep(1)

if __name__ == "__main__":
    main()