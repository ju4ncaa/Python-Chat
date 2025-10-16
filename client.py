import socket

# Variables Globales
HOST = "127.0.0.1"
PORT = 1234

# Paleta de colores ANSI
class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    CYAN = "\033[0;36m"
    YELLOW = "\033[1;33m"
    END = "\033[0m"

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print(f"\n{Colors.GREEN}[+] Cliente conectado a {HOST}:{PORT}{Colors.END}\n")

        while True:
            message = input("Escribe un mensaje ('bye' para salir): ")
            client_socket.sendall(message.encode())

            if message.lower().strip() == "bye":
                print(f"\n{Colors.RED}[!] Desconectado del servidor...{Colors.END}\n")
                break

            response = client_socket.recv(1024).decode()
            print(f"\n{Colors.CYAN}[+] Mensaje del servidor:{Colors.END} {response}\n")

if __name__ == "__main__":
    start_client()