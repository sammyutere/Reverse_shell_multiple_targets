import socket
import threading

class Server:
    def __init__(self, host='0.0.0.0', port=7676):
        self.host = host
        self.port = port
        self.clients = []
        self.current_client = None
        self.exit_flag = False
        self.lock = threading.Lock()