import array


class Client :
    def self ( self , name , ip , port ) :
        t = self
        t.name = name
        t.ip = ip
        t.port = port
        return t

    name: str = ""
    ip: str = ""
    port: int = ""


Client_List: array = [ ]


def from_name ( name: str ) :
    found = False
    for client in Client_List :
        if client.name == name :
            found = client
    if not found :
        return None
    else :
        return found


def from_ip ( ip: str ) :
    found = False
    for client in Client_List :
        if client.ip == ip :
            found = client
    if not found :
        return None
    else :
        return found


def add_client ( client: Client ) :
    Client_List.append ( Client_List , client )


def remove_client ( client: Client ) :
    Client_List.remove ( Client_List , client )
