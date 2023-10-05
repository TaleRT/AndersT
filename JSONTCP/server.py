import socket
import random
import json
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    try:
        request_json = json.loads(request)
        method = request_json.get('method')
        tal1 = request_json.get('Tal1')
        tal2 = request_json.get('Tal2')

        if method == "Random":
            result = random.randint(tal1, tal2)
            response = {"Result": result}
        elif method == "Add":
            result = tal1 + tal2
            response = {"Result": result}
        elif method == "Subtract":
            result = tal1 - tal2
            response = {"Result": result}
        else:
            response = {"Error": "Invalid method"}

        client_socket.send(json.dumps(response).encode('utf-8'))
    except json.JSONDecodeError:
        response = {"Error": "Invalid JSON format"}
        client_socket.send(json.dumps(response).encode('utf-8'))

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("192.168.1.59", 8888))
    server.listen(5)
    print("Server listening on port 8888")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    main()
