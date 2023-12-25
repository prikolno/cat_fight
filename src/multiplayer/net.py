import socket


class Connection:
    def __init__(self):
        self.addr = ('', 0)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect(self.addr)

    def say_hi(self):
        pass

    def say_bye(self):
        pass

    def update_data(self):
        pass
