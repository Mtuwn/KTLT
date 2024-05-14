import socket
import threading

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print("[*] Received: {}".format(request))

    client_socket.send(b"ACK!")

    client_socket.close()


def main():
    for port in range(1000, 2000):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            server_socket.bind(("192.168.0.103", port))
            server_socket.listen(5)
            print("[*] Listening on 1:{}".format(port))
            client_socket, addr = server_socket.accept()
            print("[*] Accepted connection from: {}:{}".format(addr[0], addr[1]))
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()

        except Exception as e:
            print("[!] Error: {}".format(e))

if __name__ == "__main__":
    main()
