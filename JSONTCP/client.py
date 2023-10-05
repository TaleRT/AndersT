import socket
import json

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("192.168.1.59", 8888))

    while True:
        method = input("Enter method (Random/Add/Subtract): ").strip()
        if method not in ["Random", "Add", "Subtract"]:
            print("Invalid method")
            continue

        tal1 = int(input("Enter first number: "))
        tal2 = int(input("Enter second number: "))

        request_data = {
            "method": method,
            "Tal1": tal1,
            "Tal2": tal2
        }
        request_json = json.dumps(request_data)
        client.send(request_json.encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        try:
            response_json = json.loads(response)
            if "Error" in response_json:
                print("Server error:", response_json["Error"])
            else:
                print("Server response:", response_json["Result"])
        except json.JSONDecodeError:
            print("Invalid JSON response from server")

if __name__ == "__main__":
    main()
