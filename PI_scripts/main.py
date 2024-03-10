from classes.serverThread import parallelServer
from classes.vidClient import vidClient
from classes.uartCom import uartCom
import time
import json

def main():
    startServer = parallelServer('', 65432)
    sendVideo = vidClient("192.168.254.20", 6789)
    arduinoCom = uartCom('/dev/serial0', 9600, 0.1)
    while(1):
        command = startServer.getCommand()
        if command is not None:
            print("Command is:", command)




if __name__ == "__main__":
    main()