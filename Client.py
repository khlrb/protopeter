from spydht import DHT

import nacl.signing, json, uuid

class Client:
    def __init__(self, hostname, port, boot_host=None, boot_port=None):
        print "generating keys..."

        self.key = nacl.signing.SigningKey.generate()

        if boot_host and boot_port:
            print "bootstrapping..."

            self.dht = DHT(hostname, port, self.key, boot_host=boot_host, boot_port=boot_port)
        else:
            print "I'm the first node. Connect to me!"

            self.dht = DHT(hostname, port, self.key)

        self.running = True

        name_ok = False

        while name_ok == False:
            self.username = raw_input("Choose a username: ")

            try:
                u = self.dht[self.username]
            except KeyError:
                u = None

            if u == None:
                name_ok = True
            else:
                print "This username is already taken!"

        self.last_status = None
        self.nick = ''
        self.bio = ''
        self.website = ''

        self.announceProfile()

    def announceProfile(self):
        self.dht[self.username] = json.dumps({
            'nick' : self.nick,
            'bio' : self.bio,
            'website' : self.website,
            'last_status' : self.last_status
            })

    def updateStatus(self, text):
        i = str(uuid.uuid4())

        self.dht[i] = json.dumps({
            'author' : self.username,
            'text' : text,
            'previous_status' : self.last_status
            })

        self.last_status = i

        self.announceProfile()

        return i
