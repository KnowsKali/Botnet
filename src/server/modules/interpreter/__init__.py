import socket


def run_interpreter(addr: tuple) -> None:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    print("Press ctrl + c to exit")
    while True:
        input_bytes = input(">").encode()
        if input_bytes.decode() == "exit":
            sock.shutdown()
        else:
            sock.send(input_bytes)
        output_bytes = sock.recv(4096)
        print(output_bytes.decode())
