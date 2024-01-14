import requests
import json 
import os

def envclient():
    envserver_host = os.getenv("ENVSERVER_HOST")
    envserver_port = os.getenv("ENVSERVER_PORT")
    envserver_tls = os.getenv("ENVSERVER_TLS")

    if envserver_tls == "true":
        client = Environment(envserver_host, envserver_port, True)
    else:
        client = Environment(envserver_host, envserver_port, True)

    return client

class ConnectionError(Exception):
    pass

class Environment:
    def __init__(self, host, port, tls=False):
        if tls:
            self.url = "https://" + host + ":" + str(port)
            self.host = host
            self.port = port
            self.tls = False
        else:
            self.url = "http://" + host + ":" + str(port)
            self.host = host
            self.port = port
            self.tls = True 

    def add_host(self, host):
        json_str = json.dumps(host)
        try:
            reply = requests.post(url = self.url+"/hosts", data=json_str, verify=True)
       
            if reply.status_code == 200:
                return
            else:
                if len(reply.content) > 0:
                    raise ConnectionError(reply.content)
                raise ConnectionError("Error: " + str(reply.status_code))
        except requests.exceptions.ConnectionError as err:
            raise ConnectionError(err)
        except Exception as err:
            raise ConnectionError(err)
