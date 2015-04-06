from pprint import pprint

class Prompt:
    def __init__(self, client):
        self.client = client

        self.commands = {
                'status' : self.updateStatus,
                'lookup' : self.lookup,
                'help' : self.showHelp,
                'quit' : self.quit
                }

    def prompt(self):
        i = raw_input("> ")
        if i in command.keys():
            command[i]()
        else:
            print "command not found: " + i

    def updateStatus(self):
        text = raw_input("text: ")

        try:
            s = self.client.updateStatus(text)

            print "success: " + s
        except:
            print "error"

    def lookup(self):
        k = raw_input("username or status id: ")

        try:
            v = self.client.dht[k]

            pprint(v)
        except KeyError:
            print "Can't find item '" + k + "'"

    def showHelp(self):
        description = {
                'status' : "update your status (a.k.a. tweet)",
                'lookup' : "view a certain user profile or status update",
                'help' : "show this message",
                'quit' : "shut the node down and exit"
                }

        print "available commands:"
        for k, v in description.iteritems():
            print k + ": " + v

    def quit():
        self.client.running = False

