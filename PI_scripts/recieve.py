from serverThread import parallelServer
import time

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