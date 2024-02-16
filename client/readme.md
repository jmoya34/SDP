# Instructions
To use import the class 'sendCommand'
```python
from messageServer import sendCommand

startServer = sendCommand('10.110.220.71', 65432)
startServer.sendMsg(command)
```
Note that ever connection will be terminated after sending a message for simplicity of code to avoid use of threading.

### Example of using from main
```python
def main():
    startServer = sendCommand('10.110.220.71', 65432)
    try:
        while True:
            command = input("What would you like to send to server?: ")
            startServer.sendMsg(command)
            time.sleep(.5)
    except KeyboardInterrupt:
        print("ending program")
        

if __name__ == "__main__":
    main()
```
