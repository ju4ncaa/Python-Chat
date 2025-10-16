import socket
import threading

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

def handle_client(conn, addr):
    print(f"\n{Colors.YELLOW}[*] Conexión entablada desde {addr}{Colors.END}\n")
    while True:
        message = conn.recv(1024).decode()

        if message.lower().strip() == "bye":
            print(f"\n{Colors.RED}[!] Cliente {addr} desconectado...{Colors.END}\n")
            break
            
        print(f"\n{Colors.CYAN}[+] Mensaje del cliente:{Colors.END} {message}\n")

        response = f"El servidor recibió {message}"
        conn.send(response.encode())
        
def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print(f"\n{Colors.GREEN}[+] Servidor iniciado en {HOST}:{PORT}{Colors.END}\n")

        while True:
            conn, addr = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(conn, addr))
            client_thread.start()
    
if __name__ == "__main__":
    start_server()