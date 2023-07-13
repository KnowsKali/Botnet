import socket


class Client:
    name: str = "DefaultName"
    addr: tuple = None
    socket: any = None
    hostOS: str = None


class ClientList:
    name = "DefaultName"
    clients = []

    def add_client(self, client: Client) -> None:
        self.clients.append(client)

    def remove_client(self, client: Client) -> None:
        self.clients.append(client)

    def get_client(self, name: str) -> Client:
        for Client in self.clients:
            if Client.name == name:
                return Client


def make_client(client: Client, name, addr, client_socket: socket.socket, host_os: str):
    client.name = name
    client.addr = addr
    client.addr = (addr[0], addr[1])
    client.socket = client_socket
    client.hostOS = host_os
    return client
