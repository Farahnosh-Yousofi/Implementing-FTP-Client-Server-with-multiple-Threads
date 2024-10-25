import socket
import sys

IP = socket.gethostbyname(socket.gethostname())
    
# Default port
port = 8080

# If a port number is provided via the command line, use that instead
if len(sys.argv) > 1:
    port = int(sys.argv[1])

def get_file_from_server(filename):
    
    try:
        
        # Send "get <filename>" command to the server
        client_socket.sendall(f'get {filename}'.encode())
    
        # Receive the file from the server
        new_Filename = "new" + filename
        with open(new_Filename, 'wb') as file:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f'File: {new_Filename} downloaded successfully')
    except Exception as e:
        print(f'Error: {e}')
    finally:
        if client_socket:
            client_socket.close()
  
def upload_file_to_server(filename):
    try:
        # Send "upload <filename>" command to the server
        client_socket.sendall(f'upload {filename}'.encode())
        
        # Open the file to be uploaded
        with open(filename, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client_socket.sendall(data)
        print(f'File: {filename} uploaded successfully')
    except Exception as e:
        print(f'Error: {e}')
        client_socket.close() if client_socket else None
    finally:
        client_socket.close()

if __name__ == '__main__':
     # Create a socket to connect to the server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, port))
    print('Connected to server')
    
    while True:
        
        print("Enter 'get <filename>' to download or 'upload <filename>' to upload or 'exit' to quit.")
        command = input("ftp> ")
        if command.startswith("get "):
            filename = command.split(" ")[1]
            get_file_from_server(filename)
        elif command.startswith("upload "):
            filename = command.split(" ")[1]
            upload_file_to_server(filename)
        elif command == "exit":
            break
        else:
            print("Invalid command. Please  use 'get', 'upload', or 'exit'..")
        



