import socket


IP = socket.gethostbyname(socket.gethostname())
PORT = 5566
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "UTF-8"
DISCONNECT_MSG = "!DISCONNECT"


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    
    print(f"[CONNECTED] Connected to server at {IP}:{PORT} ...")
    
    connected  = True
    while True:
        msg = input("Enter your message: ")
        client.send(msg.encode(FORMAT))
        if msg == DISCONNECT_MSG:
            connected = False
        else:
            msg = client.recv(SIZE).decode(FORMAT)
            print(f'[SERVER] {msg}')
            
        client.send(msg.encode(FORMAT))
        msg = client.recv(SIZE).decode(FORMAT)
        print(f"Received from server: {msg}")
    

if __name__ == '__main__':
    main()