import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "UTF-8"
DISCONNECT_MSG = "!DISCONNECT"

def handle_client(conn, address):
    print(f"[NEW CONNECTION] {address} connected.")
    
    connected = True
    while connected:
        # Receive data from client and print it
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False
            
        print(f'[{address}] {msg}')
        msg = f'Msg received: {msg}'
        conn.send(msg.encode(FORMAT))
    
    conn.close()
        
    
def main():
    
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    
    print(f"Server is running on {IP}:{PORT}")
    
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, address))
        thread.start()
        print(f'[ACTIVE CONNECTIONS] {threading.activeCount()-1}')
if __name__ == '__main__':
    main()