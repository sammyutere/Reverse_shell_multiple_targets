import socket
import threading

#Initialise the Server Class
class Server:
    def __init__(self, host='0.0.0.0', port=7676):
        self.host = host
        self.port = port
        self.clients = []
        self.current_client = None
        self.exit_flag = False
        self.lock = threading.Lock()

        #Start the TCP Server
    def run(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen(10)
            print(f"Server listening on port {self.port}...")

            connection_thread = threading.Thread(target=self.wait_for_connections, args=(server_socket,))
            connection_thread.start()

            while not self.exit_flag:
                if self.clients:
                    self.select_client()
                    self.handle_client()