from spydht import DHT

from datetime import datetime

import nacl.signing, json, uuid

class Client:
    def __init__(self, hostname, port, boot_host=None, boot_port=None):
        print "generating keys..."

        self.key = nacl.signing.SigningKey.generate()

        if bootstrap_host and bootstrap_port:
            print "bootstrapping..."

            self.dht = DHT(hostname, port, self.key, boot_host=boot_host, boot_port=boot_port)
        else:
            print "I'm the first node. Connect to me!"

            self.dht = DHT(hostname, port, self.key)

    def announceProfile(self):
        self.dht[self.username] = json.dumps({
            'nick' : self.nick,
            'bio' : self.bio,
            'website' : self.website,
            'last_status' : self.last_status
            })

    def updateStatus(self, text):
        i = uuid.uuid4()

        dht[i] = json.dumps({
            'author' : self.username,
            'text' : text,
            'timestamp' : utcnow(),
            'previous_status' : self.last_status
            })

        self.last_status = i
