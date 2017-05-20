import socket
import os

def main():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("127.0.0.1", 8888))
    serversocket.listen(0)

    # Child Process
    for i in range(10):
        if os.fork() == 0:
            return accept_conn("child_" + str(i), serversocket)

    return accept_conn("parent", serversocket)

def accept_conn(message, s):
    while True:
        c, addr = s.accept()
        print('Got connection from in {0}'.format(message))
        c.send('Thank you for your connecting to {0}\n'.format(message).encode('utf-8'))
        c.close()

if __name__ == "__main__":
    main()
