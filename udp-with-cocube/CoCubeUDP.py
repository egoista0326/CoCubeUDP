import socket
import time
from math import *
from threading import Thread

class CoCubeUDP:
    def __init__(self, robotID, ip_head = '192.168.3.1', port_head = 5000, local_ip = '192.168.3.70'):
        self.robotID = robotID
        self.robotIP = ip_head + ('0' if robotID < 10 else '') + str(robotID)
        self.robotPort = port_head + robotID
        self.localIP = local_ip
        self.localPort = port_head + robotID
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 1000)  # 增加发送缓冲区大小
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1000)  # 增加接收缓冲区大小
        self.sock.bind((self.localIP, self.localPort))
        self.sock.settimeout(3)

    def connected(self):
        if isinstance(self.message_general("position_X", [],  debug=False, testConnct = True), str):
            print(f"robot {self.robotID} connected")
            return True
        else:
            print(f"robot {self.robotID} not connected")
            return False

    # def send_message(self, message, debug: bool = False):
    #     message_bytes = message.encode()
    #     self.sock.sendto(message_bytes, (self.robotIP, self.robotPort))
    #     if debug:
    #         print(f"send message: {message}")
    #     return True
    #
    # def send_velocity(self, velocityX, velocityY, debug: bool = False):
    #     message = f"{velocityX},{velocityY}"
    #     message_bytes = message.encode()
    #     self.sock.sendto(message_bytes, (self.robotIP, self.robotPort))
    #     if debug:
    #         print(f"send message: {message}")
    #     return True
    #
    # def receive_message(self, debug: bool = False):
    #     data, addr = self.sock.recvfrom(1024)
    #     if debug:
    #         print(f"receive message from {addr}: {data.decode()}")
    #     return data.decode()
    #
    # def receive_position(self, debug: bool = False):
    #     data, addr = self.sock.recvfrom(1024)
    #     if debug:
    #         print(f"receive message from {addr}: {data.decode()}")
    #     data = data.decode().split(',')
    #     data = [float(i) for i in data]
    #     print(data[1])
    #     return data

    def message_general(self, cmdName, args=[], debug: bool = False, testConnct: bool = False):
        message = f"{cmdName},{','.join(map(str, args))}"
        message_bytes = message.encode()
        self.sock.sendto(message_bytes, (self.robotIP, self.robotPort))
        try:
            data, addr = self.sock.recvfrom(1024)
            if debug:
                print(f"receive message from {addr}: {data.decode()}")
            return data.decode()
        except socket.timeout:
            if testConnct:
                return None
            print("Timeout occurred: No response received.")
            return None
