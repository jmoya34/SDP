# Instructions
To use import the class 'parrallelServer'
```python
from serverThread import parallelServer

# Allow all platforms to connect
startServer = parallelServer('', 65432)

command = startServer.getCommand()
if command is not None:
    print("Command is:", command)
else:
    print("waiting for command")
```

getCommand() is using a queue to get all the messages being sent from the client. If there are no items then None will be returned from the function

getRecentMsg() keeps track of the most recent message that was sent from the most recent client.

### Example of using from main
```python
def main():
    startServer = parallelServer('', 65432)
    print("Doing some work in the background..")
    while True:
        command = startServer.getCommand()
        if command is not None:
            print("Command is:", command)
        else:
            print("waiting for command")
        time.sleep(1)

if __name__ == "__main__":
    main()
```